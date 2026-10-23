# Historical API inventory

Local references inspected: `origin/1.0` (228ec9e), `origin/2.0` (0e22748),
`origin/3.0` (540b062), `origin/main` (c9b22cd). Annotated local tags
`v1.0`, `v2.0`, `v3.0` preserve the first three states as historical snapshots;
the tags do not assert release quality. No remote references were deleted.

| Capability | 1.0 | 2.0 | 3.0 | main |
| --- | --- | --- | --- | --- |
| Window, Widget, Button, ComboBox, Label, TextBox | yes | yes | yes | yes |
| RichTextBox | yes | no | no | yes |
| InputBox base | yes | no | no | no |
| Screen utility | no | yes | yes | yes |
| Color naming | Colour | Color | Color | Color |
| Method style | PascalCase | PascalCase | snake_case | PascalCase |
| Interactive Tk examples | no | no | no | yes |

The `main` implementation is the compatibility base because its README and
examples use that API, and it restores multiline text. A future snake_case
facade should be additive and tested before removing PascalCase names. The
`AddWindow` behavior changed between branches, so its lifecycle needs focused
tests. The `Test/` directory contains interactive examples, not automated
tests. The package requires only Python's tkinter/ttk at runtime; Linux Python
distributions may package Tcl/Tk separately.
