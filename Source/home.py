from kroma import Anchor, Button, MessageBox, RichTextBox, State, Window

class FormHome(Window):

    def OnConstruct(self) -> None:
        self.SetIcon("Data\\Icon\\icon-kroma.ico")
        self.SetState(State.MAXIMIZED)
        self.SetTitle("Home")
    
    def OnStart(self) -> None:        
        # Upper
        self.__CreateButtons(Anchor.TOP_LEFT, "Top Left", self.__Greetings)
        self.__CreateButtons(Anchor.TOP, "Top", self.__Greetings)
        self.__CreateButtons(Anchor.TOP_RIGHT, "Top Right", self.__Greetings)

        # Middle
        self.__CreateButtons(Anchor.LEFT, "Left", self.__Greetings)

        self.__Rtb_Master = RichTextBox()
        self.__Rtb_Master.SetAnchor(Anchor.CENTER)
        self.__Rtb_Master.SetFocus(True)
        self.__Rtb_Master.SetSize(40, 20)
        self.AddWidget(self.__Rtb_Master)

        self.__CreateButtons(Anchor.RIGHT, "Right", self.__Greetings)

        # Lower
        self.__CreateButtons(Anchor.BOTTOM_LEFT, "Bottom Left", self.__Greetings)
        self.__CreateButtons(Anchor.BOTTOM, "Bottom", self.__Greetings)
        self.__CreateButtons(Anchor.BOTTOM_RIGHT, "Bottom Right", self.__Greetings)

    def __CreateButtons(self, anchor : Anchor, name : str, event = None) -> None:
        Btn_Generic = Button()
        Btn_Generic.SetAnchor(anchor)
        Btn_Generic.SetText(name)
        Btn_Generic.SetEvent(event)
        self.AddWidget(Btn_Generic)

    def __Greetings(self):
        MessageBox.Show("Welcome to Kroma!")
