# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(463, 471)
        Login.setCursor(QCursor(Qt.ArrowCursor))
        Login.setMouseTracking(False)
        Login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.img = QLabel(Login)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(180, 100, 111, 91))
        self.img.setCursor(QCursor(Qt.ForbiddenCursor))
        self.img.setStyleSheet(u"background-color: rgba(0.255,0.255,0.255,0.255);")
        self.img.setPixmap(QPixmap(u"IMG/47772-removebg.png"))
        self.img.setScaledContents(True)
        self.txt_senha = QLineEdit(Login)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(140, 320, 191, 20))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.txt_senha.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.txt_usuario = QLineEdit(Login)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(140, 250, 191, 20))
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_usuario.setReadOnly(False)
        self.btn_entrar = QPushButton(Login)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(190, 380, 91, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 0, 0, 255))
        gradient.setColorAt(1, QColor(255, 255, 255, 255))
        brush2 = QBrush(gradient)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(0, 0, 0, 255))
        gradient1.setColorAt(1, QColor(255, 255, 255, 255))
        brush3 = QBrush(gradient1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(0, 0, 0, 255))
        gradient2.setColorAt(1, QColor(255, 255, 255, 255))
        brush4 = QBrush(gradient2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(0, 0, 0, 255))
        gradient3.setColorAt(1, QColor(255, 255, 255, 255))
        brush5 = QBrush(gradient3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(0, 0, 0, 255))
        gradient4.setColorAt(1, QColor(255, 255, 255, 255))
        brush6 = QBrush(gradient4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(0, 0, 0, 255))
        gradient5.setColorAt(1, QColor(255, 255, 255, 255))
        brush7 = QBrush(gradient5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(0, 0, 0, 255))
        gradient6.setColorAt(1, QColor(255, 255, 255, 255))
        brush8 = QBrush(gradient6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(0, 0, 0, 255))
        gradient7.setColorAt(1, QColor(255, 255, 255, 255))
        brush9 = QBrush(gradient7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(0, 0, 0, 255))
        gradient8.setColorAt(1, QColor(255, 255, 255, 255))
        brush10 = QBrush(gradient8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
        self.btn_entrar.setPalette(palette1)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
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
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
#if QT_CONFIG(tooltip)
        Login.setToolTip(QCoreApplication.translate("Login", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        Login.setWhatsThis(QCoreApplication.translate("Login", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.img.setText("")
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Login", u"SENHA", None))
#if QT_CONFIG(tooltip)
        self.txt_usuario.setToolTip(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"USU\u00c1RIO", None))
        self.btn_entrar.setText(QCoreApplication.translate("Login", u"ENTRAR", None))
    # retranslateUi

