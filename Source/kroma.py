import tkinter
from tkinter import ttk
from tkinter import messagebox
from time import sleep


class Align:
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Anchor:
    CENTER = "center"
    TOP = "n"
    TOP_RIGHT = "ne"
    TOP_LEFT = "nw"
    BOTTOM = "s"
    BOTTOM_RIGHT = "se"
    BOTTOM_LEFT = "sw"
    RIGHT = "e"
    LEFT = "w"


class Color:
    AQUA = "#00FFFF"
    BLACK = "#000000"
    BLUE = "#0000FF"
    CYAN = "00FFFF"
    FUCHSIA = "#FF00FF"
    GREEN = "#008000"
    GRAY = "#808080"
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
    TRANSPARENT = None
    VIOLET = "#52057F"
    WHITE = "#FFFFFF"
    YELLOW = "#FFFF00"


class Cursor:
    ARROW = "arrow"
    HAND = "hand2"


class Event:
    DESTROY = "<Destroy>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class MessageBoxType:
    INFORMATION = 0
    WARNING = 1
    ERROR = 2
    QUESTION = 3


class MessageBox:
    @staticmethod
    def ShowInfo(message: str, title: str = "Information") -> None:
        messagebox.showinfo(title, message)

    @staticmethod
    def ShowWarning(message: str, title: str = "Warning") -> None:
        messagebox.showwarning(title, message)

    @staticmethod
    def ShowError(message: str, title: str = "Error") -> None:
        messagebox.showerror(title, message)

    @staticmethod
    def ShowQuestion(message: str, title: str = "Question") -> bool:
        return messagebox.askyesno(title, message)


class Screen:
    @staticmethod
    def GetResolution() -> tuple:
        """ Gets the user's screen resolution in pixels. """
        id = tkinter.Tk()
        resolution = (id.winfo_screenwidth(), id.winfo_screenheight())
        id.destroy()

        return resolution


class State:
    NORMAL = "normal"
    MINIMIZED = "iconic"
    MAXIMIZED = "zoomed"
    HIDDEN = "withdrawn"


class Widget:
    def __init__(self) -> None:
        self._id = None
        self._root = None
        self._foregroundColor = Color.BLACK
        self._backgroundColor = Color.WHITE
        self._enabled = True
        self._focused = False
        self._anchor = Anchor.TOP_LEFT
        self._padding = [0, 0]
        self._position = [0, 0]
        self._size = [12, 1]

    def GetId(self):
        return self._id

    def GetRoot(self) -> tkinter.Tk:
        return self._root

    def GetForeColour(self) -> str:
        return self._foregroundColor

    def GetBackgroundColour(self) -> str:
        return self._backgroundColor

    def GetFocus(self) -> bool:
        return self._focused

    def GetAnchor(self) -> str:
        return self._anchor

    def GetPosition(self) -> list:
        return self._position

    def GetSize(self) -> list:
        return self._size

    def SetRoot(self, root) -> None:
        self._root = root

    def SetForegroundColour(self, colour: str) -> None:
        self._foregroundColor = colour

    def SetBackgroundColour(self, backgroundColour: str) -> None:
        self._backgroundColor = backgroundColour

    def SetFocus(self, enable: bool) -> None:
        self._focused = enable

    def SetAnchor(self, anchor: Anchor) -> None:
        anchor_padding_map = {
            Anchor.CENTER: [0.5, 0.5],
            Anchor.TOP: [0.5, 0.0],
            Anchor.TOP_RIGHT: [1.0, 0.0],
            Anchor.TOP_LEFT: [0.0, 0.0],
            Anchor.BOTTOM: [0.5, 1.0],
            Anchor.BOTTOM_RIGHT: [1.0, 1.0],
            Anchor.BOTTOM_LEFT: [0.0, 1.0],
            Anchor.RIGHT: [1.0, 0.5],
            Anchor.LEFT: [0.0, 0.5],
        }
        self._anchor = anchor
        self._padding = anchor_padding_map.get(anchor, [0.5, 0.5])

    def SetPosition(self, x: int, y: int) -> None:
        self._position = [x, y]

    def SetSize(self, width: int, height: int) -> None:
        self._size = [width, height]


