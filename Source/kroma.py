import tkinter
from tkinter import messagebox
from tkinter import ttk
from time import sleep


class Align():

    # === Attributes ===
    
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Anchor():

    # === Attributes ===

    CENTER = "center"
    TOP = "n"
    TOP_RIGHT = "ne"
    TOP_LEFT = "nw"
    BOTTOM = "s"
    BOTTOM_RIGHT = "se"
    BOTTOM_LEFT = "sw"
    RIGHT = "e"
    LEFT = "w"


class Colour():

    # === Attributes ===

    AQUA = "#00FFFF"
    BLACK = "#000000"
    BLUE = "#0000FF"
    CYAN = "00FFFF"
    FUCHSIA = "#FF00FF"
    GREEN = "#008000"
    GREY = "#808080"
    LIME = "#00FF00"
    MAROON = "#800000"
    NAVY = "#000080"
    OLIVE = "#808000"
    ORANGE = "#F38020"
    PINK = "#EB459E"
    PURPLE = "#800080"
    RED = "#FF0000"
    ROYAL = "#4169E1"
    SILVER = "#C0C0C0"
    TEAL = "#008080"
    VIOLET = "#52057F"
    WHITE = "#FFFFFF"
    YELLOW = "#FFFF00"


class Cursor():

    # === Attributes ===

    ARROW = "arrow"
    HAND = "hand2"


class Event():

    # === Attributes ===

    DESTROY = "<Destroy>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class MessageBoxType():

    # === Attributes ===

    INFORMATION = 0
    WARNING = 1
    ERROR = 2
    QUESTION = 3


class MessageBox():

    # === MAIN methods ===

    @staticmethod
    def Show(message : str, title="Message Box", type=MessageBoxType.INFORMATION) -> bool:
        """ It shows a message box. Returns true if it succeeds or if the 'Yes' option was chosen (Question message box). """

        match (type):
            case MessageBoxType.QUESTION:
                if (title == "Message Box"):
                    title = "Question"

                return True if (messagebox.askyesno(title, message)) else False

            case MessageBoxType.ERROR:
                if (title == "Message Box"):
                    title = "Error"

                messagebox.showerror(title, message)
                return True

            case MessageBoxType.WARNING:
                if (title == "Message Box"):
                    title = "Warning"

                messagebox.showwarning(title, message)
                return True
            
            case _:
                if (title == "Message Box"):
                    title = "Information"
                    
                messagebox.showinfo(title, message)
                return True


class State():

    # === Attributes ===

    NORMAL = "normal"
    MINIMIZED = "iconic"
    MAXIMIZED = "zoomed"
    HIDDEN = "withdrawn"


