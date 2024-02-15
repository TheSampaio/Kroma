from kroma import Align, Anchor, Button, Colour, Label, MessageBox, MessageBoxType, TextBox, Window
from home import FormHome

class FormLogin(Window):

    def OnConstruct(self) -> None:
        # Set-up form's window
        self.SetIcon("Data\\Icon\\icon-kroma.ico")
        self.SetResizable(False)
        self.SetSize(400, 300)
        self.SetTitle("Login")

    def OnStart(self) -> None:
        # Creates the username's text box
        self.__Txt_User = TextBox()
        self.__Txt_User.SetAlignment(Align.CENTER)
        self.__Txt_User.SetAnchor(Anchor.CENTER)
        self.__Txt_User.SetPosition(0, -60)
        self.__Txt_User.SetSize(32, 1)
        self.__Txt_User.SetFocus(True)
        self.__Txt_User.SetPlaceholder("Username")
        self.AddWidget(self.__Txt_User)

        # Creates the password's text box
        self.__Txt_Password = TextBox()
        self.__Txt_Password.SetAlignment(Align.CENTER)
        self.__Txt_Password.SetAnchor(Anchor.CENTER)
        self.__Txt_Password.SetPosition(0, -25)
        self.__Txt_Password.SetSize(32, 1)
        self.__Txt_Password.SetPasswordCharacter('•')
        self.__Txt_Password.SetPlaceholder("Password")
        self.AddWidget(self.__Txt_Password)

        # Creates the login's button
        self.__Btn_Login = Button()
        self.__Btn_Login.SetAnchor(Anchor.CENTER)
        self.__Btn_Login.SetText("Login")
        self.__Btn_Login.SetPosition(-52, 22)
        self.__Btn_Login.SetSize(14, 0)
        self.__Btn_Login.SetEvent(self.__Btn_Login_Click)
        self.AddWidget(self.__Btn_Login)

        # Creates the close's button
        self.__Btn_Close = Button()
        self.__Btn_Close.SetAnchor(Anchor.CENTER)
        self.__Btn_Close.SetText("Close")
        self.__Btn_Close.SetPosition(52, 22)
        self.__Btn_Close.SetSize(14, 0)
        self.__Btn_Close.SetEvent(self.__Btn_Close_Click)
        self.AddWidget(self.__Btn_Close)

        # Creates the footer's label
        self.__Lbl_Footer = Label()
        self.__Lbl_Footer.SetAnchor(Anchor.BOTTOM_RIGHT)
        self.__Lbl_Footer.SetText("Kroma 2.1.1 (Alpha) Copyright © 2023-2024 Kellvyn Sampaio")
        self.__Lbl_Footer.SetForegroundColour(Colour.GREY)
        self.AddWidget(self.__Lbl_Footer)

    # Creates the login's click event
    def __Btn_Login_Click(self):
        
        if (self.__Txt_User.GetContent().lower() == "admin" and self.__Txt_Password.GetContent() == "1234"):
            self.__Txt_Password.Clear()

            # New window
            self.AddWindow(FormHome(), destroy=True)

        else:
            MessageBox.Show("Please, verify your username and password.", type=MessageBoxType.WARNING)

    # Creates the close's click event
    def __Btn_Close_Click(self):
        self.Close()