class Window:
    def __init__(self) -> None:
        self.__id = None
        self.__isChild = False
        self.__isClosed = False
        self.__icon = None
        self.__position = None
        self.__resizable = None
        self.__size = [800, 600]
        self.__state = State.NORMAL
        self.__title = "Window"
        self.__widgets = []

        self._OnConstruct()

        self.__id = tkinter.Tk()
        self.__screen = [self.__id.winfo_screenwidth(), self.__id.winfo_screenheight()]

        if self.__position is None:
            self.__position = [
                int(self.__screen[0] / 2) - int(self.__size[0] / 2),
                int(self.__screen[1] / 2) - int(self.__size[1] / 2),
            ]

        if not self.__resizable:
            self.__id.resizable(width=self.__resizable, height=self.__resizable)

        self.__id.geometry(
            f"{self.__size[0]}x{self.__size[1]}+{int(self.__position[0])}+{int(self.__position[1])}"
        )
        self.__id.iconbitmap(self.__icon)
        self.__id.state(self.__state)
        self.__id.title(self.__title)

        self.__id.bind(Event.DESTROY, self.__proc__)

    def __del__(self) -> None:
        self._OnDestruct()
        del self.__id

    def AddWidget(self, widget: Widget) -> None:
        self.__widgets.append(widget)
        widget.SetRoot(self.__id)

    def AddWindow(self, window, destroy=False, independent=False) -> None:
        if destroy:
            self.Close()
        else:
            if not independent:
                window.__isChild = True

        window.SetIcon(self.GetIcon())
        window.Run()

    def Close(self) -> None:
        self.__id.destroy()

    def Run(self) -> None:
        self._OnStart()

        for widget in self.__widgets:
            widget.Create()

        if not self.__isChild:
            while not self.__isClosed:
                self._OnUpdate()
                self.__id.update()
                sleep(0.05)

            self._OnEnd()

    def GetId(self) -> tkinter.Tk:
        return self.__id

    def GetIcon(self) -> str:
        return self.__icon

    def GetTitle(self) -> str:
        return self.__title

    def GetSize(self) -> list:
        return self.__size

    def GetScreen(self) -> list:
        return self.__screen

    def GetState(self) -> str:
        return self.__state

    def GetPosition(self) -> list:
        return self.__position

    def SetIcon(self, icon: str) -> None:
        self.__icon = icon

    def SetPosition(self, width: int, height: int) -> None:
        self.__position = [width, height]

    def SetResizable(self, resizable: bool) -> None:
        self.__resizable = resizable

    def SetSize(self, width: int, height: int) -> None:
        self.__size = [width, height]

    def SetState(self, state: State) -> None:
        self.__state = state

    def SetTitle(self, title: str) -> None:
        self.__title = title

    def _OnConstruct(self) -> None:
        pass

    def _OnDestruct(self) -> None:
        pass

    def _OnEnd(self) -> None:
        pass

    def _OnStart(self) -> None:
        pass

    def _OnUpdate(self) -> None:
        pass

    def __proc__(self, event) -> None:
        self.__isClosed = True


class Button(Widget):
    def __init__(self) -> None:
        super().__init__()
        self._foregroundColor = Color.WHITE
        self._backgroundColor = Color.ROYAL
        self.__event = None
        self.__text = "Button"

    def Create(self) -> None:
        self._id = ttk.Button(master=self._root, width=self._size[0], text=self.__text, command=self.__event)

        if self._focused:
            self._id.focus()

        self._id.bind(Event.ENTER, func=lambda e: self._id.config(cursor=Cursor.HAND))
        self._id.bind(Event.LEAVE, func=lambda e: self._id.config(cursor=Cursor.ARROW))

        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    def SetEvent(self, event: callable) -> None:
        self.__event = event

    def SetText(self, text: str) -> None:
        self.__text = text


class ComboBox(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.__values = []
        self.__selected_value = None

    def Create(self) -> None:
        self._id = ttk.Combobox(self._root, values=self.__values)
        self._id.set(self.__selected_value)
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    def SetValues(self, values: list) -> None:
        self.__values = values

    def SetSelectedValue(self, selected_value: str) -> None:
        self.__selected_value = selected_value

    def GetSelectedValue(self) -> str:
        return self._id.get()


class Label(Widget):
    def __init__(self) -> None:
        super().__init__()  # Call parent constructor
        self._foregroundColor = Color.BLACK
        self._backgroundColor = Color.TRANSPARENT
        self._size = [0, 1]
        self._text = "Label"

    def Create(self) -> bool:
        self._id = tkinter.Label(master=self._root, text=self._text)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._foregroundColor, bg=self._backgroundColor)

        # Set label's focus
        if self._focused:
            self._id.focus()

        # Place the widget on the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
        return self._id is not None

    def GetText(self) -> str:
        return self._text

    def SetText(self, text: str) -> None:
        """ Sets the label's text. """
        self._text = text

        if self._id is not None:
            self._id.config(text=self._text)


class TextBox(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.__placeholder = ""
        self.__value = ""

    def Create(self) -> None:
        self._id = ttk.Entry(self._root, width=self._size[0])

        self._id.insert(0, self.__placeholder)
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

        self._id.bind(Event.FOCUS_IN, self.__focusIn)
        self._id.bind(Event.FOCUS_OUT, self.__focusOut)

    def SetText(self, text: str) -> None:
        self.__value = text

    def SetPlaceholder(self, placeholder: str) -> None:
        self.__placeholder = placeholder

    def GetText(self) -> str:
        return self.__value

    def __focusIn(self, event: callable) -> None:
        if self._id.get() == self.__placeholder:
            self._id.delete(0, tkinter.END)

    def __focusOut(self, event: callable) -> None:
        if not self._id.get():
            self._id.insert(0, self.__placeholder)

