from kroma import *

class Application(Window):  

    def _OnConstruct(self) -> None:  
        self.SetSize(400, 300)  
        
        # Center window's position
        self.SetPosition(
            (Screen.GetResolution()[0] - self.GetSize()[0]) / 2,
            (Screen.GetResolution()[1] - self.GetSize()[1]) / 2
        )  

        self.SetResizable(False)  
        self.SetTitle("Kroma Login Window")  

    def _OnStart(self) -> None:  

        # Username text box setup
        self.__TxtUsername = TextBox()
        self.__TxtUsername.SetAnchor(Anchor.CENTER)
        self.__TxtUsername.SetAlignment(Align.CENTER)
        self.__TxtUsername.SetFocus(True)
        self.__TxtUsername.SetPosition(0, -35)
        self.__TxtUsername.SetPlaceholder("Username")
        self.__TxtUsername.SetSize(25, 1)
        self.AddWidget(self.__TxtUsername)

        # Password text box setup
        self.__TxtPassword = TextBox()
        self.__TxtPassword.SetAnchor(Anchor.CENTER)
        self.__TxtPassword.SetAlignment(Align.CENTER)
        self.__TxtPassword.SetPasswordCharacter("*")
        self.__TxtPassword.SetPosition(0, -10)
        self.__TxtPassword.SetPlaceholder("Password")
        self.__TxtPassword.SetSize(25, 1)
        self.AddWidget(self.__TxtPassword)

        # Login button  
        self.__btnLogin = Button()  
        self.__btnLogin.SetAnchor(Anchor.CENTER)  
        self.__btnLogin.SetEvent(self.__BtnLoginClick)  
        self.__btnLogin.SetPosition(0, 15)
        self.__btnLogin.SetSize(25, 1)
        self.__btnLogin.SetText("Login")  
        self.AddWidget(self.__btnLogin)  

        # Footer label  
        self.__lblFooter = Label()  
        self.__lblFooter.SetAnchor(Anchor.BOTTOM_RIGHT)  
        self.__lblFooter.SetForegroundColor(Color.GRAY)  
        self.__lblFooter.SetFocus(True)  
        self.__lblFooter.SetText("Powered by Kroma - Copyright © 2023-2025") 
        self.AddWidget(self.__lblFooter)  

    def __BtnLoginClick(self):  

        if (self.__TxtUsername.GetText() == "" or self.__TxtPassword.GetText() == ""):
            MessageBox.ShowWarning("Username or password not provided.")
            return

        if (self.__TxtUsername.GetText().lower() == "admin" and self.__TxtPassword.GetText() == "1234"):
            self.__TxtPassword.Clear()
            MessageBox.ShowInfo("Login successful! Opening a new window.")
            
        else:
            MessageBox.ShowError("Invalid login credentials.")
