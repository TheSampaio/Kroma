from interpork import *

class FormHome(Form):

    def __init__(self) -> None:
        self.Initialze()

        # Set-up form's window
        self.GetWindow().SetTitle("Home")

        # Creates the rich text box
        self.__Rxt_Text = self.CreateSubobject(RichTextBox())
        self.__Rxt_Text.SetAnchor(Anchor.CENTER)
        self.__Rxt_Text.SetFocus(True)
        self.__Rxt_Text.Create()

        # Creates window's buttons
        self.__CreateButton(Anchor.TOP, "Top")
        self.__CreateButton(Anchor.TOP_RIGHT, "Top Right")
        self.__CreateButton(Anchor.TOP_LEFT, "Top Left")
        self.__CreateButton(Anchor.BOTTOM, "Bottom")
        self.__CreateButton(Anchor.BOTTOM_RIGHT, "Bottom Right")
        self.__CreateButton(Anchor.BOTTOM_LEFT, "Bottom Left")
        self.__CreateButton(Anchor.RIGHT, "Right")
        self.__CreateButton(Anchor.LEFT, "Left")

    def __CreateButton(self, anchor: Anchor, text: str):
        Btn_Generic = self.CreateSubobject(Button())
        Btn_Generic.SetAnchor(anchor)
        Btn_Generic.SetText(text)
        Btn_Generic.Create()
