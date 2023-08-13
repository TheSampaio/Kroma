from interpork import *
from home import FormHome

class FormMain(Form):

    def __init__(self) -> None:
        self._Initialze_()
        self.__ICON = "Source\\Data\\Icon\\icon-group-retiro.ico"

        self.GetWindow().SetIcon(self.__ICON)
        self.GetWindow().SetTitle("Login")
        self.GetWindow().SetSize(400, 300)

        self.__Lbl_User = Label()
        self.__Lbl_User.SetAnchor(Anchor.CENTER)
        self.__Lbl_User.SetText("User: ")
        self.__Lbl_User.SetPosition(-84, -80)
        self.__Lbl_User.Create()

        self.__Txt_User = TextBox()
        self.__Txt_User.SetAnchor(Anchor.CENTER)
        self.__Txt_User.SetPosition(0, -60)
        self.__Txt_User.SetSize(32, 1)
        self.__Txt_User.SetFocus(True)
        self.__Txt_User.Create()

        self.__Lbl_Password = Label()
        self.__Lbl_Password.SetAnchor(Anchor.CENTER)
        self.__Lbl_Password.SetText("Password: ")
        self.__Lbl_Password.SetPosition(-69, -35)
        self.__Lbl_Password.Create()

        self.__Txt_Password = TextBox()
        self.__Txt_Password.SetAnchor(Anchor.CENTER)
        self.__Txt_Password.SetPosition(0, -15)
        self.__Txt_Password.SetSize(32, 1)
        self.__Txt_Password.Create()

        self.__Btn_Login = Button()
        self.__Btn_Login.SetAnchor(Anchor.CENTER)
        self.__Btn_Login.SetText("Login")
        self.__Btn_Login.SetPosition(-50, 22)
        self.__Btn_Login.SetEvent(self.__Btn_Login_Click)
        self.__Btn_Login.SetColor("white")
        self.__Btn_Login.SetBackgroundColor("royalblue")
        self.__Btn_Login.Create()

        self.__Btn_Close = Button()
        self.__Btn_Close.SetAnchor(Anchor.CENTER)
        self.__Btn_Close.SetText("Close")
        self.__Btn_Close.SetPosition(50, 22)
        self.__Btn_Close.SetEvent(self.__Btn_Close_Click)
        self.__Btn_Close.SetColor("white")
        self.__Btn_Close.SetBackgroundColor("royalblue")
        self.__Btn_Close.Create()

        self.__Lbl_Footer = Label()
        self.__Lbl_Footer.SetAnchor(Anchor.BOTTOM_RIGHT)
        self.__Lbl_Footer.SetText("Interpork 0.1.0 Copyright © 2023 Grupo Retiro")
        self.__Lbl_Footer.SetColor("gray")
        self.__Lbl_Footer.Create()

    def __Btn_Login_Click(self):
        print(f"\nUsername: {self.__Txt_User.GetValue()}")
        print(f"Password: {self.__Txt_Password.GetValue()}")

        Frm_Home = FormHome()
        Frm_Home.GetWindow().SetIcon(self.__ICON)
        Frm_Home.Run()

    def __Btn_Close_Click(self):
        self.GetWindow().Close()
