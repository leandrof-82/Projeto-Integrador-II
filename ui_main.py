# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 909)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.NoFocus)
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setStyleSheet(u"background-color: rgb(8, 8, 8);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.btn_table = QPushButton(self.frame)
        self.btn_table.setObjectName(u"btn_table")
        self.btn_table.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_table)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout.addWidget(self.label_16)

        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"IMG/images-removebg-preview.png"))
        self.logo.setWordWrap(True)

        self.horizontalLayout.addWidget(self.logo)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.page = QStackedWidget(self.centralwidget)
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.pg_table.setStyleSheet(u"background-color: rgb(141, 28, 30);")
        self.verticalLayout_3 = QVBoxLayout(self.pg_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(62, 62, 62);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_estoque = QLabel(self.tables)
        self.txt_estoque.setObjectName(u"txt_estoque")
        self.txt_estoque.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.txt_estoque)

        self.tw_estoque = QTreeWidget(self.tables)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setFont(3, font1);
        __qtreewidgetitem.setForeground(3, brush);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        self.tw_estoque.setHeaderItem(__qtreewidgetitem)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.tw_estoque)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_saida = QLabel(self.tables)
        self.txt_saida.setObjectName(u"txt_saida")
        self.txt_saida.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.txt_saida)

        self.tw_sada = QTreeWidget(self.tables)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(3, font1);
        __qtreewidgetitem1.setForeground(3, brush);
        __qtreewidgetitem1.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(2, font);
        __qtreewidgetitem1.setForeground(2, brush);
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(1, font);
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(0, font);
        self.tw_sada.setHeaderItem(__qtreewidgetitem1)
        self.tw_sada.setObjectName(u"tw_sada")
        self.tw_sada.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.tw_sada)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.frame_4 = QFrame(self.tables)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.btn_import = QPushButton(self.frame_4)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(21, 63, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_import)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.btn_exit = QPushButton(self.frame_4)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(100, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_exit)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.btn_estorno = QPushButton(self.frame_4)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(136, 136, 0);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_estorno)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_6.addWidget(self.label_23)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.page.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.pg_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(1060, 16777215))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignVCenter)

        self.page.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.pg_cadastro.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_17 = QLabel(self.pg_cadastro)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_29 = QLabel(self.pg_cadastro)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_12.addWidget(self.label_29)

        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.label_28 = QLabel(self.pg_cadastro)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_12.addWidget(self.label_28)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.TXT_NOME = QLineEdit(self.pg_cadastro)
        self.TXT_NOME.setObjectName(u"TXT_NOME")
        self.TXT_NOME.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")

        self.horizontalLayout_9.addWidget(self.TXT_NOME)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.TXT_USUARIO = QLineEdit(self.pg_cadastro)
        self.TXT_USUARIO.setObjectName(u"TXT_USUARIO")
        self.TXT_USUARIO.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")

        self.horizontalLayout_15.addWidget(self.TXT_USUARIO)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.TXT_SENHA = QLineEdit(self.pg_cadastro)
        self.TXT_SENHA.setObjectName(u"TXT_SENHA")
        self.TXT_SENHA.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.TXT_SENHA.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_13.addWidget(self.TXT_SENHA)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.TXT_C_SENHA = QLineEdit(self.pg_cadastro)
        self.TXT_C_SENHA.setObjectName(u"TXT_C_SENHA")
        self.TXT_C_SENHA.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.TXT_C_SENHA.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_14.addWidget(self.TXT_C_SENHA)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.pg_cadastro)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_10.addWidget(self.label_25)

        self.label_18 = QLabel(self.pg_cadastro)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_10.addWidget(self.label_13, 0, Qt.AlignVCenter)

        self.COMBOBOX_ADM_USUARIO = QComboBox(self.pg_cadastro)
        self.COMBOBOX_ADM_USUARIO.addItem("")
        self.COMBOBOX_ADM_USUARIO.addItem("")
        self.COMBOBOX_ADM_USUARIO.setObjectName(u"COMBOBOX_ADM_USUARIO")
        self.COMBOBOX_ADM_USUARIO.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.COMBOBOX_ADM_USUARIO)

        self.label_26 = QLabel(self.pg_cadastro)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_10.addWidget(self.label_26)

        self.label_19 = QLabel(self.pg_cadastro)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.BTN_CADASTRAR = QPushButton(self.pg_cadastro)
        self.BTN_CADASTRAR.setObjectName(u"BTN_CADASTRAR")
        self.BTN_CADASTRAR.setLayoutDirection(Qt.LeftToRight)
        self.BTN_CADASTRAR.setAutoFillBackground(False)
        self.BTN_CADASTRAR.setStyleSheet(u"QPushButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(98, 98, 98);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(122, 0, 0);\n"
"	\n"
"\n"
"}")
        self.BTN_CADASTRAR.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.BTN_CADASTRAR)

        self.label_15 = QLabel(self.pg_cadastro)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.page.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pg_sobre.setStyleSheet(u"background-color: rgb(157, 157, 157);")
        self.label_30 = QLabel(self.pg_sobre)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(480, 50, 101, 61))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_30.setFont(font3)
        self.page.addWidget(self.pg_sobre)

        self.verticalLayout_2.addWidget(self.page)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_7.addWidget(self.label_24)

        self.BTN_PG_CADASTRO = QPushButton(self.frame_5)
        self.BTN_PG_CADASTRO.setObjectName(u"BTN_PG_CADASTRO")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(9)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.BTN_PG_CADASTRO.setFont(font4)
        self.BTN_PG_CADASTRO.setStyleSheet(u"QPushButton{\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.494, radius:0.5, fx:0.5, fy:0.5, stop:0.40796 rgba(134, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.BTN_PG_CADASTRO)

        self.label_27 = QLabel(self.frame_5)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_7.addWidget(self.label_27)


        self.verticalLayout_2.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_table, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.BTN_PG_CADASTRO)
        QWidget.setTabOrder(self.BTN_PG_CADASTRO, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.txt_file)
        QWidget.setTabOrder(self.txt_file, self.btn_open)
        QWidget.setTabOrder(self.btn_open, self.tw_estoque)
        QWidget.setTabOrder(self.tw_estoque, self.tw_sada)
        QWidget.setTabOrder(self.tw_sada, self.btn_import)
        QWidget.setTabOrder(self.btn_import, self.btn_exit)
        QWidget.setTabOrder(self.btn_exit, self.btn_estorno)
        QWidget.setTabOrder(self.btn_estorno, self.TXT_NOME)
        QWidget.setTabOrder(self.TXT_NOME, self.COMBOBOX_ADM_USUARIO)
        QWidget.setTabOrder(self.COMBOBOX_ADM_USUARIO, self.TXT_USUARIO)
        QWidget.setTabOrder(self.TXT_USUARIO, self.TXT_SENHA)
        QWidget.setTabOrder(self.TXT_SENHA, self.BTN_CADASTRAR)
        QWidget.setTabOrder(self.BTN_CADASTRAR, self.TXT_C_SENHA)
        QWidget.setTabOrder(self.TXT_C_SENHA, self.btn_sobre)

        self.retranslateUi(MainWindow)

        self.page.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_5.setText("")
        self.label_11.setText("")
        self.btn_table.setText(QCoreApplication.translate("MainWindow", u"TABLE", None))
        self.label_6.setText("")
        self.label_16.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_3.setText("")
        self.logo.setText("")
        self.label_4.setText("")
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.txt_estoque.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O ", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"ITEM", None));
        self.txt_saida.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_sada.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"DATA SA\u00cdDA", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"C\u00d3DIGO", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"ITEM", None));
        self.label_20.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_21.setText("")
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"GERAR SA\u00cdDA", None))
        self.label_22.setText("")
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"ESTORNO", None))
        self.label_23.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#000000;\">PROJETO INTEGRADOR II:</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Sistema de Gerenciamento de Estoque</span></p><p align=\"center\"><span style=\" font-size:7pt; color:#000000;\">( LEANDRO E JO\u00c3O )</span></p><p align=\"center\"><br/><br/></p><p align=\"center\"><br/><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#cacaca;\">TELA DE CADASTRO:</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastrar Usu\u00e1rio</p></body></html>", None))
        self.label_28.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"  NOME:   ", None))
        self.TXT_NOME.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" USU\u00c1RIO:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  SENHA:  ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"  SENHA:  ", None))
        self.label_25.setText("")
        self.label_18.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">PERFIL:</span></p></body></html>", None))
        self.COMBOBOX_ADM_USUARIO.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.COMBOBOX_ADM_USUARIO.setItemText(1, QCoreApplication.translate("MainWindow", u"Adiministrador", None))

        self.label_26.setText("")
        self.label_19.setText("")
        self.label_14.setText("")
        self.BTN_CADASTRAR.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_15.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SOBRE</p></body></html>", None))
        self.label_24.setText("")
        self.BTN_PG_CADASTRO.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_27.setText("")
    # retranslateUi