class Widget():

    def __init__(self) -> None:

        # === Attributes ===

        # • Data
        self._id = None
        self._root = None

        # • Appearance
        self._foregroundColour = Colour.BLACK
        self._backgroundColour = Colour.WHITE

        # • Behavior
        self._enabled = True
        # self._visible = True (Work in progress)
        self._focused = False

        # • Layout
        self._anchor = Anchor.TOP_LEFT
        self._padding = [0, 0]
        self._position = [0, 0]
        self._size = [12, 1]

    # === GET methods ===

    # • Data
    def GetId(self):
        """ Gets the widget's id. """
        return self._id
    
    def GetRoot(self) -> tkinter.Tk:
        """ Gets the widget's root. """
        return self._root
    
    # • Appearance
    def GetForeColour(self) -> str:
        return self._foregroundColour
    
    def GetBackgroundColour(self) -> str:
        return self._backgroundColour

    # • Behavior
    def GetFocus(self) -> bool:
        return self._focused
    
    # • Layout
    def GetAnchor(self) -> str:
        """ Gets the widget's anchor. """
        return self._anchor
    
    def GetPosition(self) -> list:
        """ Gets the widget's position in pixels. """
        return self._position
    
    def GetSize(self) -> list:
        """ Gets the widget's size in pixels. """
        return self._size

    # === SET methods ===

    # • Data
    def SetRoot(self, root) -> None:
        """ Sets the widget's root. """
        self._root = root

    # • Appearance
    def SetForegroundColour(self, colour: str) -> None:
        """ Sets the widget's foreground colour. """
        self._foregroundColour = colour
    
    def SetBackgroundColour(self, backgroundColour: str) -> None:
        """ Sets the widget's background colour. """
        self._backgroundColour = backgroundColour

    # • Behavior
    def SetFocus(self, enable: bool) -> None:
        """ Focus the widget. """
        self._focused = enable

    # • Layout
    def SetAnchor(self, anchor: Anchor) -> None:
        """ Sets the widget's anchor. """

        match (anchor):
            case Anchor.CENTER:
                self._anchor = anchor
                self._padding = [0.5, 0.5]

            case Anchor.TOP:
                self._anchor = anchor
                self._padding = [0.5, 0.0]

            case Anchor.TOP_RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 0.0]

            case Anchor.TOP_LEFT:
                self._anchor = anchor
                self._padding = [0.0, 0.0]

            case Anchor.BOTTOM:
                self._anchor = anchor
                self._padding = [0.5, 1.0]

            case Anchor.BOTTOM_RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 1.0]

            case Anchor.BOTTOM_LEFT:
                self._anchor = anchor
                self._padding = [0.0, 1.0]

            case Anchor.RIGHT:
                self._anchor = anchor
                self._padding = [1.0, 0.5]

            case Anchor.LEFT:
                self._anchor = anchor
                self._padding = [0.0, 0.5]

    def SetPosition(self, x: int, y: int) -> None:
        """ Sets the widget's position in pixels. """
        self._position = [x, y]

    def SetSize(self, width: int, height: int) -> None:
        """ Sets the widget's size in pixels. """
        self._size = [width, height]


class Window():

    def __init__(self) -> None:

        # === Attributes ===

        self.__isChild = False
        self.__isClosed = False
        self.__icon = None
        self.__position = None
        self.__resizable = None
        self.__size = [800, 600]
        self.__state = State.NORMAL
        self.__title = "Window"
        self.__widgets = []

        self.OnConstruct()

        # Creates the window
        self.__id = tkinter.Tk()
        self.__screen = [self.__id.winfo_screenwidth(), self.__id.winfo_screenheight()]

        if (self.__position == None):
            self.__position = [int(self.__screen[0] / 2) - int(self.__size[0] / 2), int(self.__screen[1] / 2) - int(self.__size[1] / 2)]

        if (not self.__resizable):
            self.__id.resizable(width=self.__resizable, height=self.__resizable)

        # Set up the window
        self.__id.geometry(f"{self.__size[0]}x{self.__size[1]}+{int(self.__position[0])}+{int(self.__position[1])}")
        self.__id.iconbitmap(self.__icon)
        self.__id.state(self.__state)
        self.__id.title(self.__title)

        # === Binds ===

        self.__id.bind(Event.DESTROY, self.__procedure__)

    def __del__(self) -> None:
        self.OnDestruct()
        del self.__id

    # === MAIN methods ===
        
    def AddWidget(self, widget : Widget) -> None:
        """ Adds a widget to the window. """
        self.__widgets.append(widget)
        widget.SetRoot(self.__id)

    def AddWindow(self, window, destroy = False, independent = False) -> None:
        """ Adds a child window to the current window. """
        if (destroy):
            self.Close()

        else:
            if (not independent):
                window.__isChild = True

        window.SetIcon(self.GetIcon())
        window.Run()
        
    def Close(self) -> None:
        """ Closes the window. """
        self.__id.destroy()

    def Run(self) -> None:
        """ Runs the window. """
        self.OnStart()

        # Creates all the form's subojects
        for i in range(len(self.__widgets)):
            self.__widgets[i].Create()
        
        if (not self.__isChild):
            while (not self.__isClosed):
                # Update
                self.OnUpdate()
                self.__id.update()

                # Interval
                sleep(0.042) # 24 FPS

            self.OnEnd()

    # === GET methods ===
        
    def GetId(self) -> tkinter.Tk:
        """ Gets the window's id. """
        return self.__id
    
    def GetIcon(self) -> str:
        """ Gets the window's icon. """
        return self.__icon

    def GetTitle(self) -> str:
        """ Gets the window's title. """
        return self.__title

    def GetSize(self) -> list:
        """ Gets the window's size. """
        return self.__size

    def GetScreen(self) -> list:
        """ Gets the screen's size in pixels. """
        return self.__screen

    def GetState(self) -> str:
        """ Gets the window's state. """
        return self.__state

    def GetPosition(self) -> list:
        """ Gets the window's position in pixels. """
        return self.__position
    
    # === SET methods ===

    def SetIcon(self, icon : str):
        """ Sets the window's icon. """
        self.__icon = icon

    def SetPosition(self, width : int, height : int) -> None:
        """ Sets the window's position. """
        self.__position = [width, height]

    def SetResizable(self, resizable : bool):
        """ Sets the window's resizable. """
        self.__resizable = resizable

    def SetSize(self, width : int, height : int) -> None:
        self.__size = [width, height]

    def SetState(self, state : State):
        """ Sets the window's state. """
        self.__state = state

    def SetTitle(self, title : str) -> None:
        self.__title = title

    # === EVENT methods ===

    def OnConstruct(self) -> None:
        pass

    def OnDestruct(self) -> None:
        pass

    def OnDestroy(self) -> None:
        pass

    def OnEnd(self) -> None:
        pass

    def OnStart(self) -> None:
        pass

    def OnUpdate(self) -> None:
        pass

    # === CORE methods ===

    def __procedure__(self, event) -> None:
        self.__isClosed = True
        self.OnDestroy()


