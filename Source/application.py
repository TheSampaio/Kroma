from kroma import *

class Application(Window):
    
    def OnConstruct(self) -> None:
        self.SetSize(400, 300)
        self.SetPosition(
            (Screen.GetResolution()[0] / 2) - (self.GetSize()[0] / 2),
            (Screen.GetResolution()[1] / 2) - (self.GetSize()[1] / 2)
        )
        
        self.SetTitle("Control Panel")

    def OnStart(self) -> None:
        self.__lblFooter = Label()
        self.__lblFooter.SetAnchor(Anchor.BOTTOM_RIGHT)
        self.__lblFooter.SetFocus(True)
        self.__lblFooter.SetText("Powered By Kroma - Copyright © 2023-2024")
        self.__lblFooter.SetColour(Colour.GREY, Colour.TRANSPARENT)
        self.AddControl(self.__lblFooter)
