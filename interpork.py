from tkinter import Tk

class Window:

    def __init__(self) -> None:
        
        # Attributes
        self.__screen = [self.__id.winfo_screenwidth(), self.__id.winfo_screenheight()]
        self.__id = Tk()
        self.__title = "Window"
        self.__size = [800, 600]
        self.__position = [(self.__screen[0] / 2) - (self.__size[0] / 2), (self.__screen[1] / 2) - (self.__size[1] / 2)]

    def GetScreen(self):
        """ Gets the screen's size in pixels """
        return self.__screen

    def GetId(self):
        """ Gets the window's id """
        return self.__id

    def GetTitle(self):
        """ Gets the window's title """
        return self.__title

    def GetSize(self):
        """ Gets the window's size """
        return self.__size

    def Run(self):
        """ Creates and runs the window """
        self.__id.title(self.__title)
        self.__id.geometry(f"{self.__size[0]}x{self.__size[1]}+{int(self.__position[0])}+{int(self.__position[1])}")
        
        # Runs the window
        self.__id.mainloop()
