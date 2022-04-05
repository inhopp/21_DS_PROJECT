import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QCompleter
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QWidget
import PyQt5.QtCore
from test import Ui_MainWindow
import random
from matplotlib.figure import Figure
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFontDatabase, QFont
import PyQt5.QtCore
from os import environ

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from data_implemented import Person, get_one_user
import visualize

USER_LIST = ['228', '230', '232', '273', '276', '315', '339', '341', '342', '476', '477', '479', '486', '488', '490',
             '492', '494', '495', '496', '504', '505', '509', '511', '512', '513', '518', '519', '520', '527', '530',
             '532', '534', '535', '536', '537', '538', '540', '542', '544', '546', '547', '552', '570', '574', '580',
             '581', '582', '583', '585', '633', '635', '636', '642', '644', '650', '653', '654', '655', '656', '658',
             '661', '662', '664', '665', '667', '668', '672', '673', '705', '720', '732', '760', '768', '796', '797',
             '799', '800', '801', '802', '803', '804', '805', '806', '807', '808', '809', '811', '812', '813', '1001',
             '1002', '1003', '1004', '1008', '1009', '1011', '1012', '1013', '1015', '1016', '1018', '1019', '1020',
             '1021', '1022', '1026', '1027', '1028', '1029', '1030', '1032', '1033', '1034', '1036', '1037', '1039',
             '1040', '1042', '1043', '1045', '1046', '1047', '1048', '1050', '1052', '1053', '1054', '1055', '1056',
             '1057', '1059', '1061', '1062', '30016', '30035', '30038', '30039', '30040', '30041', '30043', '30044',
             '30045', '30046', '30047', '30048', '30049', '30050', '30052', '30053', '30055', '30056', '30058', '30059',
             '30061', '30062', '30063', '30064', '30066', '30067', '30069', '30070', '30071', '30072', '30073', '30074',
             '30075', '30076', '30077', '30078', '30079']


