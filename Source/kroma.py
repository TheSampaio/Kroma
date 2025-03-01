import tkinter
from tkinter import ttk
from tkinter import messagebox
from time import sleep


class Align:
    """Defines horizontal text alignment options."""

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class Anchor:
    """Defines anchor points for positioning elements."""

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
    """Defines common colors using hexadecimal values."""

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
    """Defines cursor styles."""

    ARROW = "arrow"
    HAND = "hand2"


class Event:
    """Defines common UI event types."""

    DESTROY = "<Destroy>"
    ENTER = "<Enter>"
    LEAVE = "<Leave>"
    FOCUS_IN = "<FocusIn>"
    FOCUS_OUT = "<FocusOut>"


class MessageBox:
    """Provides static methods for displaying message boxes."""

    @staticmethod
    def ShowInfo(message: str, title: str = "Information") -> None:
        """Displays an informational message box."""
        messagebox.showinfo(title, message)

    @staticmethod
    def ShowWarning(message: str, title: str = "Warning") -> None:
        """Displays a warning message box."""
        messagebox.showwarning(title, message)

    @staticmethod
    def ShowError(message: str, title: str = "Error") -> None:
        """Displays an error message box."""
        messagebox.showerror(title, message)

    @staticmethod
    def ShowQuestion(message: str, title: str = "Question") -> bool:
        return messagebox.askyesno(title, message)


class Screen:
    """Provides methods for retrieving screen-related information."""

    @staticmethod
    def GetResolution() -> tuple:
        """ Gets the user's screen resolution in pixels. """
        id = tkinter.Tk()
        resolution = (id.winfo_screenwidth(), id.winfo_screenheight())
        id.destroy()

        return resolution


class State:
    """Defines window state options."""

    NORMAL = "normal"     # Window is in its normal state.
    MINIMIZED = "iconic"  # Window is minimized.
    MAXIMIZED = "zoomed"  # Window is maximized.
    HIDDEN = "withdrawn"  # Window is hidden from view.


class Widget:
    """Represents a basic UI widget with customizable properties."""

    def __init__(self) -> None:
        """Initializes the widget with default properties."""
        self._id = None                      # Unique identifier for the widget.
        self._root = None                    # Reference to the root Tkinter window.
        self._enabled = True                 # Determines if the widget is enabled.
        self._focused = False                # Indicates if the widget is currently focused.
        self._anchor = Anchor.TOP_LEFT       # Anchor position for alignment.
        self._padding = [0, 0]               # Padding values for layout.
        self._position = [0, 0]              # X and Y position of the widget.
        self._size = [12, 1]                 # Width and height of the widget.

    def GetId(self):
        """Returns the unique ID of the widget."""
        return self._id

    def GetRoot(self) -> tkinter.Tk:
        """Returns the root Tkinter window associated with the widget."""
        return self._root

    def GetFocus(self) -> bool:
        """Returns whether the widget is currently focused."""
        return self._focused

    def GetAnchor(self) -> str:
        """Returns the anchor position of the widget."""
        return self._anchor

    def GetPosition(self) -> list:
        """Returns the position of the widget as [x, y]."""
        return self._position

    def GetSize(self) -> list:
        """Returns the size of the widget as [width, height]."""
        return self._size

    def SetRoot(self, root) -> None:
        """Sets the root Tkinter window for the widget."""
        self._root = root

    def SetFocus(self, enable: bool) -> None:
        """Sets the focus state of the widget."""
        self._focused = enable

    def SetAnchor(self, anchor: Anchor) -> None:
        """
        Sets the anchor position of the widget and updates its padding.

        Args:
            anchor (Anchor): The anchor position to be set.
        """
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
        """
        Sets the position of the widget.

        Args:
            x (int): The X-coordinate of the widget.
            y (int): The Y-coordinate of the widget.
        """
        self._position = [x, y]

    def SetSize(self, width: int, height: int) -> None:
        """
        Sets the size of the widget.

        Args:
            width (int): The width of the widget.
            height (int): The height of the widget.
        """
        self._size = [width, height]