class Button(Widget):

    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===

        self._foregroundColour = Colour.WHITE
        self._backgroundColour = Colour.ROYAL

        self.__event = None
        self.__text = "Button"

    # === MAIN methods ===

    def Create(self) -> None:
        """ Creates the button. """
        self._id = tkinter.Button(master=self._root, text=self.__text, command=self.__event)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._foregroundColour, bg=self._backgroundColour, border=0)

        # Set button's focus
        if (self._focused):
            self._id.focus()

        # Set button's hover and leave effect
        self._id.bind(Event.ENTER, func=lambda e: self._id.config(cursor=Cursor.HAND))
        self._id.bind(Event.LEAVE, func=lambda e: self._id.config(cursor=Cursor.ARROW))

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
            
    # === SET methods ===

    def SetEvent(self, event) -> None:
        """ Sets the button's event. """
        self.__event = event

    def SetText(self, text: str) -> None:
        """ Sets the button's text. """
        self.__text = text

        if (self._id != None):
            self._id.config(text=self.__text)


class ComboBox(Widget):

    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===

        self.__content = ["Combo Box"]
        self.__readonly = "readonly"
        self._size = [12, 0]

    # === MAIN methods ===

    def Create(self) -> None:
        """ Creates the combo box. """
        self._id = ttk.Combobox(master=self._root, values=self.__content)
        self._id.config(width=self._size[0], height=self._size[1], state=self.__readonly)

        # Sets the first combo box's element as default value
        self._id.set(self.__content[0])

        # Set button's focus
        if (self._focused):
            self._id.focus()

        # Set button's hover and leave effect
        self._id.bind(Event.ENTER, func=lambda e: self._id.config(cursor=Cursor.HAND))
        self._id.bind(Event.LEAVE, func=lambda e: self._id.config(cursor=Cursor.ARROW))

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === GET methods ===

    def GetContent(self) -> str:
        """ Gets the combo box's content. """
        return self._id.get() if (self._id.get() != "Combo Box") else ""

    # === SET methods ===

    def SetContent(self, content : list) -> None:
        """ Sets the combo box's content. """
        self.__content = content

    def SetReadOnly(self, readonly : bool) -> None:
        """ Sets the combo box's state """
        self.__readonly = "readonly" if (readonly) else "normal"


