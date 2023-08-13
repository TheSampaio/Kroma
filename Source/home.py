from interpork import *

class FormHome(Form):

    def __init__(self) -> None:
        self._Initialze_()

        # Set-up form's window
        self.GetWindow().SetTitle("Home")

        # Creates the rich text box
        self.__Rxt_Text = self._CreateSubobject_(RichTextBox())
        self.__Rxt_Text.SetAnchor(Anchor.CENTER)
        self.__Rxt_Text.Create()

        # Creates window's buttons
        self.__CreteButton(Anchor.TOP, "Top")
        self.__CreteButton(Anchor.TOP_RIGHT, "Top Right")
        self.__CreteButton(Anchor.TOP_LEFT, "Top Left")
        self.__CreteButton(Anchor.BOTTOM, "Bottom")
        self.__CreteButton(Anchor.BOTTOM_RIGHT, "Bottom Right")
        self.__CreteButton(Anchor.BOTTOM_LEFT, "Bottom Left")
        self.__CreteButton(Anchor.RIGHT, "Right")
        self.__CreteButton(Anchor.LEFT, "Left")

    def __CreteButton(self, anchor: Anchor, text: str):
        Btn_Generic = self._CreateSubobject_(Button())
        Btn_Generic.SetAnchor(anchor)
        Btn_Generic.SetText(text)
        Btn_Generic.Create()
