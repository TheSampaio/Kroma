import tkinter
from tkinter import ttk
from time import sleep


class Align:
    
    # === Attributes ===
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Anchor:

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


class Colour:

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
    TRANSPARENT = None
    VIOLET = "#52057F"
    WHITE = "#FFFFFF"
    YELLOW = "#FFFF00"


class Cursor:

    # === Attributes ===
    ARROW = "arrow"
    HAND = "hand2"


class Event:

    # === Attributes ===
    DESTROY = "<Destroy>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class State:

    # === Attributes ===
    NORMAL = "normal"
    MINIMIZED = "iconic"
    MAXIMIZED = "zoomed"
    HIDDEN = "withdrawn"


class Screen:

    # === Main methods ===

    @staticmethod
    def GetResolution() -> tuple:
        """ Gets the user's screen resolution in pixels. """
        id = tkinter.Tk()
        resolution = (id.winfo_screenwidth(), id.winfo_screenheight())
        id.destroy()

        return resolution


class Primitive:

    def __init__(self) -> None:

        # === Attributes ===
        self._position = None
        self._size = [0, 0]

    # === Get methods ===

    def GetPosition(self) -> list:
        return self._position if self._position != None else [0, 0]

    def GetSize(self) -> list:
        return self._size

    # === Set methods ===

    def SetPosition(self, x: int, y: int) -> None:
        self._position = [int(x), int(y)]

    def SetSize(self, width: int, height: int) -> None:
        self._size = [int(width), int(height)]


class Actor(Primitive):

    def __init__(self) -> None:
        super().__init__()

        self._id = None

    # === Main methods ===

    def _Create(self) -> bool:
        return False


class Control:

    def __init__(self) -> None:
        super().__init__()

        # === Attributes === #
        self._position = [0, 0]

        self._anchor = Anchor.TOP_LEFT
        self._isFocused = False
        self._padding = [0, 0]
        self._root = None

    # === Get methods === #

    def GetAnchor(self) -> str:
        return self._anchor
    
    def GetFocus(self) -> bool:
        return self._isFocused

    # === Set methods === #

    def SetAnchor(self, anchor) -> None:
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
    
    def SetFocus(self, focus: bool) -> None:
        """ Focus the widget. """
        self._isFocused = focus


class Window(Actor, Primitive):

    def __init__(self) -> None:
        Actor.__init__(self)
        Primitive.__init__(self)

        # === Attributes ===
        self._size = [800, 600]

        self.__isClosed = False
        self.__title = "Window"
        self.__controls = []

        self.OnConstruct()
        self._Create()
        self._id.bind(Event.DESTROY, self.__proc__)

    def __del__(self) -> None:
        self.OnDestruct()
        del self._id

    def __proc__(self, event) -> None:
        self.__isClosed = True

    # === Main methods ===

    def AddControl(self, control : Control) -> None:
        """ Adds a widget to the window. """
        self.__controls.append(control)
        control._root = self._id

    def Run(self) -> None:
        """ Runs the window. """
        self.OnStart()

        # Creates all the form's subojects
        for i in range(len(self.__controls)):
            self.__controls[i]._Create()

        while not self.__isClosed:
            self.OnUpdate()
            self._id.update()
            
            # Interval
            sleep(0.05) # ~24 FPS

        self.OnEnd()

    def _Create(self) -> bool:
        self._id = tkinter.Tk()
        self._id.title(self.__title)

        # Setup position and size
        if self._position != None:
            self._id.geometry(f"{self._size[0]}x{self._size[1]}+{self._position[0]}+{self._position[1]}")

        else:
            self._id.geometry(f"{self._size[0]}x{self._size[1]}")

        return True if self._id != None else False

    # === Get methods ===

    def GetTitle(self) -> str:
        return self.__title

    # === Set methods ===

    def SetTitle(self, title: str) -> None:
        self.__title = title

    # === Event methods ===

    def OnConstruct(self) -> None:
        pass

    def OnDestruct(self) -> None:
        pass

    def OnEnd(self) -> None:
        pass

    def OnStart(self) -> None:
        pass

    def OnUpdate(self) -> None:
        pass


class Label(Actor, Control):

    def __init__(self) -> None:
        Actor.__init__(self)
        Control.__init__(self)

        # === Attributes === #
        self._colour = [Colour.BLACK, Colour.TRANSPARENT]
        self._text = "Label"

    # === Main methods === #

    def _Create(self) -> bool:
        """ Creates the label. """
        self._id = tkinter.Label(master=self._root, text=self._text)
        self._id.config(width=self._size[0], height=self._size[1], fg=self._colour[0], bg=self._colour[1])

        # Set label's focus
        if self._isFocused:
            self._id.focus()

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
        return True if self._id != None else False

    # === Get methods === #

    def GetColour(self) -> list:
        return self._colour

    def GetText(self) -> str:
        return self._text

    # === Set methods === #

    def SetColour(self, foreground: str, background: str = None) -> None:
            self._colour = [foreground, background if background != None else Colour.TRANSPARENT]

    def SetText(self, text: str) -> None:
        """ Sets the label's text. """
        self._text = text

        if self._id != None:
            self._id.config(text=self._text)


class Button(Label):

    def __init__(self) -> None:
        super().__init__()

        self._size = [12, 0]

        # === Attributes === #
        self._text = "Button"
        self.__event = None

    # === Main methods === #

    def _Create(self) -> bool:
        """ Creates the button. """
        self._id = ttk.Button(master=self._root, width=self._size[0], text=self._text, command=self.__event)

        # Set button's focus
        if self._isFocused:
            self._id.focus()

        # Set button's hover and leave effect
        self._id.bind(Event.ENTER, func=lambda e: self._id.config(cursor=Cursor.HAND))
        self._id.bind(Event.LEAVE, func=lambda e: self._id.config(cursor=Cursor.ARROW))

        # Place the widget in the screen
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    # === Set methods === #

    def SetEvent(self, event) -> None:
        """ Sets the button's event. """
        self.__event = event
