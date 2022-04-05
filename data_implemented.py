from encodings import cp949

import pandas as pd
import math

# 전역변수&함수
date = []
for i in range(1, 32):
    if i < 9:
        date.append('08-0' + str(i))
    else:
        date.append('08-' + str(i))


def total_sec(data):
    time = data.split(':')
    total_sec = int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2])
    return total_sec


def sec_to_time(total_second):
    inverse_hour = int(total_second // 3600)
    inverse_minute = int((total_second - inverse_hour * 3600) // 60)
    inverse_second = int((total_second - inverse_hour * 3600 - inverse_minute * 60))

    if inverse_hour < 10:
        inverse_hour = '0' + str(inverse_hour)
    else:
        inverse_hour = str(inverse_hour)

    if inverse_minute < 10:
        inverse_minute = '0' + str(inverse_minute)
    else:
        inverse_minute = str(inverse_minute)

    if inverse_second < 10:
        inverse_second = '0' + str(inverse_second)
    else:
        inverse_second = str(inverse_second)

    inverse_time = inverse_hour + ':' + inverse_minute + ':' + inverse_second

    if total_second < 0:
        return '00:00:00'
    else:
        return inverse_time

def get_one_user(id):
    """
        한 명의 사용자 객체 (Person)를 불러온 뒤 반환해 줍니다.
        만약 잘못된 id면 None을 반환합니다.
    :return:
    """
    try:
        p = Person(id)
    except:
        p = None

    return p


class Person:
    def __init__(self, user_id):
        # 끝에 1355.csv / 1356.csv 가 다르더라고요..
        if user_id < 30064:
            file_path = '/hs_g73_m08/hs_' + str(user_id) + '_m08_0903_1355.csv'
        else:
            file_path = '/hs_g73_m08/hs_' + str(user_id) + '_m08_0903_1356.csv'

        # 데이터들 폴더 이름이 '프로그래밍언어구조론_라이프로그데이터_2021_2'로 되어있는데 영어로 간단하게 바꾸는게 좋을듯 해요
        user_data = pd.read_csv('./' + file_path, encoding='cp949')
        user_profile_data = pd.read_excel('./' + '/user_profile.xlsx')
        user_profile_data.to_csv()
        user_profile_data = user_profile_data[user_profile_data['id'] == int(user_id)].iloc[0]

        self.name = 'ID-' + str(user_profile_data['id'])
        self.sex = user_profile_data['sex']
        self.age = user_profile_data['age']
        self.sleepData = self.Sleep(user_data)
        self.eatData = self.Eat(user_data)
        self.exerciseData = self.Exercise(user_data)
        self.medicationData = self.Medication(user_data)
        self.suniData = self.Suni(user_data)

    class Sleep:
        def __init__(self, user_data):
            self.sleep_data = user_data[user_data['Act'].str.contains('기상|취침|낮잠')]

        def sleep_data_to_time(self):
            # 낮잠은 최대 두 번 카운트
            result_data = pd.DataFrame(columns=['기상', '취침', '낮잠1', '낮잠기상1', '낮잠2', '낮잠기상2'], index=range(1, 32))
            index = 1

            for day in date:
                daily_sleep_data = self.sleep_data[self.sleep_data['Time'].str.contains(day)]
                # 기상의 종류가 많아서 '기상'이 포함된 row에서 '낮잠기상' row만 제외하는 식으로 뽑았습니다
                data1 = daily_sleep_data[daily_sleep_data['Act'].str.contains('기상')]
                data1 = data1[~data1['Act'].str.contains('낮잠기상')]

                data2 = daily_sleep_data[daily_sleep_data['Act'] == '취침']

                # '낮잠, 외출' 이라는 데이터가 있는데, 무슨 소리인지 모르겠지만 일단 넣었습니다.
                data3 = daily_sleep_data[daily_sleep_data['Act'].str.contains('낮잠')]
                data3 = data3[~data3['Act'].str.contains('낮잠기상')]

                data4 = daily_sleep_data[daily_sleep_data['Act'].str.contains('낮잠기상')]

                # Time에서 날짜 제외 시간만 추출
                if not data1.empty:
                    act_time1 = data1['Time'].iloc[0]
                    result_data.loc[index, '기상'] = act_time1.split()[1]

                if not data2.empty:
                    act_time2 = data2['Time'].iloc[len(data2.index) - 1]
                    result_data.loc[index, '취침'] = act_time2.split()[1]

                if not data3.empty:
                    act_time3 = data3['Time'].iloc[0]
                    result_data.loc[index, '낮잠1'] = act_time3.split()[1]
                    if len(data3.index) > 1:
                        act_time3 = data3['Time'].iloc[1]
                        result_data.loc[index, '낮잠2'] = act_time3.split()[1]

                if not data4.empty:
                    act_time4 = data4['Time'].iloc[0]
                    result_data.loc[index, '낮잠기상1'] = act_time4.split()[1]
                    if len(data4.index) > 1:
                        act_time4 = data4['Time'].iloc[1]
                        result_data.loc[index, '낮잠기상2'] = act_time4.split()[1]

                index += 1

            return result_data

        # 데이터가 하나도 없으면 에러남 (ex. id=232)
        def find_average(self, sleep_data):
            null_check = sleep_data.isnull()
            result_data = pd.DataFrame(columns=['평균_기상', '평균_취침', '평균_낮잠', '평균_수면(낮잠제외)', 'valid_count'],
                                       index=range(1, 2))

            data1 = 0  # 평균 기상
            data2 = 0  # 평균 취침
            data3 = 0  # 평균 낮잠
            data4 = 0  # 평균 수면
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            nap_flag = False

            for index in range(1, 32):
                if ~null_check.loc[index, '기상']:
                    data1 += total_sec(sleep_data.loc[index, '기상'])
                    count1 += 1

                if ~null_check.loc[index, '취침']:
                    time = total_sec(sleep_data.loc[index, '취침'])
                    if time < 21600:
                        time = time + 86400
                    data2 += time
                    count2 += 1

                    # 낮잠기상 시간이 낮잠 시간보다 더 빠르면 제외
                if ((~null_check.loc[index, '낮잠1']) & (~null_check.loc[index, '낮잠기상1'])):
                    time1 = total_sec(sleep_data.loc[index, '낮잠1'])
                    time2 = total_sec(sleep_data.loc[index, '낮잠기상1'])
                    if time2 > time1:
                        data3 += (time2 - time1)
                        nap_flag = True

                if ((~null_check.loc[index, '낮잠2']) & (~null_check.loc[index, '낮잠기상2'])):
                    time1 = total_sec(sleep_data.loc[index, '낮잠2'])
                    time2 = total_sec(sleep_data.loc[index, '낮잠기상2'])
                    if time2 > time1:
                        data3 += (time2 - time1)
                        nap_flag = True

                if nap_flag:
                    count3 += 1

                # 평균 수면(다음 날 기상시간 - 취침시간) % valid_count 구하기
                if index < 31:
                    if ((~null_check.loc[index, '취침']) & (~null_check.loc[index + 1, '기상'])):
                        time1 = total_sec(sleep_data.loc[index, '취침'])
                        time2 = total_sec(sleep_data.loc[index + 1, '기상'])
                        # 12:00를 기준으로 24:00 이전/이후 취침 구분
                        if time1 > 43200:
                            data4 += (86400 - time1) + time2
                        else:
                            data4 += (time2 - time1)
                        count4 += 1

                nap_flag = False

            if count1 != 0:
                result_data.loc[1, '평균_기상'] = sec_to_time(data1 / count1)
            if count2 != 0:
                time = data2 / count2
                if time > 86400:
                    time = time - 86400
                result_data.loc[1, '평균_취침'] = sec_to_time(time)
            if count3 != 0:
                result_data.loc[1, '평균_낮잠'] = sec_to_time(data3 / count3)
            if count4 != 0:
                result_data.loc[1, '평균_수면(낮잠제외)'] = sec_to_time(data4 / count4)
            result_data.loc[1, 'valid_count'] = count4

            return result_data

        # 취침/수면 둘 다 비어있으면 평균값, 둘 중 하나만 비어있을 경우 (ex. 취침o, 기상x) 기상 = 취침 + 낮잠제외 평균수면시간
        def fill_missing_data(self):
            sleep_data = self.sleep_data_to_time()
            null_check = sleep_data.isnull()
            average_data = self.find_average(sleep_data)

            if null_check.loc[1, '기상']:
                sleep_data.loc[1, '기상'] = average_data.loc[1, '평균_기상']
            if null_check.loc[31, '취침']:
                sleep_data.loc[31, '취침'] = average_data.loc[1, '평균_취침']

            for index in range(1, 31):
                if ((null_check.loc[index, '취침']) & (null_check.loc[index + 1, '기상'])):
                    sleep_data.loc[index, '취침'] = average_data.loc[1, '평균_취침']
                    sleep_data.loc[index + 1, '기상'] = average_data.loc[1, '평균_기상']

                if ((null_check.loc[index, '취침']) & (~null_check.loc[index + 1, '기상'])):
                    time1 = total_sec(sleep_data.loc[index + 1, '기상'])
                    time2 = total_sec(average_data.loc[1, '평균_수면(낮잠제외)'])
                    if time1 > time2:
                        sleep_data.loc[index, '취침'] = sec_to_time(time1 - time2)
                    else:
                        sleep_data.loc[index, '취침'] = sec_to_time(86400 - (time2 - time1))

                if ((~null_check.loc[index, '취침']) & (null_check.loc[index + 1, '기상'])):
                    time1 = total_sec(sleep_data.loc[index, '취침'])
                    time2 = total_sec(average_data.loc[1, '평균_수면(낮잠제외)'])
                    if time1 > 43200:
                        sleep_data.loc[index + 1, '기상'] = sec_to_time(time2 - (86400 - time1))
                    else:
                        sleep_data.loc[index + 1, '기상'] = sec_to_time(time1 + time2)

            return sleep_data

        # 결측치 추정 이후 평균
        def find_after_average(self):
            result_data = self.find_average(self.fill_missing_data())
            return result_data

        # 수면 데이터가 3일 이하이면 true
        def exclude(self):
            count = self.find_average(self.sleep_data_to_time()).loc[1, 'valid_count']
            if count < 4:
                return True
            else:
                return False

                # 데이터 30개

        def get_monthly_sleep_times(self):
            sleep_data = self.fill_missing_data()
            monthly_sleep_data = []
            for index in range(1, 31):
                time1 = total_sec(sleep_data.loc[index, '취침'])
                time2 = total_sec(sleep_data.loc[index + 1, '기상'])
                if time2 > 79200:
                    time2 = 0

                if time1 > 43200:
                    time3 = (86400 - time1) + time2
                else:
                    time3 = time2 - time1

                if time3 < 0:
                    time3 = -time3
                monthly_sleep_data.append(int(time3 / 3600))

            return monthly_sleep_data

        # 데이터 31개
        def get_early_wakes(self):
            early_wakes = []

            for day in date:
                daily_sleep_data = self.sleep_data[self.sleep_data['Time'].str.contains(day)]
                data = daily_sleep_data[daily_sleep_data['Act'].str.contains('이른기상')]
                if not data.empty:
                    early_wakes.append(True)
                else:
                    early_wakes.append(False)

            return early_wakes

        def get_sleep_variance_score(self):
            sleep_data = self.fill_missing_data()
            average_data = self.find_after_average()
            variance1 = 0  # 기상 분산
            variance2 = 0  # 취침 분산
            variance3 = 0  # 수면 분산
            avg1 = total_sec(average_data.loc[1, '평균_기상'])
            avg2 = total_sec(average_data.loc[1, '평균_취침'])
            avg3 = total_sec(average_data.loc[1, '평균_수면(낮잠제외)'])

            for index in range(1, 32):
                time1 = total_sec(sleep_data.loc[index, '기상'])
                data1 = time1 - avg1
                variance1 += data1 * data1

                time2 = total_sec(sleep_data.loc[index, '취침'])
                if time2 < 21600:
                    time2 = time2 + 86400
                if avg2 < 21600:
                    avg2 = avg + 86400
                data2 = time2 - avg2
                variance2 += data2 * data2

                if index < 31:
                    time3 = total_sec(sleep_data.loc[index, '취침'])
                    time4 = total_sec(sleep_data.loc[index, '기상'])
                    if time3 > 43200:
                        time5 = (86400 - time3) + time4
                    else:
                        time5 = time4 - time3
                    data3 = time5 - avg3
                    variance3 += data3 * data3

            variance1 = math.sqrt(variance1 / 31)
            variance2 = math.sqrt(variance2 / 31)
            variance3 = math.sqrt(variance3 / 30)
            total_var = (variance1 + variance2 + variance3) / 3
            total_var = int(total_var / 3600)
            score = 100 - total_var * 10  # 편차 1시간 이내 10점감점, 2시간 이내 20점감점, ...

            return score

        def get_sleep_overall_score(self):
            average_data = self.find_after_average()
            var_score = self.get_sleep_variance_score()
            avg = average_data.loc[1, '평균_수면(낮잠제외)']
            time1 = total_sec(avg)
            time2 = total_sec('08:00:00')
            data = time1 - time2
            avg_var = math.sqrt(data * data)
            avg_var = int(avg_var / 3600)
            avg_score = 100 - avg_var * 10  # 편차 1시간 이내 10점감점, 2시간 이내 20점감점, ...

            total_score = int((avg_score + var_score) / 2)

            return total_score

    class Eat:
        def __init__(self, user_data):
            self.eat_data = user_data[user_data['Act'].str.contains('식사|간식|야식')]

        def eat_data_to_time(self):
            result_data = pd.DataFrame(columns=['아침식사', '점심식사', '저녁식사'], index=range(1, 32))
            index = 1

            for day in date:
                daily_eat_data = self.eat_data[self.eat_data['Time'].str.contains(day)]

                data1 = daily_eat_data[daily_eat_data['Act'] == '아침식사']
                if not data1.empty:
                    act_time1 = data1['Time'].iloc[0]
                    result_data.loc[index, '아침식사'] = act_time1.split()[1]

                data2 = daily_eat_data[daily_eat_data['Act'] == '점심식사']
                if not data2.empty:
                    act_time2 = data2['Time'].iloc[0]
                    result_data.loc[index, '점심식사'] = act_time2.split()[1]

                data3 = daily_eat_data[daily_eat_data['Act'] == '저녁식사']
                if not data3.empty:
                    act_time3 = data3['Time'].iloc[0]
                    result_data.loc[index, '저녁식사'] = act_time3.split()[1]

                # 아침식사/점심식사/저녁식사 로 표기되지 않은 식사들 처리 (ex. 12시에 먹는 간식. 이런 데이터 많음)
                data4 = daily_eat_data[~daily_eat_data['Act'].str.contains('아침식사|점심식사|저녁식사')]
                for i in range(0, len(data4.index)):
                    act_time4 = data4['Time'].iloc[i].split()[1]
                    act_time4_sec = total_sec(act_time4)

                    # 04~10 아침
                    if ((act_time4_sec > 14400) & (act_time4_sec < 36000)):
                        if data1.empty:
                            result_data.loc[index, '아침식사'] = act_time4
                    # 11~14 점심
                    if ((act_time4_sec > 39600) & (act_time4_sec < 50400)):
                        if data2.empty:
                            result_data.loc[index, '점심식사'] = act_time4
                    # 17~20 저녁
                    if ((act_time4_sec > 61200) & (act_time4_sec < 72000)):
                        if data3.empty:
                            result_data.loc[index, '저녁식사'] = act_time4

                index += 1

            return result_data

        def get_monthly_eat_snack_count(self):
            eat_data = self.eat_data_to_time()
            null_check = eat_data.isnull()
            eat_count = self.get_monthly_eat_count()
            snack_count = []

            for index in range(1, 32):
                count = 0
                if not null_check.loc[index, '아침식사']:
                    count += 1
                if not null_check.loc[index, '점심식사']:
                    count += 1
                if not null_check.loc[index, '저녁식사']:
                    count += 1
                snack_count.append(eat_count[index - 1] - count)

            return snack_count

        def get_eat_type(self):
            eat_data = self.eat_data_to_time()
            null_check = eat_data.isnull()
            eat_type = []
            count1 = 0
            count2 = 0
            count3 = 0

            for index in range(1, 32):
                if not null_check.loc[index, '아침식사']:
                    count1 += 1
                if not null_check.loc[index, '점심식사']:
                    count2 += 1
                if not null_check.loc[index, '저녁식사']:
                    count3 += 1

            eat_type.append(count1)
            eat_type.append(count2)
            eat_type.append(count3)

            return eat_type

        def find_average(self, eat_data):
            null_check = eat_data.isnull()
            result_data = pd.DataFrame(columns=['평균_아침', '평균_점심', '평균_저녁'], index=range(1, 2))

            data1 = 0  # 아침
            data2 = 0  # 점심
            data3 = 0  # 저녁
            count1 = 0
            count2 = 0
            count3 = 0

            for index in range(1, 32):
                if ~null_check.loc[index, '아침식사']:
                    data1 += total_sec(eat_data.loc[index, '아침식사'])
                    count1 += 1

                if ~null_check.loc[index, '점심식사']:
                    data2 += total_sec(eat_data.loc[index, '점심식사'])
                    count2 += 1

                if ~null_check.loc[index, '저녁식사']:
                    data3 += total_sec(eat_data.loc[index, '저녁식사'])
                    count3 += 1

            if count1 != 0:
                result_data.loc[1, '평균_아침'] = sec_to_time(data1 / count1)
            if count2 != 0:
                result_data.loc[1, '평균_점심'] = sec_to_time(data2 / count2)
            if count3 != 0:
                result_data.loc[1, '평균_저녁'] = sec_to_time(data3 / count3)

            return result_data

        # 평균값으로 채우기
        def fill_missing_data(self):
            eat_data = self.eat_data_to_time()
            null_check = eat_data.isnull()
            average_data = self.find_average(eat_data)

            for index in range(1, 32):
                if null_check.loc[index, '아침식사']:
                    eat_data.loc[index, '아침식사'] = average_data.loc[1, '평균_아침']
                if null_check.loc[index, '점심식사']:
                    eat_data.loc[index, '점심식사'] = average_data.loc[1, '평균_점심']
                if null_check.loc[index, '저녁식사']:
                    eat_data.loc[index, '저녁식사'] = average_data.loc[1, '평균_저녁']

            return eat_data

        # 결측치 추정 이후 평균
        def find_after_average(self):
            result_data = self.find_average(self.fill_missing_data())
            return result_data

        def exclude(self):
            eat_data = self.eat_data_to_time()
            null_check = eat_data.isnull()
            count1 = 0
            count2 = 0
            count3 = 0
            check = False

            for index in range(1, 32):
                if not null_check.loc[index, '아침식사']:
                    count1 += 1
                if not null_check.loc[index, '점심식사']:
                    count2 += 1
                if not null_check.loc[index, '저녁식사']:
                    count3 += 1

            if count1 < 3:
                check = True
            if count2 < 3:
                check = True
            if count3 < 3:
                check = True

            return check

        def get_monthly_eat_count(self):
            count = 0
            monthly_count = []

            for day in date:
                daily_eat_data = self.eat_data[self.eat_data['Time'].str.contains(day)]
                if not daily_eat_data.empty:
                    count = len(daily_eat_data.index)
                else:
                    count = 0
                monthly_count.append(count)

            return monthly_count

        # 데이터 31개  // 결측치 추정 이전?이후?
        def get_monthly_eat_time(self):
            eat_data = self.eat_data_to_time()
            null_check = eat_data.isnull()
            result = []

            for index in range(1, 32):
                data = []
                if not null_check.loc[index, '아침식사']:
                    data.append(eat_data.loc[index, '아침식사'])
                if not null_check.loc[index, '점심식사']:
                    data.append(eat_data.loc[index, '점심식사'])
                if not null_check.loc[index, '저녁식사']:
                    data.append(eat_data.loc[index, '저녁식사'])
                result.append(data)

            return result

        def get_eat_variance_score(self):
            eat_data = self.fill_missing_data()
            average_data = self.find_after_average()
            variance1 = 0
            variance2 = 0
            variance3 = 0
            avg1 = total_sec(average_data.loc[1, '평균_아침'])
            avg2 = total_sec(average_data.loc[1, '평균_점심'])
            avg3 = total_sec(average_data.loc[1, '평균_저녁'])

            for index in range(1, 32):
                time1 = total_sec(eat_data.loc[index, '아침식사'])
                data1 = time1 - avg1
                variance1 += data1 * data1

                time2 = total_sec(eat_data.loc[index, '점심식사'])
                data2 = time2 - avg2
                variance2 += data2 * data2

                time3 = total_sec(eat_data.loc[index, '저녁식사'])
                data3 = time3 - avg3
                variance3 += data3 * data3

            variance1 = math.sqrt(variance1 / 31)
            variance2 = math.sqrt(variance2 / 31)
            variance3 = math.sqrt(variance3 / 31)
            total_var = (variance1 + variance2 + variance3) / 3
            total_var = int(total_var / 300)  # 5분당 10점 감점
            score = 100 - total_var * 10

            return score

        def get_eat_score(self):
            average_data = self.find_after_average()
            var_score = self.get_eat_variance_score()
            avg1 = average_data.loc[1, '평균_아침']
            avg1 = total_sec(avg1)
            avg2 = average_data.loc[1, '평균_점심']
            avg2 = total_sec(avg2)
            avg3 = average_data.loc[1, '평균_저녁']
            avg3 = total_sec(avg3)
            time1 = total_sec('07:30:00')
            time2 = total_sec('11:30:00')
            time3 = total_sec('17:30:00')

            data1 = time1 - avg1
            data2 = time2 - avg2
            data3 = time3 - avg3
            var1 = math.sqrt(data1 * data1)
            var2 = math.sqrt(data2 * data2)
            var3 = math.sqrt(data3 * data3)
            avg_var = (var1 + var2 + var3) / 3
            avg_var = int(avg_var / 1800)
            avg_score = 100 - avg_var * 10
            total_score = int((avg_score + var_score) / 2)

            return total_score

    # 여기서부터 운동 데이터입니다.
    # |
    # |
    # |
    # |
    # |

    class Exercise:
        def __init__(self, user_data):
            self.exercise_data = user_data[user_data['State'].str.contains('외출|정리|운동|설거지|체조')]
            self.user_data = user_data
            self.score1 = ['주방 정리하기', '냉장고 정리하기', '설거지 하기', '밥솥 정리하기']
            self.score2 = ['외출하기', '실내운동하기', '순이체조']
            self.score3 = ['실외운동하기', '운동 후 귀가']

        def exclude(self):
            monthly_score = self.get_monthly_active_score()
            sum = 0
            for i in range(0, len(monthly_score)):
                sum += monthly_score[i]
            if sum == 0:
                return True
            else:
                return False

        # 하루에 5점이 만점이 되도록 환산
        def get_monthly_active_score(self):
            count = 0
            monthly_active_score = []

            for day in date:
                daily_exercise_data = self.exercise_data[self.exercise_data['Time'].str.contains(day)]
                score = 0

                if not daily_exercise_data.empty:
                    for index in range(0, len(daily_exercise_data.index)):
                        if daily_exercise_data.iloc[index]['State'] in self.score1:
                            score += 1
                        elif daily_exercise_data.iloc[index]['State'] in self.score2:
                            score += 2
                        elif daily_exercise_data.iloc[index]['State'] in self.score3:
                            score += 3
                    if score > 5:
                        monthly_active_score.append(100)
                    else:
                        monthly_active_score.append(score * 20)

                else:
                    monthly_active_score.append(0)

            return monthly_active_score

        def get_total_active_score(self):
            monthly_score = self.get_monthly_active_score()
            sum = 0
            count = 0
            for i in range(0, len(monthly_score)):
                if monthly_score[i] != 0:
                    sum += monthly_score[i]
                    count += 1
            if count == 0:
                return 0
            else:
                return int(sum / count)

        def get_activity_list(self):
            result_dict = {}
            data = self.user_data[self.user_data['Act'].str.contains('프로그램')]
            count = len(data.index)
            result_dict["Program"] = count

            data = self.user_data[self.user_data['Act'].str.contains('TV')]
            count = len(data.index)
            result_dict["TV"] = count

            data = self.user_data[self.user_data['Act'].str.contains('실외운동')]
            count = len(data.index)
            result_dict["Exercise_outside"] = count

            data = self.user_data[self.user_data['Act'].str.contains('실내운동')]
            count = len(data.index)
            result_dict["Exercise_inside"] = count

            data = self.user_data[self.user_data['Act'].str.contains('휴식')]
            count = len(data.index)
            result_dict["Rest"] = count

            data = self.user_data[self.user_data['Act'].str.contains('외출')]
            count = len(data.index)
            result_dict["Outing"] = count

            data = self.user_data[self.user_data['Act'].str.contains('낮잠')]
            data = data[~data['Act'].str.contains('낮잠기상')]
            count = len(data.index)
            result_dict["Nap"] = count

            return result_dict

        def get_weekly_active_group(self):
            """
                5주 중 운동을 많이한 주차, 운동을 적당히 한 주차, 운동이 부족한 주차를 나누어서 return.
                다른 사용자와의 절대적 점수 비교가 아니라
            :return:
            """

    # 여기서부터 약 복용 데이터입니다.
    #
    #
    #
    #
    class Medication:
        def __init__(self, user_data):
            self.medication_data = user_data[user_data['State'].str.contains('약')]

        def medication_data_to_time(self):
            result_data = pd.DataFrame(columns=['복용1', '복용2', '복용3'], index=range(1, 32))
            index = 1

            for day in date:
                daily_medication_data = self.medication_data[self.medication_data['Time'].str.contains(day)]
                count = len(daily_medication_data.index)
                if count == 1:
                    time1 = daily_medication_data['Time'].iloc[0]
                    result_data.loc[index, '복용1'] = time1.split()[1]

                if count == 2:
                    time1 = daily_medication_data['Time'].iloc[0]
                    time2 = daily_medication_data['Time'].iloc[1]
                    result_data.loc[index, '복용1'] = time1.split()[1]
                    result_data.loc[index, '복용2'] = time2.split()[1]

                if count > 2:
                    time1 = daily_medication_data['Time'].iloc[0]
                    time2 = daily_medication_data['Time'].iloc[1]
                    time3 = daily_medication_data['Time'].iloc[len(daily_medication_data.index) - 1]
                    result_data.loc[index, '복용1'] = time1.split()[1]
                    result_data.loc[index, '복용2'] = time2.split()[1]
                    result_data.loc[index, '복용3'] = time3.split()[1]

                index += 1

            return result_data

        def exclude(self):
            morning = self.get_morning_medication_list()
            lunch = self.get_lunch_medication_list()
            dinner = self.get_dinner_medication_list()

            count = 0
            if morning != None:
                count = 1
            if lunch != None:
                count = 1
            if dinner != None:
                count = 1

            if count == 0:
                return True
            else:
                return False

        def get_medication_count_by_day(self):
            morning = self.get_morning_medication_list()
            lunch = self.get_lunch_medication_list()
            dinner = self.get_dinner_medication_list()
            count = 0

            if morning != None:
                count += 1
            if lunch != None:
                count += 1
            if dinner != None:
                count += 1

            return count

        def get_medication_count(self):
            medication_data = self.medication_data_to_time()
            null_check = medication_data.isnull()
            monthly_count = []

            for index in range(1, 32):
                count = 0
                if not null_check.loc[index, '복용1']:
                    count += 1
                if not null_check.loc[index, '복용2']:
                    count += 1
                if not null_check.loc[index, '복용3']:
                    count += 1
                monthly_count.append(count)

            return monthly_count

        def get_medication_time(self):
            medication_data = self.medication_data_to_time()
            null_check = medication_data.isnull()
            result = []

            for index in range(1, 32):
                data = []
                if not null_check.loc[index, '복용1']:
                    data.append(medication_data.loc[index, '복용1'])
                if not null_check.loc[index, '복용2']:
                    data.append(medication_data.loc[index, '복용2'])
                if not null_check.loc[index, '복용3']:
                    data.append(medication_data.loc[index, '복용3'])
                result.append(data)

            return result

        def get_medication_score(self):
            morning = self.get_morning_medication_list()
            lunch = self.get_lunch_medication_list()
            dinner = self.get_dinner_medication_list()
            count = 0
            score1 = 0
            score2 = 0
            score3 = 0

            if morning != None:
                for i in range(0, len(morning)):
                    if morning[i] == True:
                        score1 += 1
                count += 1

            if lunch != None:
                for i in range(0, len(lunch)):
                    if lunch[i] == True:
                        score2 += 1
                count += 1

            if dinner != None:
                for i in range(0, len(dinner)):
                    if dinner[i] == True:
                        score3 += 1
                count += 1

            if count == 1:
                scale = 3
            elif count == 2:
                scale = 1.5
            else:
                scale = 1

            total_score = int((score1 + score2 + score3) * (scale))

            return total_score

        def get_morning_medication_list(self):
            medication_data = self.medication_data_to_time()
            null_check = medication_data.isnull()
            total_count = 0
            result = []

            for index in range(1, 32):
                count = 0
                if not null_check.loc[index, '복용1']:
                    time = total_sec(medication_data.loc[index, '복용1'])
                    if time < 43200:
                        count += 1

                if not null_check.loc[index, '복용2']:
                    time = total_sec(medication_data.loc[index, '복용2'])
                    if time < 43200:
                        count += 1

                if not null_check.loc[index, '복용3']:
                    time = total_sec(medication_data.loc[index, '복용3'])
                    if time < 43200:
                        count += 1

                if count > 0:
                    result.append(True)
                    total_count += 1
                else:
                    result.append(False)

            if total_count < 4:
                return None
            else:
                return result

        def get_lunch_medication_list(self):
            medication_data = self.medication_data_to_time()
            null_check = medication_data.isnull()
            total_count = 0
            result = []

            for index in range(1, 32):
                count = 0
                if not null_check.loc[index, '복용1']:
                    time = total_sec(medication_data.loc[index, '복용1'])
                    if ((time > 43200) & (time < 64800)):
                        count += 1

                if not null_check.loc[index, '복용2']:
                    time = total_sec(medication_data.loc[index, '복용2'])
                    if ((time > 43200) & (time < 64800)):
                        count += 1

                if not null_check.loc[index, '복용3']:
                    time = total_sec(medication_data.loc[index, '복용3'])
                    if ((time > 43200) & (time < 64800)):
                        count += 1

                if count > 0:
                    result.append(True)
                    total_count += 1
                else:
                    result.append(False)

            if total_count < 4:
                return None
            else:
                return result

        def get_dinner_medication_list(self):
            medication_data = self.medication_data_to_time()
            null_check = medication_data.isnull()
            total_count = 0
            result = []

            for index in range(1, 32):
                count = 0
                if not null_check.loc[index, '복용1']:
                    time = total_sec(medication_data.loc[index, '복용1'])
                    if time > 64800:
                        count += 1

                if not null_check.loc[index, '복용2']:
                    time = total_sec(medication_data.loc[index, '복용2'])
                    if time > 64800:
                        count += 1

                if not null_check.loc[index, '복용3']:
                    time = total_sec(medication_data.loc[index, '복용3'])
                    if time > 64800:
                        count += 1

                if count > 0:
                    result.append(True)
                    total_count += 1
                else:
                    result.append(False)

            if total_count < 4:
                return None
            else:
                return result

    class Suni:
        # 여기서부터는 구현 안한 부분!!!
        def __init__(self, user_data):
            self.user_data = user_data

        # 기본점수 30점
        def get_suni_friendly_score(self):
            program_score = self.get_program_participation_score()
            message_data = self.get_message_count()
            sst_data = self.get_sst_count()
            message_count = 0
            sst_count = 0

            for i in range(0, 3):
                message_count += message_data[i]
                sst_count += sst_data[i]

            if message_count == 0:
                response_ratio = 0
            else:
                response_ratio = sst_count / message_count

            communication_score = response_ratio * 30

            total_score = int(program_score * 0.35 + communication_score * 0.35 + 30)

            return total_score

        def get_program_participation_score(self):
            program_count = self.get_total_program_count()
            if program_count == 0:
                program_count = 0
            elif program_count < 50:
                program_count += 20
            elif program_count > 100:
                program_count = 100

            return program_count

        def get_count_method(self):
            program = ['도전 실버벨', '영어교실', '명언산책', '순이대화', '순이 특별대화', '듣는대화', '시낭독', '순이체조',
                       '노래자랑', '요가명상', '마음그림터', '마음 스트레칭', '순이인생', '마음세탁소', '꿀잠소리', '순이극장', '무비순이']
            count = [0] * 17

            data = self.user_data
            for i in range(0, len(program)):
                program_data = data[data['State'] == program[i]]
                if not program_data.empty:
                    count[i] = len(program_data)
                else:
                    count[i] = 0

            return count

        def get_total_program_count(self):
            count = self.get_count_method()
            total_count = 0
            for i in range(0, len(count)):
                total_count += count[i]

            return total_count

        def get_program_count(self):
            program = ['도전 실버벨', '영어교실', '명언산책', '순이대화', '순이 특별대화', '듣는대화', '시낭독', '순이체조',
                       '노래자랑', '요가명상', '마음그림터', '마음 스트레칭', '순이인생', '마음세탁소', '꿀잠소리', '순이극장', '무비순이']
            count = self.get_count_method()
            sorted_count = sorted(count, reverse=True)
            result_list = []
            index = []

            j = 0
            while (True):
                duplicate = 0
                for index in range(0, len(count)):
                    if count[index] == sorted_count[j]:
                        result_list.append((program[index], count[index]))
                        duplicate += 1

                j += duplicate
                if j > len(sorted_count) - 2:
                    break

            result_list = result_list[0:5]

            return result_list

        def get_message_count(self):
            null_check = self.user_data.isnull()
            count1 = 0  # Message1
            count2 = 0  # Message2
            count3 = 0  # Message3

            for index in range(0, len(self.user_data)):
                if not null_check.loc[index, 'Message_1']:
                    count1 += 1
                if not null_check.loc[index, 'Message_2']:
                    count2 += 1
                if not null_check.loc[index, 'Message_3']:
                    count3 += 1

            count = (count1, count2, count3)

            return count

        def get_sst_count(self):
            null_check = self.user_data.isnull()
            count1 = 0  # STT1
            count2 = 0  # STT2
            count3 = 0  # STT3

            for index in range(0, len(self.user_data)):
                if not null_check.loc[index, 'STT_1']:
                    count1 += 1
                if not null_check.loc[index, 'STT_2']:
                    count2 += 1
                if not null_check.loc[index, 'STT_3']:
                    count3 += 1

            count = (count1, count2, count3)

            return count

        def get_program_category_count(self):
            data1 = self.user_data[self.user_data['State'].str.contains('도전 실버벨|영어교실|마음그림터|명언산책')]  # 교육
            data2 = self.user_data[self.user_data['State'].str.contains('순이대화|순이 특별대화|듣는대화|시낭독')]  # 소통
            data3 = self.user_data[self.user_data['State'].str.contains('순이체조|노래자랑|요가명상|마음그림터')]  # 운동
            data4 = self.user_data[self.user_data['State'].str.contains('마음스트레칭|순이인생|마음세탁소|꿀잠소리')]  # 휴식
            data5 = self.user_data[self.user_data['State'].str.contains('순이체조|노래자랑|도전 실버벨|순이극장|마음그림터|무비순이')]  # 엔터

            count1 = len(data1)
            count2 = len(data2)
            count3 = len(data3)
            count4 = len(data4)
            count5 = len(data5)

            count = (count1, count2, count3, count4, count5)

            return count
