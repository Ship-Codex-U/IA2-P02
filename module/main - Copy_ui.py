# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main - Copy.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(966, 596)
        MainWindow.setStyleSheet(u"QTextEdit {\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #45a049;\n"
"border-radius: 7px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 200))
        self.frame.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 31, 31);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.layout_graphic = QVBoxLayout()
        self.layout_graphic.setObjectName(u"layout_graphic")

        self.horizontalLayout_5.addLayout(self.layout_graphic)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(10, 134, 169);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.output_weight_01 = QTextEdit(self.frame_2)
        self.output_weight_01.setObjectName(u"output_weight_01")
        self.output_weight_01.setMaximumSize(QSize(16777215, 25))
        self.output_weight_01.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.output_weight_01.setTabChangesFocus(True)
        self.output_weight_01.setReadOnly(True)
        self.output_weight_01.setCursorWidth(0)

        self.verticalLayout_7.addWidget(self.output_weight_01)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.output_weight_02 = QTextEdit(self.frame_2)
        self.output_weight_02.setObjectName(u"output_weight_02")
        self.output_weight_02.setMaximumSize(QSize(16777215, 25))
        self.output_weight_02.setStyleSheet(u"background-color: rgb(236, 243, 244);")
        self.output_weight_02.setTabChangesFocus(True)
        self.output_weight_02.setReadOnly(True)
        self.output_weight_02.setCursorWidth(0)

        self.verticalLayout_8.addWidget(self.output_weight_02)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.output_bias = QTextEdit(self.frame_2)
        self.output_bias.setObjectName(u"output_bias")
        self.output_bias.setMaximumSize(QSize(16777215, 25))
        self.output_bias.setStyleSheet(u"background-color: rgb(236, 243, 244);")
        self.output_bias.setTabChangesFocus(True)
        self.output_bias.setReadOnly(True)
        self.output_bias.setCursorWidth(0)

        self.verticalLayout_9.addWidget(self.output_bias)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_12.addWidget(self.label_14)

        self.input_alpha = QTextEdit(self.frame_2)
        self.input_alpha.setObjectName(u"input_alpha")
        self.input_alpha.setMaximumSize(QSize(16777215, 25))
        self.input_alpha.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.input_alpha.setTabChangesFocus(True)

        self.verticalLayout_12.addWidget(self.input_alpha)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.input_iterations = QTextEdit(self.frame_2)
        self.input_iterations.setObjectName(u"input_iterations")
        self.input_iterations.setMaximumSize(QSize(16777215, 25))
        self.input_iterations.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.input_iterations.setTabChangesFocus(True)

        self.verticalLayout_14.addWidget(self.input_iterations)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.button_generate_data_new = QPushButton(self.frame_2)
        self.button_generate_data_new.setObjectName(u"button_generate_data_new")
        self.button_generate_data_new.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(8)
        self.button_generate_data_new.setFont(font2)
        self.button_generate_data_new.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_13.addWidget(self.button_generate_data_new)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_start = QPushButton(self.frame_2)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(0, 35))
        self.button_start.setFont(font2)
        self.button_start.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_5.addWidget(self.button_start)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.button_clean = QPushButton(self.frame_2)
        self.button_clean.setObjectName(u"button_clean")
        self.button_clean.setMinimumSize(QSize(0, 35))
        self.button_clean.setFont(font2)
        self.button_clean.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_15.addWidget(self.button_clean)


        self.horizontalLayout.addLayout(self.verticalLayout_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.v3 = QVBoxLayout()
        self.v3.setSpacing(12)
        self.v3.setObjectName(u"v3")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.v3.addWidget(self.label_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.slider_weight_01 = QSlider(self.frame_2)
        self.slider_weight_01.setObjectName(u"slider_weight_01")
        self.slider_weight_01.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.slider_weight_01)

        self.label_weight_01 = QLabel(self.frame_2)
        self.label_weight_01.setObjectName(u"label_weight_01")
        self.label_weight_01.setFont(font1)
        self.label_weight_01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_weight_01)


        self.v3.addLayout(self.verticalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.slider_weight_02 = QSlider(self.frame_2)
        self.slider_weight_02.setObjectName(u"slider_weight_02")
        self.slider_weight_02.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_weight_02)

        self.label_weight_02 = QLabel(self.frame_2)
        self.label_weight_02.setObjectName(u"label_weight_02")
        self.label_weight_02.setFont(font1)
        self.label_weight_02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_weight_02)


        self.v3.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.slider_bias = QSlider(self.frame_2)
        self.slider_bias.setObjectName(u"slider_bias")
        self.slider_bias.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.slider_bias)

        self.label_bias = QLabel(self.frame_2)
        self.label_bias.setObjectName(u"label_bias")
        self.label_bias.setFont(font1)
        self.label_bias.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_bias)


        self.v3.addLayout(self.verticalLayout_11)


        self.verticalLayout_3.addLayout(self.v3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Perceptr\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Parametros Iniciales", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Peso 1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Peso 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Taza Aprendizaje", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Numero Iteraciones", None))
        self.button_generate_data_new.setText(QCoreApplication.translate("MainWindow", u"Nuevos\n"
"Parametros", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Iniciar Analisis", None))
        self.button_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Modificaci\u00f3n de los parametros.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peso 01", None))
        self.label_weight_01.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso 02", None))
        self.label_weight_02.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.label_bias.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

