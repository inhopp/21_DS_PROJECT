"""
    여기서부터는 각각의 데이터를 불러와서 그래프를 만들거나 적절한 문자열로 변환해주는 함수입니다.
    즉, visualising 을 담당하는 함수를 정의합니다. 다만 몇 가지 문자열만을 hard-code 하면 다소
    진부해 보일 수 있으므로 모두 구현 후 시간이 남으면 리스트에 문자열을 여러 개 추가한 뒤 random하게
    불러와서 보여주는 방식을 취할 예정입니다.

"""
import operator
import random
import matplotlib.pyplot as plt
import PyQt5.QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from numpy import average
from math import pi


plt.rcParams['font.family'] = 'Malgun Gothic'


def tb_main_summary_visualize(exercise_score, sleep_score, eat_score, medication_score, suni_friendly_score=50):
    """
        8월은 '순이와 더 친해지는 계기가 된' 달이었어요.
        8월은 '활력 넘치는' 달이었어요.
        ...
        이처럼 개인 페이지에서 전체 데이터에 대한 요약 정보를 문자열 형태로 반환해 주는 함수입니다.

    :param exercise_score: 운동 종합 점수
    :param sleep_score: 수면 종합 점수
    :param eat_score: 식사 종합 점수
    :param medication_score: 약 복용 종합 점수
    :param suni_friendly_score: 순이와의 친화도 점수
    :return:
    """

    # None인 요소는 분석이 불가능하므로 제외해야 한다.
    category_str = ['exercise_score', 'sleep_score', 'eat_score', 'medication_score', 'suni_friendly_score']
    category_list = [exercise_score, sleep_score, eat_score, medication_score, suni_friendly_score]
    category_list_valid = []

    # 일단 점수대로 정렬해야 하므로 tuple을 리스트에 집어넣고 람다식을 활용하여 정렬을 해준다.
    for i in range(len(category_str)):
        if category_list[i] is not None:
            category_list_valid.append((category_str[i], category_list[i]))

    if len(category_list_valid) == 0:
        return f"8월에는 수집된 데이터가 아예 없네요"

    category_list_sorted = sorted(category_list_valid, key=lambda x: x[1], reverse=True)

    # 1등을 한 점수를 뽑아낸다.
    summarized_category = category_list_sorted[0][0]

    # 1등 결과에 따라서 반환할 문자열을 만든다.
    list_str_exercise = ['활력 넘치는', '활기 넘치는', '활동량이 많은', '힘이 넘치는']
    list_str_sleep = ['잠이 잘 오는', '양질의 수면이 가득한', '꿀잠으로 가득한']
    list_str_eat = ['밥이 잘 넘어가는', '식사 습관이 개선된']
    list_str_medication = ['약을 잘 챙겨먹은', '약 복용을 잘 한']
    list_str_suni = ['순이와 더 가까워진', '순이와 조금 더 친해진', '순이와의 사이가 개선된']

    # category_str = ['exercise_score', 'sleep_score', 'eat_score', 'medication_score', 'suni_friendly_score']
    if summarized_category == 'exercise_score':
        temp_str = random.choice(list_str_exercise)
        return f'8월은 {temp_str} 달이었어요'

    elif summarized_category == 'sleep_score':
        temp_str = random.choice(list_str_sleep)
        return f'8월은 {temp_str} 달이었어요'

    elif summarized_category == 'eat_score':
        temp_str = random.choice(list_str_eat)
        return f'8월은 {temp_str} 달이었어요'

    elif summarized_category == 'medication_score':
        temp_str = random.choice(list_str_medication)
        return f'8월은 {temp_str} 달이었어요'

    else:
        temp_str = random.choice(list_str_suni)
        return f'8월은 {temp_str} 달이었어요'


def tb_personal_info_visualize(name, sex, age):
    """
        박순자 / 여성 / 96세 형태로 문자열을 반환해 준다.
    :param name: 'ID-OOO'
    :param sex: 'F' | 'M'
    :param age: 96
    :return:
    """
    sex_converted = ''
    if sex == 'F':
        sex_converted = '여성'
    elif sex == 'M':
        sex_converted = '남성'
    else:
        sex_converted = '기타'

    return f'{name} / {sex_converted} / {age}세'


def sleep_score_comment_visualize(score, name):
    """
    :param name: 사용자 이름입니다.
    :param score: 수면 점수를 정수형으로 전달받습니다. None을 입력받을 가능성도 있습니다.
    :return: 수면 점수를 포함한 문자열입니다.
    """

    # 여기 있는 5개의 리스트는 결과 출력을 위한 문자열 집합입니다. 리스트 내부의 원소들 중 random하게
    # 선택하는 과정이 구현되어 있으므로 원소를 자유자재로 추가하셔도 됩니다.
    list_str_best = ["님은 이번 달에 굉장히 잠을 잘 주무셨군요! 대단해요!",
                     "님은 잠을 너무너무 잘 주무세요. 제가 더 드릴 말씀이 없군요!"]
    list_str_good = ["님은 이번 달에 잠을 잘 주무셨네요"]
    list_str_mid = ["님은 이번 달에 잠을 보통으로 주무셨네요"]
    list_str_bad = ["님, 요즘 무슨 일 있으신가요? 잠을 자주 설치시는 것 같네요."]
    list_str_worst = ["님, 요즘 잠을 잘 못 주무셔서 건강 상태가 걱정되네요. 진료를 받아보시는게 어떨까요?"]

    # 여기서부터는 앞의 리스트 중 수면 점수에 맞는 리스트를 하나 가져온 뒤, 사용자 이름을 추가하여
    # 결과 문자열을 return 하게 됩니다.

    if score is None:
        return name + "님, 수면 패턴이 기록되지 않았어요. 센서를 한 번 점검해 보세요."
    elif score >= 90:
        return name + random.choice(list_str_best)
    elif score >= 80:
        return name + random.choice(list_str_good)
    elif score >= 65:
        return name + random.choice(list_str_mid)
    elif score >= 45:
        return name + random.choice(list_str_bad)
    else:
        return name + random.choice(list_str_worst)