class Window:
    """Represents a window in a GUI application."""

    def __init__(self) -> None:
        """Initializes the window with default properties and creates a Tkinter window."""
        self.__id = None             # Reference to the Tkinter window instance
        self.__isChild = False       # Indicates if the window is a child window
        self.__isClosed = False      # Tracks whether the window is closed
        self.__icon = None           # Window icon file path
        self.__position = None       # Window position on the screen
        self.__resizable = None      # Determines if the window is resizable
        self.__size = [800, 600]     # Default window size (width, height)
        self.__state = State.NORMAL  # Initial window state (e.g., normal, maximized)
        self.__title = "Window"      # Default window title
        self.__widgets = []          # List of widgets added to the window

        self._OnConstruct()

        # Create the main Tkinter window
        self.__id = tkinter.Tk()
        self.__screen = [self.__id.winfo_screenwidth(), self.__id.winfo_screenheight()]

        # Center the window on the screen if no position is set
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
        """Handles window destruction."""
        self._OnDestruct()
        del self.__id

    def AddWidget(self, widget: Widget) -> None:
        """
        Adds a widget to the window.

        Args:
            widget (Widget): The widget to add.
        """
        self.__widgets.append(widget)
        widget.SetRoot(self.__id)

    def AddWindow(self, window, destroy=False, independent=False) -> None:
        """
        Adds another window.

        Args:
            window (Window): The window to add.
            destroy (bool): Whether to close the current window before opening the new one.
            independent (bool): If False, the new window is considered a child of this one.
        """
        if destroy:
            self.Close()
        else:
            if not independent:
                window.__isChild = True

        window.SetIcon(self.GetIcon())
        window.Run()

    def Close(self) -> None:
        """Closes the window."""
        self.__id.destroy()

    def Run(self) -> None:
        """Runs the window's event loop and updates widgets."""
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
        """Returns the Tkinter window instance."""
        return self.__id

    def GetIcon(self) -> str:
        """Returns the window's icon file path."""
        return self.__icon

    def GetTitle(self) -> str:
        """Returns the window's title."""
        return self.__title

    def GetSize(self) -> list:
        """Returns the window size as [width, height]."""
        return self.__size

    def GetScreen(self) -> list:
        """Returns the screen resolution as [width, height]."""
        return self.__screen

    def GetState(self) -> str:
        """Returns the window's current state."""
        return self.__state

    def GetPosition(self) -> list:
        """Returns the window's position as [x, y]."""
        return self.__position

    def SetIcon(self, icon: str) -> None:
        """
        Sets the window icon.

        Args:
            icon (str): The file path of the icon.
        """
        self.__icon = icon

    def SetPosition(self, x: int, y: int) -> None:
        """
        Sets the window's position.

        Args:
            x (int): The X-coordinate of the window.
            y (int): The Y-coordinate of the window.
        """
        self.__position = [x, y]

    def SetResizable(self, resizable: bool) -> None:
        """
        Sets whether the window is resizable.

        Args:
            resizable (bool): True to allow resizing, False otherwise.
        """
        self.__resizable = resizable

    def SetSize(self, width: int, height: int) -> None:
        """
        Sets the window's size.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """
        self.__size = [width, height]

    def SetState(self, state: State) -> None:
        """
        Sets the window's state.

        Args:
            state (State): The new state (e.g., normal, maximized).
        """
        self.__state = state

    def SetTitle(self, title: str) -> None:
        """
        Sets the window's title.

        Args:
            title (str): The title of the window.
        """
        self.__title = title

    def _OnConstruct(self) -> None:
        """Called when the window is constructed. Can be overridden."""
        pass

    def _OnDestruct(self) -> None:
        """Called when the window is destroyed. Can be overridden."""
        pass

    def _OnEnd(self) -> None:
        """Called when the window closes. Can be overridden."""
        pass

    def _OnStart(self) -> None:
        """Called when the window starts running. Can be overridden."""
        pass

    def _OnUpdate(self) -> None:
        """Called during the window's update loop. Can be overridden."""
        pass

    def __proc__(self, event) -> None:
        """Handles the window's close event."""
        self.__isClosed = True


class Button(Widget):
    """
    A Button widget that extends the base Widget class.
    Allows setting text, events, and handling cursor interactions.
    """
    def __init__(self) -> None:
        """Initializes the button with default colors, text, and no event handler."""
        super().__init__()
        self.__event = None
        self.__text = "Button"


    def Create(self) -> None:
        """
        Creates a button widget and places it on the screen.
        Binds hover events to change the cursor style.
        """
        self._id = ttk.Button(master=self._root, width=self._size[0], text=self.__text, command=self.__event)

        if self._focused:
            self._id.focus()

        self._id.bind(Event.ENTER, func=lambda e: self._id.config(cursor=Cursor.HAND))
        self._id.bind(Event.LEAVE, func=lambda e: self._id.config(cursor=Cursor.ARROW))

        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    def SetEvent(self, event: callable) -> None:
        """Sets the event handler function for the button click event."""
        self.__event = event

    def SetText(self, text: str) -> None:
        """Sets the button's displayed text."""
        self.__text = text


