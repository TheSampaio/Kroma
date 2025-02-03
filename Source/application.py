from kroma import *

class Application(Window):
    
    def _OnConstruct(self) -> None:
        self.SetSize(400, 300)
        self.SetPosition(
            (Screen.GetResolution()[0] / 2) - (self.GetSize()[0] / 2),
            (Screen.GetResolution()[1] / 2) - (self.GetSize()[1] / 2))
        
        self.SetResizable(False)
        self.SetTitle("Kroma Control Panel")

    def _OnStart(self) -> None:
        self.__lblFooter = Label()
        self.__lblFooter.SetAnchor(Anchor.BOTTOM_RIGHT)
        self.__lblFooter.SetForegroundColour(Color.GRAY)
        self.__lblFooter.SetFocus(True)
        self.__lblFooter.SetText("Powered By Kroma - Copyright © 2023-2025")
        self.AddWidget(self.__lblFooter)

        self.__btnLogin = Button()
        self.__btnLogin.SetAnchor(Anchor.CENTER)
        self.__btnLogin.SetText("Login")
        self.__btnLogin.SetEvent(self.__BtnLoginClick)
        self.AddWidget(self.__btnLogin)

    def __BtnLoginClick(self):
        MessageBox.ShowWarning("It's not functional yet, but I'm still working on it!")
