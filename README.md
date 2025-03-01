# Kroma

Kroma is a lightweight, object-oriented GUI framework built on top of Tkinter, designed to simplify the creation of graphical user interfaces in Python. It provides an intuitive API for building windows, managing widgets, and handling events efficiently.

## Features
- **Simplified Window & Widget Management** – Easily create and manage GUI components.
- **Predefined Color & Alignment Options** – Enhance UI customization with built-in styles.
- **Message Box Utilities** – Display pop-up dialogs for user interaction.
- **Screen Resolution Retrieval** – Easily access screen dimensions.
- **Customizable Widget Properties** – Dynamically modify UI elements.
- **Event-Driven Design** – Efficiently handle user interactions and input events.

## Installation
Kroma is built on top of Tkinter, which comes pre-installed with Python. No additional installation is required.

## Getting Started

### Creating a Window
```python
from kroma import Window  

class MyWindow(Window):  
    pass  

# Your main function (can be in a separate file)
if __name__ == "__main__":  
    MyWindow().Run()  
```

### Customizing the Window
```python
from kroma import Window  

class MyWindow(Window):  

    def _OnConstruct(self):  

        # Window setup  
        self.SetIcon("path-to-your-icon/icon.ico")  
        self.SetResizable(False)  
        self.SetSize(1280, 720)  
        self.SetTitle("Kroma Window")  
```

### Adding a Button
```python
from kroma import Anchor, Button, MessageBox, Window  

class MyWindow(Window):  

    def _OnStart(self):  

        # Button setup  
        self.__btnClickMe = Button()  
        self.__btnClickMe.SetAnchor(Anchor.CENTER)  
        self.__btnClickMe.SetText("Click Me")  
        self.__btnClickMe.SetEvent(self.__BtnClickMeEvent)  

        # Add button to the window  
        self.AddWidget(self.__btnClickMe)  

    def __BtnClickMeEvent(self):  
        """Handles the 'Click Me' button event."""

        # TODO: Do something... Like open another window!  
```

### Displaying Message Boxes
```python
from kroma import MessageBox  

MessageBox.ShowInfo("Hello Kroma!", "Greeting")  
```

### Retrieving Screen Resolution
```python
from kroma import MessageBox, Screen  

resolution = Screen.GetResolution()  
MessageBox.ShowInfo(f"Screen Resolution: {resolution[0]}x{resolution[1]}")   
```

### Full Example: Kroma Login Window
```python
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

if __name__ == "__main__":  
    Application().Run()  
```

## License
Kroma is open-source and free to use in personal and commercial projects under the **BSD 2-Clause License**.

You are free to use, modify, and distribute the software, provided that proper attribution is given.

For full details, see the LICENSE file included in the repository.
