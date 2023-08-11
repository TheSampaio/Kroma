from interpork import *

if __name__ == "__main__":

    Wnd_Window = Window()
    Wnd_Window.SetTitle("Login")
    Wnd_Window.SetSize(400, 300)

    Lbl_User = Label()
    Lbl_User.SetAnchor(Anchor.CENTER)
    Lbl_User.SetText("User: ")
    Lbl_User.SetPosition(-84, -80)
    Lbl_User.Create()

    Txt_User = TextBox()
    Txt_User.SetAnchor(Anchor.CENTER)
    Txt_User.SetPosition(0, -60)
    Txt_User.SetSize(24, 1)
    Txt_User.Create()

    Lbl_Password = Label()
    Lbl_Password.SetAnchor(Anchor.CENTER)
    Lbl_Password.SetText("Password: ")
    Lbl_Password.SetPosition(-69, -35)
    Lbl_Password.Create()

    Txt_Password = TextBox()
    Txt_Password.SetAnchor(Anchor.CENTER)
    Txt_Password.SetPosition(0, -15)
    Txt_Password.SetSize(24, 1)
    Txt_Password.Create()

    Btn_Login = Button()
    Btn_Login.SetAnchor(Anchor.CENTER)
    Btn_Login.SetText("Login")
    Btn_Login.SetPosition(-50, 22)
    Btn_Login.Create()

    Btn_Close = Button()
    Btn_Close.SetAnchor(Anchor.CENTER)
    Btn_Close.SetText("Close")
    Btn_Close.SetPosition(50, 22)
    Btn_Close.SetEvent(Wnd_Window.Close)
    Btn_Close.Create()

    Lbl_Footer = Label()
    Lbl_Footer.SetAnchor(Anchor.BOTTOM_RIGHT)
    Lbl_Footer.SetText("Interpork 0.1.0 Copyright © 2023 Grupo Retiro")
    Lbl_Footer.Create()

    Wnd_Window.Create()
