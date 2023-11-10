import sys
from PySide2.QtWidgets import(QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
from database import DataBase




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
       
    
        

        #*************PAGINAS DO SISTEMA***********************************************
        self.btn_home.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_home))
        self.btn_table.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_table))
        self.btn_sobre.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_sobre))
        

        self.BTN_PG_CADASTRO.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_cadastro))
    
        self.BTN_CADASTRAR.clicked.connect(self.subscribe_users)
    
    
    def subscribe_users(self):

        if self.TXT_SENHA.text() != self.TXT_C_SENHA.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Divergentes")
            msg.setText("A senha não é igual!")
            msg.exec_()
            return None
        
        nome = self.TXT_NOME.text()
        user = self.TXT_USUARIO.text()
        password = self.TXT_SENHA.text()
        access = self.COMBOBOX_ADM_USUARIO.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()
        
        self.TXT_NOME.setText("")
        self.TXT_USUARIO.setText("")
        self.TXT_SENHA.setText("")
        self.TXT_C_SENHA.setText("")

class Login(QWidget, Ui_Login, DataBase):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_entrar.clicked.connect(self.open_system)
        
    def open_system(self):
       if self.txt_senha.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
       else:
            print('SENHA INVÁLIDA')

    

if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

