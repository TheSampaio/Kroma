"""Tests that do not require a display server."""

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "Source" / "kroma.py"
SPEC = importlib.util.spec_from_file_location("kroma_under_test", MODULE_PATH)
kroma = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kroma)


class WindowLifecycleTests(unittest.TestCase):
    def test_close_stops_loop_and_destroys_once(self):
        root = MagicMock()
        root.winfo_screenwidth.return_value = 1280
        root.winfo_screenheight.return_value = 720
        with patch.object(kroma.tkinter, "Tk", return_value=root):
            window = kroma.Window()
        root.iconbitmap.assert_not_called()
        window.Close()
        window.Close()
        root.destroy.assert_called_once()
        root.update.assert_not_called()

    def test_child_destroy_does_not_close_root(self):
        root = MagicMock()
        root.winfo_screenwidth.return_value = 1280
        root.winfo_screenheight.return_value = 720
        with patch.object(kroma.tkinter, "Tk", return_value=root):
            window = kroma.Window()
        child_event = MagicMock(widget=object())
        window.__proc__(child_event)
        window.Close()
        root.destroy.assert_called_once()

    def test_public_widgets_remain_available(self):
        for name in ("Button", "ComboBox", "Label", "TextBox", "RichTextBox"):
            self.assertTrue(hasattr(kroma, name), name)

    def test_textbox_applies_text_and_mask_on_creation(self):
        entry = MagicMock()
        with patch.object(kroma.ttk, "Entry", return_value=entry):
            widget = kroma.TextBox()
            widget.SetText("sample")
            widget.SetPasswordCharacter("*")
            widget.Create()
        entry.insert.assert_called_with(0, "sample")
        entry.configure.assert_called_with(show="*")

    def test_combobox_omits_unset_selection(self):
        combo = MagicMock()
        with patch.object(kroma.ttk, "Combobox", return_value=combo):
            widget = kroma.ComboBox()
            widget.Create()
        combo.set.assert_not_called()

    def test_snake_case_aliases_preserve_existing_calls(self):
        button = kroma.Button()
        button.set_text("Apply")
        self.assertIs(kroma.Window.run, kroma.Window.Run)
        self.assertIs(kroma.TextBox.get_text, kroma.TextBox.GetText)
        self.assertTrue(callable(kroma.MessageBox.show_info))


if __name__ == "__main__":
    unittest.main()
