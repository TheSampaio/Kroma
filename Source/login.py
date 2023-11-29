from kroma import *
from home import FormHome

class FormMain(Form):

    def __init__(self) -> None:
        self.Initialize()

        # Set-up form's window
        self.GetWindow().SetIcon("Data\\Icon\\icon-group-retiro.ico")
        self.GetWindow().SetTitle("Login")
        self.GetWindow().SetSize(400, 300)
        self.GetWindow().SetResizable(False)

        # Creates the username's text box
        self.__Txt_User = self.CreateSubobject(TextBox())
        self.__Txt_User.SetAlignment(Align.CENTER)
        self.__Txt_User.SetAnchor(Anchor.CENTER)
        self.__Txt_User.SetPosition(0, -60)
        self.__Txt_User.SetSize(32, 1)
        self.__Txt_User.SetFocus(True)
        self.__Txt_User.SetPlaceholder("Username")

        # Creates the password's text box
        self.__Txt_Password = self.CreateSubobject(TextBox())
        self.__Txt_Password.SetAlignment(Align.CENTER)
        self.__Txt_Password.SetAnchor(Anchor.CENTER)
        self.__Txt_Password.SetPosition(0, -25)
        self.__Txt_Password.SetSize(32, 1)
        self.__Txt_Password.SetPasswordCharacter('*')
        self.__Txt_Password.SetPlaceholder("Password")

        # Creates the login's button
        self.__Btn_Login = self.CreateSubobject(Button())
        self.__Btn_Login.SetAnchor(Anchor.CENTER)
        self.__Btn_Login.SetText("Login")
        self.__Btn_Login.SetPosition(-50, 22)
        self.__Btn_Login.SetColor("white")
        self.__Btn_Login.SetBackgroundColor("royalblue")
        self.__Btn_Login.SetEvent(self.__Btn_Login_Click)

        # Creates the close's button
        self.__Btn_Close = self.CreateSubobject(Button())
        self.__Btn_Close.SetAnchor(Anchor.CENTER)
        self.__Btn_Close.SetText("Close")
        self.__Btn_Close.SetPosition(50, 22)
        self.__Btn_Close.SetColor("white")
        self.__Btn_Close.SetBackgroundColor("royalblue")
        self.__Btn_Close.SetEvent(self.__Btn_Close_Click)

        # Creates the footer's label
        self.__Lbl_Footer = self.CreateSubobject(Label())
        self.__Lbl_Footer.SetAnchor(Anchor.BOTTOM_RIGHT)
        self.__Lbl_Footer.SetText("Kroma 0.18.2 Copyright © 2023 - Kellvyn Sampaio")
        self.__Lbl_Footer.SetColor("gray")

    # Creates the login's click event
    def __Btn_Login_Click(self):
        
        if (self.__Txt_User.GetContent().lower() == "admin" and self.__Txt_Password.GetContent() == "1234"):
            self.__Txt_Password.Clear()

            # New form
            Frm_Home = FormHome()
            Frm_Home.GetWindow().SetIcon(self.GetWindow().GetIcon())
            Frm_Home.Run()

        else:
            MessageBox.Show("Please, verify your username and password.", MessageBoxType.WARNING)
            self.GetWindow().Shake()

    # Creates the close's click event
    def __Btn_Close_Click(self):
        self.GetWindow().Close()