class MainWindow:
    def __init__(self):
        self.currentSearchID = -1
        self.currentPerson = None
        # QMainWindow() 생성자는 말 그대로 MainWindow 객체를 하나 생성한다.
        self.main_win = QMainWindow()
        self.main_win.setFixedSize(1024, 859)
        self.msg = QtWidgets.QMessageBox()
        # Inport 해준 모듈에서 ui 파일을 가져온다.
        self.ui = Ui_MainWindow()
        self.main_win.setFixedSize(1024, 859)
        # 여기가 중요하다. 가져온 UI 파일을 import한 모듈에 존재하는 메소드의 매개변수로
        # 넘겨주면 메인 화면이 바뀌는 것이다.
        self.ui.setupUi(self.main_win)

        # 자동완성 기능을 적용하고 엔터 키를 눌러도 검색이 되게 한다.
        completer = QCompleter(USER_LIST)
        completer.popup().setStyleSheet("""font: 25pt "Nanum Brush Script";""")
        self.ui.id_blank.setCompleter(completer)
        self.ui.id_blank.returnPressed.connect(self.search)

        # 검색을 잘못했을 때 보여줄 아이콘이다.
        self.errorIcon = QPixmap('images/suni.png')

        # 크기 조절을 합니다.
        self.errorIcon = self.errorIcon.scaled(50, 50)



    # 크기 조절을 합니다.
    # self.trafficLight = self.trafficLight.scaled(self.ui.trafficLight.size())


        # 람다식을 이용하여 각각의 버튼들을 눌렀을 때 현재 위젯을 바꿔줄 수 있다. 이걸 이용하면 다 구현 가능할 것 같다.
        # QStackedWidget 안에는 QWidget 객체들이 들어가므로 해당 객체들만 잘 구현하면 된다.
        # self.ui.btn_total.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.total))
        # self.ui.btn_individual.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.individual))

        # 폰트 연결
        print("폰트 연결을 시작합니다")
        QFontDatabase.addApplicationFont('fonts/AppleSDGothicNeoB.ttf')
        QFontDatabase.addApplicationFont('fonts/NanumBrushScript-Regular.ttf')
        QFontDatabase.addApplicationFont('fonts/KirangHaerang-Regular.ttf')
        QFontDatabase.addApplicationFont('fonts/ygo160.ttf')
        print("폰트 연결이 끝났습니다")

        # 홈, 뒤로가기 버튼 연결을 위한 내부 함수
        print("home 버튼, 뒤로가기 버튼을 연결합니다")
        def home():
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_search_page)

        def back():
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_page)

        for i in range(1, 7):
            eval_str = f"self.ui.btn_home_{i}.clicked.connect(home)"
            eval(eval_str)

        # 뒤로가기 버튼 연결
        for i in range(1, 6):
            eval_str = f"self.ui.btn_back_{i}.clicked.connect(back)"
            eval(eval_str)

        print("개인별 선택 화면에서 수면, 식사, 운동, 약 복용 화면 버튼을 연결합니다")
        # 개인별 선택 화면에서 수면, 식사, 운동, 약 복용 화면 버튼 연결
        self.ui.btn_individual_sleep.clicked.connect(self.open_individual_sleep)
        self.ui.btn_individual_eat.clicked.connect(self.open_individual_eat)
        self.ui.btn_individual_exercise.clicked.connect(self.open_individual_exercise)
        self.ui.btn_individual_medication.clicked.connect(self.open_individual_medication)

        print("면, 식사, 운동, 약 복용 보고서에서 다른 항목으로 이동 버튼을 연결합니다")
        # 수면, 식사, 운동, 약 복용 보고서에서 다른 항목으로 이동 버튼 연결
        self.ui.btn_goto_sleep.clicked.connect(self.open_individual_sleep)
        self.ui.btn_goto_sleep_2.clicked.connect(self.open_individual_sleep)
        self.ui.btn_goto_sleep_3.clicked.connect(self.open_individual_sleep)
        self.ui.btn_goto_eat.clicked.connect(self.open_individual_eat)
        self.ui.btn_goto_eat_2.clicked.connect(self.open_individual_eat)
        self.ui.btn_goto_eat_3.clicked.connect(self.open_individual_eat)
        self.ui.btn_goto_exercise.clicked.connect(self.open_individual_exercise)
        self.ui.btn_goto_exercise_2.clicked.connect(self.open_individual_exercise)
        self.ui.btn_goto_exercise_3.clicked.connect(self.open_individual_exercise)
        self.ui.btn_goto_medication.clicked.connect(self.open_individual_medication)
        self.ui.btn_goto_medication_2.clicked.connect(self.open_individual_medication)
        self.ui.btn_goto_medication_3.clicked.connect(self.open_individual_medication)

        print("순이와의 대화, 프로그램 참여 버튼 연결, 개별 사용자 id 검색 버튼 연결")
        # 순이와의 대화, 프로그램 참여 버튼 연결
        self.ui.btn_goto_suni_1.clicked.connect(self.open_suni)
        self.ui.btn_goto_suni_2.clicked.connect(self.open_suni)
        self.ui.btn_goto_suni_3.clicked.connect(self.open_suni)
        self.ui.btn_goto_suni_4.clicked.connect(self.open_suni)
        self.ui.btn_goto_suni_5.clicked.connect(self.open_suni)

        # 개별 사용자 id 검색 버튼 연결
        self.ui.btn_idSearch.clicked.connect(self.search)


    # 개인별 수면 화면을 열어서 정보를 보여주는 메소드이다.
    def open_individual_sleep(self):
        print("open_individual_sleep 호출")
        person = self.currentPerson

        print("사용자 이름, 수면 점수를 저장합니다")
        name = person.name  # 사용자 이름을 저장

        if person.sleepData.exclude():
            sleep_score = None
        else:
            sleep_score = person.sleepData.get_sleep_overall_score()  # 수면 점수 저장 (None도 가능)

        if person.sleepData.exclude():
            sleep_score_variance = None
            sleep_score_str = "No Data"
        else:
            sleep_score_variance = person.sleepData.get_sleep_variance_score() # 수면 패턴 저장 (None도 가능)
            sleep_score_str = "수면 점수 " + str(sleep_score) + "점!"  # 수면 점수 출력 형식 지정


        print("수면 점수에 대한 평가를 5개 범주로 연결합니다")
        # 수면 점수에 대한 평가 연결 (5개 범주로 구분)
        sleep_score_evaluation_str = visualize.sleep_score_comment_visualize(sleep_score, name)
        self.ui.monthly_sleep_score.setText(sleep_score_str)
        self.ui.sleep_evaluation.setText(sleep_score_evaluation_str)

        print("수면 품질에 대한 순이의 잔소리 연결 (9개 범주로 구분)")
        # 수면 품질에 대한 순이의 잔소리 연결 (9개 범주로 구분)
        sleep_suni_evaluation_str = visualize.sleep_suni_comment_visualize(sleep_score, name, sleep_score_variance)
        self.ui.label_sleep_suni_talk.setText(sleep_suni_evaluation_str)

        print("수면 점수에 따른 얼굴 표정 삽입 (4개 범주로 구분)")
        # 수면 점수에 따른 얼굴 표정 삽입 (4개 범주로 구분)
        visualize.sleep_face_visualize(self, sleep_score)

        print("수면 Matplotlib 그래프 삽입")
        # Matplotlib 그래프 삽입
        if person.sleepData.exclude():
            sleep_time_list = None
        else:
            sleep_time_list = person.sleepData.get_monthly_sleep_times()
            visualize.insert_sleep_graph(self, sleep_time_list)

        # 신호등 삽입
        # 만약 분석 불가능하면 리스트를 아예 None으로 바꿔서 이를 알려준다.
        print("Sleep - 신호등을 삽입합니다")
        if person.sleepData.exclude():
            sleep_time_list = None

        print("수면 시간 원형 바를 띄웁니다")
        mean_sleep_time = visualize.circle_bar_light_visualize(self, sleep_time_list)
        visualize.sleep_light_visualize(self, mean_sleep_time)

        print("수면 시간이 충분한지 텍스트를 삽입합니다")
        # 수면 시간 충분한지 텍스트 삽입
        visualize.sleep_time_evaluation_visualize(self, mean_sleep_time)

        # 현재 창을 개인별 수면 창으로 변경
        print("현재 창을 개인별 수면 창으로 변경합니다")
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_sleep)

    # 개인별 식사 화면 열기
    def open_individual_eat(self):
        print("open_individual_eat 호출, person 저장")
        person = self.currentPerson
        isExcluded = person.eatData.exclude()
        name = person.name

        print("식사 점수 텍스트 연결")
        # 식사 점수 받아와서 텍스트 연결

        if isExcluded:
            eat_score = None
            eat_score_str = "No Data"
        else:
            eat_score = person.eatData.get_eat_score()
            eat_score_str = str(eat_score) + "점"

        # 데이터 연결
        self.ui.monthly_eat_score.setText(eat_score_str)

        print("식사 횟수 텍스트 연결")
        # 식사 횟수 받아와서 텍스트 연결
        if isExcluded:
            snack_eat_count = 0
            total_eat_count = 0
        else:
            snack_eat_count = sum(person.eatData.get_monthly_eat_snack_count())
            total_eat_count = sum(person.eatData.get_monthly_eat_count())

        self.ui.snack_eat_count.setText(str(snack_eat_count) + '회')
        self.ui.total_eat_count.setText(str(total_eat_count) + '회')


        print("식사 간식 비율 평가 텍스트 연결")
        # 식사와 간식 비율에 대한 순이의 평가 텍스트 연결
        if isExcluded:
            snack_ratio = None
        else:
            snack_ratio = (snack_eat_count / total_eat_count) * 100

        snack_ratio_str = visualize.snack_ratio_suni_comment_visualize(name, snack_ratio)
        self.ui.snack_ratio_comment.setText(snack_ratio_str)


        print("식사 규칙성 순이 평가 텍스트 연결")
        # 식사 규칙성에 대한 순이의 평가 텍스트 연결
        if isExcluded:
            eat_variance_score = None
        else:
            eat_variance_score = person.eatData.get_eat_variance_score()
        eat_variance_suni_comment = visualize.eat_variance_score_visualize(name, eat_variance_score)
        self.ui.eat_time_analysis.setText(eat_variance_suni_comment)


        print("체크 표시 그림 삽입")
        # 체크 표시 그림 삽입
        visualize.snack_check_mark_visualize(self, snack_ratio, eat_variance_score)

        print("matplotlib 그래프 삽입")
        # 식사 횟수 matplotlib 그래프 연결
        if isExcluded:
            eat_type_list = None
        else:
            eat_type_list = person.eatData.get_eat_type()
            visualize.insert_eat_graph(self, eat_type_list)

        print("visualize 호출 완료")

        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_eat)


    # 개인별 운동 화면 열기
    def open_individual_exercise(self):
        person = self.currentPerson
        name = person.name
        isExcluded = person.exerciseData.exclude()

        # 운동 점수 받아와서 텍스트 연결
        if isExcluded:
            exercise_score = None
            exercise_score_str = "0점"
        else:
            exercise_score = person.exerciseData.get_total_active_score()
            exercise_score_str = str(exercise_score) + "점"

        self.ui.monthly_exercise_score.setText(exercise_score_str)

        # 운동 점수에 대한 평가를 받아와서 텍스트 연결
        exercise_score_comment = visualize.exercise_score_comment_visualize(name, exercise_score)
        self.ui.exercise_score_comment.setText(exercise_score_comment)

        # 이번 달 OOO님의 평균 활동 분석이에요. 문자열 연결
        label_activity_with_name = f"이번 달 {name}님의 평균 활동 분석이에요"
        self.ui.label_activity_with_name.setText(label_activity_with_name)

        # 활동 matplotlib 그래프 연결5
        if isExcluded:
            activity_dict = None
        else:
            activity_dict = person.exerciseData.get_activity_list()
            visualize.insert_activity_graph(self, activity_dict)

        # 활동 그래프 보여준 후 이에 대한 평가
        activity_list_comment = visualize.activity_visualize_comment(name, activity_dict)
        self.ui.label_activity_list_comment.setText(activity_list_comment)

        # 한 달 동안 주별 활동성 수치 그래프 삽입
        if isExcluded:
            monthly_active_score_list = None
        else:
            monthly_active_score_list = person.exerciseData.get_monthly_active_score()
            visualize.insert_weekly_active_score_graph(self, monthly_active_score_list)

        # 주별 활동성 수치 평가 텍스트 연결
        good, mid, bad = visualize.active_score_bar_comment(name, monthly_active_score_list)
        self.ui.label_active_week_good.setText(good)
        self.ui.label_active_week_mid.setText(mid)
        self.ui.label_active_week_bad.setText(bad)

        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_exercise)


    # 개인별 약 복용 화면 열기
    def open_individual_medication(self):
        person = self.currentPerson
        name = person.name
        isExcluded = person.medicationData.exclude()

        # 약 복용 규칙성 점수 가져오기
        if isExcluded:
            score = None
        else:
            score = person.medicationData.get_medication_score()

        # 약 복용 점수 문자열 가져오기
        score_str = visualize.medication_score_visualize(score)
        self.ui.medication_variance_score.setText(score_str)

        # 약 복용 달력 가져와서 텍스트 연결
        morning_medication_boolean = person.medicationData.get_morning_medication_list()
        lunch_medication_boolean = person.medicationData.get_lunch_medication_list()
        dinner_medication_boolean = person.medicationData.get_dinner_medication_list()

        medication_calendar = visualize.medication_calendar_visualize(morning_medication_boolean,
                                                                      lunch_medication_boolean,
                                                                      dinner_medication_boolean)

        # 하나하나 연결하지 않고 format 문자열과 eval 활용
        for i in range(1, 32):
            evaluation_str = f"self.ui.day{i}_2.setText(medication_calendar[{i} - 1])"
            eval(evaluation_str)

        print("달력 eval 완료")
        # 약 복용 달력 코멘트와 문자열 2개 연결
        # 반환값 (comment1, comment2, 하루 복용 횟수)
        medication_calendar_comment = visualize.medication_comment_visualize(name, morning_medication_boolean,
                                                                             lunch_medication_boolean,
                                                                             dinner_medication_boolean,
                                                                             score)

        # 알약 오른쪽 횟수 시각화
        visualize.medication_right_side_visualize(self, medication_calendar_comment[3])

        # 1회, 2회, 3회, 초록색 체크표시 연결
        visualize.medication_count_marks_visualize(self, medication_calendar_comment[2], score)

        self.ui.medication_calendar_comment.setText(medication_calendar_comment[0])
        self.ui.medication_calendar_comment_2.setText(medication_calendar_comment[1])

        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_medication)


    # 순이와의 대화, 프로그램 참여 창 열기
    def open_suni(self):
        person = self.currentPerson
        name = person.name

        # 순이와의 친밀도 점수를 가져온다.
        friendly_score = person.suniData.get_suni_friendly_score()
        friendly_score_str = str(friendly_score) + '점'
        self.ui.label_suni_friendly_score.setText(friendly_score_str)

        # 순이 표정 넣기
        visualize.suni_face_visualize(self, friendly_score)

        # 순이와의 대화 횟수 채우기
        sst_sum = sum(person.suniData.get_sst_count())
        sst_sum_str = str(sst_sum) + '회'
        self.ui.label_suni_talk_count.setText(sst_sum_str)

        # 순이와의 대화 점수에 대한 코멘트 연결
        suni_talk_comment = visualize.suni_talk_comment_visualize(name, sst_sum)
        self.ui.label_suni_talk_count_comment.setText(suni_talk_comment[0])
        self.ui.label_suni_talk_count_comment_2.setText(suni_talk_comment[1])

        # 순이의 프로그램 전체 참여 횟수 (label_program_total_count) 텍스트 연결
        program_total_count_str = str(person.suniData.get_total_program_count()) + '회'
        self.ui.label_program_total_count.setText(program_total_count_str)

        # 프로그램 참여도 (label_program_comment) 텍스트 연결
        program_participation_score = person.suniData.get_program_participation_score()
        program_comment_str = visualize.program_participation_comment_visualize(name, program_participation_score)
        self.ui.label_program_comment.setText(program_comment_str)

        # 상위 5개 프로그램과 참여 횟수 텍스트 연결
        program_5_count_list = person.suniData.get_program_count()

        for i in range(1, 6):
            # 프로그램 이름 5개 연결
            name_eval_str = f"self.ui.label_program_{i}_name.setText(program_5_count_list[i - 1][0])"
            eval(name_eval_str)
            # 프로그램 빈도 5개 연결
            count_eval_str = f"self.ui.label_program_{i}_count.setText(str(program_5_count_list[i - 1][1]) + '회')"
            eval(count_eval_str)

        # 프로그램 사진 5개 연결
        program_5_names = [element[0] for element in program_5_count_list]
        print("프로그램 이름 받아오기 완료")
        visualize.visualize_5_programs(self, program_5_names)
        print("이미지 삽입 모두 완료")

        # 프로그램 참여 관련 방사형 차트 띄우기
        program_category_count = person.suniData.get_program_category_count()
        print("Progra_category_count 받아오기 완료")
        visualize.insert_category_radar_graph(self, program_category_count)
        print("방사형 차트 삽입 완료")

        # 현재 창을 순이 창으로 변경
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_suni)
        print("창 변경 완료")

        # 참여한 프로그램의 특성 설명 텍스트 연결
        program_preference_comment = visualize.tb_program_preference_comment(name, program_category_count)
        print("comment: ", program_preference_comment)
        self.ui.tb_program_preference_comment_1.setText(program_preference_comment[0])
        self.ui.tb_program_preference_comment_2.setText(program_preference_comment[1])
        self.ui.tb_program_preference_comment_3.setText(program_preference_comment[2])

    def search(self):
        # 검색한 아이디를 객체의 currentSearchID 필드에 저장하고 person 객체를 받아온다.
        # 이후에 정보 출력을 위해 이름, 성별, 나이도 받이온다.

        temp = self.ui.id_blank.text()
        if temp != '':
            self.currentSearchID = int(temp)
            self.currentSearchID = int(self.ui.id_blank.text())
        else:
            self.currentSearchID = None

        # print("Person 객체를 딕셔너리에서 가져옵니다")
        # person = person_dic[self.currentSearchID.__str__()]

        self.currentPerson = get_one_user(self.currentSearchID)

        # 만약 None이라면 검색이 제대로 안 된 것이므로 경고창을 띄운다.
        if self.currentPerson is None:
            self.msg.setWindowTitle('다시 확인해 주세요')
            self.msg.setText('잘못된 아이디를 입력하셨습니다.')
            self.msg.setIconPixmap(self.errorIcon)
            ret = self.msg.exec_()
            return


        person = self.currentPerson

        print("name, sex, age를 가져옵니다")
        name = self.currentPerson.name
        sex = self.currentPerson.sex
        age = self.currentPerson.age

        # person 객체를 통해서 메인 페이지에 요약 정보를 보여줘야 하므로 점수들을
        # 모두 가져온다.
        print("메인 페이지에서 사용할 점수 5가지를 모두 가져옵니다")
        print("운동 점수 가져오기")
        if self.currentPerson.exerciseData.exclude():
            exercise_score = None
        else:
            exercise_score = self.currentPerson.exerciseData.get_total_active_score()

        print("수면 점수 가져오기")
        if self.currentPerson.sleepData.exclude():
            sleep_score = None
        else:
            sleep_score = self.currentPerson.sleepData.get_sleep_overall_score()

        print("식사 점수 가져오기")
        if self.currentPerson.eatData.exclude():
            eat_score = None
        else:
            eat_score = self.currentPerson.eatData.get_eat_score()

        print("의약품 점수 가져오기")
        if self.currentPerson.medicationData.exclude():
            medication_score = None
        else:
            medication_score = self.currentPerson.medicationData.get_medication_score()

        print("순이 친밀도 점수 가져오기")
        suni_friendly_score = self.currentPerson.suniData.get_suni_friendly_score()

        # visualize 모듈에서 정의한 함수를 통해서 화면에 띄울 문자열을 받아온다.
        tb_main_summary_str = visualize.tb_main_summary_visualize(exercise_score, sleep_score, eat_score,
                                                                       medication_score, suni_friendly_score)

        # 위젯에 접근해서 텍스트를 바꾸어 준다.
        self.ui.tb_main_summary.setText(tb_main_summary_str)

        # OOO / 여성 / 75세 textBox를 띄우는 부분이다.
        tb_personal_info_str = visualize.tb_personal_info_visualize(name, sex, age)
        self.ui.tb_personal_info.setText(tb_personal_info_str)

        # OOO님, 순이와 함께 보낸 시간을 보러 가볼까요? 를 띄우는 부분이다.
        tb_suni_time_str = "순이와 함께 보낸 시간을 확인하러 가볼까요?"
        self.ui.tb_suni_time.setText(tb_suni_time_str)
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.individual_page)

        # 순이와 궁합 65점! 우리는 점점 가까워지는 중 을 띄우는 부분이다.
        suni_summarized_comment_str = visualize.suni_summarized_comment(name, suni_friendly_score)
        self.ui.suni_summarized_comment.setText(suni_summarized_comment_str)

        # woman / man 사진 띄우기
        if sex == 'F':
            self.ui.label.setPixmap(QtGui.QPixmap("images/woman.png"))
            self.ui.label.setScaledContents(True)
        else:
            self.ui.label.setPixmap(QtGui.QPixmap("images/man.png"))
            self.ui.label.setScaledContents(True)

        # 원형 막대 게이지 채우기
        visualize.circle_bar_visualize(self, person.suniData.get_suni_friendly_score())

    def show(self):
        self.main_win.show()


# def suppress_warnings():
#     environ["QT_DEVICE_PIXEL_RATIO"] = "0"
#     environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     environ["QT_SCREEN_SCALE_FACTORS"] = "1"
#     environ["QT_SCALE_FACTOR"] = "1"

if __name__ == '__main__':
    # suppress_warnings()
    # Handle high resolution displays:
    # QApplication.setAttribute(PyQt5.QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
