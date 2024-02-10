from kroma import Anchor, Button, Colour, MessageBox, State, Window

class FormHome(Window):

    def OnConstruct(self) -> None:
        self.SetIcon("Data\\Icon\\icon-kroma.ico")
        self.SetState(State.MAXIMIZED)
        self.SetTitle("Home")
    
    def OnStart(self) -> None:        
        # Upper
        self.__CreateButtons(Anchor.TOP_LEFT, "Top Left")
        self.__CreateButtons(Anchor.TOP, "Top")
        self.__CreateButtons(Anchor.TOP_RIGHT, "Top Right")

        # Middle
        self.__CreateButtons(Anchor.LEFT, "Left")
        self.__CreateButtons(Anchor.CENTER, "Center", True, self.__Greetings)
        self.__CreateButtons(Anchor.RIGHT, "Right")

        # Lower
        self.__CreateButtons(Anchor.BOTTOM_LEFT, "Bottom Left")
        self.__CreateButtons(Anchor.BOTTOM, "Bottom")
        self.__CreateButtons(Anchor.BOTTOM_RIGHT, "Bottom Right")

    def __CreateButtons(self, anchor : Anchor, name : str, focus = False, event = None) -> None:
        Btn_Generic = Button()
        Btn_Generic.SetAnchor(anchor)
        Btn_Generic.SetText(name)
        Btn_Generic.SetFocus(focus)
        Btn_Generic.SetEvent(event)
        self.AddWidget(Btn_Generic)

    def __Greetings(self):
        MessageBox.Show("Welcome to Kroma!")