class ComboBox(Widget):
    """
    A ComboBox widget that allows users to select an option from a dropdown list.
    """
    def __init__(self) -> None:
        """
        Initializes a ComboBox widget with an empty list of values and no selected value.
        """
        super().__init__()
        self.__values = []
        self.__selected_value = None

    def Create(self) -> None:
        """
        Creates the ComboBox widget and places it within the parent container.
        """
        self._id = ttk.Combobox(self._root, values=self.__values)
        self._id.set(self.__selected_value)
        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

    def SetValues(self, values: list) -> None:
        """
        Sets the list of values that the ComboBox can display.
        
        :param values: List of selectable values.
        """
        self.__values = values

    def SetSelectedValue(self, selected_value: str) -> None:
        """
        Sets the default selected value for the ComboBox.
        
        :param selected_value: The value to be selected by default.
        """
        self.__selected_value = selected_value

    def GetSelectedValue(self) -> str:
        """
        Retrieves the currently selected value from the ComboBox.
        
        :return: The selected value as a string.
        """
        return self._id.get()


class Label(Widget):
    """
    A Label widget for displaying text within the user interface.
    """
    def __init__(self) -> None:
        """
        Initializes a Label widget with default text, colors, and size.
        """
        super().__init__()
        self._size = [0, 1]
        self._text = "Label"
        self.__foregroundColor = Color.BLACK
        self.__backgroundColor = Color.TRANSPARENT

    def Create(self) -> bool:
        """
        Creates the Label widget and places it within the parent container.
        
        :return: True if the label is successfully created, otherwise False.
        """
        self._id = tkinter.Label(master=self._root, text=self._text)
        self._id.config(width=self._size[0], height=self._size[1], fg=self.__foregroundColor, bg=self.__backgroundColor)

        if self._focused:
            self._id.focus()

        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])
        return self._id is not None

    def GetBackgroundColor(self) -> str:
        """Returns the background color of the Label."""
        return self.__backgroundColor
    
    def GetForegroundColor(self) -> str:
        """Returns the foreground (text) color of the Label."""
        return self.__foregroundColor

    def GetText(self) -> str:
        """
        Retrieves the text displayed on the Label.
        
        :return: The current text of the Label.
        """
        return self._text

    def SetBackgroundColor(self, backgroundColor: str) -> None:
        """Sets the background color of the Label."""
        self.__backgroundColor = backgroundColor

    def SetForegroundColor(self, color: str) -> None:
        """Sets the foreground (text) color of the Label."""
        self.__foregroundColor = color

    def SetText(self, text: str) -> None:
        """
        Sets the label's text and updates it if the widget is already created.
        
        :param text: The new text to display on the Label.
        """
        self._text = text
        if self._id is not None:
            self._id.config(text=self._text)


class TextBox(Widget):
    """
    A TextBox widget that allows users to input and edit text.
    """
    def __init__(self) -> None:
        """
        Initializes a TextBox widget with a placeholder and an empty value.
        """
        super().__init__()
        self.__alignment = Align.LEFT
        self.__foregroundColor = Color.BLACK
        self.__character = None
        self.__placeholderChar = ""
        self.__placeholderColor = Color.GRAY

    def Create(self) -> None:
        """
        Creates the TextBox widget and places it within the parent container.
        """
        self._id = ttk.Entry(self._root, width=self._size[0], justify=self.__alignment)

        if (self.__placeholderChar != ""):
            self._id.insert(0, self.__placeholderChar)
            self._id.config(foreground=self.__placeholderColor)

        self._id.place(anchor=self._anchor, x=self._position[0], y=self._position[1], relx=self._padding[0], rely=self._padding[1])

        self._id.bind(Event.FOCUS_IN, self.__focusIn)
        self._id.bind(Event.FOCUS_OUT, self.__focusOut)

    def GetText(self) -> str:
        """
        Retrieves the current text input from the TextBox.
        
        :return: The text currently entered in the TextBox.
        """
        if (self._id.get() == self.__placeholderChar):
            return ""

        return self._id.get()
    
    def SetAlignment(self, align : Align) -> None:
        """ Sets the text box's alignment. """
        self.__alignment = align

    def SetText(self, text: str) -> None:
        """
        Sets the text value of the TextBox.
        
        :param text: The text to be displayed in the TextBox.
        """
        self.__value = text

    def SetPasswordCharacter(self, character) -> None:
        """ Sets the entry box's password character. """
        self.__character = character

    def SetPlaceholder(self, placeholder: str) -> None:
        """
        Sets the placeholder text for the TextBox.
        
        :param placeholder: The placeholder text.
        """
        self.__placeholderChar = placeholder
    
    def Clear(self) -> None:
        """ Clears the text box's content. """
        self._id.delete(0, "end")

    def __focusIn(self, event: callable) -> None:
        """
        Event handler for when the TextBox gains focus.
        Clears the placeholder text if it is still present.
        """
        if self._id.get() == self.__placeholderChar:
            self._id.delete(0, tkinter.END)
            self._id.config(show=self.__character, foreground=self.__foregroundColor)

    def __focusOut(self, event: callable) -> None:
        """
        Event handler for when the TextBox loses focus.
        Restores the placeholder text if the TextBox is empty.
        """
        if not self._id.get():
            self._id.config(show="", foreground=self.__placeholderColor)
            self._id.insert(0, self.__placeholderChar)