class InputBox(Widget):

    def __init__(self) -> None:
        super().__init__()

    # === MAIN methods ===

    def Clear(self) -> None:
        """ Clears the input box's content. """
        self._id.delete(0, "end")

    # === GET methods ===

    def GetContent(self) -> str:
        """ Gets the input box's content. """
        return self._id.get() if (self._placeholderMode) else ""
    
    # === SET methods ===

    def SetContent(self, text : str) -> None:
        """ Sets the input box's content. """
        if (self._id != None):
            self._id.insert(0, text)


class Label(Widget):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===

        self.__text = "Label"
        self._size = [0, 0]
        self._backgroundColour = None

    # === MAIN methods ===

    def Create(self) -> None:
        """ Creates the label. """
        self._id = tkinter.Label(master=self._root, text=self.__text)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._foregroundColour, bg=self._backgroundColour)

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === GET methods ===

    def GetText(self) -> str:
        """ Sets the label's text. """
        return self.__text
    
    # === SET methods ===

    def SetText(self, text: str) -> None:
        """ Sets the label's text. """
        self.__text = text

        if (self._id != None):
            self._id.config(text=self.__text)


class RichTextBox(InputBox):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===

        self._size = [20, 10]

    # === MAIN methods ===

    def Create(self) -> None:
        """ Creates the rich text box. """
        self._id = tkinter.Text(master=self._root)
        self._id.config(width=self._size[0], height=self._size[1], border=0)

        # Set rich text box's focus
        if (self._focused):
            self._id.focus()

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])


class TextBox(InputBox):
    
    def __init__(self) -> None:
        super().__init__()

        # === Attributes ===

        self.__alignment = Align.LEFT
        self.__character = None
        self._placeholderMode = False
        self._placeholderText = None
        self._placeholderColor = None

    # === MAIN methods ===

    def _OnFocusIn(self, *args) -> None:
        """ Set-up the begin of the focus event. """
        if (self._id["fg"] == self._placeholderColor):
            self._placeholderMode = True
            self._id.delete(0, "end")
            self._id["fg"] = self._foregroundColour
            self._id.config(show=self.__character)

    def _OnFocusOut(self, *args) -> None:
        """ Set-up the end of the focus event. """
        if (not self._id.get()):
            self._placeholderMode = False
            self._id.insert(0, self._placeholderText)
            self._id["fg"] = self._placeholderColor
            self._id.config(show="")

    def Create(self) -> None:
        """ Creates the text box. """
        self._id = tkinter.Entry(master=self._root)
        self._id.config(justify=self.__alignment, width=self._size[0], fg=self._foregroundColour, bg=self._backgroundColour, border=0)

        # Set text box's placeholder
        if (self._placeholderText != None):
            self._id.bind(Event.FOCUS_IN, self._OnFocusIn)
            self._id.bind(Event.FOCUS_OUT, self._OnFocusOut)
            self._id.insert(0, self._placeholderText)
            self._id["fg"] = self._placeholderColor

        # Set text box's focus
        if (self._focused):
            self._id.focus()

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === SET methods ===

    def SetAlignment(self, align : Align) -> None:
        """ Sets the text box's alignment. """
        self.__alignment = align

    def SetPasswordCharacter(self, character) -> None:
        """ Sets the entry box's password character. """
        self.__character = character

    def SetPlaceholder(self, text : str, colour=Colour.GREY) -> None:
        """ Sets the input box's placeholder. """
        if (text != ""):
            self._placeholderText = text
            self._placeholderColor = colour
