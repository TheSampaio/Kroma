from interpork import *

if __name__ == "__main__":

    Wnd_Window = Window()
    Wnd_Window.SetTitle("Login")
    Wnd_Window.SetSize(400, 300)

    Btn_Login = Button()
    Btn_Login.SetText("Login")
    Btn_Login.SetAnchor(Anchor.CENTER)
    Btn_Login.SetPosition(-50, 60)
    Btn_Login.Create()

    Btn_Close = Button()
    Btn_Close.SetEvent(Wnd_Window.Close)
    Btn_Close.SetText("Close")
    Btn_Close.SetAnchor(Anchor.CENTER)
    Btn_Close.SetPosition(50, 60)
    Btn_Close.Create()

    Wnd_Window.Create()