def insert_sleep_graph(self, sleep_data):
    """
    :param self: 함수 호출 시 MainWidget 객체를 전달하면 됩니다.
    :param sleep_data: Person 클래스의 Sleep 객체에서 get_monthly_sleep_times() 메소드를 이용하여
                       수면 시간 리스트를 받아옵니다.
    :return: None
    """

    # 이미 그래프가 삽입되어 있는 상태에서 reload를 하는 부분이다. 이 부분을 작성하지 않으면 해당 페이지에
    # 들어갈 떄마다 위젯이 하나씩 추가되므로 그래프가 계속해서 늘어나게 된다.
    if not self.ui.graph_verticalLayout.count() >= 1:
        print("그래프가 아직 없네요? 하나 집어넣겠습니다.")
        self.sleep_fig = plt.Figure()
        self.sleep_canvas = FigureCanvas(self.sleep_fig)
        self.ui.graph_verticalLayout.addWidget(self.sleep_canvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout.removeWidget(self.sleep_canvas)
        self.sleep_fig = plt.Figure()
        self.sleep_canvas = FigureCanvas(self.sleep_fig)
        self.ui.graph_verticalLayout.addWidget(self.sleep_canvas)

    x = [x for x in range(1, 31)]
    y = sleep_data
    plt.rc('font', family='Malgun Gothic')
    ax = self.sleep_fig.add_subplot(111)
    ax.plot(x, y, label="sleep time")
    ax.set_xlabel("날짜")
    ax.set_xlabel("수면 시간")

    ax.set_title("my sleep graph")
    ax.legend()
    self.sleep_canvas.draw()


def sleep_suni_comment_visualize(score, name, variance_score):
    """

    :param score: 수면 총 점수, None도 가능
    :param name: 사용자 이름
    :param variance_score: 수면 일정함 점수, None도 가능
    :return:
    """

    # 여기 있는 9개의 리스트는 결과 출력을 위한 문자열 집합입니다. 리스트 내부의 원소들 중 random하게
    # 선택하는 과정이 구현되어 있으므로 원소를 자유자재로 추가하셔도 됩니다.
    # (총 점수 X 분산 점수)의 Cartesian product 로 생각하면 됩니다. 너무 많으면 골치아프므로
    # 3 X 3으로 총 9가지만 정의합니다.

    list_str_good_good = ["님은 수면 시간도 충분하고 규칙적으로 수면을 취하시네요\n순이가 걱정할"
                          "일이 전혀 없을 것 같아요!"]
    list_str_good_mid = ["님은 수면 시간은 충분한데 규칙적으로 수면을 취하시는 것 같지는 않네요\n"
                         " 순이와 함께 매일매일 같은 시간에 잠에 들어봐요"]
    list_str_good_bad = ["님은 잠은 많이 주무시지만 너무 불규칙적으로 잠에 드세요.\n규칙적인"
                         " 수면이 건강에 좋다는거 잘 알고 계시죠?"]

    list_str_mid_good = ["님은 항상 규칙적으로 잠에 드시는군요, 멋저요! \n그런데 수면 시간이 약간 부족한"
                         " 느낌이 있어요"]
    list_str_mid_mid = ["님은 딱 필요한 만큼만 수면을 취하시는군요! 지금보다 조금 더, 그리고 더"
                        " 규칙적으로 수면을 취하면 하루가 더 상쾌해진답니다!"]
    list_str_mid_bad = ["님은 수면 시간은 다른 분들과 비슷한데, 너무 불규칙적으로 잠에 드세요."
                        " 규칙적인 수면이 건강에 좋답니다."]

    list_str_bad_good = ["님은 항상 규칙적으로 조금만 주무시는군요! 수면 시간이 너무 부족하면"
                         " 여러 가지 질병에 걸릴 가능성이 있어요. 요즘 부쩍 피곤하신 것 같지 않으"
                         "신가요?"]
    list_str_bad_mid = ["님은 수면 시간이 너무 부족해요. 그리고 별로 규칙적으로 수면을 취하시는"
                        " 것 같지도 않네요. 순이가 도와드릴테니 수면 개선을 위한 프로그램에 참여해"
                        " 보시면 좋을 것 같아요."]
    list_str_bad_bad = ["님, 요즘 잠드는데 어려움을 겪고 계시는 것 같아요. 수면 시간이 충분하지 않고"
                        " 규칙적이지도 않아서 걱정이 많이 되네요."]

    if None in (score, variance_score):
        # 수면 데이터가 분석 불가능한 경우
        return "수면 데이터가 존재하지 않거나 너무 적어서 분석이 불가능합니다. 센서를 확인해 보세요."

    elif score >= 90:
        if variance_score >= 90:
            return name + random.choice(list_str_good_good)
        elif variance_score >= 70:
            return name + random.choice(list_str_good_mid)
        else:
            return name + random.choice(list_str_good_bad)

    elif score >= 70:
        if variance_score >= 90:
            return name + random.choice(list_str_mid_good)
        elif variance_score >= 70:
            return name + random.choice(list_str_mid_mid)
        else:
            return name + random.choice(list_str_mid_bad)

    else:
        if variance_score >= 90:
            return name + random.choice(list_str_bad_good)
        elif variance_score >= 70:
            return name + random.choice(list_str_bad_mid)
        else:
            return name + random.choice(list_str_bad_bad)


def snack_ratio_suni_comment_visualize(name, snack_ratio):
    """
    :param name: 사용자 이름
    :param snack_ratio: 전체 식사량 대비 간식 섭취량 비율, None도 가능
    :return:
    """

    # 데이터 없을 때
    if snack_ratio is None:
        return f"{name}님은 식사 정보 기록이 없어요. 센서를 한 번 점검해 보세요."

    # 여기 있는 5개의 리스트는 결과 출력을 위한 문자열 집합입니다. 리스트 내부의 원소들 중 random하게
    # 선택하는 과정이 구현되어 있으므로 원소를 자유자재로 추가하셔도 됩니다.

    list_str_stack_ratio_best = ["간식을 거의 드시지 않고 건강한 식사를 하시네요."]
    list_str_snack_ratio_good = ["가끔씩 간식을 드시기는 하지만 주로 식사로 배를 채우시나봐요?"]
    list_str_snack_ratio_mid = ["간식을 즐겨 드시는군요? 입이 심심할 때 간식을 챙겨먹는 것도 좋지만"
                                " 건강을 위해 조금 참아보시는게 어떨까요?"]
    list_str_snack_ratio_bad = ["전체 식사 대비 간식 섭취가 너무 많아요. 영양소가 골고루"
                                " 포함된 음식을 먹어야 좋은 건강을 유지할 수 있어요."]
    list_str_snack_ratio_worst = ["거의 식사를 하지 않고 간식만 드시는군요? 식습관을 고치지"
                                  " 않으시면 영양소 불균형으로 건강 상태가 나빠질 수 있어요."]

    if snack_ratio <= 20:
        return random.choice(list_str_stack_ratio_best)
    elif snack_ratio <= 35:
        return random.choice(list_str_snack_ratio_good)
    elif snack_ratio <= 50:
        return random.choice(list_str_snack_ratio_mid)
    elif snack_ratio <= 70:
        return random.choice(list_str_snack_ratio_bad)
    else:
        return random.choice(list_str_snack_ratio_worst)


def eat_variance_score_visualize(name, variance_score):
    list_str_good = ["식사를 항상 규칙적으로 하시는군요! 대단해요!"]
    list_str_mid = ["대체로 식사 시간을 지키시지만 조금 들쭉날쭉 하네요. 규칙적인 식사 습관을 갖는게 건강에 좋답니다."]
    list_str_bad = ["거의 식사 시간을 정해두지 않으시는군요! 이렇게 불규칙적인 생활을 계속 하시면 건강이 나빠질 수"
                    "있어요. 순이가 하루 3번 식사 시간을 정해서 알려드릴게요!"]
    if variance_score is None:
        return "식사 데이터가 없어서 분석이 불가능합니다"
    elif variance_score >= 70:
        return random.choice(list_str_good)
    elif variance_score >= 40:
        return random.choice(list_str_mid)
    else:
        return random.choice(list_str_bad)


def insert_eat_graph(self, eat_type_list):
    """
        한 달동안 먹은 조식, 중식, 석식 횟수가 31일에서 차지하는 비율을 matplotlib 그래프로
        나타내고 삽입해 줍니다.
    :param self: 함수 호출 시 MainWidget 객체를 전달하면 됩니다.
    :param eat_type_list: Person 클래스의 Eat 객체에서 get_eat_type() 메소드를 이용하여
                       조식, 중식, 석식 횟수 리스트를 받아옵니다.
    :return: None
    """

    # self.donut_fig_eat = plt.Figure()
    # self.eat_type_canvas = FigureCanvas(self.donut_fig_eat)

    # 이미 그래프가 삽입되어 있는 상태에서 reload를 하는 부분이다. 이 부분을 작성하지 않으면 해당 페이지에
    # 들어갈 떄마다 위젯이 하나씩 추가되므로 그래프가 계속해서 늘어나게 된다.
    # if not self.ui.graph_verticalLayout_eat.count() >= 1:
    #     self.ui.graph_verticalLayout_eat.addWidget(self.eat_type_canvas)
    if not self.ui.graph_verticalLayout_eat.count() >= 1:
        print("그래프가 아직 없네요? 하나 집어넣겠습니다.")
        self.donut_fig_eat = plt.Figure()
        self.eat_type_canvas = FigureCanvas(self.donut_fig_eat)
        self.ui.graph_verticalLayout_eat.addWidget(self.eat_type_canvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout_eat.removeWidget(self.eat_type_canvas)
        self.donut_fig_eat = plt.Figure()
        self.eat_type_canvas = FigureCanvas(self.donut_fig_eat)
        self.ui.graph_verticalLayout_eat.addWidget(self.eat_type_canvas)

    colors = ['#d26e60', '#fbc8b4']

    labels_morning = ['섭취', '미섭취']
    sizes_morning = [eat_type_list[0], 31 - eat_type_list[0]]

    labels_lunch = ['섭취', '미섭취']
    sizes_lunch = [eat_type_list[1], 31 - eat_type_list[1]]

    labels_dinner = ['섭취', '미섭취']
    sizes_dinner = [eat_type_list[2], 31 - eat_type_list[2]]

    explode = (0.05, 0.05)

    # create a figure with three subplots
    ax1 = self.donut_fig_eat.add_subplot(131)
    ax1.pie(sizes_morning, explode=explode, labels=labels_morning, autopct='%1.1f%%', shadow=True, startangle=90,
            colors=colors)
    ax2 = self.donut_fig_eat.add_subplot(132)
    ax2.pie(sizes_lunch, explode=explode, labels=labels_lunch, autopct='%1.1f%%', shadow=True, startangle=90,
            colors=colors)
    ax3 = self.donut_fig_eat.add_subplot(133)
    ax3.pie(sizes_dinner, explode=explode, labels=labels_dinner, autopct='%1.1f%%', shadow=True, startangle=90,
            colors=colors)

    self.eat_type_canvas.draw()


def snack_check_mark_visualize(self, snack_ratio, eat_variance_score):
    """
    :param self:
    :param snack_ratio: 간식 섭취 점수 (None도 가능)
    :param eat_variance_score: 규칙적 식사 점수 (None도 가능)
    :return:
    """
    filename1 = ''
    filename2 = ''

    # Load the first check mark
    if snack_ratio is None:
        filename1 = 'question_2.png'
    elif snack_ratio <= 35:
        filename1 = 'green_check.png'
    elif snack_ratio <= 50:
        filename1 = 'question.png'
    else:
        filename1 = 'prohibited.png'

    # Load the second check mark
    if eat_variance_score is None:
        filename2 = 'question_2.png'
    elif eat_variance_score >= 70:
        filename2 = 'green_check.png'
    elif eat_variance_score >= 40:
        filename2 = 'question.png'
    else:
        filename2 = 'prohibited.png'

    check1 = QPixmap(f'images/{filename1}')
    check2 = QPixmap(f'images/{filename2}')

    # 크기 조절을 합니다.
    # self.trafficLight = self.trafficLight.scaled(self.ui.trafficLight.size())

    # label에 이미지를 삽입합니다.
    self.ui.check_1.setPixmap(check1)
    self.ui.check_2.setPixmap(check2)



def exercise_score_comment_visualize(name, score):
    """
    :param name: 사용자 이름
    :param score: 활동성 점수 (None도 가능)
    :return:
    """

    # 여기 있는 5개의 리스트는 결과 출력을 위한 문자열 집합입니다. 리스트 내부의 원소들 중 random하게
    # 선택하는 과정이 구현되어 있으므로 원소를 자유자재로 추가하셔도 됩니다.
    list_str_best = ["님께서는 매일매일 꾸준히 운동을 하시는군요? 한 달동안 운동량이 굉장히 많아요! 열정 넘치게 운동을 하는"
                     " 모습을 순이가 항상 응원할게요!"]
    list_str_good = ["님은 항상 운동을 많이 하셔서 순이가 걱정할 일이 없어요. 대단해요!"]
    list_str_mid = ["님은 적당한 운동으로 건강관리를 하고 계시네요. 가끔씩은 삶의 활력을 위해 열정 넘치게 운동을"
                    "해보는건 어떨까요?"]
    list_str_bad = ["님은 이번 달에 통 움직이지 않으셨군요. 무슨 일이 있는건 아닌지 걱정되네요."]
    list_str_worst = ["님, 이번 달 운동량이 현저히 낮아요. 이러다가 큰일날 수도 있어요. 순이와 함께 열심히 운동해봐요!"]

    if score is None:
        return "수집된 활동 데이터가 전혀 없어요. 센서를 점검해 보셔야 할 것 같아요."
    elif score >= 90:
        return name + random.choice(list_str_best)
    elif score >= 75:
        return name + random.choice(list_str_good)
    elif score >= 50:
        return name + random.choice(list_str_mid)
    elif score >= 35:
        return name + random.choice(list_str_bad)
    else:
        return name + random.choice(list_str_worst)


def insert_activity_graph(self, activity_dict):
    """
        한 달동안 참여한 활동의 비율을 도넛 차트의 형태로 출력해 줍니다.
    :param self: 함수 호출 시 MainWidget 객체를 전달하면 됩니다.
    :param activity_dict: Person 클래스에 있는 Exercise 객체의 get_activity_list() 메소드를 이용해
                          활동 횟수를 받아와 사용합니다.
    :return: None
    """

    # self.donut_fig_activity = plt.Figure()
    # self.activity_canvas = FigureCanvas(self.donut_fig_activity)

    # 이미 그래프가 삽입되어 있는 상태에서 reload를 하는 부분이다. 이 부분을 작성하지 않으면 해당 페이지에
    # 들어갈 떄마다 위젯이 하나씩 추가되므로 그래프가 계속해서 늘어나게 된다.
    # if not self.ui.graph_verticalLayout_activity.count() >= 1:
    #     self.ui.graph_verticalLayout_activity.addWidget(self.activity_canvas)

    if not self.ui.graph_verticalLayout_activity.count() >= 1:
        self.donut_fig_activity = plt.Figure()
        self.activity_canvas = FigureCanvas(self.donut_fig_activity)
        self.ui.graph_verticalLayout_activity.addWidget(self.activity_canvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout_activity.removeWidget(self.activity_canvas)
        self.donut_fig_activity = plt.Figure()
        self.activity_canvas = FigureCanvas(self.donut_fig_activity)
        self.ui.graph_verticalLayout_activity.addWidget(self.activity_canvas)

    # 7개를 모두 출력하면 너무 공간이 없으므로 상위 5개를 뽑는다. 레이블과 값들도 다 적절하게 정해야 한다.
    conversion_dict = {"Program": "프로그램", "TV": "TV 시청", "Exercise_outside": "실외운동",
                       "Exercise_inside": "실내운동", "Rest": "휴식", "Outing": "외출", "Nap": "낮잠"}

    colors = ['#e89dbb', '#22b573', '#00a99d', '#29abe2', '#0071bc', '#8b71dc', '#d97edc']

    # Value를 이용한 내림차순 정렬 -> 많이 참여한 활동부터 정렬
    activity_tuples_list_sorted = sorted(activity_dict.items(), key=operator.itemgetter(1), reverse=True)
    activity_tuples_list_sorted = activity_tuples_list_sorted[:-2]  # 마지막 2개 삭제 -> 5개만 남김.

    labels_activity = []
    sizes_activity = []
    for element in activity_tuples_list_sorted:
        labels_activity.append(conversion_dict[element[0]])
        sizes_activity.append(element[1])

    ax1 = self.donut_fig_activity.add_subplot(111)

    explode = (0.05, 0.05, 0.05, 0.05, 0.05)

    ax1.pie(sizes_activity, labels=labels_activity, autopct='%1.1f%%', shadow=True, startangle=90,
            colors=colors, explode=explode)
    self.activity_canvas.draw()


def activity_visualize_comment(name, activity_dict):
    """
    :param name: 사용자 이름
    :param activity_dict: Person 클래스에 있는 Exercise 객체의 get_activity_list() 메소드를 이용해
                          활동 횟수를 받아와 사용합니다. None도 가능.
    :return:
    """

    # 활동 정보가 없을 때
    if activity_dict is None:
        return "활동 정보가 없어서 분석이 불가능합니다"

    # 우선 가장 많이 참여한 활동을 first_activity에 저장합니다.
    activity_tuples_list_sorted = sorted(activity_dict.items(), key=operator.itemgetter(1), reverse=True)
    first_activity_name, count = activity_tuples_list_sorted[0][0], activity_tuples_list_sorted[0][1]

    list_str_Program = [f"님은 이번 한 달동안 순이와 함께하는 프로그램에 {count}번이나 참여하셨어요. 정말 대단해요!"
                        f" 순이도 {name}님과 함께할 수 있어서 즐거웠어요."]
    list_str_TV = [f"님은 이번 한 달동안 TV를 {count}번이나 시청하셨군요! TV 시청처럼 가만히 앉아서 하는 활동보다는"
                   f" 조금 더 활동적인 취미를 가져보는건 어떨까요?"]
    list_str_Exercise_outside = [f"님은 이번 한 달동안 실외운동을 {count}번이나 하셨어요! 밖에 나가서 자주 운동하시는"
                                 f" {name}님 덕분에 순이도 덩달아 활력이 나는 것 같네요."]
    list_str_Exercise_inside = [f"님은 이번 한 달동안 실내운동을 {count}번이나 하셨어요! {name}님이 운동하시는걸 지켜볼"
                                f" 때마다 순이도 덩달아 활력이 나는 것 같네요."]
    list_str_Rest = [f"님은 이번 한 달동안 휴식을 취하시면서 취미활동을 많이 즐기셨군요! 혹시 다음 달에는 순이와 함께"
                     f" 새로운 취미에 도전해 보시는건 어떨까요?"]
    list_str_Outing = [f"님은 이번 한 달동안 외출을 {count}번이나 하셨어요! {name}님은 밖에 나가시는걸 좋아하시나봐요."]
    list_str_Nap = [f"님은 이번 한 달동안 낮잠을 {count}번이나 주무셨어요! 적당한 낮잠은 피로회복에 좋지만 너무 많은 수면도"
                    f" 오히려 건강에 해롭다는 사실! 알고 계셨나요? 순이가 알람을 맞춰서 깨워드릴게요!"]

    if first_activity_name == "Program":
        return name + random.choice(list_str_Program)
    elif first_activity_name == "TV":
        return name + random.choice(list_str_TV)
    elif first_activity_name == "Exercise_outside":
        return name + random.choice(list_str_Exercise_outside)
    elif first_activity_name == "Exercise_inside":
        return name + random.choice(list_str_Exercise_inside)
    elif first_activity_name == "Rest":
        return name + random.choice(list_str_Rest)
    elif first_activity_name == "Outing":
        return name + random.choice(list_str_Outing)
    else:
        return name + random.choice(list_str_Nap)


def insert_weekly_active_score_graph(self, monthly_active_score_list):
    """
        1, 2, 3, 4, 5주차의 활동 내역을 막대 그래프로 나타냅니다.
    :param monthly_active_score_list: Person 클래스에 있는 Exercise 객체의 get_monthly() 메소드를 이용해
                          활동 횟수를 받아와 사용합니다.
    :param self: 함수 호출 시 MainWidget 객체를 전달하면 됩니다.
    :return: None
    """

    # 이미 그래프가 삽입되어 있는 상태에서 reload를 하는 부분이다. 이 부분을 작성하지 않으면 해당 페이지에
    # 들어갈 떄마다 위젯이 하나씩 추가되므로 그래프가 계속해서 늘어나게 된다.
    # self.ui.graph_verticalLayout_weekActiveScore

    if not self.ui.graph_verticalLayout_weekActiveScore.count() >= 1:
        print("그래프가 아직 없네요? 하나 집어넣겠습니다.")
        self.fig_weekActiveScore = plt.Figure()
        self.weekActiveScoreCanvas = FigureCanvas(self.fig_weekActiveScore)
        self.ui.graph_verticalLayout_weekActiveScore.addWidget(self.weekActiveScoreCanvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout_weekActiveScore.removeWidget(self.weekActiveScoreCanvas)
        self.fig_weekActiveScore = plt.Figure()
        self.weekActiveScoreCanvas = FigureCanvas(self.fig_weekActiveScore)
        self.ui.graph_verticalLayout_weekActiveScore.addWidget(self.weekActiveScoreCanvas)

    # Argument로 전달된 score list는 각 날짜별 정보를 포함하므로 이를 주간 정보로 평균을 내면 된다.
    weekly_active_score_list = [average(monthly_active_score_list[:7]), average(monthly_active_score_list[7:14]),
                                average(monthly_active_score_list[14:21]), average(monthly_active_score_list[21:28]),
                                average(monthly_active_score_list[28:32])]

    # 색상 정의
    color = ['#272b3a', '#f9be2d', '#a3a9aa', '#f9be2d', '#272b3a']
    # x축 레이블
    labels_week = ['1주차', '2주차', '3주차', '4주차', '5주차']

    # 그래프 띄우기
    ax1 = self.fig_weekActiveScore.add_subplot(111)
    ax1.bar(labels_week, weekly_active_score_list, color=color, width=0.4, )

    self.weekActiveScoreCanvas.draw()


def active_score_bar_comment(name, monthly_active_score_list):
    # Argument로 전달된 score list는 각 날짜별 정보를 포함하므로 이를 주간 정보로 평균을 내면 된다.

    # 데이터가 없을 때
    if monthly_active_score_list is None:
        return "충분히 운동을 한 주차 : 분석 불가능", "운동이 조금 더 필요한 주차 : 분석 불가능", "심각한" \
                                                                    " 운동 분족 주차 : 분석 불가능"

    weekly_active_score_list = [average(monthly_active_score_list[:7]), average(monthly_active_score_list[7:14]),
                                average(monthly_active_score_list[14:21]), average(monthly_active_score_list[21:28]),
                                average(monthly_active_score_list[28:32])]

    good = [True if score >= 75 else False for score in weekly_active_score_list]
    mid = [True if 35 <= score < 75 else False for score in weekly_active_score_list]
    bad = [True if score < 35 else False for score in weekly_active_score_list]

    good_weeks_str = ""
    mid_weeks_str = ""
    bad_weeks_str = ""

    for i in range(len(good)):
        good_weeks_str += good[i] * f"{i + 1}주차, "

    for i in range(len(mid)):
        mid_weeks_str += mid[i] * f"{i + 1}주차, "

    for i in range(len(bad)):
        bad_weeks_str += bad[i] * f"{i + 1}주차, "

    # If not empty
    if good_weeks_str:
        good_weeks_str = good_weeks_str[:-2]
        good_weeks_str = "충분히 운동을 한 주차 : " + good_weeks_str
    else:
        good_weeks_str = "충분히 운동을 한 주차 : " + "없음"

    if mid_weeks_str:
        mid_weeks_str = mid_weeks_str[:-2]
        mid_weeks_str = "운동이 조금 더 필요한 주차 : " + mid_weeks_str
    else:
        mid_weeks_str = "운동이 조금 더 필요한 주차 : " + "없음"

    if bad_weeks_str:
        bad_weeks_str = bad_weeks_str[:-2]
        bad_weeks_str = "심각한 운동 부족 주차 : " + bad_weeks_str
    else:
        bad_weeks_str = "심각한 운동 부족 주차 : " + "없음"

    return good_weeks_str, mid_weeks_str, bad_weeks_str


def medication_calendar_visualize(morning, lunch, dinner):
    """
        아침, 점심, 저녁약 복용 여부를 포함한 리스트 3개를 인자로 받아서 이를 'OOX', 'XXX' 형태의 문자열 리스트로
        반환해 줍니다.
    :param morning:
    :param lunch:
    :param dinner:
    :return:
    """
    result_list = [""] * 31

    if morning is not None:
        for i in range(len(morning)):
            # True이면 O를 붙이고 False이면 X를 붙인다.
            result_list[i] += morning[i] * 'O'
            result_list[i] += (not morning[i]) * 'X'

    if lunch is not None:
        for i in range(len(lunch)):
            # True이면 O를 붙이고 False이면 X를 붙인다.
            result_list[i] += lunch[i] * 'O'
            result_list[i] += (not lunch[i]) * 'X'

    if dinner is not None:
        for i in range(len(dinner)):
            # True이면 O를 붙이고 False이면 X를 붙인다.
            result_list[i] += dinner[i] * 'O'
            result_list[i] += (not dinner[i]) * 'X'

    return result_list


def medication_comment_visualize(name, morning, lunch, dinner, score):
    """
    :param name: 사용자 이름
    :param morning: 아침약 boolean list or None
    :param lunch: 점심약 boolean list or None
    :param dinner: 저녁약 boolean list or None
    :param score: 약 복용 규칙성 점수
    :return: 하루에 몇 번 먹는지
    """

    # 우선 약 복용을 언제 하는지에 대한 문자열 생성 (first_comment_str)
    medication_period_str = ''
    includeMorning = morning is not None
    includeLunch = lunch is not None
    includeDinner = dinner is not None
    medication_period_int = (includeMorning, includeLunch, includeDinner).count(True)
    if medication_period_int == 0:
        return f"{name}님은 약을 안 드시네요!", "약 복용 규칙성 평가가 불가능합니다", None, 0

    # 약을 31일중 며칠동안 먹었는지 반환하기 위한 boolean 리스트 생성, OR 연산
    hadMedication = [False] * 31
    if includeMorning:
        hadMedication = [hadMedication[i] or morning[i] for i in range(len(hadMedication))]

    if includeLunch:
        hadMedication = [hadMedication[i] or lunch[i] for i in range(len(hadMedication))]

    if includeDinner:
        hadMedication = [hadMedication[i] or dinner[i] for i in range(len(hadMedication))]

    medication_period_str += includeMorning * '아침, '
    medication_period_str += includeLunch * '점심, '
    medication_period_str += includeDinner * '저녁, '
    medication_period_str = medication_period_str[:-2]

    first_comment_str = f"{name}님은 총 하루 {medication_period_int}번 {medication_period_str}에 약을 드시는군요! "

    # 약 복용 점수에 대한 평가
    list_str_best = [f"그리고 약을 규칙적으로 잘 챙겨 드시는 것 같아서 순이가 마음이 편해요. "]
    list_str_good = [f"그리고 약을 나름 규칙적으로 챙겨 드시는군요! 이정도면 양호해요."]
    list_str_mid = [f"그런데 약은 규칙적으로 잘 챙겨먹어야 의미가 있답니다."]
    list_str_bad = [f"그런데 요즘 약 먹는걸 자주 깜빡하시네요. 알람을 맞춰드릴테니꼭 시간 맞춰 드세요!"]
    list_str_worst = [f"그런데 약을 시간 맞춰 드시지 않는군요. 순이는 {name}님이 걱정돼요."]

    if score >= 85:
        return first_comment_str, random.choice(list_str_best), medication_period_int, hadMedication.count(True)
    elif score >= 70:
        return first_comment_str, random.choice(list_str_good), medication_period_int, hadMedication.count(True)
    elif score >= 55:
        return first_comment_str, random.choice(list_str_mid), medication_period_int, hadMedication.count(True)
    elif score >= 40:
        return first_comment_str, random.choice(list_str_bad), medication_period_int, hadMedication.count(True)
    else:
        return first_comment_str, random.choice(list_str_worst), medication_period_int, hadMedication.count(True)


def medication_count_marks_visualize(self, medication_count, variance_score):
    """
    :param self: 전달된 객체
    :param variance_score: 약 복용 규칙성 점수
    :param medication_count: 하루에 약을 복용하는 횟수
    :return:
    """
    filename1 = ''
    filename2 = ''

    # 우선 하루 복용 횟수 처리
    if medication_count is None:
        filename1 = 'keycap_question.png'
    elif medication_count == 0:
        filename1 = 'keycap_zero.png'
    elif medication_count == 1:
        filename1 = 'keycap_one.png'
    elif medication_count == 2:
        filename1 = 'keycap_two.png'
    elif medication_count == 3:
        filename1 = 'keycap_three.png'
    else:
        filename1 = 'keycap_question.png'

    # 복용 규칙성 점수 처리
    if variance_score is None:
        filename2 = 'keycap_question.png'
    elif variance_score >= 70:
        filename2 = 'green_check.png'
    elif variance_score >= 40:
        filename2 = 'question.png'
    elif variance_score >= 0:
        filename2 = 'prohibited.png'
    else:
        filename2 = 'keycap_question.png'


    check1 = QPixmap(f'images/{filename1}')
    check2 = QPixmap(f'images/{filename2}')

    # 크기 조절을 합니다.
    # self.trafficLight = self.trafficLight.scaled(self.ui.trafficLight.size())

    # label에 이미지를 삽입합니다.
    self.ui.medication_mark1.setPixmap(check1)
    self.ui.medication_mark2.setPixmap(check2)


def medication_right_side_visualize(self, times):
    """
        알약의 오른쪽 횟수, 아래 설명을 시각화합니다.

    :param times: 31일 중 먹은 횟수
    :return:
    """
    self.ui.med_right.setText(str(times))
    self.ui.med_left.setText(str(31))
    self.ui.medication_day_count.setText(f"31일 중 {str(times)}일")

    # 정렬을 해준다
    self.ui.med_left.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
    self.ui.med_right.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
    self.ui.medication_day_count.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
    self.ui.medication_day_count_trail.setAlignment(PyQt5.QtCore.Qt.AlignCenter)




def medication_score_visualize(score):
    """
    :param score: 약 복용 규칙성 점수
    :return:
    """
    score_str = ''
    if score is None:
        score_str = '미존재'
    else:
        score_str = str(score) + '점'

    return f"복용 점수 {score_str}"


def suni_face_visualize(self, score):
    # 점수에 따라서 images 경로에서 이미지를 불러옵니다.
    filename = ''
    if score >= 70:
        filename = 'face_best.png'
    elif score >= 50:
        filename = 'face_good.png'
    elif score >= 30:
        filename = 'face_bad.png'
    else:
        filename = 'face_worst.png'

    self.suni_face = QPixmap(f'images/{filename}')

    # 크기 조절을 합니다.
    self.suni_face = self.suni_face.scaled(self.ui.image_suni_face.size())

    # label에 이미지를 삽입합니다.
    self.ui.image_suni_face.setPixmap(self.suni_face)


def sleep_face_visualize(self, score):
    # 점수에 따라서 images 경로에서 이미지를 불러옵니다.
    filename = ''
    if score is None:
        filename = 'suni.png'
    elif score >= 70:
        filename = 'icon1.png'
    elif score >= 50:
        filename = 'icon2.png'
    elif score >= 30:
        filename = 'icon3.png'
    else:
        filename = 'icon4.png'

    self.sleep_face = QPixmap(f'images/{filename}')

    # 크기 조절을 합니다.
    self.sleep_face = self.sleep_face.scaled(self.ui.label_sleep_face.size())

    # label에 이미지를 삽입합니다.
    self.ui.label_sleep_face.setPixmap(self.sleep_face)


def sleep_light_visualize(self, mean):
    # 수면 평균 시간에 따라서 images 경로에서 이미지를 불러옵니다.
    filename = ''
    if mean is None:
        filename = 'no_data.png'
    elif mean >= 8:
        filename = 'green.png'
    elif mean >= 6:
        filename = 'yellow.png'
    else:
        filename = 'red.png'

    self.trafficLight = QPixmap(f'images/{filename}')

    # 크기 조절을 합니다.
    self.trafficLight = self.trafficLight.scaled(self.ui.trafficLight.size())

    # label에 이미지를 삽입합니다.
    self.ui.trafficLight.setPixmap(self.trafficLight)


def sleep_time_evaluation_visualize(self, mean):
    if mean is None:
        self.ui.sleep_time_evaluation.setText('No Data')
        return

    if mean >= 8:
        self.ui.sleep_time_evaluation.setText('충분히 많이 주무시고 계십니다')
    elif mean >= 6:
        self.ui.sleep_time_evaluation.setText('나쁘지 않은 수면 시간입니다')
    elif mean >= 5:
        self.ui.sleep_time_evaluation.setText('수면 시간이 부족합니다')
    elif mean >= 4:
        self.ui.sleep_time_evaluation.setText('수면 시간이 많이 부족합니다')
    else:
        self.ui.sleep_time_evaluation.setText('수면 시간이 매우 부족합니다')


def suni_talk_comment_visualize(name, count):
    """
    :param name: 사용자 이름
    :param count: 순이와의 총 대화 횟수
    :return:
    """

    list_str_best = [f'{name}님은 순이와 정말 대화를 많이 나누시는군요!']
    list_str_best_trail = f'순이도 {name}님이 있어서 심심하지 않고 좋아요.'

    list_str_good = [f'{name}님은 순이가 말을 걸면 잘 대답해 주세요.']
    list_str_good_trail = f'앞으로도 항상 잘 대답해 주실거죠?'

    list_str_mid = [f'{name}님은 순이가 말을 걸면 가끔씩 무시하세요.']
    list_str_mid_trail = f'순이는 {name}님께 도움이 되는 말씀을 드리니 꼭 대답해 주세요.'

    list_str_bad = [f'{name}님은 순이가 하는 말에 좀처럼 대답을 하지 않으시는군요.']
    list_str_bad_trail = f'그래도 순이는 {name}님과 친해질 수 있도록 더 노력할게요.'

    list_str_worst = [f'{name}님은 순이가 하는 말에 거의 대답을 안 해주세요.']
    list_str_worst_trail = f'다음 번에는 순이의 말에 귀를 기울여 봐요.'

    list_str_none = [f'{name}님은 순이의 말에 한 번도 대답을 안해주셨어요.']
    list_str_none_trail = f'다음 번에는 대답 해주실거죠? 순이가 기대하고 있어요.'

    if count >= 80:
        return random.choice(list_str_best), list_str_best_trail
    elif count >= 50:
        return random.choice(list_str_good), list_str_good_trail
    elif count >= 30:
        return random.choice(list_str_mid), list_str_mid_trail
    elif count >= 20:
        return random.choice(list_str_bad), list_str_bad_trail
    elif count >= 1:
        return random.choice(list_str_worst), list_str_worst_trail
    else:
        return random.choice(list_str_none), list_str_none_trail


def program_participation_comment_visualize(name, score):
    """
    :param name: 사용자 이름
    :param score: 프로그램 참여 점수
    :return:
    """

    list_str_best = ["매우 적극적으로 참여해 주셨습니다."]
    list_str_good = ["프로그램에 자주 참여해 주셨습니다."]
    list_str_mid = ["프로그램에 주기적으로 참여해 주셨습니다."]
    list_str_bad = ["프로그램에 가끔씩 참여해 주셨습니다."]
    list_str_worst = ["프로그램에 거의 참여하지 않으셨습니다."]
    list_str_none = ["프로그램에 아예 참여하지 않으셨습니다."]

    if score >= 85:
        return random.choice(list_str_best)
    elif score >= 65:
        return random.choice(list_str_good)
    elif score >= 45:
        return random.choice(list_str_mid)
    elif score >= 30:
        return random.choice(list_str_bad)
    elif score >= 1:
        return random.choice(list_str_worst)
    else:
        return random.choice(list_str_none)


def suni_summarized_comment(name, score):
    list_str_best = [f'순이와의 궁합 {score}점! {name}님과 순이는 천생연분이에요']
    list_str_good = [f'{name}님과 순이는 요즘들어 부쩍 가까워진 것 같아요']
    list_str_mid = [f'{name}님과 순이는 아직은 어색한 사이에요']
    list_str_bad = [f'순이와의 친밀도가 {score}점으로 낮은 편에 속합니다']
    list_str_worst = [f'순이와 거의 교류를 하지 않으셨습니다']

    if score >= 85:
        return random.choice(list_str_best)
    elif score >= 70:
        return random.choice(list_str_good)
    elif score >= 50:
        return random.choice(list_str_mid)
    elif score >= 30:
        return random.choice(list_str_bad)
    else:
        return random.choice(list_str_worst)


def insert_category_radar_graph_custom(self, program_category_count):
    """
        Matplotlib 테스트를 위한 함수입니다.
    :param self:
    :param program_category_count:
    :return:
    """

    if not self.ui.graph_verticalLayout_radar_chart.count() >= 1:
        print("그래프가 아직 없네요? 하나 집어넣겠습니다.")
        self.fig_radar = plt.Figure()
        self.radarCanvas = FigureCanvas(self.fig_radar)
        self.ui.graph_verticalLayout_radar_chart.addWidget(self.radarCanvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout_radar_chart.removeWidget(self.radarCanvas)
        self.fig_radar = plt.Figure()
        self.radarCanvas = FigureCanvas(self.fig_radar)
        self.ui.graph_verticalLayout_radar_chart.addWidget(self.radarCanvas)

    print("이미 있는지 체크 완료")

    # 방사형 차트를 위해서 레이블과 극좌표 리스트를 만든다.
    labels = ['교육', '소통', '운동', '휴식', '엔터']
    angles = [x / float(5) * (2 * pi) for x in range(5)]
    angles += angles[:1]

    # 그래프 띄우기
    data = program_category_count
    ax1 = self.fig_radar.add_subplot(111, polar=True)

    plt.xticks(angles[:-1], labels, color='grey', size=8)

    ax1.set_theta_offset(pi / 2)
    ax1.set_theta_direction(-1)  # clockwise
    print("ax1 정의 완료")

    data += data[:1]
    ax1.plot(angles, data, linewidth=2, linestyle='solid', color='grey')
    print("ax1.bar 완료")

    # yLabels 설정
    ax1.set_rlabel_position(0)
    ax1.fill(angles, data, 'b', alpha=0.1)
    ax1.set_xticklabels(labels)

    print("ax1.xticks 완료")
    self.radarCanvas.draw()
    print("draw 완료")


def insert_category_radar_graph(self, program_category_count):
    """
        방사형 차트를 집어넣는 함수입니다.
    :param program_category_count: (교육, 소통, 운동, 휴식, 엔터)
    :param self: 함수 호출 시 MainWidget 객체를 전달하면 됩니다.
    :return: None
    """

    # 이미 그래프가 삽입되어 있는 상태에서 reload를 하는 부분이다. 이 부분을 작성하지 않으면 해당 페이지에
    # 들어갈 떄마다 위젯이 하나씩 추가되므로 그래프가 계속해서 늘어나게 된다.
    # self.ui.graph_verticalLayout_weekActiveScore
    print("방사형 차트 함수 호출")
    if not self.ui.graph_verticalLayout_radar_chart.count() >= 1:
        print("그래프가 아직 없네요? 하나 집어넣겠습니다.")
        self.fig_radar = plt.Figure()
        self.radarCanvas = FigureCanvas(self.fig_radar)
        self.ui.graph_verticalLayout_radar_chart.addWidget(self.radarCanvas)
    else:
        # 원래 있던 위젯을 삭제 후 새로운 그래프로 대체한다.
        self.ui.graph_verticalLayout_radar_chart.removeWidget(self.radarCanvas)
        self.fig_radar = plt.Figure()
        self.radarCanvas = FigureCanvas(self.fig_radar)
        self.ui.graph_verticalLayout_radar_chart.addWidget(self.radarCanvas)

    print("이미 있는지 체크 완료")

    # 방사형 차트를 위해서 레이블과 극좌표 리스트를 만든다.
    labels = ['교육', '소통', '운동', '휴식', '엔터']
    angles = [x / float(5) * (2 * pi) for x in range(5)]
    angles += angles[:1]

    # 그래프 띄우기
    data = program_category_count
    ax1 = self.fig_radar.add_subplot(111, polar=True)

    plt.xticks(angles[:-1], labels, color='grey', size=8)

    ax1.set_theta_offset(pi / 2)
    ax1.set_theta_direction(-1)  # clockwise
    print("ax1 정의 완료")

    data += data[:1]
    ax1.plot(angles, data, linewidth=2, linestyle='solid', color='grey')
    print("ax1.bar 완료")

    # yLabels 설정
    ax1.set_rlabel_position(0)
    ax1.fill(angles, data, 'b', alpha=0.1)
    ax1.set_xticklabels(labels)

    print("ax1.xticks 완료")
    self.radarCanvas.draw()
    print("draw 완료")


def visualize_5_programs(self, program_5_names):
    # 프로그램 이름을 key로 하고 그에 해당하는 파일명을 value로 갖는 딕셔너리를 정의합니다.
    program_name_convert_dict = {'도전 실버벨': 'bell', '영어교실': 'english', '마음그림터': 'paint', '명언산책': 'walk',
                                 '순이대화': 'suni_border', '순이 특별대화': 'suni', '듣는대화': 'conversation',
                                 '시낭독': 'poetry', '순이체조': 'exercising', '노래자랑': 'sing', '요가명상': 'meditation',
                                 '마음 스트레칭': 'yoga', '순이인생': 'suni_border', '마음세탁소': 'cry',
                                 '꿀잠소리': 'sleep', '순이극장': 'theater', '무비순이': 'movie'}

    # 우선 filenames 리스트에 [name1.png, name2.png , ...] 꼴로 모두 저장합니다. 길이는 5입니다.
    filenames = [program_name_convert_dict[name] + '.png' for name in program_5_names]
    print("filenames 모두 저장 완료")
    print("filenames:", filenames)

    # QPixmap 객체를 picture_objects 리스트에 모두 저장합니다.
    picture_objects = []
    for filename in filenames:
        picture_objects.append(QPixmap(f'images/{filename}'))

    # 크기 조절
    size = self.ui.program_pic_1.size()
    print("pic_1 size :", size)
    for picture in picture_objects:
        picture = picture.scaled(self.ui.program_pic_1.size(), PyQt5.QtCore.Qt.KeepAspectRatio)
        print("picture resized:", picture.size())

    # 이미지  삽입
    for i in range(1, 6):
        size_eval_str = f'self.ui.program_pic_{i}.setScaledContents(True)'
        picture_eval_str = f"self.ui.program_pic_{i}.setPixmap(picture_objects[{i - 1}])"
        eval(size_eval_str)
        eval(picture_eval_str)

    print("이미지 삽입 완료")


def tb_program_preference_comment(name, program_category_count):
    """
        (교육, 소통, 운동, 휴식, 엔터테인먼트)에 해당하는 프로그램의 참여 횟수를 리스트로 입력받은 뒤
        가장 많이 참여한 범주 / 가장 적게 참여한 범주에 대해서 순이가 조언을 해주도록 한다. 3개의 문자열을
        반환하도록 한다. 만약 프로그램 참여가 없으면 없다고 반환하면 된다. 만약 아예 참가하지 않은 범주가
        있다면 AA, BB, CC는 아예 참가하지 않으셨어요. / 다 조금씩 참가했다면 OO는 거의 하지 않으셨네요.

    :param name: 사용자 이름
    :param program_category_count: (교육, 소통, 운동, 휴식, 엔터테인먼트)
    :return:
    """
    print("preference called!")
    category = ('교육', '소통', '운동', '휴식', '엔터테인먼트')
    Not_participated = '프로그램에 참여하지 않아 분석이 불가능합니다'
    best_str_list = ["배움에 있어서 나이는 숫자에 불과하죠", f"{name}님은 타인과 소통하는걸 좋아하시는군요",
                     "열정 넘치는 운동도 좋지만 무리는 금물!", "요즘 휴식을 자주 취하시네요", f"{name}님은 문화생활을"
                                                                  f" 잘 즐기시는 것 같네요"]

    max_index = np.argmax(program_category_count)
    min_index = np.argmin(program_category_count)

    print("max:", max_index, "min:", min_index)
    if program_category_count[max_index] == 0:
        # 아예 참여 X
        return [Not_participated] * 3

    # 적어도 하나 이상의 프로그램에 참여한 경우
    best1 = best_str_list[max_index]
    best2 = f"{category[max_index]} 카테고리의 프로그램에 {program_category_count[max_index]}번 참여하셨어요"
    worst_str = ''
    if 0 in program_category_count:
        worst_str = f"{category[program_category_count.index(0)]} 카테고리의 프로그램에는 아예 참가하지 않으셨어요"
    else:
        worst_str = f"{category[min_index]} 카테고리의 프로그램에는 거의 참가하지 않으셨네요"

    return best1, best2, worst_str


def circle_bar_visualize(self, score):
    """
        Score가 45점이라고 하면 (100 - 45) / 100 을 문자열로 바꿔서 집어넣어야 한다.
    :param score: 순이 친밀도 점수
    :return:
    """
    css = """QFrame{
	border-radius: 50px;	
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.150 rgba(255, 0, 127, 255), stop:0.145 rgba(255, 255, 255, 0));
    }"""

    if score >= 95:
        score_first = '0.005'
        score_second = '0.000'
    else:
        score_first = str((100 - score) / 100)
        score_second = str((100 - score) / 100 - 0.005)

    css = css.replace('0.150', score_first)
    css = css.replace('0.145', score_second)

    self.ui.circularBar.setStyleSheet(css)
    self.ui.circularText.setText(str(score))


def circle_bar_light_visualize(self, sleep_hour_list):
    """
        우선 한 달 동안의 수면 시간 리스트를 받는다. 만약에 데이터가 없으면 데이터가 없다고 띄워주고
        0시간으로 처리해야 한다.
        수면 분석이 가능한지를 return한다. 가능하다면 평균 시간을, 아니라면 None을 return한다.

    :param sleep_hour_list: 수면 시간 리스트 (한 달), 분석 불가능하면 None
    :return:
    """
    OPTIMAL_TIME = 8
    css = """QFrame{
	border-radius: 50px;	
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.150 rgba(39, 43, 58, 255), stop:0.145 rgba(255, 255, 255, 0));
    }"""

    # 우선 수면 시간이 분석 가능한지를 먼저 고려해야 한다.
    if sleep_hour_list is None:
        # 분석 불가능한 경우
        first_param = '1.000'
        second_param = '0.995'
        css = css.replace('0.150', '1.000')
        css = css.replace('0.145', '0.995')
        self.ui.sleep_average_time.setText('No Data')
        self.ui.circularBar_2.setStyleSheet(css)
        return None

    # 평균 수면 시간을 구한다.
    mean_sleep_time = sum(sleep_hour_list) / len(sleep_hour_list)

    # 6.5시간 -> 6시간 30분 문자열로 바꿔주는 함수 정의
    def hour_to_hourMin(hour):
        h, m = divmod(hour, 1)
        return f"{int(h)}시간 {int(60 * m)}분"

    # 텍스트 연결
    self.ui.sleep_average_time.setText(hour_to_hourMin(mean_sleep_time))

    # 상태바 연결
    first, second = str(round(1 - mean_sleep_time / 8, 3)), str(round(1 - mean_sleep_time / 8, 3) - 0.005)
    if float(first) <= 0.005:
        first, second = '0.005', '0.000'

    css = css.replace('0.150', first)
    css = css.replace('0.145', second)

    self.ui.circularBar_2.setStyleSheet(css)
    return mean_sleep_time
