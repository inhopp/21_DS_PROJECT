# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_please.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 960)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 960))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 960))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 3, -1, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(1050, 910))
        self.scrollArea.setMaximumSize(QtCore.QSize(1050, 910))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1031, 968))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.mainStackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.mainStackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainStackedWidget.setSizePolicy(sizePolicy)
        self.mainStackedWidget.setMinimumSize(QtCore.QSize(1000, 950))
        self.mainStackedWidget.setMaximumSize(QtCore.QSize(1000, 950))
        self.mainStackedWidget.setSizeIncrement(QtCore.QSize(1000, 720))
        self.mainStackedWidget.setBaseSize(QtCore.QSize(1000, 950))
        self.mainStackedWidget.setAcceptDrops(True)
        self.mainStackedWidget.setAutoFillBackground(True)
        self.mainStackedWidget.setStyleSheet("#tb_personal_info{\n"
"  background: transparent;\n"
"}\n"
"\n"
"#tb_main_summary{\n"
"  qproperty-alignment: AlignCenter;\n"
"}")
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.individual_search_page = QtWidgets.QWidget()
        self.individual_search_page.setObjectName("individual_search_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.individual_search_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_4 = QtWidgets.QWidget(self.individual_search_page)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_13 = QtWidgets.QFrame(self.widget_4)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.widget_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_16.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_23.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setMinimumSize(QtCore.QSize(435, 440))
        self.frame_17.setMaximumSize(QtCore.QSize(435, 440))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.widget_6 = QtWidgets.QWidget(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:10px;")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_39 = QtWidgets.QLabel(self.widget_5)
        self.label_39.setStyleSheet("color:rgba(0,0,0, 200);\n"
"font: 30pt \"Nanum Brush Script\";\n"
"background-color: transparent;")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_46.addWidget(self.label_39, 0, QtCore.Qt.AlignHCenter)
        self.label_38 = QtWidgets.QLabel(self.widget_5)
        self.label_38.setMaximumSize(QtCore.QSize(200, 200))
        self.label_38.setStyleSheet("background-color: transparent;")
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("images/suni.svg"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_46.addWidget(self.label_38, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout_15.addWidget(self.widget_5)
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setStyleSheet("color:rgba(0,0,0, 200);\n"
"font: 30pt \"Nanum Brush Script\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.frame_24 = QtWidgets.QFrame(self.widget_6)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.id_blank = QtWidgets.QLineEdit(self.frame_24)
        self.id_blank.setMinimumSize(QtCore.QSize(0, 40))
        self.id_blank.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;\n"
"font: 25pt \"Nanum Brush Script\";\n"
"qproperty-alignment: AlignCenter;")
        self.id_blank.setObjectName("id_blank")
        self.horizontalLayout_37.addWidget(self.id_blank)
        self.btn_idSearch = QtWidgets.QPushButton(self.frame_24)
        self.btn_idSearch.setMinimumSize(QtCore.QSize(150, 50))
        self.btn_idSearch.setStyleSheet("QPushButton#btn_idSearch{\n"
"  font: 18pt \"Apple SD Gothic Neo\";\n"
"  background-color:rgba(85,98,112,255);\n"
"  color: rgba(255,255,255,200);\n"
"  border-radius:15px;\n"
"}\n"
"QPushButton#btn_idSearch:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(225,107,107,225);\n"
"  background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_idSearch:hover{\n"
"  background-color:rgba(225,107,107,225);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_idSearch.setIcon(icon)
        self.btn_idSearch.setIconSize(QtCore.QSize(30, 30))
        self.btn_idSearch.setObjectName("btn_idSearch")
        self.horizontalLayout_37.addWidget(self.btn_idSearch, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_15.addWidget(self.frame_24)
        self.horizontalLayout_28.addWidget(self.widget_6)
        self.horizontalLayout_23.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_14)
        self.frame_18.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_23.addWidget(self.frame_18)
        self.verticalLayout_10.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.widget_4)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_10.addWidget(self.frame_15)
        self.gridLayout_6.addWidget(self.widget_4, 0, 2, 1, 1)
        self.mainStackedWidget.addWidget(self.individual_search_page)
        self.individual_page = QtWidgets.QWidget()
        self.individual_page.setMinimumSize(QtCore.QSize(1000, 800))
        self.individual_page.setMaximumSize(QtCore.QSize(1000, 100000))
        self.individual_page.setObjectName("individual_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.individual_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_10 = QtWidgets.QWidget(self.individual_page)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_10.setMaximumSize(QtCore.QSize(10000000, 100))
        self.widget_10.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;\n"
"color:white;\n"
"padding-top:5px;")
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_home_1 = QtWidgets.QPushButton(self.widget_10)
        self.btn_home_1.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_home_1.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_home_1.setBaseSize(QtCore.QSize(25, 25))
        self.btn_home_1.setStyleSheet("QPushButton#btn_home_1{\n"
"font: bold 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid white;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_1:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}\n"
"")
        self.btn_home_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home_1.setIcon(icon1)
        self.btn_home_1.setIconSize(QtCore.QSize(30, 30))
        self.btn_home_1.setObjectName("btn_home_1")
        self.horizontalLayout_13.addWidget(self.btn_home_1, 0, QtCore.Qt.AlignVCenter)
        self.tb_main_summary = QtWidgets.QLabel(self.widget_10)
        self.tb_main_summary.setMinimumSize(QtCore.QSize(0, 70))
        self.tb_main_summary.setStyleSheet("font: bold 23pt \"AppleSDGothicNeoB00\";")
        self.tb_main_summary.setWordWrap(True)
        self.tb_main_summary.setObjectName("tb_main_summary")
        self.horizontalLayout_13.addWidget(self.tb_main_summary)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.individual_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setMinimumSize(QtCore.QSize(985, 145))
        self.widget_11.setMaximumSize(QtCore.QSize(985, 145))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label = QtWidgets.QLabel(self.widget_11)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(130, 130))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/woman.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.tb_personal_info = QtWidgets.QLabel(self.widget_11)
        self.tb_personal_info.setStyleSheet("font: 30pt \"AppleSDGothicNeoB00\";")
        self.tb_personal_info.setObjectName("tb_personal_info")
        self.horizontalLayout_14.addWidget(self.tb_personal_info, 0, QtCore.Qt.AlignBottom)
        self.tb_suni_recommendation = QtWidgets.QLabel(self.widget_11)
        self.tb_suni_recommendation.setText("")
        self.tb_suni_recommendation.setObjectName("tb_suni_recommendation")
        self.horizontalLayout_14.addWidget(self.tb_suni_recommendation)
        self.verticalLayout_7.addWidget(self.widget_11)
        self.ButtonForm = QtWidgets.QWidget(self.individual_page)
        self.ButtonForm.setMinimumSize(QtCore.QSize(985, 400))
        self.ButtonForm.setMaximumSize(QtCore.QSize(985, 400))
        self.ButtonForm.setObjectName("ButtonForm")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.ButtonForm)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_13 = QtWidgets.QWidget(self.ButtonForm)
        self.widget_13.setMinimumSize(QtCore.QSize(240, 0))
        self.widget_13.setMaximumSize(QtCore.QSize(240, 16777215))
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_33 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("font: 24pt \"AppleSDGothicNeoB00\";")
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_5.addWidget(self.label_33)
        self.btn_individual_sleep = QtWidgets.QPushButton(self.widget_13)
        self.btn_individual_sleep.setStyleSheet("QPushButton#btn_individual_sleep{\n"
"    font: 25pt \"AppleSDGothicNeoB00\";\n"
"    background-color: rgb(237, 227, 255);\n"
"    text-align: bottom;\n"
"    padding: 20px;\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#btn_individual_sleep:pressed{\n"
"    padding-left:5px;\n"
"      padding-top:5px;\n"
"      background-color:rgb(255, 179, 150);\n"
"      background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_individual_sleep:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}")
        self.btn_individual_sleep.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/sleep2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_individual_sleep.setIcon(icon2)
        self.btn_individual_sleep.setIconSize(QtCore.QSize(150, 150))
        self.btn_individual_sleep.setObjectName("btn_individual_sleep")
        self.verticalLayout_5.addWidget(self.btn_individual_sleep)
        self.horizontalLayout_15.addWidget(self.widget_13)
        self.widget_14 = QtWidgets.QWidget(self.ButtonForm)
        self.widget_14.setMinimumSize(QtCore.QSize(240, 0))
        self.widget_14.setMaximumSize(QtCore.QSize(240, 16777215))
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_35 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("font: 24pt \"AppleSDGothicNeoB00\";")
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_22.addWidget(self.label_35)
        self.btn_individual_eat = QtWidgets.QPushButton(self.widget_14)
        self.btn_individual_eat.setStyleSheet("QPushButton#btn_individual_eat{\n"
"font: 25pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 20px;\n"
"border: 1px solid orange;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#btn_individual_eat:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgb(255, 179, 150);\n"
"  background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_individual_eat:hover{\n"
"  background-color:rgba(225,107,107,225);\n"
"  color:white;\n"
"}")
        self.btn_individual_eat.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/eat2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_individual_eat.setIcon(icon3)
        self.btn_individual_eat.setIconSize(QtCore.QSize(150, 150))
        self.btn_individual_eat.setObjectName("btn_individual_eat")
        self.verticalLayout_22.addWidget(self.btn_individual_eat)
        self.horizontalLayout_15.addWidget(self.widget_14)
        self.widget_15 = QtWidgets.QWidget(self.ButtonForm)
        self.widget_15.setMinimumSize(QtCore.QSize(240, 0))
        self.widget_15.setMaximumSize(QtCore.QSize(240, 16777215))
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_49 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("font: 24pt \"AppleSDGothicNeoB00\";")
        self.label_49.setWordWrap(True)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_23.addWidget(self.label_49)
        self.btn_individual_exercise = QtWidgets.QPushButton(self.widget_15)
        self.btn_individual_exercise.setAutoFillBackground(False)
        self.btn_individual_exercise.setStyleSheet("QPushButton#btn_individual_exercise{\n"
"font: 25pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 20px;\n"
"background-color:orange;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#btn_individual_exercise:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgb(255, 179, 150);\n"
"  background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_individual_exercise:hover{\n"
"  background-color:rgba(225,107,107,225);\n"
"}")
        self.btn_individual_exercise.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/workout1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_individual_exercise.setIcon(icon4)
        self.btn_individual_exercise.setIconSize(QtCore.QSize(150, 150))
        self.btn_individual_exercise.setObjectName("btn_individual_exercise")
        self.verticalLayout_23.addWidget(self.btn_individual_exercise)
        self.horizontalLayout_15.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.ButtonForm)
        self.widget_16.setMinimumSize(QtCore.QSize(240, 0))
        self.widget_16.setMaximumSize(QtCore.QSize(240, 16777215))
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_50 = QtWidgets.QLabel(self.widget_16)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("font: 24pt \"AppleSDGothicNeoB00\";")
        self.label_50.setWordWrap(True)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_24.addWidget(self.label_50)
        self.btn_individual_medication = QtWidgets.QPushButton(self.widget_16)
        self.btn_individual_medication.setStyleSheet("\n"
"\n"
"QPushButton#btn_individual_medication{\n"
"    font: 25pt \"AppleSDGothicNeoB00\";\n"
"    text-align: bottom;\n"
"    padding: 20px;\n"
"    border: 1px solid purple;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#btn_individual_medication:pressed{\n"
"    padding-left:5px;\n"
"      padding-top:5px;\n"
"      background-color:rgb(255, 179, 150);\n"
"      background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_individual_medication:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}")
        self.btn_individual_medication.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/medication1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_individual_medication.setIcon(icon5)
        self.btn_individual_medication.setIconSize(QtCore.QSize(150, 150))
        self.btn_individual_medication.setObjectName("btn_individual_medication")
        self.verticalLayout_24.addWidget(self.btn_individual_medication)
        self.horizontalLayout_15.addWidget(self.widget_16)
        self.verticalLayout_7.addWidget(self.ButtonForm)
        self.widget_17 = QtWidgets.QWidget(self.individual_page)
        self.widget_17.setMinimumSize(QtCore.QSize(985, 135))
        self.widget_17.setMaximumSize(QtCore.QSize(985, 135))
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_7 = QtWidgets.QFrame(self.widget_17)
        self.frame_7.setMinimumSize(QtCore.QSize(120, 120))
        self.frame_7.setMaximumSize(QtCore.QSize(120, 120))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_27.setSpacing(7)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.circularBar = QtWidgets.QFrame(self.frame_7)
        self.circularBar.setMinimumSize(QtCore.QSize(100, 100))
        self.circularBar.setMaximumSize(QtCore.QSize(100, 100))
        self.circularBar.setStyleSheet("QFrame{\n"
"    border-radius: 50px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.150 rgba(255, 0, 127, 255), stop:0.145 rgba(255, 255, 255, 0));\n"
"}")
        self.circularBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBar.setObjectName("circularBar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.circularBar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.circularContainer_5 = QtWidgets.QFrame(self.circularBar)
        self.circularContainer_5.setMinimumSize(QtCore.QSize(82, 82))
        self.circularContainer_5.setMaximumSize(QtCore.QSize(85, 85))
        self.circularContainer_5.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_5.setStyleSheet("QFrame{\n"
"    border-radius: 41px;    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.circularContainer_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_5.setObjectName("circularContainer_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.circularContainer_5)
        self.gridLayout_11.setContentsMargins(-1, -1, 11, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.circularText = QtWidgets.QLabel(self.circularContainer_5)
        self.circularText.setMinimumSize(QtCore.QSize(50, 50))
        self.circularText.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.circularText.setFont(font)
        self.circularText.setStyleSheet("color: rgb(0, 0, 0); padding: 0px; background-color: none;\n"
"font: 30pt \"AppleSDGothicNeoB00\";")
        self.circularText.setAlignment(QtCore.Qt.AlignCenter)
        self.circularText.setIndent(-1)
        self.circularText.setObjectName("circularText")
        self.gridLayout_11.addWidget(self.circularText, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.circularContainer_5, 0, 0, 1, 1)
        self.verticalLayout_27.addWidget(self.circularBar)
        self.horizontalLayout_11.addWidget(self.frame_7)
        self.widget_9 = QtWidgets.QWidget(self.widget_17)
        self.widget_9.setMinimumSize(QtCore.QSize(685, 120))
        self.widget_9.setMaximumSize(QtCore.QSize(685, 120))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.tb_suni_time = QtWidgets.QLabel(self.widget_9)
        self.tb_suni_time.setStyleSheet("font:bold 20pt \"AppleSDGothicNeoB00\";\n"
"")
        self.tb_suni_time.setWordWrap(True)
        self.tb_suni_time.setObjectName("tb_suni_time")
        self.verticalLayout_25.addWidget(self.tb_suni_time)
        self.suni_summarized_comment = QtWidgets.QLabel(self.widget_9)
        self.suni_summarized_comment.setStyleSheet("font: 15pt \"AppleSDGothicNeoB00\";")
        self.suni_summarized_comment.setWordWrap(True)
        self.suni_summarized_comment.setObjectName("suni_summarized_comment")
        self.verticalLayout_25.addWidget(self.suni_summarized_comment)
        self.horizontalLayout_11.addWidget(self.widget_9)
        self.btn_goto_suni_1 = QtWidgets.QPushButton(self.widget_17)
        self.btn_goto_suni_1.setMinimumSize(QtCore.QSize(150, 100))
        self.btn_goto_suni_1.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_goto_suni_1.setStyleSheet("QPushButton#btn_goto_suni_1{\n"
"  font: 18pt \"AppleSDGothicNeoB00\";\n"
"  background-color:rgba(85,98,112,255);\n"
"  color: rgba(255,255,255,200);\n"
"  border-radius:2px;\n"
"  margin-right:10px;\n"
"}\n"
"QPushButton#btn_goto_suni_1:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(225,107,107,225);\n"
"  background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#btn_goto_suni_1:hover{\n"
"  background-color:rgba(225,107,107,225);\n"
"}")
        self.btn_goto_suni_1.setObjectName("btn_goto_suni_1")
        self.horizontalLayout_11.addWidget(self.btn_goto_suni_1)
        self.verticalLayout_7.addWidget(self.widget_17)
        self.mainStackedWidget.addWidget(self.individual_page)
        self.individual_sleep = QtWidgets.QWidget()
        self.individual_sleep.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.individual_sleep.setObjectName("individual_sleep")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.individual_sleep)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_23 = QtWidgets.QWidget(self.individual_sleep)
        self.widget_23.setMinimumSize(QtCore.QSize(0, 400))
        self.widget_23.setObjectName("widget_23")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_23)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_verticalLayout = QtWidgets.QVBoxLayout()
        self.graph_verticalLayout.setObjectName("graph_verticalLayout")
        self.horizontalLayout.addLayout(self.graph_verticalLayout)
        self.widget_24 = QtWidgets.QWidget(self.widget_23)
        self.widget_24.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_24.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_24.setObjectName("widget_24")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.widget_24)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_52 = QtWidgets.QLabel(self.widget_24)
        self.label_52.setStyleSheet("font:18pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_52.setObjectName("label_52")
        self.verticalLayout_31.addWidget(self.label_52)
        self.frame_8 = QtWidgets.QFrame(self.widget_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_8.setMaximumSize(QtCore.QSize(200, 200))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.circularBar_2 = QtWidgets.QFrame(self.frame_8)
        self.circularBar_2.setMinimumSize(QtCore.QSize(150, 150))
        self.circularBar_2.setMaximumSize(QtCore.QSize(200, 150))
        self.circularBar_2.setStyleSheet("QFrame{\n"
"    border-radius: 50px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.150 rgba(39, 43, 58, 255), stop:0.145 rgba(255, 255, 255, 0));\n"
"}")
        self.circularBar_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBar_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.circularBar_2.setObjectName("circularBar_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.circularBar_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.circularContainer_6 = QtWidgets.QFrame(self.circularBar_2)
        self.circularContainer_6.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_6.setStyleSheet("QFrame{\n"
"    border-radius: 41px;    \n"
"    background-color: rgb(192, 192, 192);\n"
"}")
        self.circularContainer_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_6.setObjectName("circularContainer_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.circularContainer_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.sleep_average_time = QtWidgets.QLabel(self.circularContainer_6)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoB00")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sleep_average_time.setFont(font)
        self.sleep_average_time.setStyleSheet("color: rgb(0, 0, 0); padding: 0px; background-color: none;\n"
"font: 18pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.sleep_average_time.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sleep_average_time.setAlignment(QtCore.Qt.AlignCenter)
        self.sleep_average_time.setIndent(-1)
        self.sleep_average_time.setObjectName("sleep_average_time")
        self.gridLayout_13.addWidget(self.sleep_average_time, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_12.addWidget(self.circularContainer_6, 0, 0, 1, 1)
        self.verticalLayout_30.addWidget(self.circularBar_2)
        self.verticalLayout_31.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget_30 = QtWidgets.QWidget(self.widget_24)
        self.widget_30.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.sleep_time_evaluation = QtWidgets.QLabel(self.widget_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sleep_time_evaluation.sizePolicy().hasHeightForWidth())
        self.sleep_time_evaluation.setSizePolicy(sizePolicy)
        self.sleep_time_evaluation.setStyleSheet("font: 15pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.sleep_time_evaluation.setWordWrap(True)
        self.sleep_time_evaluation.setObjectName("sleep_time_evaluation")
        self.horizontalLayout_25.addWidget(self.sleep_time_evaluation)
        self.trafficLight = QtWidgets.QLabel(self.widget_30)
        self.trafficLight.setMinimumSize(QtCore.QSize(80, 80))
        self.trafficLight.setMaximumSize(QtCore.QSize(80, 80))
        self.trafficLight.setText("")
        self.trafficLight.setPixmap(QtGui.QPixmap("images/red.png"))
        self.trafficLight.setScaledContents(True)
        self.trafficLight.setObjectName("trafficLight")
        self.horizontalLayout_25.addWidget(self.trafficLight, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_31.addWidget(self.widget_30)
        self.horizontalLayout.addWidget(self.widget_24, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addWidget(self.widget_23, 2, 0, 1, 1)
        self.widget_25 = QtWidgets.QWidget(self.individual_sleep)
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_28 = QtWidgets.QWidget(self.widget_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy)
        self.widget_28.setStyleSheet("background-color: rgb(255, 188, 159);\n"
"border-radius: 20px;\n"
"padding:5px;\n"
"content: \"\";\n"
"width: 0px;\n"
"height: 0px;\n"
"position: absolute;\n"
"border-left: 24px solid rgb(255, 188, 159);\n"
"border-right: 12px solid transparent;\n"
"border-top: 12px solid rgb(255, 188, 159);\n"
"left: 32px;\n"
"bottom: -24px;\n"
"")
        self.widget_28.setObjectName("widget_28")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.widget_28)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_sleep_suni_talk = QtWidgets.QLabel(self.widget_28)
        self.label_sleep_suni_talk.setStyleSheet("font: 15pt \"AppleSDGothicNeoB00\";")
        self.label_sleep_suni_talk.setWordWrap(True)
        self.label_sleep_suni_talk.setObjectName("label_sleep_suni_talk")
        self.verticalLayout_29.addWidget(self.label_sleep_suni_talk)
        self.horizontalLayout_3.addWidget(self.widget_28)
        self.label_suni = QtWidgets.QLabel(self.widget_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_suni.sizePolicy().hasHeightForWidth())
        self.label_suni.setSizePolicy(sizePolicy)
        self.label_suni.setMinimumSize(QtCore.QSize(100, 100))
        self.label_suni.setMaximumSize(QtCore.QSize(100, 100))
        self.label_suni.setText("")
        self.label_suni.setPixmap(QtGui.QPixmap("images/suni_border.svg"))
        self.label_suni.setScaledContents(True)
        self.label_suni.setObjectName("label_suni")
        self.horizontalLayout_3.addWidget(self.label_suni, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addWidget(self.widget_25, 3, 0, 1, 1)
        self.frame_sleep_score = QtWidgets.QWidget(self.individual_sleep)
        self.frame_sleep_score.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_sleep_score.setObjectName("frame_sleep_score")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_sleep_score)
        self.horizontalLayout_19.setSpacing(15)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_48 = QtWidgets.QLabel(self.frame_sleep_score)
        self.label_48.setMaximumSize(QtCore.QSize(100, 100))
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap("images/sleep2_border.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.horizontalLayout_19.addWidget(self.label_48)
        self.monthly_sleep_score = QtWidgets.QLabel(self.frame_sleep_score)
        self.monthly_sleep_score.setMinimumSize(QtCore.QSize(0, 100))
        self.monthly_sleep_score.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.monthly_sleep_score.setObjectName("monthly_sleep_score")
        self.horizontalLayout_19.addWidget(self.monthly_sleep_score, 0, QtCore.Qt.AlignLeft)
        self.widget_29 = QtWidgets.QWidget(self.frame_sleep_score)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy)
        self.widget_29.setObjectName("widget_29")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_29)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.sleep_evaluation = QtWidgets.QLabel(self.widget_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sleep_evaluation.sizePolicy().hasHeightForWidth())
        self.sleep_evaluation.setSizePolicy(sizePolicy)
        self.sleep_evaluation.setStyleSheet("font:18pt \"AppleSDGothicNeoB00\";\n"
"border: 1px solid rgb(255, 138, 53);\n"
"border-radius: 20px;\n"
"padding:5px;\n"
"qproperty-alignment: AlignCenter;")
        self.sleep_evaluation.setWordWrap(True)
        self.sleep_evaluation.setObjectName("sleep_evaluation")
        self.horizontalLayout_22.addWidget(self.sleep_evaluation)
        self.label_sleep_face = QtWidgets.QLabel(self.widget_29)
        self.label_sleep_face.setMinimumSize(QtCore.QSize(80, 80))
        self.label_sleep_face.setMaximumSize(QtCore.QSize(80, 80))
        self.label_sleep_face.setText("")
        self.label_sleep_face.setPixmap(QtGui.QPixmap("images/icon4.png"))
        self.label_sleep_face.setScaledContents(True)
        self.label_sleep_face.setObjectName("label_sleep_face")
        self.horizontalLayout_22.addWidget(self.label_sleep_face)
        self.horizontalLayout_19.addWidget(self.widget_29)
        self.gridLayout_5.addWidget(self.frame_sleep_score, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.individual_sleep)
        self.widget.setMinimumSize(QtCore.QSize(0, 130))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget.setStyleSheet("background-color:rgb(255, 179, 150);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_26 = QtWidgets.QWidget(self.widget)
        self.widget_26.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.btn_home_2 = QtWidgets.QPushButton(self.widget_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_2.sizePolicy().hasHeightForWidth())
        self.btn_home_2.setSizePolicy(sizePolicy)
        self.btn_home_2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_home_2.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_home_2.setStyleSheet("QPushButton#btn_home_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_2:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_home_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/1433244.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home_2.setIcon(icon6)
        self.btn_home_2.setIconSize(QtCore.QSize(80, 80))
        self.btn_home_2.setObjectName("btn_home_2")
        self.horizontalLayout_38.addWidget(self.btn_home_2)
        self.btn_back_1 = QtWidgets.QPushButton(self.widget_26)
        self.btn_back_1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_back_1.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_back_1.setBaseSize(QtCore.QSize(100, 25))
        self.btn_back_1.setStyleSheet("QPushButton#btn_back_1{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_back_1:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_back_1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/1433243.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back_1.setIcon(icon7)
        self.btn_back_1.setIconSize(QtCore.QSize(80, 80))
        self.btn_back_1.setObjectName("btn_back_1")
        self.horizontalLayout_38.addWidget(self.btn_back_1)
        self.horizontalLayout_2.addWidget(self.widget_26, 0, QtCore.Qt.AlignLeft)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(300, 25))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setStyleSheet("font:25pt \"AppleSDGothicNeoB00\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.widget_27 = QtWidgets.QWidget(self.widget)
        self.widget_27.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_27.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_27.setObjectName("widget_27")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_27)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btn_goto_eat = QtWidgets.QPushButton(self.widget_27)
        self.btn_goto_eat.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat.setStyleSheet("QPushButton#btn_goto_eat{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_eat:hover{\n"
"    background-color:rgb(253, 128, 8);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_eat.setObjectName("btn_goto_eat")
        self.gridLayout_8.addWidget(self.btn_goto_eat, 0, 0, 1, 1)
        self.btn_goto_exercise = QtWidgets.QPushButton(self.widget_27)
        self.btn_goto_exercise.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise.setStyleSheet("QPushButton#btn_goto_exercise{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_exercise:hover{\n"
"    background-color:rgb(136, 189, 255);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.btn_goto_exercise.setObjectName("btn_goto_exercise")
        self.gridLayout_8.addWidget(self.btn_goto_exercise, 0, 1, 1, 1)
        self.btn_goto_medication = QtWidgets.QPushButton(self.widget_27)
        self.btn_goto_medication.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication.setStyleSheet("QPushButton#btn_goto_medication{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_medication:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_medication.setObjectName("btn_goto_medication")
        self.gridLayout_8.addWidget(self.btn_goto_medication, 1, 0, 1, 1)
        self.btn_goto_suni_2 = QtWidgets.QPushButton(self.widget_27)
        self.btn_goto_suni_2.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_2.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_2.setStyleSheet("QPushButton#btn_goto_suni_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_suni_2:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_suni_2.setObjectName("btn_goto_suni_2")
        self.gridLayout_8.addWidget(self.btn_goto_suni_2, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_27, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)
        self.mainStackedWidget.addWidget(self.individual_sleep)
        self.individual_eat = QtWidgets.QWidget()
        self.individual_eat.setObjectName("individual_eat")
        self.gridLayout = QtWidgets.QGridLayout(self.individual_eat)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_37 = QtWidgets.QWidget(self.individual_eat)
        self.widget_37.setObjectName("widget_37")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.widget_37)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.graph_verticalLayout_eat = QtWidgets.QVBoxLayout()
        self.graph_verticalLayout_eat.setObjectName("graph_verticalLayout_eat")
        self.verticalLayout_34.addLayout(self.graph_verticalLayout_eat)
        self.widget_38 = QtWidgets.QWidget(self.widget_37)
        self.widget_38.setObjectName("widget_38")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.widget_38)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.widget_39 = QtWidgets.QWidget(self.widget_38)
        self.widget_39.setObjectName("widget_39")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_39)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.check_1 = QtWidgets.QLabel(self.widget_39)
        self.check_1.setMinimumSize(QtCore.QSize(100, 100))
        self.check_1.setMaximumSize(QtCore.QSize(100, 99))
        self.check_1.setText("")
        self.check_1.setPixmap(QtGui.QPixmap("images/green_check.png"))
        self.check_1.setScaledContents(True)
        self.check_1.setObjectName("check_1")
        self.horizontalLayout_6.addWidget(self.check_1)
        self.widget_41 = QtWidgets.QWidget(self.widget_39)
        self.widget_41.setObjectName("widget_41")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.widget_41)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_3 = QtWidgets.QLabel(self.widget_41)
        self.label_3.setStyleSheet("font:18pt \"AppleSDGothicNeoB00\";\n"
"padding:5px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_36.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.snack_ratio_comment = QtWidgets.QLabel(self.widget_41)
        self.snack_ratio_comment.setEnabled(True)
        self.snack_ratio_comment.setStyleSheet("background-color : rgb(242, 239, 244);\n"
"padding:5px;\n"
"font: 13pt \"AppleSDGothicNeoB00\";\n"
"")
        self.snack_ratio_comment.setWordWrap(True)
        self.snack_ratio_comment.setObjectName("snack_ratio_comment")
        self.verticalLayout_36.addWidget(self.snack_ratio_comment)
        self.horizontalLayout_6.addWidget(self.widget_41)
        self.verticalLayout_35.addWidget(self.widget_39)
        self.widget_40 = QtWidgets.QWidget(self.widget_38)
        self.widget_40.setObjectName("widget_40")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.widget_40)
        self.horizontalLayout_26.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.check_2 = QtWidgets.QLabel(self.widget_40)
        self.check_2.setMinimumSize(QtCore.QSize(100, 100))
        self.check_2.setMaximumSize(QtCore.QSize(100, 100))
        self.check_2.setText("")
        self.check_2.setPixmap(QtGui.QPixmap("images/prohibited.png"))
        self.check_2.setScaledContents(True)
        self.check_2.setObjectName("check_2")
        self.horizontalLayout_26.addWidget(self.check_2)
        self.widget_42 = QtWidgets.QWidget(self.widget_40)
        self.widget_42.setObjectName("widget_42")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.widget_42)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_15 = QtWidgets.QLabel(self.widget_42)
        self.label_15.setStyleSheet("font:18pt \"AppleSDGothicNeoB00\";\n"
"padding:5px;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_37.addWidget(self.label_15)
        self.eat_time_analysis = QtWidgets.QLabel(self.widget_42)
        self.eat_time_analysis.setStyleSheet("background-color : rgb(242, 239, 244);\n"
"padding:5px;\n"
"font: 13pt \"AppleSDGothicNeoB00\";\n"
"")
        self.eat_time_analysis.setWordWrap(True)
        self.eat_time_analysis.setObjectName("eat_time_analysis")
        self.verticalLayout_37.addWidget(self.eat_time_analysis)
        self.horizontalLayout_26.addWidget(self.widget_42)
        self.verticalLayout_35.addWidget(self.widget_40)
        self.verticalLayout_34.addWidget(self.widget_38)
        self.gridLayout.addWidget(self.widget_37, 2, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.individual_eat)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_2.setStyleSheet("background-color: orange;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_64 = QtWidgets.QWidget(self.widget_2)
        self.widget_64.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_64.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_64.setObjectName("widget_64")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.widget_64)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.btn_home_3 = QtWidgets.QPushButton(self.widget_64)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_3.sizePolicy().hasHeightForWidth())
        self.btn_home_3.setSizePolicy(sizePolicy)
        self.btn_home_3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_home_3.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_home_3.setStyleSheet("QPushButton#btn_home_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_3:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_home_3.setText("")
        self.btn_home_3.setIcon(icon6)
        self.btn_home_3.setIconSize(QtCore.QSize(80, 80))
        self.btn_home_3.setObjectName("btn_home_3")
        self.horizontalLayout_39.addWidget(self.btn_home_3)
        self.btn_back_2 = QtWidgets.QPushButton(self.widget_64)
        self.btn_back_2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_back_2.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_back_2.setBaseSize(QtCore.QSize(100, 25))
        self.btn_back_2.setStyleSheet("QPushButton#btn_back_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_back_2:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_back_2.setText("")
        self.btn_back_2.setIcon(icon7)
        self.btn_back_2.setIconSize(QtCore.QSize(80, 80))
        self.btn_back_2.setObjectName("btn_back_2")
        self.horizontalLayout_39.addWidget(self.btn_back_2)
        self.horizontalLayout_4.addWidget(self.widget_64, 0, QtCore.Qt.AlignLeft)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setMinimumSize(QtCore.QSize(300, 25))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_9.setSizeIncrement(QtCore.QSize(0, 25))
        self.label_9.setStyleSheet("font:25pt \"AppleSDGothicNeoB00\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(self.widget_2)
        self.frame_10.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.btn_goto_sleep = QtWidgets.QPushButton(self.frame_10)
        self.btn_goto_sleep.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep.setStyleSheet("QPushButton#btn_goto_sleep{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_sleep:hover{\n"
"    background-color:rgb(255, 179, 150);\n"
"    color: white;\n"
"}")
        self.btn_goto_sleep.setObjectName("btn_goto_sleep")
        self.gridLayout_9.addWidget(self.btn_goto_sleep, 0, 0, 1, 1)
        self.btn_goto_exercise_2 = QtWidgets.QPushButton(self.frame_10)
        self.btn_goto_exercise_2.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise_2.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise_2.setStyleSheet("QPushButton#btn_goto_exercise_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_exercise_2:hover{\n"
"    background-color:rgb(136, 189, 255);\n"
"    color: white;\n"
"}")
        self.btn_goto_exercise_2.setObjectName("btn_goto_exercise_2")
        self.gridLayout_9.addWidget(self.btn_goto_exercise_2, 0, 1, 1, 1)
        self.btn_goto_medication_2 = QtWidgets.QPushButton(self.frame_10)
        self.btn_goto_medication_2.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication_2.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication_2.setStyleSheet("QPushButton#btn_goto_medication_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_medication_2:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_medication_2.setObjectName("btn_goto_medication_2")
        self.gridLayout_9.addWidget(self.btn_goto_medication_2, 1, 0, 1, 1)
        self.btn_goto_suni_3 = QtWidgets.QPushButton(self.frame_10)
        self.btn_goto_suni_3.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_3.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_3.setStyleSheet("QPushButton#btn_goto_suni_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_suni_3:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_suni_3.setObjectName("btn_goto_suni_3")
        self.gridLayout_9.addWidget(self.btn_goto_suni_3, 1, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 2)
        self.widget_31 = QtWidgets.QWidget(self.individual_eat)
        self.widget_31.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_31.setObjectName("widget_31")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.widget_31)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.widget_36 = QtWidgets.QWidget(self.widget_31)
        self.widget_36.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_36.setObjectName("widget_36")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.widget_36)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_18 = QtWidgets.QLabel(self.widget_36)
        self.label_18.setMaximumSize(QtCore.QSize(100, 100))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("images/eat.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_33.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(self.widget_36)
        self.label_13.setStyleSheet("font: 13pt \"Kirang Haerang\";\n"
"color: rgb(174, 0, 29);\n"
"qproperty-alignment: AlignCenter;")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_33.addWidget(self.label_13)
        self.horizontalLayout_24.addWidget(self.widget_36, 0, QtCore.Qt.AlignLeft)
        self.widget_32 = QtWidgets.QWidget(self.widget_31)
        self.widget_32.setObjectName("widget_32")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_32)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.snack_eat_count = QtWidgets.QLabel(self.widget_32)
        self.snack_eat_count.setStyleSheet("font: 36pt \"Kirang Haerang\";\n"
"")
        self.snack_eat_count.setObjectName("snack_eat_count")
        self.verticalLayout_11.addWidget(self.snack_eat_count, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_24.addWidget(self.widget_32)
        self.widget_33 = QtWidgets.QWidget(self.widget_31)
        self.widget_33.setObjectName("widget_33")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_33)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.widget_33)
        self.label_5.setMaximumSize(QtCore.QSize(100, 100))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/eat2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.widget_33)
        self.label_14.setStyleSheet("font: 13pt \"Kirang Haerang\";\n"
"color: rgb(174, 0, 29);\n"
"qproperty-alignment: AlignCenter;")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_24.addWidget(self.widget_33, 0, QtCore.Qt.AlignLeft)
        self.total_eat_count = QtWidgets.QLabel(self.widget_31)
        self.total_eat_count.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.total_eat_count.setObjectName("total_eat_count")
        self.horizontalLayout_24.addWidget(self.total_eat_count, 0, QtCore.Qt.AlignLeft)
        self.widget_34 = QtWidgets.QWidget(self.widget_31)
        self.widget_34.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_34.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_34.setObjectName("widget_34")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_34)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_47 = QtWidgets.QLabel(self.widget_34)
        self.label_47.setStyleSheet("font: 20pt \"Kirang Haerang\";")
        self.label_47.setObjectName("label_47")
        self.verticalLayout_13.addWidget(self.label_47)
        self.horizontalLayout_24.addWidget(self.widget_34)
        self.widget_35 = QtWidgets.QWidget(self.widget_31)
        self.widget_35.setObjectName("widget_35")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_35)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.monthly_eat_score = QtWidgets.QLabel(self.widget_35)
        self.monthly_eat_score.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.monthly_eat_score.setObjectName("monthly_eat_score")
        self.verticalLayout_14.addWidget(self.monthly_eat_score, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_24.addWidget(self.widget_35)
        self.gridLayout.addWidget(self.widget_31, 1, 0, 1, 2)
        self.mainStackedWidget.addWidget(self.individual_eat)
        self.individual_exercise = QtWidgets.QWidget()
        self.individual_exercise.setObjectName("individual_exercise")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.individual_exercise)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_3 = QtWidgets.QWidget(self.individual_exercise)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_3.setStyleSheet("background-color: rgb(136, 189, 255);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_65 = QtWidgets.QWidget(self.widget_3)
        self.widget_65.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_65.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_65.setObjectName("widget_65")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.widget_65)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.btn_home_4 = QtWidgets.QPushButton(self.widget_65)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_4.sizePolicy().hasHeightForWidth())
        self.btn_home_4.setSizePolicy(sizePolicy)
        self.btn_home_4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_home_4.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_home_4.setStyleSheet("QPushButton#btn_home_4{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_4:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_home_4.setText("")
        self.btn_home_4.setIcon(icon6)
        self.btn_home_4.setIconSize(QtCore.QSize(80, 80))
        self.btn_home_4.setObjectName("btn_home_4")
        self.horizontalLayout_40.addWidget(self.btn_home_4)
        self.btn_back_3 = QtWidgets.QPushButton(self.widget_65)
        self.btn_back_3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_back_3.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_back_3.setBaseSize(QtCore.QSize(100, 25))
        self.btn_back_3.setStyleSheet("QPushButton#btn_back_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_back_3:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_back_3.setText("")
        self.btn_back_3.setIcon(icon7)
        self.btn_back_3.setIconSize(QtCore.QSize(80, 80))
        self.btn_back_3.setObjectName("btn_back_3")
        self.horizontalLayout_40.addWidget(self.btn_back_3)
        self.horizontalLayout_7.addWidget(self.widget_65, 0, QtCore.Qt.AlignLeft)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setStyleSheet("font:25pt \"AppleSDGothicNeoB00\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.widget_44 = QtWidgets.QWidget(self.widget_3)
        self.widget_44.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_44.setObjectName("widget_44")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_44)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.btn_goto_sleep_2 = QtWidgets.QPushButton(self.widget_44)
        self.btn_goto_sleep_2.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep_2.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep_2.setStyleSheet("QPushButton#btn_goto_sleep_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_sleep_2:hover{\n"
"    background-color:rgb(255, 179, 150);\n"
"    color: white;\n"
"}")
        self.btn_goto_sleep_2.setObjectName("btn_goto_sleep_2")
        self.gridLayout_14.addWidget(self.btn_goto_sleep_2, 0, 0, 1, 1)
        self.btn_goto_eat_2 = QtWidgets.QPushButton(self.widget_44)
        self.btn_goto_eat_2.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat_2.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat_2.setStyleSheet("QPushButton#btn_goto_eat_2{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_eat_2:hover{\n"
"    background-color:rgb(253, 128, 8);\n"
"    color: white;\n"
"}")
        self.btn_goto_eat_2.setObjectName("btn_goto_eat_2")
        self.gridLayout_14.addWidget(self.btn_goto_eat_2, 0, 1, 1, 1)
        self.btn_goto_medication_3 = QtWidgets.QPushButton(self.widget_44)
        self.btn_goto_medication_3.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication_3.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_medication_3.setStyleSheet("QPushButton#btn_goto_medication_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_medication_3:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_medication_3.setObjectName("btn_goto_medication_3")
        self.gridLayout_14.addWidget(self.btn_goto_medication_3, 1, 0, 1, 1)
        self.btn_goto_suni_4 = QtWidgets.QPushButton(self.widget_44)
        self.btn_goto_suni_4.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_4.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_4.setStyleSheet("QPushButton#btn_goto_suni_4{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_suni_4:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_suni_4.setObjectName("btn_goto_suni_4")
        self.gridLayout_14.addWidget(self.btn_goto_suni_4, 1, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.widget_44, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_9.addWidget(self.widget_3)
        self.widget_45 = QtWidgets.QWidget(self.individual_exercise)
        self.widget_45.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_45.setMaximumSize(QtCore.QSize(16777215, 140))
        self.widget_45.setObjectName("widget_45")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_45)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_46 = QtWidgets.QWidget(self.widget_45)
        self.widget_46.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_46.setObjectName("widget_46")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.widget_46)
        self.verticalLayout_39.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_17 = QtWidgets.QLabel(self.widget_46)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_39.addWidget(self.label_17)
        self.horizontalLayout_8.addWidget(self.widget_46, 0, QtCore.Qt.AlignLeft)
        self.widget_47 = QtWidgets.QWidget(self.widget_45)
        self.widget_47.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_47.setObjectName("widget_47")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_47)
        self.verticalLayout_40.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.monthly_exercise_score = QtWidgets.QLabel(self.widget_47)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monthly_exercise_score.sizePolicy().hasHeightForWidth())
        self.monthly_exercise_score.setSizePolicy(sizePolicy)
        self.monthly_exercise_score.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.monthly_exercise_score.setObjectName("monthly_exercise_score")
        self.verticalLayout_40.addWidget(self.monthly_exercise_score)
        self.horizontalLayout_8.addWidget(self.widget_47, 0, QtCore.Qt.AlignLeft)
        self.exercise_score_comment = QtWidgets.QLabel(self.widget_45)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exercise_score_comment.sizePolicy().hasHeightForWidth())
        self.exercise_score_comment.setSizePolicy(sizePolicy)
        self.exercise_score_comment.setMinimumSize(QtCore.QSize(0, 0))
        self.exercise_score_comment.setStyleSheet("font:13pt \"AppleSDGothicNeoB00\";\n"
"border: 1px solid rgb(136, 189, 255);\n"
"border-radius: 20px;\n"
"padding:5px;\n"
"\n"
"")
        self.exercise_score_comment.setWordWrap(True)
        self.exercise_score_comment.setObjectName("exercise_score_comment")
        self.horizontalLayout_8.addWidget(self.exercise_score_comment)
        self.verticalLayout_9.addWidget(self.widget_45)
        self.widget_48 = QtWidgets.QWidget(self.individual_exercise)
        self.widget_48.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_48.setObjectName("widget_48")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.widget_48)
        self.verticalLayout_41.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.label_activity_with_name = QtWidgets.QLabel(self.widget_48)
        self.label_activity_with_name.setMaximumSize(QtCore.QSize(16777215, 49))
        self.label_activity_with_name.setStyleSheet("background-color: rgb(136, 189, 255);\n"
"padding:5px;\n"
"font: 18pt \"AppleSDGothicNeoB00\";\n"
"")
        self.label_activity_with_name.setObjectName("label_activity_with_name")
        self.verticalLayout_41.addWidget(self.label_activity_with_name)
        self.widget_49 = QtWidgets.QWidget(self.widget_48)
        self.widget_49.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget_49.setObjectName("widget_49")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_49)
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_11 = QtWidgets.QFrame(self.widget_49)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_42.setContentsMargins(-1, 3, -1, -1)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.graph_verticalLayout_activity = QtWidgets.QVBoxLayout()
        self.graph_verticalLayout_activity.setObjectName("graph_verticalLayout_activity")
        self.verticalLayout_42.addLayout(self.graph_verticalLayout_activity)
        self.horizontalLayout_27.addWidget(self.frame_11)
        self.widget_50 = QtWidgets.QWidget(self.widget_49)
        self.widget_50.setObjectName("widget_50")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.widget_50)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_activity_list_comment = QtWidgets.QLabel(self.widget_50)
        self.label_activity_list_comment.setMinimumSize(QtCore.QSize(0, 100))
        self.label_activity_list_comment.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_activity_list_comment.setStyleSheet("background-color : rgb(242, 239, 244);\n"
"border-radius: 20px;\n"
"padding:5px;\n"
"font: 18pt \"Kirang Haerang\";\n"
"border: 1px solid rgb(0, 0, 128);\n"
"")
        self.label_activity_list_comment.setLineWidth(1)
        self.label_activity_list_comment.setTextFormat(QtCore.Qt.AutoText)
        self.label_activity_list_comment.setScaledContents(True)
        self.label_activity_list_comment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_activity_list_comment.setWordWrap(True)
        self.label_activity_list_comment.setObjectName("label_activity_list_comment")
        self.verticalLayout_45.addWidget(self.label_activity_list_comment, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_27.addWidget(self.widget_50)
        self.verticalLayout_41.addWidget(self.widget_49)
        self.verticalLayout_9.addWidget(self.widget_48)
        self.widget_51 = QtWidgets.QWidget(self.individual_exercise)
        self.widget_51.setObjectName("widget_51")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_51)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_12 = QtWidgets.QFrame(self.widget_51)
        self.frame_12.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_43.setContentsMargins(-1, 3, -1, -1)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.graph_verticalLayout_weekActiveScore = QtWidgets.QVBoxLayout()
        self.graph_verticalLayout_weekActiveScore.setObjectName("graph_verticalLayout_weekActiveScore")
        self.verticalLayout_43.addLayout(self.graph_verticalLayout_weekActiveScore)
        self.horizontalLayout_12.addWidget(self.frame_12)
        self.widget_52 = QtWidgets.QWidget(self.widget_51)
        self.widget_52.setObjectName("widget_52")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.widget_52)
        self.verticalLayout_44.setContentsMargins(-1, 3, -1, -1)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_active_week_good = QtWidgets.QLabel(self.widget_52)
        self.label_active_week_good.setStyleSheet("font: 18pt \"AppleSDGothicNeoB00\";\n"
"color: rgb(16, 128, 64);\n"
"")
        self.label_active_week_good.setObjectName("label_active_week_good")
        self.verticalLayout_44.addWidget(self.label_active_week_good)
        self.label_active_week_mid = QtWidgets.QLabel(self.widget_52)
        self.label_active_week_mid.setStyleSheet("font: 18pt \"AppleSDGothicNeoB00\";\n"
"color: rgb(16, 128, 128);\n"
"")
        self.label_active_week_mid.setObjectName("label_active_week_mid")
        self.verticalLayout_44.addWidget(self.label_active_week_mid)
        self.label_active_week_bad = QtWidgets.QLabel(self.widget_52)
        self.label_active_week_bad.setStyleSheet("font: 18pt \"AppleSDGothicNeoB00\";\n"
"color: rgb(7, 64, 128);")
        self.label_active_week_bad.setObjectName("label_active_week_bad")
        self.verticalLayout_44.addWidget(self.label_active_week_bad)
        self.horizontalLayout_12.addWidget(self.widget_52)
        self.verticalLayout_9.addWidget(self.widget_51)
        self.mainStackedWidget.addWidget(self.individual_exercise)
        self.individual_medication = QtWidgets.QWidget()
        self.individual_medication.setObjectName("individual_medication")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.individual_medication)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame1 = QtWidgets.QWidget(self.individual_medication)
        self.frame1.setMinimumSize(QtCore.QSize(0, 130))
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame1.setBaseSize(QtCore.QSize(0, 49))
        self.frame1.setStyleSheet("background-color: #b578b5")
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_66 = QtWidgets.QWidget(self.frame1)
        self.widget_66.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_66.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_66.setObjectName("widget_66")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.widget_66)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.btn_home_5 = QtWidgets.QPushButton(self.widget_66)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_5.sizePolicy().hasHeightForWidth())
        self.btn_home_5.setSizePolicy(sizePolicy)
        self.btn_home_5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_home_5.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_home_5.setStyleSheet("QPushButton#btn_home_5{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_5:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_home_5.setText("")
        self.btn_home_5.setIcon(icon6)
        self.btn_home_5.setIconSize(QtCore.QSize(80, 80))
        self.btn_home_5.setObjectName("btn_home_5")
        self.horizontalLayout_41.addWidget(self.btn_home_5)
        self.btn_back_4 = QtWidgets.QPushButton(self.widget_66)
        self.btn_back_4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_back_4.setMaximumSize(QtCore.QSize(80, 80))
        self.btn_back_4.setBaseSize(QtCore.QSize(100, 25))
        self.btn_back_4.setStyleSheet("QPushButton#btn_back_4{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_back_4:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_back_4.setText("")
        self.btn_back_4.setIcon(icon7)
        self.btn_back_4.setIconSize(QtCore.QSize(80, 80))
        self.btn_back_4.setObjectName("btn_back_4")
        self.horizontalLayout_41.addWidget(self.btn_back_4)
        self.horizontalLayout_5.addWidget(self.widget_66, 0, QtCore.Qt.AlignLeft)
        self.label_11 = QtWidgets.QLabel(self.frame1)
        self.label_11.setStyleSheet("font:25pt \"AppleSDGothicNeoB00\";\\n\n"
"color:white;\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.frame_20 = QtWidgets.QFrame(self.frame1)
        self.frame_20.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_goto_sleep_3 = QtWidgets.QPushButton(self.frame_20)
        self.btn_goto_sleep_3.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep_3.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_sleep_3.setStyleSheet("QPushButton#btn_goto_sleep_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_sleep_3:hover{\n"
"    background-color:rgb(255, 179, 150);\n"
"    color: white;\n"
"}")
        self.btn_goto_sleep_3.setObjectName("btn_goto_sleep_3")
        self.gridLayout_4.addWidget(self.btn_goto_sleep_3, 0, 0, 1, 1)
        self.btn_goto_eat_3 = QtWidgets.QPushButton(self.frame_20)
        self.btn_goto_eat_3.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat_3.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_eat_3.setStyleSheet("QPushButton#btn_goto_eat_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_eat_3:hover{\n"
"    background-color:rgb(253, 128, 8);\n"
"    color: white;\n"
"}")
        self.btn_goto_eat_3.setObjectName("btn_goto_eat_3")
        self.gridLayout_4.addWidget(self.btn_goto_eat_3, 0, 1, 1, 1)
        self.btn_goto_exercise_3 = QtWidgets.QPushButton(self.frame_20)
        self.btn_goto_exercise_3.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise_3.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_exercise_3.setStyleSheet("QPushButton#btn_goto_exercise_3{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_exercise_3:hover{\n"
"    background-color:rgb(136, 189, 255);\n"
"    color: white;\n"
"}")
        self.btn_goto_exercise_3.setObjectName("btn_goto_exercise_3")
        self.gridLayout_4.addWidget(self.btn_goto_exercise_3, 1, 0, 1, 1)
        self.btn_goto_suni_5 = QtWidgets.QPushButton(self.frame_20)
        self.btn_goto_suni_5.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_5.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_goto_suni_5.setStyleSheet("QPushButton#btn_goto_suni_5{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_goto_suni_5:hover{\n"
"    background-color:rgb(128, 0, 128);\n"
"    color: white;\n"
"}\n"
"")
        self.btn_goto_suni_5.setObjectName("btn_goto_suni_5")
        self.gridLayout_4.addWidget(self.btn_goto_suni_5, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_20)
        self.verticalLayout_8.addWidget(self.frame1)
        self.widget_53 = QtWidgets.QWidget(self.individual_medication)
        self.widget_53.setMinimumSize(QtCore.QSize(0, 250))
        self.widget_53.setMaximumSize(QtCore.QSize(16777215, 250))
        self.widget_53.setObjectName("widget_53")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.widget_53)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label_7 = QtWidgets.QLabel(self.widget_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(250, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_7.setStyleSheet("font: 18pt \"AppleSDGothicNeoB00\";\n"
"text-align: center;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_48.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget_57 = QtWidgets.QWidget(self.widget_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy)
        self.widget_57.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_57.setObjectName("widget_57")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.widget_57)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.widget_58 = QtWidgets.QWidget(self.widget_57)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy)
        self.widget_58.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_58.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_58.setObjectName("widget_58")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.widget_58)
        self.horizontalLayout_32.setContentsMargins(-1, 0, -1, 3)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.medication_variance_score = QtWidgets.QLabel(self.widget_58)
        self.medication_variance_score.setMinimumSize(QtCore.QSize(0, 0))
        self.medication_variance_score.setStyleSheet("font: 36pt \"Kirang Haerang\";")
        self.medication_variance_score.setObjectName("medication_variance_score")
        self.horizontalLayout_32.addWidget(self.medication_variance_score)
        self.horizontalLayout_29.addWidget(self.widget_58, 0, QtCore.Qt.AlignLeft)
        self.widget_59 = QtWidgets.QWidget(self.widget_57)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_59.sizePolicy().hasHeightForWidth())
        self.widget_59.setSizePolicy(sizePolicy)
        self.widget_59.setObjectName("widget_59")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.widget_59)
        self.verticalLayout_49.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.frame_22 = QtWidgets.QFrame(self.widget_59)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.medication_mark1 = QtWidgets.QLabel(self.frame_22)
        self.medication_mark1.setMinimumSize(QtCore.QSize(80, 80))
        self.medication_mark1.setMaximumSize(QtCore.QSize(80, 80))
        self.medication_mark1.setText("")
        self.medication_mark1.setPixmap(QtGui.QPixmap("images/green_check.png"))
        self.medication_mark1.setScaledContents(True)
        self.medication_mark1.setObjectName("medication_mark1")
        self.horizontalLayout_30.addWidget(self.medication_mark1)
        self.medication_calendar_comment = QtWidgets.QLabel(self.frame_22)
        self.medication_calendar_comment.setMinimumSize(QtCore.QSize(0, 50))
        self.medication_calendar_comment.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.medication_calendar_comment.setStyleSheet("font:16pt \"AppleSDGothicNeoB00\";")
        self.medication_calendar_comment.setWordWrap(True)
        self.medication_calendar_comment.setIndent(10)
        self.medication_calendar_comment.setObjectName("medication_calendar_comment")
        self.horizontalLayout_30.addWidget(self.medication_calendar_comment)
        self.verticalLayout_49.addWidget(self.frame_22)
        self.frame_21 = QtWidgets.QFrame(self.widget_59)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.medication_mark2 = QtWidgets.QLabel(self.frame_21)
        self.medication_mark2.setMinimumSize(QtCore.QSize(80, 80))
        self.medication_mark2.setMaximumSize(QtCore.QSize(80, 80))
        self.medication_mark2.setText("")
        self.medication_mark2.setPixmap(QtGui.QPixmap("images/prohibited.png"))
        self.medication_mark2.setScaledContents(True)
        self.medication_mark2.setObjectName("medication_mark2")
        self.horizontalLayout_31.addWidget(self.medication_mark2)
        self.medication_calendar_comment_2 = QtWidgets.QLabel(self.frame_21)
        self.medication_calendar_comment_2.setMinimumSize(QtCore.QSize(0, 80))
        self.medication_calendar_comment_2.setStyleSheet("font:16pt \"AppleSDGothicNeoB00\";")
        self.medication_calendar_comment_2.setWordWrap(True)
        self.medication_calendar_comment_2.setIndent(10)
        self.medication_calendar_comment_2.setObjectName("medication_calendar_comment_2")
        self.horizontalLayout_31.addWidget(self.medication_calendar_comment_2)
        self.verticalLayout_49.addWidget(self.frame_21)
        self.horizontalLayout_29.addWidget(self.widget_59)
        self.verticalLayout_48.addWidget(self.widget_57)
        self.verticalLayout_8.addWidget(self.widget_53)
        self.widget_54 = QtWidgets.QWidget(self.individual_medication)
        self.widget_54.setMinimumSize(QtCore.QSize(0, 450))
        self.widget_54.setObjectName("widget_54")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.widget_54)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.frame_3 = QtWidgets.QFrame(self.widget_54)
        self.frame_3.setMinimumSize(QtCore.QSize(600, 400))
        self.frame_3.setMaximumSize(QtCore.QSize(600, 400))
        self.frame_3.setStyleSheet("border: 3px solid black;\n"
"\n"
"\n"
"")
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.day2_2 = QtWidgets.QLabel(self.frame_3)
        self.day2_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day2_2.setObjectName("day2_2")
        self.gridLayout_15.addWidget(self.day2_2, 2, 1, 1, 1)
        self.day5_2 = QtWidgets.QLabel(self.frame_3)
        self.day5_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day5_2.setObjectName("day5_2")
        self.gridLayout_15.addWidget(self.day5_2, 2, 4, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.frame_3)
        self.label_53.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_53.setObjectName("label_53")
        self.gridLayout_15.addWidget(self.label_53, 1, 5, 1, 1)
        self.day3_2 = QtWidgets.QLabel(self.frame_3)
        self.day3_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day3_2.setObjectName("day3_2")
        self.gridLayout_15.addWidget(self.day3_2, 2, 2, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.frame_3)
        self.label_54.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_54.setObjectName("label_54")
        self.gridLayout_15.addWidget(self.label_54, 1, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.frame_3)
        self.label_56.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_56.setObjectName("label_56")
        self.gridLayout_15.addWidget(self.label_56, 1, 1, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.frame_3)
        self.label_58.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_58.setObjectName("label_58")
        self.gridLayout_15.addWidget(self.label_58, 1, 3, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.frame_3)
        self.label_59.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_59.setScaledContents(True)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.gridLayout_15.addWidget(self.label_59, 1, 0, 1, 1)
        self.day7_2 = QtWidgets.QLabel(self.frame_3)
        self.day7_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day7_2.setObjectName("day7_2")
        self.gridLayout_15.addWidget(self.day7_2, 2, 6, 1, 1)
        self.day1_2 = QtWidgets.QLabel(self.frame_3)
        self.day1_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day1_2.setObjectName("day1_2")
        self.gridLayout_15.addWidget(self.day1_2, 2, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.frame_3)
        self.label_60.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_60.setWordWrap(True)
        self.label_60.setIndent(-1)
        self.label_60.setOpenExternalLinks(False)
        self.label_60.setObjectName("label_60")
        self.gridLayout_15.addWidget(self.label_60, 1, 4, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.frame_3)
        self.label_61.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_61.setObjectName("label_61")
        self.gridLayout_15.addWidget(self.label_61, 1, 6, 1, 1)
        self.day4_2 = QtWidgets.QLabel(self.frame_3)
        self.day4_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day4_2.setObjectName("day4_2")
        self.gridLayout_15.addWidget(self.day4_2, 2, 3, 1, 1)
        self.day6_2 = QtWidgets.QLabel(self.frame_3)
        self.day6_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day6_2.setObjectName("day6_2")
        self.gridLayout_15.addWidget(self.day6_2, 2, 5, 1, 1)
        self.day10_2 = QtWidgets.QLabel(self.frame_3)
        self.day10_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day10_2.setObjectName("day10_2")
        self.gridLayout_15.addWidget(self.day10_2, 4, 2, 1, 1)
        self.day9_2 = QtWidgets.QLabel(self.frame_3)
        self.day9_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day9_2.setObjectName("day9_2")
        self.gridLayout_15.addWidget(self.day9_2, 4, 1, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.frame_3)
        self.label_62.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_62.setObjectName("label_62")
        self.gridLayout_15.addWidget(self.label_62, 3, 2, 1, 1)
        self.day8_2 = QtWidgets.QLabel(self.frame_3)
        self.day8_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day8_2.setObjectName("day8_2")
        self.gridLayout_15.addWidget(self.day8_2, 4, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.frame_3)
        self.label_63.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_63.setObjectName("label_63")
        self.gridLayout_15.addWidget(self.label_63, 3, 3, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.frame_3)
        self.label_64.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_64.setObjectName("label_64")
        self.gridLayout_15.addWidget(self.label_64, 3, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.frame_3)
        self.label_65.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_65.setObjectName("label_65")
        self.gridLayout_15.addWidget(self.label_65, 3, 4, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.frame_3)
        self.label_66.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_66.setObjectName("label_66")
        self.gridLayout_15.addWidget(self.label_66, 3, 5, 1, 1)
        self.day11_2 = QtWidgets.QLabel(self.frame_3)
        self.day11_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day11_2.setObjectName("day11_2")
        self.gridLayout_15.addWidget(self.day11_2, 4, 3, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.frame_3)
        self.label_67.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_67.setObjectName("label_67")
        self.gridLayout_15.addWidget(self.label_67, 3, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.frame_3)
        self.label_68.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_68.setObjectName("label_68")
        self.gridLayout_15.addWidget(self.label_68, 3, 6, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.frame_3)
        self.label_69.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_69.setObjectName("label_69")
        self.gridLayout_15.addWidget(self.label_69, 5, 6, 1, 1)
        self.day12_2 = QtWidgets.QLabel(self.frame_3)
        self.day12_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day12_2.setObjectName("day12_2")
        self.gridLayout_15.addWidget(self.day12_2, 4, 4, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.frame_3)
        self.label_70.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_70.setObjectName("label_70")
        self.gridLayout_15.addWidget(self.label_70, 5, 0, 1, 1)
        self.day14_2 = QtWidgets.QLabel(self.frame_3)
        self.day14_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day14_2.setObjectName("day14_2")
        self.gridLayout_15.addWidget(self.day14_2, 4, 6, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.frame_3)
        self.label_71.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_71.setObjectName("label_71")
        self.gridLayout_15.addWidget(self.label_71, 5, 4, 1, 1)
        self.day15_2 = QtWidgets.QLabel(self.frame_3)
        self.day15_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day15_2.setObjectName("day15_2")
        self.gridLayout_15.addWidget(self.day15_2, 6, 0, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.frame_3)
        self.label_72.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_72.setObjectName("label_72")
        self.gridLayout_15.addWidget(self.label_72, 5, 1, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_3)
        self.label_73.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_73.setObjectName("label_73")
        self.gridLayout_15.addWidget(self.label_73, 5, 2, 1, 1)
        self.day13_2 = QtWidgets.QLabel(self.frame_3)
        self.day13_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day13_2.setObjectName("day13_2")
        self.gridLayout_15.addWidget(self.day13_2, 4, 5, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.frame_3)
        self.label_74.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_74.setObjectName("label_74")
        self.gridLayout_15.addWidget(self.label_74, 5, 5, 1, 1)
        self.day16_2 = QtWidgets.QLabel(self.frame_3)
        self.day16_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day16_2.setObjectName("day16_2")
        self.gridLayout_15.addWidget(self.day16_2, 6, 1, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.frame_3)
        self.label_75.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_75.setObjectName("label_75")
        self.gridLayout_15.addWidget(self.label_75, 5, 3, 1, 1)
        self.day19_2 = QtWidgets.QLabel(self.frame_3)
        self.day19_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day19_2.setObjectName("day19_2")
        self.gridLayout_15.addWidget(self.day19_2, 6, 4, 1, 1)
        self.label_109 = QtWidgets.QLabel(self.frame_3)
        self.label_109.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_109.setObjectName("label_109")
        self.gridLayout_15.addWidget(self.label_109, 7, 0, 1, 1)
        self.day21_2 = QtWidgets.QLabel(self.frame_3)
        self.day21_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day21_2.setObjectName("day21_2")
        self.gridLayout_15.addWidget(self.day21_2, 6, 6, 1, 1)
        self.day17_2 = QtWidgets.QLabel(self.frame_3)
        self.day17_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day17_2.setObjectName("day17_2")
        self.gridLayout_15.addWidget(self.day17_2, 6, 2, 1, 1)
        self.day24_2 = QtWidgets.QLabel(self.frame_3)
        self.day24_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day24_2.setObjectName("day24_2")
        self.gridLayout_15.addWidget(self.day24_2, 8, 2, 1, 1)
        self.day26_2 = QtWidgets.QLabel(self.frame_3)
        self.day26_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day26_2.setObjectName("day26_2")
        self.gridLayout_15.addWidget(self.day26_2, 8, 4, 1, 1)
        self.day20_2 = QtWidgets.QLabel(self.frame_3)
        self.day20_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day20_2.setObjectName("day20_2")
        self.gridLayout_15.addWidget(self.day20_2, 6, 5, 1, 1)
        self.day25_2 = QtWidgets.QLabel(self.frame_3)
        self.day25_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day25_2.setObjectName("day25_2")
        self.gridLayout_15.addWidget(self.day25_2, 8, 3, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.frame_3)
        self.label_110.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_110.setObjectName("label_110")
        self.gridLayout_15.addWidget(self.label_110, 7, 1, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.frame_3)
        self.label_111.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_111.setObjectName("label_111")
        self.gridLayout_15.addWidget(self.label_111, 7, 2, 1, 1)
        self.day23_2 = QtWidgets.QLabel(self.frame_3)
        self.day23_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day23_2.setObjectName("day23_2")
        self.gridLayout_15.addWidget(self.day23_2, 8, 1, 1, 1)
        self.day22_2 = QtWidgets.QLabel(self.frame_3)
        self.day22_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day22_2.setObjectName("day22_2")
        self.gridLayout_15.addWidget(self.day22_2, 8, 0, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.frame_3)
        self.label_112.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_112.setObjectName("label_112")
        self.gridLayout_15.addWidget(self.label_112, 7, 6, 1, 1)
        self.label_113 = QtWidgets.QLabel(self.frame_3)
        self.label_113.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_113.setObjectName("label_113")
        self.gridLayout_15.addWidget(self.label_113, 7, 5, 1, 1)
        self.label_114 = QtWidgets.QLabel(self.frame_3)
        self.label_114.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_114.setObjectName("label_114")
        self.gridLayout_15.addWidget(self.label_114, 7, 4, 1, 1)
        self.day18_2 = QtWidgets.QLabel(self.frame_3)
        self.day18_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day18_2.setObjectName("day18_2")
        self.gridLayout_15.addWidget(self.day18_2, 6, 3, 1, 1)
        self.day27_2 = QtWidgets.QLabel(self.frame_3)
        self.day27_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day27_2.setObjectName("day27_2")
        self.gridLayout_15.addWidget(self.day27_2, 8, 5, 1, 1)
        self.label_119 = QtWidgets.QLabel(self.frame_3)
        self.label_119.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_119.setObjectName("label_119")
        self.gridLayout_15.addWidget(self.label_119, 9, 0, 1, 1)
        self.day28_2 = QtWidgets.QLabel(self.frame_3)
        self.day28_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day28_2.setObjectName("day28_2")
        self.gridLayout_15.addWidget(self.day28_2, 8, 6, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.frame_3)
        self.label_120.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_120.setObjectName("label_120")
        self.gridLayout_15.addWidget(self.label_120, 9, 1, 1, 1)
        self.label_121 = QtWidgets.QLabel(self.frame_3)
        self.label_121.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_121.setObjectName("label_121")
        self.gridLayout_15.addWidget(self.label_121, 9, 2, 1, 1)
        self.day30_2 = QtWidgets.QLabel(self.frame_3)
        self.day30_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day30_2.setObjectName("day30_2")
        self.gridLayout_15.addWidget(self.day30_2, 10, 1, 1, 1)
        self.day29_2 = QtWidgets.QLabel(self.frame_3)
        self.day29_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day29_2.setObjectName("day29_2")
        self.gridLayout_15.addWidget(self.day29_2, 10, 0, 1, 1)
        self.day31_2 = QtWidgets.QLabel(self.frame_3)
        self.day31_2.setStyleSheet("font: 20pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.day31_2.setObjectName("day31_2")
        self.gridLayout_15.addWidget(self.day31_2, 10, 2, 1, 1)
        self.label_115 = QtWidgets.QLabel(self.frame_3)
        self.label_115.setStyleSheet("border: 3px solid black;\n"
"background-color: rgb(128, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font:12pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;\n"
"")
        self.label_115.setObjectName("label_115")
        self.gridLayout_15.addWidget(self.label_115, 7, 3, 1, 1)
        self.horizontalLayout_33.addWidget(self.frame_3)
        self.frame_23 = QtWidgets.QFrame(self.widget_54)
        self.frame_23.setMinimumSize(QtCore.QSize(355, 400))
        self.frame_23.setMaximumSize(QtCore.QSize(355, 400))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_50.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.widget_60 = QtWidgets.QWidget(self.frame_23)
        self.widget_60.setObjectName("widget_60")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.widget_60)
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_6 = QtWidgets.QLabel(self.widget_60)
        self.label_6.setMinimumSize(QtCore.QSize(315, 80))
        self.label_6.setMaximumSize(QtCore.QSize(315, 80))
        self.label_6.setStyleSheet("font:22pt \"-윤고딕160\";\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setIndent(10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_34.addWidget(self.label_6)
        self.verticalLayout_50.addWidget(self.widget_60, 0, QtCore.Qt.AlignTop)
        self.widget_61 = QtWidgets.QWidget(self.frame_23)
        self.widget_61.setMinimumSize(QtCore.QSize(330, 150))
        self.widget_61.setMaximumSize(QtCore.QSize(330, 150))
        self.widget_61.setObjectName("widget_61")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.widget_61)
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.widget_63 = QtWidgets.QWidget(self.widget_61)
        self.widget_63.setMinimumSize(QtCore.QSize(300, 130))
        self.widget_63.setMaximumSize(QtCore.QSize(300, 130))
        self.widget_63.setStyleSheet("QWidget#widget{\n"
"    padding: 0 0 0 0;\n"
"    border-spacing: 0px 0px;\n"
"    margin: 0px;\n"
"\n"
"}\n"
"\n"
"")
        self.widget_63.setObjectName("widget_63")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.widget_63)
        self.horizontalLayout_35.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.med_left = QtWidgets.QLabel(self.widget_63)
        self.med_left.setMinimumSize(QtCore.QSize(141, 112))
        self.med_left.setMaximumSize(QtCore.QSize(141, 112))
        font = QtGui.QFont()
        font.setFamily("-윤고딕160")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.med_left.setFont(font)
        self.med_left.setStyleSheet("QLabel#med_left{\n"
"color:white; \n"
"font: 40pt \"-윤고딕160\";\n"
"background-color:rgba(220,89,66,225);\n"
"border-top-left-radius: 55px;    \n"
"border-bottom-left-radius: 55px;\n"
"}\n"
"")
        self.med_left.setAlignment(QtCore.Qt.AlignCenter)
        self.med_left.setIndent(-1)
        self.med_left.setObjectName("med_left")
        self.horizontalLayout_35.addWidget(self.med_left)
        self.med_right = QtWidgets.QLabel(self.widget_63)
        self.med_right.setMinimumSize(QtCore.QSize(141, 112))
        self.med_right.setMaximumSize(QtCore.QSize(141, 112))
        font = QtGui.QFont()
        font.setFamily("-윤고딕160")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.med_right.setFont(font)
        self.med_right.setStyleSheet("QLabel#med_right{\n"
"color: rgba(220,89,66,225);\n"
"font: 40pt \"-윤고딕160\";\n"
"background-color:white;\n"
"border-top-right-radius: 55px;    \n"
"border-bottom-right-radius: 55px;\n"
"background-color:rgba(162, 211, 249,225);\n"
"}\n"
"")
        self.med_right.setAlignment(QtCore.Qt.AlignCenter)
        self.med_right.setIndent(-1)
        self.med_right.setObjectName("med_right")
        self.horizontalLayout_35.addWidget(self.med_right)
        self.horizontalLayout_36.addWidget(self.widget_63)
        self.verticalLayout_50.addWidget(self.widget_61, 0, QtCore.Qt.AlignHCenter)
        self.widget_62 = QtWidgets.QWidget(self.frame_23)
        self.widget_62.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_62.setMaximumSize(QtCore.QSize(11111, 140))
        self.widget_62.setObjectName("widget_62")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.widget_62)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.medication_day_count = QtWidgets.QLabel(self.widget_62)
        self.medication_day_count.setMinimumSize(QtCore.QSize(280, 0))
        self.medication_day_count.setStyleSheet("font: 20pt \"-윤고딕160\";")
        self.medication_day_count.setObjectName("medication_day_count")
        self.verticalLayout_51.addWidget(self.medication_day_count)
        self.medication_day_count_trail = QtWidgets.QLabel(self.widget_62)
        self.medication_day_count_trail.setStyleSheet("font: 20pt \"-윤고딕160\";")
        self.medication_day_count_trail.setObjectName("medication_day_count_trail")
        self.verticalLayout_51.addWidget(self.medication_day_count_trail)
        self.verticalLayout_50.addWidget(self.widget_62, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_33.addWidget(self.frame_23)
        self.verticalLayout_8.addWidget(self.widget_54)
        self.widget_55 = QtWidgets.QWidget(self.individual_medication)
        self.widget_55.setObjectName("widget_55")
        self.verticalLayout_8.addWidget(self.widget_55)
        self.mainStackedWidget.addWidget(self.individual_medication)
        self.individual_suni = QtWidgets.QWidget()
        self.individual_suni.setObjectName("individual_suni")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.individual_suni)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.RadarChartFrame = QtWidgets.QWidget(self.individual_suni)
        self.RadarChartFrame.setMinimumSize(QtCore.QSize(600, 300))
        self.RadarChartFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RadarChartFrame.setObjectName("RadarChartFrame")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.RadarChartFrame)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.RadarEmbedWidget = QtWidgets.QWidget(self.RadarChartFrame)
        self.RadarEmbedWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.RadarEmbedWidget.setObjectName("RadarEmbedWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.RadarEmbedWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graph_verticalLayout_radar_chart = QtWidgets.QVBoxLayout()
        self.graph_verticalLayout_radar_chart.setContentsMargins(-1, -1, 0, -1)
        self.graph_verticalLayout_radar_chart.setObjectName("graph_verticalLayout_radar_chart")
        self.verticalLayout_6.addLayout(self.graph_verticalLayout_radar_chart)
        self.horizontalLayout_21.addWidget(self.RadarEmbedWidget)
        self.widget_12 = QtWidgets.QWidget(self.RadarChartFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_57 = QtWidgets.QLabel(self.widget_12)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_21.addWidget(self.label_57)
        self.tb_program_preference_comment_1 = QtWidgets.QLabel(self.widget_12)
        self.tb_program_preference_comment_1.setStyleSheet("font: 15pt \"AppleSDGothicNeoB00\";")
        self.tb_program_preference_comment_1.setObjectName("tb_program_preference_comment_1")
        self.verticalLayout_21.addWidget(self.tb_program_preference_comment_1)
        self.tb_program_preference_comment_2 = QtWidgets.QLabel(self.widget_12)
        self.tb_program_preference_comment_2.setStyleSheet("font: 10pt \"AppleSDGothicNeoB00\";")
        self.tb_program_preference_comment_2.setObjectName("tb_program_preference_comment_2")
        self.verticalLayout_21.addWidget(self.tb_program_preference_comment_2, 0, QtCore.Qt.AlignTop)
        self.label_55 = QtWidgets.QLabel(self.widget_12)
        self.label_55.setStyleSheet("font: 15pt \"AppleSDGothicNeoB00\";")
        self.label_55.setObjectName("label_55")
        self.verticalLayout_21.addWidget(self.label_55)
        self.tb_program_preference_comment_3 = QtWidgets.QLabel(self.widget_12)
        self.tb_program_preference_comment_3.setStyleSheet("font: 10pt \"AppleSDGothicNeoB00\";")
        self.tb_program_preference_comment_3.setObjectName("tb_program_preference_comment_3")
        self.verticalLayout_21.addWidget(self.tb_program_preference_comment_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_21.addWidget(self.widget_12)
        self.gridLayout_7.addWidget(self.RadarChartFrame, 4, 0, 1, 1)
        self.ProgramFrame = QtWidgets.QWidget(self.individual_suni)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgramFrame.sizePolicy().hasHeightForWidth())
        self.ProgramFrame.setSizePolicy(sizePolicy)
        self.ProgramFrame.setObjectName("ProgramFrame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.ProgramFrame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_7 = QtWidgets.QWidget(self.ProgramFrame)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_36 = QtWidgets.QLabel(self.widget_7)
        self.label_36.setStyleSheet("font: 24pt \"Kirang Haerang\";\n"
"border:0;\n"
"qproperty-alignment: AlignCenter;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_3.addWidget(self.label_36, 0, QtCore.Qt.AlignTop)
        self.label_program_total_count = QtWidgets.QLabel(self.widget_7)
        self.label_program_total_count.setStyleSheet("font: 30pt \"Kirang Haerang\";\n"
"border:0;\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_total_count.setObjectName("label_program_total_count")
        self.verticalLayout_3.addWidget(self.label_program_total_count)
        self.label_37 = QtWidgets.QLabel(self.widget_7)
        self.label_37.setStyleSheet("font: 24pt \"Kirang Haerang\";\n"
"border:0;\n"
"qproperty-alignment: AlignCenter;")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_3.addWidget(self.label_37)
        self.horizontalLayout_9.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.ProgramFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_program_comment = QtWidgets.QLabel(self.widget_8)
        self.label_program_comment.setStyleSheet("font: 81 bold 18pt \"Apple SD Gothic Neo\";\n"
"border:0;\n"
"color: rgb(252, 2, 128);")
        self.label_program_comment.setIndent(20)
        self.label_program_comment.setObjectName("label_program_comment")
        self.verticalLayout_4.addWidget(self.label_program_comment, 0, QtCore.Qt.AlignTop)
        self.pictures_5_Frame = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictures_5_Frame.sizePolicy().hasHeightForWidth())
        self.pictures_5_Frame.setSizePolicy(sizePolicy)
        self.pictures_5_Frame.setObjectName("pictures_5_Frame")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.pictures_5_Frame)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_6 = QtWidgets.QFrame(self.pictures_5_Frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_program_1_count = QtWidgets.QLabel(self.frame_6)
        self.label_program_1_count.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_1_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_program_1_count.setObjectName("label_program_1_count")
        self.verticalLayout_16.addWidget(self.label_program_1_count)
        self.program_pic_1 = QtWidgets.QLabel(self.frame_6)
        self.program_pic_1.setMaximumSize(QtCore.QSize(100, 100))
        self.program_pic_1.setText("")
        self.program_pic_1.setPixmap(QtGui.QPixmap("images/movie.png"))
        self.program_pic_1.setScaledContents(True)
        self.program_pic_1.setObjectName("program_pic_1")
        self.verticalLayout_16.addWidget(self.program_pic_1)
        self.label_program_1_name = QtWidgets.QLabel(self.frame_6)
        self.label_program_1_name.setMinimumSize(QtCore.QSize(110, 0))
        self.label_program_1_name.setMaximumSize(QtCore.QSize(80, 80))
        self.label_program_1_name.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_1_name.setScaledContents(True)
        self.label_program_1_name.setObjectName("label_program_1_name")
        self.verticalLayout_16.addWidget(self.label_program_1_name)
        self.horizontalLayout_18.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(self.pictures_5_Frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_program_2_count = QtWidgets.QLabel(self.frame)
        self.label_program_2_count.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_2_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_program_2_count.setObjectName("label_program_2_count")
        self.verticalLayout_17.addWidget(self.label_program_2_count)
        self.program_pic_2 = QtWidgets.QLabel(self.frame)
        self.program_pic_2.setMaximumSize(QtCore.QSize(100, 100))
        self.program_pic_2.setText("")
        self.program_pic_2.setPixmap(QtGui.QPixmap("images/meditation.png"))
        self.program_pic_2.setScaledContents(True)
        self.program_pic_2.setObjectName("program_pic_2")
        self.verticalLayout_17.addWidget(self.program_pic_2)
        self.label_program_2_name = QtWidgets.QLabel(self.frame)
        self.label_program_2_name.setMinimumSize(QtCore.QSize(110, 0))
        self.label_program_2_name.setMaximumSize(QtCore.QSize(80, 80))
        self.label_program_2_name.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_2_name.setScaledContents(True)
        self.label_program_2_name.setObjectName("label_program_2_name")
        self.verticalLayout_17.addWidget(self.label_program_2_name)
        self.horizontalLayout_18.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.pictures_5_Frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_program_3_count = QtWidgets.QLabel(self.frame_2)
        self.label_program_3_count.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_3_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_program_3_count.setObjectName("label_program_3_count")
        self.verticalLayout_18.addWidget(self.label_program_3_count)
        self.program_pic_3 = QtWidgets.QLabel(self.frame_2)
        self.program_pic_3.setMaximumSize(QtCore.QSize(100, 100))
        self.program_pic_3.setText("")
        self.program_pic_3.setPixmap(QtGui.QPixmap("images/woman.png"))
        self.program_pic_3.setScaledContents(True)
        self.program_pic_3.setObjectName("program_pic_3")
        self.verticalLayout_18.addWidget(self.program_pic_3)
        self.label_program_3_name = QtWidgets.QLabel(self.frame_2)
        self.label_program_3_name.setMinimumSize(QtCore.QSize(110, 0))
        self.label_program_3_name.setMaximumSize(QtCore.QSize(80, 80))
        self.label_program_3_name.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_3_name.setScaledContents(True)
        self.label_program_3_name.setObjectName("label_program_3_name")
        self.verticalLayout_18.addWidget(self.label_program_3_name)
        self.horizontalLayout_18.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.pictures_5_Frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_program_4_count = QtWidgets.QLabel(self.frame_4)
        self.label_program_4_count.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_4_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_program_4_count.setObjectName("label_program_4_count")
        self.verticalLayout_20.addWidget(self.label_program_4_count)
        self.program_pic_4 = QtWidgets.QLabel(self.frame_4)
        self.program_pic_4.setMaximumSize(QtCore.QSize(100, 100))
        self.program_pic_4.setText("")
        self.program_pic_4.setPixmap(QtGui.QPixmap("images/poetry.png"))
        self.program_pic_4.setScaledContents(True)
        self.program_pic_4.setObjectName("program_pic_4")
        self.verticalLayout_20.addWidget(self.program_pic_4)
        self.label_program_4_name = QtWidgets.QLabel(self.frame_4)
        self.label_program_4_name.setMinimumSize(QtCore.QSize(110, 0))
        self.label_program_4_name.setMaximumSize(QtCore.QSize(80, 80))
        self.label_program_4_name.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_4_name.setScaledContents(True)
        self.label_program_4_name.setObjectName("label_program_4_name")
        self.verticalLayout_20.addWidget(self.label_program_4_name)
        self.horizontalLayout_18.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.pictures_5_Frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_program_5_count = QtWidgets.QLabel(self.frame_5)
        self.label_program_5_count.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_5_count.setAlignment(QtCore.Qt.AlignCenter)
        self.label_program_5_count.setObjectName("label_program_5_count")
        self.verticalLayout_19.addWidget(self.label_program_5_count)
        self.program_pic_5 = QtWidgets.QLabel(self.frame_5)
        self.program_pic_5.setMinimumSize(QtCore.QSize(0, 70))
        self.program_pic_5.setMaximumSize(QtCore.QSize(100, 100))
        self.program_pic_5.setText("")
        self.program_pic_5.setPixmap(QtGui.QPixmap("images/theater.png"))
        self.program_pic_5.setScaledContents(True)
        self.program_pic_5.setObjectName("program_pic_5")
        self.verticalLayout_19.addWidget(self.program_pic_5)
        self.label_program_5_name = QtWidgets.QLabel(self.frame_5)
        self.label_program_5_name.setMinimumSize(QtCore.QSize(110, 0))
        self.label_program_5_name.setMaximumSize(QtCore.QSize(80, 80))
        self.label_program_5_name.setStyleSheet("font: bold 13pt \"AppleSDGothicNeoB00\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_program_5_name.setScaledContents(True)
        self.label_program_5_name.setObjectName("label_program_5_name")
        self.verticalLayout_19.addWidget(self.label_program_5_name)
        self.horizontalLayout_18.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.pictures_5_Frame)
        self.horizontalLayout_9.addWidget(self.widget_8)
        self.gridLayout_7.addWidget(self.ProgramFrame, 3, 0, 1, 1)
        self.widget_18 = QtWidgets.QWidget(self.individual_suni)
        self.widget_18.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_18.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;\n"
"color:white;\n"
"padding-top:5px;")
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_67 = QtWidgets.QWidget(self.widget_18)
        self.widget_67.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_67.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_67.setObjectName("widget_67")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.widget_67)
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.btn_home_6 = QtWidgets.QPushButton(self.widget_67)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_6.sizePolicy().hasHeightForWidth())
        self.btn_home_6.setSizePolicy(sizePolicy)
        self.btn_home_6.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_home_6.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_home_6.setStyleSheet("QPushButton#btn_home_6{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_home_6:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_home_6.setText("")
        self.btn_home_6.setIcon(icon6)
        self.btn_home_6.setIconSize(QtCore.QSize(60, 60))
        self.btn_home_6.setObjectName("btn_home_6")
        self.horizontalLayout_42.addWidget(self.btn_home_6)
        self.btn_back_5 = QtWidgets.QPushButton(self.widget_67)
        self.btn_back_5.setMinimumSize(QtCore.QSize(60, 60))
        self.btn_back_5.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_back_5.setBaseSize(QtCore.QSize(100, 25))
        self.btn_back_5.setStyleSheet("QPushButton#btn_back_5{\n"
"font: 15pt \"AppleSDGothicNeoB00\";\n"
"text-align: bottom;\n"
"padding: 2px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#btn_back_5:hover{\n"
"    background-color:white;\n"
"    color: black;\n"
"}")
        self.btn_back_5.setText("")
        self.btn_back_5.setIcon(icon7)
        self.btn_back_5.setIconSize(QtCore.QSize(60, 60))
        self.btn_back_5.setObjectName("btn_back_5")
        self.horizontalLayout_42.addWidget(self.btn_back_5)
        self.horizontalLayout_10.addWidget(self.widget_67, 0, QtCore.Qt.AlignLeft)
        self.label_51 = QtWidgets.QLabel(self.widget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QtCore.QSize(800, 0))
        self.label_51.setStyleSheet("font: bold 25pt \"AppleSDGothicNeoB00\";")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_10.addWidget(self.label_51, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_7.addWidget(self.widget_18, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 2, 0, 1, 1)
        self.widget_19 = QtWidgets.QWidget(self.individual_suni)
        self.widget_19.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.widget_20 = QtWidgets.QWidget(self.widget_19)
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_34 = QtWidgets.QLabel(self.widget_20)
        self.label_34.setStyleSheet("font: 30pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_2.addWidget(self.label_34)
        self.label_suni_friendly_score = QtWidgets.QLabel(self.widget_20)
        self.label_suni_friendly_score.setStyleSheet("font: 30pt \"Kirang Haerang\";\n"
"qproperty-alignment: AlignCenter;")
        self.label_suni_friendly_score.setObjectName("label_suni_friendly_score")
        self.verticalLayout_2.addWidget(self.label_suni_friendly_score)
        self.horizontalLayout_16.addWidget(self.widget_20, 0, QtCore.Qt.AlignLeft)
        self.widget_21 = QtWidgets.QWidget(self.widget_19)
        self.widget_21.setMaximumSize(QtCore.QSize(130, 16777215))
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.image_suni_face = QtWidgets.QLabel(self.widget_21)
        self.image_suni_face.setMinimumSize(QtCore.QSize(100, 100))
        self.image_suni_face.setMaximumSize(QtCore.QSize(100, 100))
        self.image_suni_face.setStyleSheet("")
        self.image_suni_face.setText("")
        self.image_suni_face.setPixmap(QtGui.QPixmap("images/face_bad.png"))
        self.image_suni_face.setScaledContents(True)
        self.image_suni_face.setObjectName("image_suni_face")
        self.verticalLayout_26.addWidget(self.image_suni_face, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_16.addWidget(self.widget_21, 0, QtCore.Qt.AlignLeft)
        self.widget_22 = QtWidgets.QWidget(self.widget_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_28.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.widget_43 = QtWidgets.QWidget(self.widget_22)
        self.widget_43.setObjectName("widget_43")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_43)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_12 = QtWidgets.QLabel(self.widget_43)
        self.label_12.setStyleSheet("font: 15pt \"Kirang Haerang\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_20.addWidget(self.label_12, 0, QtCore.Qt.AlignLeft)
        self.label_suni_talk_count = QtWidgets.QLabel(self.widget_43)
        self.label_suni_talk_count.setStyleSheet("font: 87 18pt \"AppleSDGothicNeoB00\";")
        self.label_suni_talk_count.setObjectName("label_suni_talk_count")
        self.horizontalLayout_20.addWidget(self.label_suni_talk_count, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.verticalLayout_28.addWidget(self.widget_43)
        self.label_suni_talk_count_comment = QtWidgets.QLabel(self.widget_22)
        self.label_suni_talk_count_comment.setStyleSheet("font: 16pt \"Kirang Haerang\";\n"
"color: rgb(252, 1, 7);")
        self.label_suni_talk_count_comment.setWordWrap(True)
        self.label_suni_talk_count_comment.setObjectName("label_suni_talk_count_comment")
        self.verticalLayout_28.addWidget(self.label_suni_talk_count_comment)
        self.label_suni_talk_count_comment_2 = QtWidgets.QLabel(self.widget_22)
        self.label_suni_talk_count_comment_2.setAutoFillBackground(True)
        self.label_suni_talk_count_comment_2.setStyleSheet("font: 16pt \"Kirang Haerang\";\n"
"color: rgb(252, 1, 7);")
        self.label_suni_talk_count_comment_2.setObjectName("label_suni_talk_count_comment_2")
        self.verticalLayout_28.addWidget(self.label_suni_talk_count_comment_2)
        self.horizontalLayout_16.addWidget(self.widget_22)
        self.gridLayout_7.addWidget(self.widget_19, 1, 0, 1, 1)
        self.mainStackedWidget.addWidget(self.individual_suni)
        self.verticalLayout_32.addWidget(self.mainStackedWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainStackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_39.setText(_translate("MainWindow", "슬기로운 순이생활"))
        self.label_2.setText(_translate("MainWindow", "ID를 입력하세요"))
        self.id_blank.setPlaceholderText(_translate("MainWindow", "505"))
        self.btn_idSearch.setText(_translate("MainWindow", "검색"))
        self.tb_main_summary.setText(_translate("MainWindow", "8월은 순이와 조금 더 친해진 달이었어요."))
        self.tb_personal_info.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">(박순자 / 여성 / 96세)</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">슬기로운</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">수면생활</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">슬기로운</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">식사생활</span></p></body></html>"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">슬기로운</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">운동생활</span></p></body></html>"))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">슬기로운</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">건강생활</span></p></body></html>"))
        self.circularText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">25</span></p></body></html>"))
        self.tb_suni_time.setText(_translate("MainWindow", "(OOO님, 순이와 함께 보낸 시간을 보러 가볼까요?)"))
        self.suni_summarized_comment.setText(_translate("MainWindow", "순이와 궁합 65점! 우리 서로 가까워지는 중"))
        self.btn_goto_suni_1.setText(_translate("MainWindow", "자세히\n"
"보러가기"))
        self.label_52.setText(_translate("MainWindow", "평균 수면 시간"))
        self.sleep_average_time.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">3시간 54분</span></p></body></html>"))
        self.sleep_time_evaluation.setText(_translate("MainWindow", "적절한 수면 시간입니다"))
        self.label_sleep_suni_talk.setText(_translate("MainWindow", "순이의 잔소리 1"))
        self.monthly_sleep_score.setText(_translate("MainWindow", "(수면 점수)"))
        self.sleep_evaluation.setText(_translate("MainWindow", "(수면 점수 평가)"))
        self.label_8.setText(_translate("MainWindow", "8월 수면 레포트"))
        self.btn_goto_eat.setText(_translate("MainWindow", "식사"))
        self.btn_goto_exercise.setText(_translate("MainWindow", "운동"))
        self.btn_goto_medication.setText(_translate("MainWindow", "건강"))
        self.btn_goto_suni_2.setText(_translate("MainWindow", "순이 기록"))
        self.label_3.setText(_translate("MainWindow", "식사 대비 간식 섭취 횟수"))
        self.snack_ratio_comment.setText(_translate("MainWindow", "(식사와 간식 비율 평가)"))
        self.label_15.setText(_translate("MainWindow", "규칙적인 식사 여부"))
        self.eat_time_analysis.setText(_translate("MainWindow", "(식사 시간 규칙성 분석)"))
        self.label_9.setText(_translate("MainWindow", "8월 식사 레포트"))
        self.btn_goto_sleep.setText(_translate("MainWindow", "수면"))
        self.btn_goto_exercise_2.setText(_translate("MainWindow", "운동"))
        self.btn_goto_medication_2.setText(_translate("MainWindow", "건강"))
        self.btn_goto_suni_3.setText(_translate("MainWindow", "순이 기록"))
        self.label_13.setText(_translate("MainWindow", "간식 섭취 횟수"))
        self.snack_eat_count.setText(_translate("MainWindow", "(횟수)"))
        self.label_14.setText(_translate("MainWindow", "전체 음식 섭취 횟수"))
        self.total_eat_count.setText(_translate("MainWindow", "(횟수)"))
        self.label_47.setText(_translate("MainWindow", "식사 점수"))
        self.monthly_eat_score.setText(_translate("MainWindow", "(점수)"))
        self.label_10.setText(_translate("MainWindow", "8월 활동 레포트"))
        self.btn_goto_sleep_2.setText(_translate("MainWindow", "수면"))
        self.btn_goto_eat_2.setText(_translate("MainWindow", "식사"))
        self.btn_goto_medication_3.setText(_translate("MainWindow", "건강"))
        self.btn_goto_suni_4.setText(_translate("MainWindow", "순이 기록"))
        self.label_17.setText(_translate("MainWindow", "운동 점수"))
        self.monthly_exercise_score.setText(_translate("MainWindow", "(운동 점수)"))
        self.exercise_score_comment.setText(_translate("MainWindow", "(운동 점수에 대한 평가)"))
        self.label_activity_with_name.setText(_translate("MainWindow", "(이번 달 ___님의 평균 활동 분석이에요.)"))
        self.label_activity_list_comment.setText(_translate("MainWindow", "(활동 분석 그래프에 대한 순이의 평가)"))
        self.label_active_week_good.setText(_translate("MainWindow", "충분히 운동을 한 주차 : 5주차"))
        self.label_active_week_mid.setText(_translate("MainWindow", "운동이 조금 더 필요한 주차 : 1주차, 3주차, 4주차"))
        self.label_active_week_bad.setText(_translate("MainWindow", "심각한 운동 부족 주차 : 2주차"))
        self.label_11.setText(_translate("MainWindow", "8월 약 복용 레포트"))
        self.btn_goto_sleep_3.setText(_translate("MainWindow", "수면"))
        self.btn_goto_eat_3.setText(_translate("MainWindow", "식사"))
        self.btn_goto_exercise_3.setText(_translate("MainWindow", "운동"))
        self.btn_goto_suni_5.setText(_translate("MainWindow", "순이 기록"))
        self.label_7.setText(_translate("MainWindow", "이번 달 약 복용 기록"))
        self.medication_variance_score.setText(_translate("MainWindow", "TextLabel"))
        self.medication_calendar_comment.setText(_translate("MainWindow", "(OOO님, 이번 달에는...)"))
        self.medication_calendar_comment_2.setText(_translate("MainWindow", "(이렇게 불규칙적으로 약을 드시면...)"))
        self.day2_2.setText(_translate("MainWindow", "TextLabel"))
        self.day5_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_53.setText(_translate("MainWindow", "6日"))
        self.day3_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_54.setText(_translate("MainWindow", "3日"))
        self.label_56.setText(_translate("MainWindow", "2日"))
        self.label_58.setText(_translate("MainWindow", "4日"))
        self.label_59.setText(_translate("MainWindow", "1日"))
        self.day7_2.setText(_translate("MainWindow", "TextLabel"))
        self.day1_2.setText(_translate("MainWindow", "OOX"))
        self.label_60.setText(_translate("MainWindow", "5日"))
        self.label_61.setText(_translate("MainWindow", "7日"))
        self.day4_2.setText(_translate("MainWindow", "TextLabel"))
        self.day6_2.setText(_translate("MainWindow", "TextLabel"))
        self.day10_2.setText(_translate("MainWindow", "TextLabel"))
        self.day9_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_62.setText(_translate("MainWindow", "10日"))
        self.day8_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_63.setText(_translate("MainWindow", "11日"))
        self.label_64.setText(_translate("MainWindow", "9日"))
        self.label_65.setText(_translate("MainWindow", "12日"))
        self.label_66.setText(_translate("MainWindow", "13日"))
        self.day11_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_67.setText(_translate("MainWindow", "8日"))
        self.label_68.setText(_translate("MainWindow", "14日"))
        self.label_69.setText(_translate("MainWindow", "21日"))
        self.day12_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_70.setText(_translate("MainWindow", "15日"))
        self.day14_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_71.setText(_translate("MainWindow", "19日"))
        self.day15_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_72.setText(_translate("MainWindow", "16日"))
        self.label_73.setText(_translate("MainWindow", "17日"))
        self.day13_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_74.setText(_translate("MainWindow", "20日"))
        self.day16_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_75.setText(_translate("MainWindow", "18日"))
        self.day19_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_109.setText(_translate("MainWindow", "22日"))
        self.day21_2.setText(_translate("MainWindow", "TextLabel"))
        self.day17_2.setText(_translate("MainWindow", "TextLabel"))
        self.day24_2.setText(_translate("MainWindow", "TextLabel"))
        self.day26_2.setText(_translate("MainWindow", "TextLabel"))
        self.day20_2.setText(_translate("MainWindow", "TextLabel"))
        self.day25_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_110.setText(_translate("MainWindow", "23日"))
        self.label_111.setText(_translate("MainWindow", "24日"))
        self.day23_2.setText(_translate("MainWindow", "TextLabel"))
        self.day22_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_112.setText(_translate("MainWindow", "28日"))
        self.label_113.setText(_translate("MainWindow", "27日"))
        self.label_114.setText(_translate("MainWindow", "26日"))
        self.day18_2.setText(_translate("MainWindow", "TextLabel"))
        self.day27_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_119.setText(_translate("MainWindow", "29日"))
        self.day28_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_120.setText(_translate("MainWindow", "30日"))
        self.label_121.setText(_translate("MainWindow", "31日"))
        self.day30_2.setText(_translate("MainWindow", "TextLabel"))
        self.day29_2.setText(_translate("MainWindow", "TextLabel"))
        self.day31_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_115.setText(_translate("MainWindow", "25日"))
        self.label_6.setText(_translate("MainWindow", "8월 약 복용 횟수"))
        self.med_left.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">31</span></p></body></html>"))
        self.med_right.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">16</span></p></body></html>"))
        self.medication_day_count.setText(_translate("MainWindow", "31일 중 16일"))
        self.medication_day_count_trail.setText(_translate("MainWindow", "약을 복용하셨습니다"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">참여하신 프로그램의 특성은 아래와 같아요.</span></p></body></html>"))
        self.tb_program_preference_comment_1.setText(_translate("MainWindow", "(1. OOO님은 ___한 프로그램을 좋아하시는군요? ...)"))
        self.tb_program_preference_comment_2.setText(_translate("MainWindow", "(~~~에 ~~번이나 참가하셨어요.)"))
        self.label_55.setText(_translate("MainWindow", "참여도가 낮은 프로그램"))
        self.tb_program_preference_comment_3.setText(_translate("MainWindow", "(~~~에 ~~번이나 참가하셨어요.)"))
        self.label_36.setText(_translate("MainWindow", "순이 프로그램"))
        self.label_program_total_count.setText(_translate("MainWindow", "(139회)"))
        self.label_37.setText(_translate("MainWindow", "전체 합계"))
        self.label_program_comment.setText(_translate("MainWindow", "(매우 적극적으로 참여해 주셨습니다)"))
        self.label_program_1_count.setText(_translate("MainWindow", "(점수)"))
        self.label_program_1_name.setText(_translate("MainWindow", "무비순이"))
        self.label_program_2_count.setText(_translate("MainWindow", "(점수)"))
        self.label_program_2_name.setText(_translate("MainWindow", "시시콜콜"))
        self.label_program_3_count.setText(_translate("MainWindow", "(점수)"))
        self.label_program_3_name.setText(_translate("MainWindow", "순이극장"))
        self.label_program_4_count.setText(_translate("MainWindow", "(점수)"))
        self.label_program_4_name.setText(_translate("MainWindow", "순이체조"))
        self.label_program_5_count.setText(_translate("MainWindow", "(점수)"))
        self.label_program_5_name.setText(_translate("MainWindow", "마음산책"))
        self.label_51.setText(_translate("MainWindow", "     순이와의 대화, 프로그램 참여 내역"))
        self.label_34.setText(_translate("MainWindow", " 순이 친밀도"))
        self.label_suni_friendly_score.setText(_translate("MainWindow", "(친밀도 점수)"))
        self.label_12.setText(_translate("MainWindow", "순이와의 대화 횟수: "))
        self.label_suni_talk_count.setText(_translate("MainWindow", "(OO회)"))
        self.label_suni_talk_count_comment.setText(_translate("MainWindow", "(순이와 대화를 많이 나누지 않으셨습니다.)"))
        self.label_suni_talk_count_comment_2.setText(_translate("MainWindow", "(순이는 OO님이 있어서 즐거워요!)"))

