from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.camera
import open3d.geometry
import open3d.t.geometry
import open3d.visualization.gui
import open3d.visualization.rendering
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = [
    "A",
    "ALT",
    "AMPERSAND",
    "ASTERISK",
    "AT",
    "Application",
    "B",
    "BACKSLASH",
    "BACKSPACE",
    "BACKTICK",
    "BUTTON4",
    "BUTTON5",
    "Button",
    "C",
    "CAPS_LOCK",
    "CARET",
    "COLON",
    "COMMA",
    "CTRL",
    "CheckableTextTreeCell",
    "Checkbox",
    "CollapsableVert",
    "Color",
    "ColorEdit",
    "ColormapTreeCell",
    "Combobox",
    "D",
    "DELETE",
    "DOLLAR_SIGN",
    "DOUBLE_QUOTE",
    "DOWN",
    "Dialog",
    "E",
    "EIGHT",
    "END",
    "ENTER",
    "EQUALS",
    "ESCAPE",
    "EXCLAMATION_MARK",
    "F",
    "F1",
    "F10",
    "F11",
    "F12",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "FIVE",
    "FOUR",
    "FileDialog",
    "FontDescription",
    "FontStyle",
    "G",
    "GREATER_THAN",
    "H",
    "HASH",
    "HOME",
    "Horiz",
    "I",
    "INSERT",
    "ImageWidget",
    "J",
    "K",
    "KeyEvent",
    "KeyModifier",
    "KeyName",
    "L",
    "LEFT",
    "LEFT_BRACE",
    "LEFT_BRACKET",
    "LEFT_CONTROL",
    "LEFT_PAREN",
    "LEFT_SHIFT",
    "LESS_THAN",
    "LUTTreeCell",
    "Label",
    "Label3D",
    "Layout1D",
    "LayoutContext",
    "ListView",
    "M",
    "META",
    "MIDDLE",
    "MINUS",
    "Margins",
    "Menu",
    "MouseButton",
    "MouseEvent",
    "N",
    "NINE",
    "NONE",
    "NumberEdit",
    "O",
    "ONE",
    "P",
    "PAGE_DOWN",
    "PAGE_UP",
    "PERCENT",
    "PERIOD",
    "PIPE",
    "PLUS",
    "ProgressBar",
    "Q",
    "QUESTION_MARK",
    "QUOTE",
    "R",
    "RIGHT",
    "RIGHT_BRACE",
    "RIGHT_BRACKET",
    "RIGHT_CONTROL",
    "RIGHT_PAREN",
    "RIGHT_SHIFT",
    "RadioButton",
    "Rect",
    "S",
    "SEMICOLON",
    "SEVEN",
    "SHIFT",
    "SIX",
    "SLASH",
    "SPACE",
    "SceneWidget",
    "ScrollableVert",
    "Size",
    "Slider",
    "StackedWidget",
    "T",
    "TAB",
    "THREE",
    "TILDE",
    "TWO",
    "TabControl",
    "TextEdit",
    "Theme",
    "ToggleSwitch",
    "TreeView",
    "U",
    "UIImage",
    "UNDERSCORE",
    "UNKNOWN",
    "UP",
    "V",
    "VGrid",
    "VectorEdit",
    "Vert",
    "W",
    "Widget",
    "WidgetProxy",
    "WidgetStack",
    "Window",
    "WindowBase",
    "X",
    "Y",
    "Z",
    "ZERO",
]

class Application:
    """
    Global application singleton. This owns the menubar, windows, and event loop
    """

    def __repr__(self) -> str: ...
    def add_font(self, arg0: FontDescription) -> int:
        """
        Adds a font. Must be called after initialize() and before a window is created. Returns the font id, which can be used to change the font in widgets such as Label which support custom fonts.
        """
    def add_window(self, arg0: open3d.visualization.gui.Window) -> None:
        """
        Adds a window to the application. This is only necessary when creating an object that is a Window directly, rather than with create_window
        """
    def create_window(
        self,
        title: str = "",
        width: int = -1,
        height: int = -1,
        x: int = -1,
        y: int = -1,
        flags: int = 0,
    ) -> open3d.visualization.gui.Window:
        """
        Creates a window and adds it to the application. To programmatically destroy the window do window.close().Usage: create_window(title, width, height, x, y, flags). x, y, and flags are optional.
        """
    @typing.overload
    def initialize(self) -> None:
        """
        Initializes the application, using the resources included in the wheel. One of the `initialize` functions _must_ be called prior to using anything in the gui module

        Initializes the application with location of the resources provided by the caller. One of the `initialize` functions _must_ be called prior to using anything in the gui module
        """
    @typing.overload
    def initialize(self, arg0: str) -> None: ...
    def post_to_main_thread(
        self, arg0: open3d.visualization.gui.Window, arg1: typing.Callable[[], None]
    ) -> None:
        """
        Runs the provided function on the main thread. This can be used to execute UI-related code at a safe point in time. If the UI changes, you will need to manually request a redraw of the window with w.post_redraw()
        """
    def quit(self) -> None:
        """
        Closes all the windows, exiting as a result
        """
    def render_to_image(
        self, arg0: open3d.visualization.rendering.Open3DScene, arg1: int, arg2: int
    ) -> open3d.geometry.Image:
        """
        Renders a scene to an image and returns the image. If you are rendering without a visible window you should use open3d.visualization.rendering.RenderToImage instead
        """
    def run(self) -> None:
        """
        Runs the event loop. After this finishes, all windows and widgets should be considered uninitialized, even if they are still held by Python variables. Using them is unsafe, even if run() is called again.
        """
    def run_in_thread(self, arg0: typing.Callable[[], None]) -> None:
        """
        Runs function in a separate thread. Do not call GUI functions on this thread, call post_to_main_thread() if this thread needs to change the GUI.
        """
    def run_one_tick(self) -> bool:
        """
        Runs the event loop once, returns True if the app is still running, or False if all the windows have closed or quit() has been called.
        """
    def set_font(self, arg0: int, arg1: FontDescription) -> None:
        """
        Changes the contents of an existing font, for instance, the default font.
        """
    @property
    def menubar(self) -> open3d.visualization.gui.Menu:
        """
        The Menu for the application (initially None)

        :type: open3d.visualization.gui.Menu
        """
    @menubar.setter
    def menubar(self, arg1: open3d.visualization.gui.Menu) -> None:
        """
        The Menu for the application (initially None)
        """
    @property
    def now(self) -> float:
        """
        Returns current time in seconds

        :type: float
        """
    @property
    def resource_path(self) -> str:
        """
        Returns a string with the path to the resources directory

        :type: str
        """
    DEFAULT_FONT_ID = 0
    instance: open3d.visualization.gui.Application  # value = Application singleton instance
    pass

class Widget:
    """
    Base widget class
    """

    class Constraints:
        """
        Constraints object for Widget.calc_preferred_size()
        """

        def __init__(self) -> None: ...
        @property
        def height(self) -> int:
            """
            :type: int
            """
        @height.setter
        def height(self, arg0: int) -> None:
            pass
        @property
        def width(self) -> int:
            """
            :type: int
            """
        @width.setter
        def width(self, arg0: int) -> None:
            pass
        pass

    class EventCallbackResult:
        """
        Returned by event handlers

        Members:

          IGNORED : Event handler ignored the event, widget will handle event normally

          HANDLED : Event handler handled the event, but widget will still handle the event normally. This is useful when you are augmenting base functionality

          CONSUMED : Event handler consumed the event, event handling stops, widget will not handle the event. This is useful when you are replacing functionality
        """

        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        CONSUMED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.CONSUMED: 2>
        HANDLED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.HANDLED: 1>
        IGNORED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.IGNORED: 0>
        __members__: dict  # value = {'IGNORED': <EventCallbackResult.IGNORED: 0>, 'HANDLED': <EventCallbackResult.HANDLED: 1>, 'CONSUMED': <EventCallbackResult.CONSUMED: 2>}
        pass
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def add_child(self, arg0: Widget) -> None:
        """
        Adds a child widget
        """
    def calc_preferred_size(
        self, arg0: LayoutContext, arg1: Widget.Constraints
    ) -> Size:
        """
        Returns the preferred size of the widget. This is intended to be called only during layout, although it will also work during drawing. Calling it at other times will not work, as it requires some internal setup in order to function properly
        """
    def get_children(self) -> typing.List[Widget]:
        """
        Returns the array of children. Do not modify.
        """
    @property
    def background_color(self) -> Color:
        """
        Background color of the widget

        :type: Color
        """
    @background_color.setter
    def background_color(self, arg1: Color) -> None:
        """
        Background color of the widget
        """
    @property
    def enabled(self) -> bool:
        """
        True if widget is enabled, False if disabled

        :type: bool
        """
    @enabled.setter
    def enabled(self, arg1: bool) -> None:
        """
        True if widget is enabled, False if disabled
        """
    @property
    def frame(self) -> Rect:
        """
        The widget's frame. Setting this value will be overridden if the frame is within a layout.

        :type: Rect
        """
    @frame.setter
    def frame(self, arg1: Rect) -> None:
        """
        The widget's frame. Setting this value will be overridden if the frame is within a layout.
        """
    @property
    def tooltip(self) -> str:
        """
        Widget's tooltip that is displayed on mouseover

        :type: str
        """
    @tooltip.setter
    def tooltip(self, arg1: str) -> None:
        """
        Widget's tooltip that is displayed on mouseover
        """
    @property
    def visible(self) -> bool:
        """
        True if widget is visible, False otherwise

        :type: bool
        """
    @visible.setter
    def visible(self, arg1: bool) -> None:
        """
        True if widget is visible, False otherwise
        """
    CONSUMED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.CONSUMED: 2>
    HANDLED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.HANDLED: 1>
    IGNORED: open3d.visualization.gui.Widget.EventCallbackResult  # value = <EventCallbackResult.IGNORED: 0>
    pass

class CheckableTextTreeCell(Widget):
    """
    TreeView cell with a checkbox and text
    """

    def __init__(
        self, arg0: str, arg1: bool, arg2: typing.Callable[[bool], None]
    ) -> None:
        """
        Creates a TreeView cell with a checkbox and text. CheckableTextTreeCell(text, is_checked, on_toggled): on_toggled takes a boolean and returns None
        """
    @property
    def checkbox(self) -> Checkbox:
        """
        Returns the checkbox widget (property is read-only)

        :type: Checkbox
        """
    @property
    def label(self) -> Label:
        """
        Returns the label widget (property is read-only)

        :type: Label
        """
    pass

class Checkbox(Widget):
    """
    Checkbox
    """

    def __init__(self, arg0: str) -> None:
        """
        Creates a checkbox with the given text
        """
    def __repr__(self) -> str: ...
    def set_on_checked(self, arg0: typing.Callable[[bool], None]) -> None:
        """
        Calls passed function when checkbox changes state
        """
    @property
    def checked(self) -> bool:
        """
        True if checked, False otherwise

        :type: bool
        """
    @checked.setter
    def checked(self, arg1: bool) -> None:
        """
        True if checked, False otherwise
        """
    pass

class Layout1D(Widget):
    """
    Layout base class
    """

    @typing.overload
    def add_fixed(self, arg0: float) -> None:
        """
        Adds a fixed amount of empty space to the layout

        Adds a fixed amount of empty space to the layout
        """
    @typing.overload
    def add_fixed(self, arg0: int) -> None: ...
    def add_stretch(self) -> None:
        """
        Adds empty space to the layout that will take up as much extra space as there is available in the layout
        """
    pass

class Color:
    """
    Stores color for gui classes
    """

    def __init__(
        self, r: float = 1.0, g: float = 1.0, b: float = 1.0, a: float = 1.0
    ) -> None: ...
    def set_color(self, r: float, g: float, b: float, a: float = 1.0) -> None:
        """
        Sets red, green, blue, and alpha channels, (range: [0.0, 1.0])
        """
    @property
    def alpha(self) -> float:
        """
        Returns alpha channel in the range [0.0, 1.0] (read-only)

        :type: float
        """
    @property
    def blue(self) -> float:
        """
        Returns blue channel in the range [0.0, 1.0] (read-only)

        :type: float
        """
    @property
    def green(self) -> float:
        """
        Returns green channel in the range [0.0, 1.0] (read-only)

        :type: float
        """
    @property
    def red(self) -> float:
        """
        Returns red channel in the range [0.0, 1.0] (read-only)

        :type: float
        """
    pass

class ColorEdit(Widget):
    """
    Color picker
    """

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def set_on_value_changed(self, arg0: typing.Callable[[Color], None]) -> None:
        """
        Calls f(Color) when color changes by user input
        """
    @property
    def color_value(self) -> Color:
        """
        Color value (gui.Color)

        :type: Color
        """
    @color_value.setter
    def color_value(self, arg1: Color) -> None:
        """
        Color value (gui.Color)
        """
    pass

class ColormapTreeCell(Widget):
    """
    TreeView cell with a number edit and color edit
    """

    def __init__(
        self,
        arg0: float,
        arg1: Color,
        arg2: typing.Callable[[float], None],
        arg3: typing.Callable[[Color], None],
    ) -> None:
        """
        Creates a TreeView cell with a number and a color edit. ColormapTreeCell(value, color, on_value_changed, on_color_changed): on_value_changed takes a double and returns None; on_color_changed takes a gui.Color and returns None
        """
    @property
    def color_edit(self) -> ColorEdit:
        """
        Returns the ColorEdit widget (property is read-only)

        :type: ColorEdit
        """
    @property
    def number_edit(self) -> NumberEdit:
        """
        Returns the NumberEdit widget (property is read-only)

        :type: NumberEdit
        """
    pass

class Combobox(Widget):
    """
    Exclusive selection from a pull-down menu
    """

    def __init__(self) -> None:
        """
        Creates an empty combobox. Use add_item() to add items
        """
    def add_item(self, arg0: str) -> int:
        """
        Adds an item to the end
        """
    @typing.overload
    def change_item(self, arg0: int, arg1: str) -> None:
        """
        Changes the text of the item at index: change_item(index, newtext)

        Changes the text of the matching item: change_item(text, newtext)
        """
    @typing.overload
    def change_item(self, arg0: str, arg1: str) -> None: ...
    def clear_items(self) -> None:
        """
        Removes all items
        """
    def get_item(self, arg0: int) -> str:
        """
        Returns the item at the given index
        """
    @typing.overload
    def remove_item(self, arg0: int) -> None:
        """
        Removes the first item of the given text

        Removes the item at the index
        """
    @typing.overload
    def remove_item(self, arg0: str) -> None: ...
    def set_on_selection_changed(self, arg0: typing.Callable[[str, int], None]) -> None:
        """
        Calls f(str, int) when user selects item from combobox. Arguments are the selected text and selected index, respectively
        """
    @property
    def number_of_items(self) -> int:
        """
        The number of items (read-only)

        :type: int
        """
    @property
    def selected_index(self) -> int:
        """
        The index of the currently selected item

        :type: int
        """
    @selected_index.setter
    def selected_index(self, arg1: int) -> None:
        """
        The index of the currently selected item
        """
    @property
    def selected_text(self) -> str:
        """
        The index of the currently selected item

        :type: str
        """
    @selected_text.setter
    def selected_text(self, arg1: str) -> None:
        """
        The index of the currently selected item
        """
    pass

class Dialog(Widget):
    """
    Dialog
    """

    def __init__(self, arg0: str) -> None:
        """
        Creates a dialog with the given title
        """
    pass

class FileDialog(Dialog, Widget):
    """
    File picker dialog
    """

    class Mode:
        """
        Enum class for FileDialog modes.
        """

        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        OPEN: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.OPEN: 0>
        OPEN_DIR: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.OPEN_DIR: 2>
        SAVE: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.SAVE: 1>
        __members__: dict  # value = {'OPEN': <Mode.OPEN: 0>, 'SAVE': <Mode.SAVE: 1>, 'OPEN_DIR': <Mode.OPEN_DIR: 2>}
        pass
    def __init__(self, arg0: FileDialog.Mode, arg1: str, arg2: Theme) -> None:
        """
        Creates either an open or save file dialog. The first parameter is either FileDialog.OPEN or FileDialog.SAVE. The second is the title of the dialog, and the third is the theme, which is used internally by the dialog for layout. The theme should normally be retrieved from window.theme.
        """
    def add_filter(self, arg0: str, arg1: str) -> None:
        """
        Adds a selectable file-type filter: add_filter('.stl', 'Stereolithography mesh'
        """
    def set_on_cancel(self, arg0: typing.Callable[[], None]) -> None:
        """
        Cancel callback; required
        """
    def set_on_done(self, arg0: typing.Callable[[str], None]) -> None:
        """
        Done callback; required
        """
    def set_path(self, arg0: str) -> None:
        """
        Sets the initial path path of the dialog
        """
    OPEN: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.OPEN: 0>
    OPEN_DIR: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.OPEN_DIR: 2>
    SAVE: open3d.visualization.gui.FileDialog.Mode  # value = <Mode.SAVE: 1>
    pass

class FontDescription:
    """
    Class to describe a custom font
    """

    def __init__(
        self,
        typeface: str = "sans-serif",
        style: FontStyle = FontStyle.NORMAL,
        point_size: int = 0,
    ) -> None:
        """
        Creates a FontDescription. 'typeface' is a path to a TrueType (.ttf), TrueType Collection (.ttc), or OpenType (.otf) file, or it is the name of the font, in which case the system font paths will be searched to find the font file. This typeface will be used for roman characters (Extended Latin, that is, European languages
        """
    def add_typeface_for_code_points(self, arg0: str, arg1: typing.List[int]) -> None:
        """
        Adds specific code points from the typeface. This is useful for selectively adding glyphs, for example, from an icon font.
        """
    def add_typeface_for_language(self, arg0: str, arg1: str) -> None:
        """
        Adds code points outside Extended Latin from the specified typeface. Supported languages are:
           'ja' (Japanese)
           'ko' (Korean)
           'th' (Thai)
           'vi' (Vietnamese)
           'zh' (Chinese, 2500 most common characters, 50 MB per window)
           'zh_all' (Chinese, all characters, ~200 MB per window)
        All other languages will be assumed to be Cyrillic. Note that generally fonts do not have CJK glyphs unless they are specifically a CJK font, although operating systems generally use a CJK font for you. We do not have the information necessary to do this, so you will need to provide a font that has the glyphs you need. In particular, common fonts like 'Arial', 'Helvetica', and SANS_SERIF do not contain CJK glyphs.
        """
    MONOSPACE = "monospace"
    SANS_SERIF = "sans-serif"
    pass

class FontStyle:
    """
    Font style

    Members:

      NORMAL

      BOLD

      ITALIC

      BOLD_ITALIC
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    BOLD: open3d.visualization.gui.FontStyle  # value = <FontStyle.BOLD: 1>
    BOLD_ITALIC: open3d.visualization.gui.FontStyle  # value = <FontStyle.BOLD_ITALIC: 3>
    ITALIC: open3d.visualization.gui.FontStyle  # value = <FontStyle.ITALIC: 2>
    NORMAL: open3d.visualization.gui.FontStyle  # value = <FontStyle.NORMAL: 0>
    __members__: dict  # value = {'NORMAL': <FontStyle.NORMAL: 0>, 'BOLD': <FontStyle.BOLD: 1>, 'ITALIC': <FontStyle.ITALIC: 2>, 'BOLD_ITALIC': <FontStyle.BOLD_ITALIC: 3>}
    pass

class Horiz(Layout1D, Widget):
    """
    Horizontal layout
    """

    @typing.overload
    def __init__(self, spacing: float = 0.0, margins: Margins = ...) -> None:
        """
        Creates a layout that arranges widgets horizontally, left to right, making their height equal to the layout's height (which will generally be the largest height of the items). First argument is the spacing between widgets, the second is the margins. Both default to 0.

        Creates a layout that arranges widgets horizontally, left to right, making their height equal to the layout's height (which will generally be the largest height of the items). First argument is the spacing between widgets, the second is the margins. Both default to 0.
        """
    @typing.overload
    def __init__(self, spacing: int = 0, margins: Margins = ...) -> None: ...
    @property
    def preferred_height(self) -> int:
        """
        Sets the preferred height of the layout

        :type: int
        """
    @preferred_height.setter
    def preferred_height(self, arg1: int) -> None:
        """
        Sets the preferred height of the layout
        """
    pass

class ImageWidget(Widget):
    """
    Displays a bitmap
    """

    @typing.overload
    def __init__(self) -> None:
        """
        Creates an ImageWidget with no image

        Creates an ImageWidget from the image at the specified path

        Creates an ImageWidget from the provided image

        Creates an ImageWidget from the provided tgeometry image
        """
    @typing.overload
    def __init__(self, arg0: open3d.geometry.Image) -> None: ...
    @typing.overload
    def __init__(self, arg0: open3d.t.geometry.Image) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def update_image(self, arg0: open3d.geometry.Image) -> None:
        """
        Mostly a convenience function for ui_image.update_image(). If 'image' is the same size as the current image, will update the texture with the contents of 'image'. This is the fastest path for setting an image, and is recommended if you are displaying video. If 'image' is a different size, it will allocate a new texture, which is essentially the same as creating a new UIImage and calling SetUIImage(). This is the slow path, and may eventually exhaust internal texture resources.

        Mostly a convenience function for ui_image.update_image(). If 'image' is the same size as the current image, will update the texture with the contents of 'image'. This is the fastest path for setting an image, and is recommended if you are displaying video. If 'image' is a different size, it will allocate a new texture, which is essentially the same as creating a new UIImage and calling SetUIImage(). This is the slow path, and may eventually exhaust internal texture resources.
        """
    @typing.overload
    def update_image(self, arg0: open3d.t.geometry.Image) -> None: ...
    @property
    def ui_image(self) -> UIImage:
        """
        Replaces the texture with a new texture. This is not a fast path, and is not recommended for video as you will exhaust internal texture resources.

        :type: UIImage
        """
    @ui_image.setter
    def ui_image(self, arg1: UIImage) -> None:
        """
        Replaces the texture with a new texture. This is not a fast path, and is not recommended for video as you will exhaust internal texture resources.
        """
    pass

class KeyEvent:
    """
    Object that stores key events
    """

    class Type:
        """
        Members:

          DOWN

          UP
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        DOWN: open3d.visualization.gui.KeyEvent.Type  # value = <Type.DOWN: 0>
        UP: open3d.visualization.gui.KeyEvent.Type  # value = <Type.UP: 1>
        __members__: dict  # value = {'DOWN': <Type.DOWN: 0>, 'UP': <Type.UP: 1>}
        pass
    @property
    def is_repeat(self) -> bool:
        """
        True if this key down event comes from a key repeat

        :type: bool
        """
    @is_repeat.setter
    def is_repeat(self, arg0: bool) -> None:
        """
        True if this key down event comes from a key repeat
        """
    @property
    def key(self) -> int:
        """
        This is the actual key that was pressed, not the character generated by the key. This event is not suitable for text entry

        :type: int
        """
    @key.setter
    def key(self, arg0: int) -> None:
        """
        This is the actual key that was pressed, not the character generated by the key. This event is not suitable for text entry
        """
    @property
    def type(self) -> KeyEvent.Type:
        """
        Key event type

        :type: KeyEvent.Type
        """
    @type.setter
    def type(self, arg0: KeyEvent.Type) -> None:
        """
        Key event type
        """
    DOWN: open3d.visualization.gui.KeyEvent.Type  # value = <Type.DOWN: 0>
    UP: open3d.visualization.gui.KeyEvent.Type  # value = <Type.UP: 1>
    pass

class KeyModifier:
    """
    Key modifier identifiers

    Members:

      NONE

      SHIFT

      CTRL

      ALT

      META
    """

    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ALT: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.ALT: 4>
    CTRL: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.CTRL: 2>
    META: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.META: 8>
    NONE: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.NONE: 0>
    SHIFT: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.SHIFT: 1>
    __members__: dict  # value = {'NONE': <KeyModifier.NONE: 0>, 'SHIFT': <KeyModifier.SHIFT: 1>, 'CTRL': <KeyModifier.CTRL: 2>, 'ALT': <KeyModifier.ALT: 4>, 'META': <KeyModifier.META: 8>}
    pass

class KeyName:
    """
    Names of keys. Used by KeyEvent.key

    Members:

      NONE

      BACKSPACE

      TAB

      ENTER

      ESCAPE

      SPACE

      EXCLAMATION_MARK

      DOUBLE_QUOTE

      HASH

      DOLLAR_SIGN

      PERCENT

      AMPERSAND

      QUOTE

      LEFT_PAREN

      RIGHT_PAREN

      ASTERISK

      PLUS

      COMMA

      MINUS

      PERIOD

      SLASH

      ZERO

      ONE

      TWO

      THREE

      FOUR

      FIVE

      SIX

      SEVEN

      EIGHT

      NINE

      COLON

      SEMICOLON

      LESS_THAN

      EQUALS

      GREATER_THAN

      QUESTION_MARK

      AT

      LEFT_BRACKET

      BACKSLASH

      RIGHT_BRACKET

      CARET

      UNDERSCORE

      BACKTICK

      A

      B

      C

      D

      E

      F

      G

      H

      I

      J

      K

      L

      M

      N

      O

      P

      Q

      R

      S

      T

      U

      V

      W

      X

      Y

      Z

      LEFT_BRACE

      PIPE

      RIGHT_BRACE

      TILDE

      DELETE

      LEFT_SHIFT

      RIGHT_SHIFT

      LEFT_CONTROL

      RIGHT_CONTROL

      ALT

      META

      CAPS_LOCK

      LEFT

      RIGHT

      UP

      DOWN

      INSERT

      HOME

      END

      PAGE_UP

      PAGE_DOWN

      F1

      F2

      F3

      F4

      F5

      F6

      F7

      F8

      F9

      F10

      F11

      F12

      UNKNOWN
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    A: open3d.visualization.gui.KeyName  # value = <KeyName.A: 97>
    ALT: open3d.visualization.gui.KeyName  # value = <KeyName.ALT: 260>
    AMPERSAND: open3d.visualization.gui.KeyName  # value = <KeyName.AMPERSAND: 38>
    ASTERISK: open3d.visualization.gui.KeyName  # value = <KeyName.ASTERISK: 42>
    AT: open3d.visualization.gui.KeyName  # value = <KeyName.AT: 64>
    B: open3d.visualization.gui.KeyName  # value = <KeyName.B: 98>
    BACKSLASH: open3d.visualization.gui.KeyName  # value = <KeyName.BACKSLASH: 92>
    BACKSPACE: open3d.visualization.gui.KeyName  # value = <KeyName.BACKSPACE: 8>
    BACKTICK: open3d.visualization.gui.KeyName  # value = <KeyName.BACKTICK: 96>
    C: open3d.visualization.gui.KeyName  # value = <KeyName.C: 99>
    CAPS_LOCK: open3d.visualization.gui.KeyName  # value = <KeyName.CAPS_LOCK: 262>
    CARET: open3d.visualization.gui.KeyName  # value = <KeyName.CARET: 94>
    COLON: open3d.visualization.gui.KeyName  # value = <KeyName.COLON: 58>
    COMMA: open3d.visualization.gui.KeyName  # value = <KeyName.COMMA: 44>
    D: open3d.visualization.gui.KeyName  # value = <KeyName.D: 100>
    DELETE: open3d.visualization.gui.KeyName  # value = <KeyName.DELETE: 127>
    DOLLAR_SIGN: open3d.visualization.gui.KeyName  # value = <KeyName.DOLLAR_SIGN: 36>
    DOUBLE_QUOTE: open3d.visualization.gui.KeyName  # value = <KeyName.DOUBLE_QUOTE: 34>
    DOWN: open3d.visualization.gui.KeyName  # value = <KeyName.DOWN: 266>
    E: open3d.visualization.gui.KeyName  # value = <KeyName.E: 101>
    EIGHT: open3d.visualization.gui.KeyName  # value = <KeyName.EIGHT: 56>
    END: open3d.visualization.gui.KeyName  # value = <KeyName.END: 269>
    ENTER: open3d.visualization.gui.KeyName  # value = <KeyName.ENTER: 10>
    EQUALS: open3d.visualization.gui.KeyName  # value = <KeyName.EQUALS: 61>
    ESCAPE: open3d.visualization.gui.KeyName  # value = <KeyName.ESCAPE: 27>
    EXCLAMATION_MARK: open3d.visualization.gui.KeyName  # value = <KeyName.EXCLAMATION_MARK: 33>
    F: open3d.visualization.gui.KeyName  # value = <KeyName.F: 102>
    F1: open3d.visualization.gui.KeyName  # value = <KeyName.F1: 290>
    F10: open3d.visualization.gui.KeyName  # value = <KeyName.F10: 299>
    F11: open3d.visualization.gui.KeyName  # value = <KeyName.F11: 300>
    F12: open3d.visualization.gui.KeyName  # value = <KeyName.F12: 301>
    F2: open3d.visualization.gui.KeyName  # value = <KeyName.F2: 291>
    F3: open3d.visualization.gui.KeyName  # value = <KeyName.F3: 292>
    F4: open3d.visualization.gui.KeyName  # value = <KeyName.F4: 293>
    F5: open3d.visualization.gui.KeyName  # value = <KeyName.F5: 294>
    F6: open3d.visualization.gui.KeyName  # value = <KeyName.F6: 295>
    F7: open3d.visualization.gui.KeyName  # value = <KeyName.F7: 296>
    F8: open3d.visualization.gui.KeyName  # value = <KeyName.F8: 297>
    F9: open3d.visualization.gui.KeyName  # value = <KeyName.F9: 298>
    FIVE: open3d.visualization.gui.KeyName  # value = <KeyName.FIVE: 53>
    FOUR: open3d.visualization.gui.KeyName  # value = <KeyName.FOUR: 52>
    G: open3d.visualization.gui.KeyName  # value = <KeyName.G: 103>
    GREATER_THAN: open3d.visualization.gui.KeyName  # value = <KeyName.GREATER_THAN: 62>
    H: open3d.visualization.gui.KeyName  # value = <KeyName.H: 104>
    HASH: open3d.visualization.gui.KeyName  # value = <KeyName.HASH: 35>
    HOME: open3d.visualization.gui.KeyName  # value = <KeyName.HOME: 268>
    I: open3d.visualization.gui.KeyName  # value = <KeyName.I: 105>
    INSERT: open3d.visualization.gui.KeyName  # value = <KeyName.INSERT: 267>
    J: open3d.visualization.gui.KeyName  # value = <KeyName.J: 106>
    K: open3d.visualization.gui.KeyName  # value = <KeyName.K: 107>
    L: open3d.visualization.gui.KeyName  # value = <KeyName.L: 108>
    LEFT: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT: 263>
    LEFT_BRACE: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_BRACE: 123>
    LEFT_BRACKET: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_BRACKET: 91>
    LEFT_CONTROL: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_CONTROL: 258>
    LEFT_PAREN: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_PAREN: 40>
    LEFT_SHIFT: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_SHIFT: 256>
    LESS_THAN: open3d.visualization.gui.KeyName  # value = <KeyName.LESS_THAN: 60>
    M: open3d.visualization.gui.KeyName  # value = <KeyName.M: 109>
    META: open3d.visualization.gui.KeyName  # value = <KeyName.META: 261>
    MINUS: open3d.visualization.gui.KeyName  # value = <KeyName.MINUS: 45>
    N: open3d.visualization.gui.KeyName  # value = <KeyName.N: 110>
    NINE: open3d.visualization.gui.KeyName  # value = <KeyName.NINE: 57>
    NONE: open3d.visualization.gui.KeyName  # value = <KeyName.NONE: 0>
    O: open3d.visualization.gui.KeyName  # value = <KeyName.O: 111>
    ONE: open3d.visualization.gui.KeyName  # value = <KeyName.ONE: 49>
    P: open3d.visualization.gui.KeyName  # value = <KeyName.P: 112>
    PAGE_DOWN: open3d.visualization.gui.KeyName  # value = <KeyName.PAGE_DOWN: 271>
    PAGE_UP: open3d.visualization.gui.KeyName  # value = <KeyName.PAGE_UP: 270>
    PERCENT: open3d.visualization.gui.KeyName  # value = <KeyName.PERCENT: 37>
    PERIOD: open3d.visualization.gui.KeyName  # value = <KeyName.PERIOD: 46>
    PIPE: open3d.visualization.gui.KeyName  # value = <KeyName.PIPE: 124>
    PLUS: open3d.visualization.gui.KeyName  # value = <KeyName.PLUS: 43>
    Q: open3d.visualization.gui.KeyName  # value = <KeyName.Q: 113>
    QUESTION_MARK: open3d.visualization.gui.KeyName  # value = <KeyName.QUESTION_MARK: 63>
    QUOTE: open3d.visualization.gui.KeyName  # value = <KeyName.QUOTE: 39>
    R: open3d.visualization.gui.KeyName  # value = <KeyName.R: 114>
    RIGHT: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT: 264>
    RIGHT_BRACE: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_BRACE: 125>
    RIGHT_BRACKET: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_BRACKET: 93>
    RIGHT_CONTROL: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_CONTROL: 259>
    RIGHT_PAREN: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_PAREN: 41>
    RIGHT_SHIFT: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_SHIFT: 257>
    S: open3d.visualization.gui.KeyName  # value = <KeyName.S: 115>
    SEMICOLON: open3d.visualization.gui.KeyName  # value = <KeyName.SEMICOLON: 59>
    SEVEN: open3d.visualization.gui.KeyName  # value = <KeyName.SEVEN: 55>
    SIX: open3d.visualization.gui.KeyName  # value = <KeyName.SIX: 54>
    SLASH: open3d.visualization.gui.KeyName  # value = <KeyName.SLASH: 47>
    SPACE: open3d.visualization.gui.KeyName  # value = <KeyName.SPACE: 32>
    T: open3d.visualization.gui.KeyName  # value = <KeyName.T: 116>
    TAB: open3d.visualization.gui.KeyName  # value = <KeyName.TAB: 9>
    THREE: open3d.visualization.gui.KeyName  # value = <KeyName.THREE: 51>
    TILDE: open3d.visualization.gui.KeyName  # value = <KeyName.TILDE: 126>
    TWO: open3d.visualization.gui.KeyName  # value = <KeyName.TWO: 50>
    U: open3d.visualization.gui.KeyName  # value = <KeyName.U: 117>
    UNDERSCORE: open3d.visualization.gui.KeyName  # value = <KeyName.UNDERSCORE: 95>
    UNKNOWN: open3d.visualization.gui.KeyName  # value = <KeyName.UNKNOWN: 1000>
    UP: open3d.visualization.gui.KeyName  # value = <KeyName.UP: 265>
    V: open3d.visualization.gui.KeyName  # value = <KeyName.V: 118>
    W: open3d.visualization.gui.KeyName  # value = <KeyName.W: 119>
    X: open3d.visualization.gui.KeyName  # value = <KeyName.X: 120>
    Y: open3d.visualization.gui.KeyName  # value = <KeyName.Y: 121>
    Z: open3d.visualization.gui.KeyName  # value = <KeyName.Z: 122>
    ZERO: open3d.visualization.gui.KeyName  # value = <KeyName.ZERO: 48>
    __members__: dict  # value = {'NONE': <KeyName.NONE: 0>, 'BACKSPACE': <KeyName.BACKSPACE: 8>, 'TAB': <KeyName.TAB: 9>, 'ENTER': <KeyName.ENTER: 10>, 'ESCAPE': <KeyName.ESCAPE: 27>, 'SPACE': <KeyName.SPACE: 32>, 'EXCLAMATION_MARK': <KeyName.EXCLAMATION_MARK: 33>, 'DOUBLE_QUOTE': <KeyName.DOUBLE_QUOTE: 34>, 'HASH': <KeyName.HASH: 35>, 'DOLLAR_SIGN': <KeyName.DOLLAR_SIGN: 36>, 'PERCENT': <KeyName.PERCENT: 37>, 'AMPERSAND': <KeyName.AMPERSAND: 38>, 'QUOTE': <KeyName.QUOTE: 39>, 'LEFT_PAREN': <KeyName.LEFT_PAREN: 40>, 'RIGHT_PAREN': <KeyName.RIGHT_PAREN: 41>, 'ASTERISK': <KeyName.ASTERISK: 42>, 'PLUS': <KeyName.PLUS: 43>, 'COMMA': <KeyName.COMMA: 44>, 'MINUS': <KeyName.MINUS: 45>, 'PERIOD': <KeyName.PERIOD: 46>, 'SLASH': <KeyName.SLASH: 47>, 'ZERO': <KeyName.ZERO: 48>, 'ONE': <KeyName.ONE: 49>, 'TWO': <KeyName.TWO: 50>, 'THREE': <KeyName.THREE: 51>, 'FOUR': <KeyName.FOUR: 52>, 'FIVE': <KeyName.FIVE: 53>, 'SIX': <KeyName.SIX: 54>, 'SEVEN': <KeyName.SEVEN: 55>, 'EIGHT': <KeyName.EIGHT: 56>, 'NINE': <KeyName.NINE: 57>, 'COLON': <KeyName.COLON: 58>, 'SEMICOLON': <KeyName.SEMICOLON: 59>, 'LESS_THAN': <KeyName.LESS_THAN: 60>, 'EQUALS': <KeyName.EQUALS: 61>, 'GREATER_THAN': <KeyName.GREATER_THAN: 62>, 'QUESTION_MARK': <KeyName.QUESTION_MARK: 63>, 'AT': <KeyName.AT: 64>, 'LEFT_BRACKET': <KeyName.LEFT_BRACKET: 91>, 'BACKSLASH': <KeyName.BACKSLASH: 92>, 'RIGHT_BRACKET': <KeyName.RIGHT_BRACKET: 93>, 'CARET': <KeyName.CARET: 94>, 'UNDERSCORE': <KeyName.UNDERSCORE: 95>, 'BACKTICK': <KeyName.BACKTICK: 96>, 'A': <KeyName.A: 97>, 'B': <KeyName.B: 98>, 'C': <KeyName.C: 99>, 'D': <KeyName.D: 100>, 'E': <KeyName.E: 101>, 'F': <KeyName.F: 102>, 'G': <KeyName.G: 103>, 'H': <KeyName.H: 104>, 'I': <KeyName.I: 105>, 'J': <KeyName.J: 106>, 'K': <KeyName.K: 107>, 'L': <KeyName.L: 108>, 'M': <KeyName.M: 109>, 'N': <KeyName.N: 110>, 'O': <KeyName.O: 111>, 'P': <KeyName.P: 112>, 'Q': <KeyName.Q: 113>, 'R': <KeyName.R: 114>, 'S': <KeyName.S: 115>, 'T': <KeyName.T: 116>, 'U': <KeyName.U: 117>, 'V': <KeyName.V: 118>, 'W': <KeyName.W: 119>, 'X': <KeyName.X: 120>, 'Y': <KeyName.Y: 121>, 'Z': <KeyName.Z: 122>, 'LEFT_BRACE': <KeyName.LEFT_BRACE: 123>, 'PIPE': <KeyName.PIPE: 124>, 'RIGHT_BRACE': <KeyName.RIGHT_BRACE: 125>, 'TILDE': <KeyName.TILDE: 126>, 'DELETE': <KeyName.DELETE: 127>, 'LEFT_SHIFT': <KeyName.LEFT_SHIFT: 256>, 'RIGHT_SHIFT': <KeyName.RIGHT_SHIFT: 257>, 'LEFT_CONTROL': <KeyName.LEFT_CONTROL: 258>, 'RIGHT_CONTROL': <KeyName.RIGHT_CONTROL: 259>, 'ALT': <KeyName.ALT: 260>, 'META': <KeyName.META: 261>, 'CAPS_LOCK': <KeyName.CAPS_LOCK: 262>, 'LEFT': <KeyName.LEFT: 263>, 'RIGHT': <KeyName.RIGHT: 264>, 'UP': <KeyName.UP: 265>, 'DOWN': <KeyName.DOWN: 266>, 'INSERT': <KeyName.INSERT: 267>, 'HOME': <KeyName.HOME: 268>, 'END': <KeyName.END: 269>, 'PAGE_UP': <KeyName.PAGE_UP: 270>, 'PAGE_DOWN': <KeyName.PAGE_DOWN: 271>, 'F1': <KeyName.F1: 290>, 'F2': <KeyName.F2: 291>, 'F3': <KeyName.F3: 292>, 'F4': <KeyName.F4: 293>, 'F5': <KeyName.F5: 294>, 'F6': <KeyName.F6: 295>, 'F7': <KeyName.F7: 296>, 'F8': <KeyName.F8: 297>, 'F9': <KeyName.F9: 298>, 'F10': <KeyName.F10: 299>, 'F11': <KeyName.F11: 300>, 'F12': <KeyName.F12: 301>, 'UNKNOWN': <KeyName.UNKNOWN: 1000>}
    pass

class LUTTreeCell(Widget):
    """
    TreeView cell with checkbox, text, and color edit
    """

    def __init__(
        self,
        arg0: str,
        arg1: bool,
        arg2: Color,
        arg3: typing.Callable[[bool], None],
        arg4: typing.Callable[[Color], None],
    ) -> None:
        """
        Creates a TreeView cell with a checkbox, text, and a color editor. LUTTreeCell(text, is_checked, color, on_enabled, on_color): on_enabled is called when the checkbox toggles, and takes a boolean and returns None; on_color is called when the user changes the color and it takes a gui.Color and returns None.
        """
    @property
    def checkbox(self) -> Checkbox:
        """
        Returns the checkbox widget (property is read-only)

        :type: Checkbox
        """
    @property
    def color_edit(self) -> ColorEdit:
        """
        Returns the ColorEdit widget (property is read-only)

        :type: ColorEdit
        """
    @property
    def label(self) -> Label:
        """
        Returns the label widget (property is read-only)

        :type: Label
        """
    pass

class Label(Widget):
    """
    Displays text
    """

    def __init__(self, arg0: str) -> None:
        """
        Creates a Label with the given text
        """
    def __repr__(self) -> str: ...
    @property
    def font_id(self) -> int:
        """
        Set the font using the FontId returned from Application.add_font()

        :type: int
        """
    @font_id.setter
    def font_id(self, arg1: int) -> None:
        """
        Set the font using the FontId returned from Application.add_font()
        """
    @property
    def text(self) -> str:
        """
        The text of the label. Newlines will be treated as line breaks

        :type: str
        """
    @text.setter
    def text(self, arg1: str) -> None:
        """
        The text of the label. Newlines will be treated as line breaks
        """
    @property
    def text_color(self) -> Color:
        """
        The color of the text (gui.Color)

        :type: Color
        """
    @text_color.setter
    def text_color(self, arg1: Color) -> None:
        """
        The color of the text (gui.Color)
        """
    pass

class Label3D:
    """
    Displays text in a 3D scene
    """

    def __init__(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        """
        Create a 3D Label with given text and position
        """
    @property
    def color(self) -> Color:
        """
        The color of the text (gui.Color)

        :type: Color
        """
    @color.setter
    def color(self, arg1: Color) -> None:
        """
        The color of the text (gui.Color)
        """
    @property
    def position(self) -> Annotated[npt.NDArray[np.float32], (3, 1)]:
        """
        The position of the text in 3D coordinates

        :type: Annotated[npt.NDArray[np.float32], (3, 1)]
        """
    @position.setter
    def position(self, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]) -> None:
        """
        The position of the text in 3D coordinates
        """
    @property
    def scale(self) -> float:
        """
        The scale of the 3D label. When set to 1.0 (the default) text will be rendered at its native font size. Larger and smaller values of scale will enlarge or shrink the rendered text. Note: large values of scale may result in blurry text as the underlying font is not resized.

        :type: float
        """
    @scale.setter
    def scale(self, arg1: float) -> None:
        """
        The scale of the 3D label. When set to 1.0 (the default) text will be rendered at its native font size. Larger and smaller values of scale will enlarge or shrink the rendered text. Note: large values of scale may result in blurry text as the underlying font is not resized.
        """
    @property
    def text(self) -> str:
        """
        The text to display with this label.

        :type: str
        """
    @text.setter
    def text(self, arg1: str) -> None:
        """
        The text to display with this label.
        """
    pass

class Vert(Layout1D, Widget):
    """
    Vertical layout
    """

    @typing.overload
    def __init__(self, spacing: float = 0.0, margins: Margins = ...) -> None:
        """
        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the spacing between widgets, the second is the margins. Both default to 0.

        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the spacing between widgets, the second is the margins. Both default to 0.
        """
    @typing.overload
    def __init__(self, spacing: int = 0, margins: Margins = ...) -> None: ...
    @property
    def preferred_width(self) -> int:
        """
        Sets the preferred width of the layout

        :type: int
        """
    @preferred_width.setter
    def preferred_width(self, arg1: int) -> None:
        """
        Sets the preferred width of the layout
        """
    pass

class LayoutContext:
    """
    Context passed to Window's on_layout callback
    """

    @property
    def theme(self) -> open3d.visualization.gui.Theme:
        """
        :type: open3d.visualization.gui.Theme
        """
    pass

class ListView(Widget):
    """
    Displays a list of text
    """

    def __init__(self) -> None:
        """
        Creates an empty list
        """
    def __repr__(self) -> str: ...
    def set_items(self, arg0: typing.List[str]) -> None:
        """
        Sets the list to display the list of items provided
        """
    def set_max_visible_items(self, arg0: int) -> None:
        """
        Limit the max visible items shown to user. Set to negative number will make list extends vertically as much as possible, otherwise the list will at least show 3 items and at most show num items.
        """
    def set_on_selection_changed(
        self, arg0: typing.Callable[[str, bool], None]
    ) -> None:
        """
        Calls f(new_val, is_double_click) when user changes selection
        """
    @property
    def selected_index(self) -> int:
        """
        The index of the currently selected item

        :type: int
        """
    @selected_index.setter
    def selected_index(self, arg1: int) -> None:
        """
        The index of the currently selected item
        """
    @property
    def selected_value(self) -> str:
        """
        The text of the currently selected item

        :type: str
        """
    pass

class Margins:
    """
    Margins for layouts
    """

    @typing.overload
    def __init__(
        self,
        left: float = 0.0,
        top: float = 0.0,
        right: float = 0.0,
        bottom: float = 0.0,
    ) -> None:
        """
        Creates margins. Arguments are left, top, right, bottom. Use the em-size (window.theme.font_size) rather than pixels for more consistency across platforms and monitors. Margins are the spacing from the edge of the widget's frame to its content area. They act similar to the 'padding' property in CSS

        Creates margins. Arguments are left, top, right, bottom. Use the em-size (window.theme.font_size) rather than pixels for more consistency across platforms and monitors. Margins are the spacing from the edge of the widget's frame to its content area. They act similar to the 'padding' property in CSS
        """
    @typing.overload
    def __init__(
        self, left: int = 0, top: int = 0, right: int = 0, bottom: int = 0
    ) -> None: ...
    def get_horiz(self) -> int: ...
    def get_vert(self) -> int: ...
    @property
    def bottom(self) -> int:
        """
        :type: int
        """
    @bottom.setter
    def bottom(self, arg0: int) -> None:
        pass
    @property
    def left(self) -> int:
        """
        :type: int
        """
    @left.setter
    def left(self, arg0: int) -> None:
        pass
    @property
    def right(self) -> int:
        """
        :type: int
        """
    @right.setter
    def right(self, arg0: int) -> None:
        pass
    @property
    def top(self) -> int:
        """
        :type: int
        """
    @top.setter
    def top(self, arg0: int) -> None:
        pass
    pass

class Menu:
    """
    A menu, possibly a menu tree
    """

    def __init__(self) -> None: ...
    def add_item(self, arg0: str, arg1: int) -> None:
        """
        Adds a menu item with id to the menu
        """
    def add_menu(self, arg0: str, arg1: Menu) -> None:
        """
        Adds a submenu to the menu
        """
    def add_separator(self) -> None:
        """
        Adds a separator to the menu
        """
    def is_checked(self, arg0: int) -> bool:
        """
        Returns True if menu item is checked
        """
    def set_checked(self, arg0: int, arg1: bool) -> None:
        """
        Sets menu item (un)checked
        """
    def set_enabled(self, arg0: int, arg1: bool) -> None:
        """
        Sets menu item enabled or disabled
        """
    pass

class MouseButton:
    """
    Mouse button identifiers

    Members:

      NONE

      LEFT

      MIDDLE

      RIGHT

      BUTTON4

      BUTTON5
    """

    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    BUTTON4: open3d.visualization.gui.MouseButton  # value = <MouseButton.BUTTON4: 8>
    BUTTON5: open3d.visualization.gui.MouseButton  # value = <MouseButton.BUTTON5: 16>
    LEFT: open3d.visualization.gui.MouseButton  # value = <MouseButton.LEFT: 1>
    MIDDLE: open3d.visualization.gui.MouseButton  # value = <MouseButton.MIDDLE: 2>
    NONE: open3d.visualization.gui.MouseButton  # value = <MouseButton.NONE: 0>
    RIGHT: open3d.visualization.gui.MouseButton  # value = <MouseButton.RIGHT: 4>
    __members__: dict  # value = {'NONE': <MouseButton.NONE: 0>, 'LEFT': <MouseButton.LEFT: 1>, 'MIDDLE': <MouseButton.MIDDLE: 2>, 'RIGHT': <MouseButton.RIGHT: 4>, 'BUTTON4': <MouseButton.BUTTON4: 8>, 'BUTTON5': <MouseButton.BUTTON5: 16>}
    pass

class MouseEvent:
    """
    Object that stores mouse events
    """

    class Type:
        """
        Members:

          MOVE

          BUTTON_DOWN

          DRAG

          BUTTON_UP

          WHEEL
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        BUTTON_DOWN: open3d.visualization.gui.MouseEvent.Type  # value = <Type.BUTTON_DOWN: 1>
        BUTTON_UP: open3d.visualization.gui.MouseEvent.Type  # value = <Type.BUTTON_UP: 3>
        DRAG: open3d.visualization.gui.MouseEvent.Type  # value = <Type.DRAG: 2>
        MOVE: open3d.visualization.gui.MouseEvent.Type  # value = <Type.MOVE: 0>
        WHEEL: open3d.visualization.gui.MouseEvent.Type  # value = <Type.WHEEL: 4>
        __members__: dict  # value = {'MOVE': <Type.MOVE: 0>, 'BUTTON_DOWN': <Type.BUTTON_DOWN: 1>, 'DRAG': <Type.DRAG: 2>, 'BUTTON_UP': <Type.BUTTON_UP: 3>, 'WHEEL': <Type.WHEEL: 4>}
        pass
    def is_button_down(self, arg0: MouseButton) -> bool:
        """
        Convenience function to more easily deterimine if a mouse button is pressed
        """
    def is_modifier_down(self, arg0: KeyModifier) -> bool:
        """
        Convenience function to more easily deterimine if a modifier key is down
        """
    @property
    def buttons(self) -> int:
        """
        ORed mouse buttons

        :type: int
        """
    @buttons.setter
    def buttons(self, arg1: int) -> None:
        """
        ORed mouse buttons
        """
    @property
    def modifiers(self) -> int:
        """
        ORed mouse modifiers

        :type: int
        """
    @modifiers.setter
    def modifiers(self, arg0: int) -> None:
        """
        ORed mouse modifiers
        """
    @property
    def type(self) -> MouseEvent.Type:
        """
        Mouse event type

        :type: MouseEvent.Type
        """
    @type.setter
    def type(self, arg0: MouseEvent.Type) -> None:
        """
        Mouse event type
        """
    @property
    def wheel_dx(self) -> int:
        """
        Mouse wheel horizontal motion

        :type: int
        """
    @wheel_dx.setter
    def wheel_dx(self, arg1: int) -> None:
        """
        Mouse wheel horizontal motion
        """
    @property
    def wheel_dy(self) -> int:
        """
        Mouse wheel vertical motion

        :type: int
        """
    @wheel_dy.setter
    def wheel_dy(self, arg1: int) -> None:
        """
        Mouse wheel vertical motion
        """
    @property
    def wheel_is_trackpad(self) -> bool:
        """
        Is mouse wheel event from a trackpad

        :type: bool
        """
    @wheel_is_trackpad.setter
    def wheel_is_trackpad(self, arg1: bool) -> None:
        """
        Is mouse wheel event from a trackpad
        """
    @property
    def x(self) -> int:
        """
        x coordinate  of the mouse event

        :type: int
        """
    @x.setter
    def x(self, arg0: int) -> None:
        """
        x coordinate  of the mouse event
        """
    @property
    def y(self) -> int:
        """
        y coordinate of the mouse event

        :type: int
        """
    @y.setter
    def y(self, arg0: int) -> None:
        """
        y coordinate of the mouse event
        """
    BUTTON_DOWN: open3d.visualization.gui.MouseEvent.Type  # value = <Type.BUTTON_DOWN: 1>
    BUTTON_UP: open3d.visualization.gui.MouseEvent.Type  # value = <Type.BUTTON_UP: 3>
    DRAG: open3d.visualization.gui.MouseEvent.Type  # value = <Type.DRAG: 2>
    MOVE: open3d.visualization.gui.MouseEvent.Type  # value = <Type.MOVE: 0>
    WHEEL: open3d.visualization.gui.MouseEvent.Type  # value = <Type.WHEEL: 4>
    pass

class NumberEdit(Widget):
    """
    Allows the user to enter a number.
    """

    class Type:
        """
        Enum class for NumberEdit types.
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        DOUBLE: open3d.visualization.gui.NumberEdit.Type  # value = <Type.DOUBLE: 1>
        INT: open3d.visualization.gui.NumberEdit.Type  # value = <Type.INT: 0>
        __members__: dict  # value = {'INT': <Type.INT: 0>, 'DOUBLE': <Type.DOUBLE: 1>}
        pass
    def __init__(self, arg0: NumberEdit.Type) -> None:
        """
        Creates a NumberEdit that is either integers (INT) or floating point (DOUBLE). The initial value is 0 and the limits are +/- max integer (roughly).
        """
    def __repr__(self) -> str: ...
    def set_limits(self, arg0: float, arg1: float) -> None:
        """
        Sets the minimum and maximum values for the number
        """
    def set_on_value_changed(self, arg0: typing.Callable[[float], None]) -> None:
        """
        Sets f(new_value) which is called with a Float when user changes widget's value
        """
    @typing.overload
    def set_preferred_width(self, arg0: float) -> None:
        """
        Sets the preferred width of the NumberEdit

        Sets the preferred width of the NumberEdit
        """
    @typing.overload
    def set_preferred_width(self, arg0: int) -> None: ...
    def set_value(self, arg0: float) -> None:
        """
        Sets value
        """
    @property
    def decimal_precision(self) -> int:
        """
        Number of fractional digits shown

        :type: int
        """
    @decimal_precision.setter
    def decimal_precision(self, arg1: int) -> None:
        """
        Number of fractional digits shown
        """
    @property
    def double_value(self) -> float:
        """
        Current value (double)

        :type: float
        """
    @double_value.setter
    def double_value(self, arg1: float) -> None:
        """
        Current value (double)
        """
    @property
    def int_value(self) -> int:
        """
        Current value (int)

        :type: int
        """
    @int_value.setter
    def int_value(self, arg1: int) -> None:
        """
        Current value (int)
        """
    @property
    def maximum_value(self) -> float:
        """
        The maximum value number can contain (read-only, use set_limits() to set)

        :type: float
        """
    @property
    def minimum_value(self) -> float:
        """
        The minimum value number can contain (read-only, use set_limits() to set)

        :type: float
        """
    DOUBLE: open3d.visualization.gui.NumberEdit.Type  # value = <Type.DOUBLE: 1>
    INT: open3d.visualization.gui.NumberEdit.Type  # value = <Type.INT: 0>
    pass

class ProgressBar(Widget):
    """
    Displays a progress bar
    """

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def value(self) -> float:
        """
        The value of the progress bar, ranges from 0.0 to 1.0

        :type: float
        """
    @value.setter
    def value(self, arg1: float) -> None:
        """
        The value of the progress bar, ranges from 0.0 to 1.0
        """
    pass

class RadioButton(Widget):
    """
    Exclusive selection from radio button list
    """

    class Type:
        """
        Enum class for RadioButton types.
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        HORIZ: open3d.visualization.gui.RadioButton.Type  # value = <Type.HORIZ: 1>
        VERT: open3d.visualization.gui.RadioButton.Type  # value = <Type.VERT: 0>
        __members__: dict  # value = {'VERT': <Type.VERT: 0>, 'HORIZ': <Type.HORIZ: 1>}
        pass
    def __init__(self, arg0: RadioButton.Type) -> None:
        """
        Creates an empty radio buttons. Use set_items() to add items
        """
    def set_items(self, arg0: typing.List[str]) -> None:
        """
        Set radio items, each item is a radio button.
        """
    def set_on_selection_changed(self, arg0: typing.Callable[[int], None]) -> None:
        """
        Calls f(new_idx) when user changes selection
        """
    @property
    def selected_index(self) -> int:
        """
        The index of the currently selected item

        :type: int
        """
    @selected_index.setter
    def selected_index(self, arg1: int) -> None:
        """
        The index of the currently selected item
        """
    @property
    def selected_value(self) -> str:
        """
        The text of the currently selected item

        :type: str
        """
    HORIZ: open3d.visualization.gui.RadioButton.Type  # value = <Type.HORIZ: 1>
    VERT: open3d.visualization.gui.RadioButton.Type  # value = <Type.VERT: 0>
    pass

class Rect:
    """
    Represents a widget frame
    """

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def __repr__(self) -> str: ...
    def get_bottom(self) -> int: ...
    def get_left(self) -> int: ...
    def get_right(self) -> int: ...
    def get_top(self) -> int: ...
    @property
    def height(self) -> int:
        """
        :type: int
        """
    @height.setter
    def height(self, arg0: int) -> None:
        pass
    @property
    def width(self) -> int:
        """
        :type: int
        """
    @width.setter
    def width(self, arg0: int) -> None:
        pass
    @property
    def x(self) -> int:
        """
        :type: int
        """
    @x.setter
    def x(self, arg0: int) -> None:
        pass
    @property
    def y(self) -> int:
        """
        :type: int
        """
    @y.setter
    def y(self, arg0: int) -> None:
        pass
    pass

class SceneWidget(Widget):
    """
    Displays 3D content
    """

    class Controls:
        """
        Enum class describing mouse interaction.
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        FLY: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.FLY: 2>
        PICK_POINTS: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.PICK_POINTS: 6>
        ROTATE_CAMERA: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_CAMERA: 0>
        ROTATE_CAMERA_SPHERE: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_CAMERA_SPHERE: 1>
        ROTATE_IBL: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_IBL: 4>
        ROTATE_MODEL: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_MODEL: 5>
        ROTATE_SUN: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_SUN: 3>
        __members__: dict  # value = {'ROTATE_CAMERA': <Controls.ROTATE_CAMERA: 0>, 'ROTATE_CAMERA_SPHERE': <Controls.ROTATE_CAMERA_SPHERE: 1>, 'FLY': <Controls.FLY: 2>, 'ROTATE_SUN': <Controls.ROTATE_SUN: 3>, 'ROTATE_IBL': <Controls.ROTATE_IBL: 4>, 'ROTATE_MODEL': <Controls.ROTATE_MODEL: 5>, 'PICK_POINTS': <Controls.PICK_POINTS: 6>}
        pass
    def __init__(self) -> None:
        """
        Creates an empty SceneWidget. Assign a Scene with the 'scene' property
        """
    def add_3d_label(
        self, arg0: Annotated[npt.NDArray[np.float32], (3, 1)], arg1: str
    ) -> Label3D:
        """
        Add a 3D text label to the scene. The label will be anchored at the specified 3D point.
        """
    def enable_scene_caching(self, arg0: bool) -> None:
        """
        Enable/Disable caching of scene content when the view or model is not changing. Scene caching can help improve UI responsiveness for large models and point clouds
        """
    def force_redraw(self) -> None:
        """
        Ensures scene redraws even when scene caching is enabled.
        """
    def look_at(
        self,
        arg0: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
    ) -> None: ...
    def remove_3d_label(self, arg0: Label3D) -> None:
        """
        Removes the 3D text label from the scene
        """
    def set_on_key(self, arg0: typing.Callable[[KeyEvent], int]) -> None:
        """
        Sets a callback for key events. This callback is passed a KeyEvent object. The callback must return EventCallbackResult.IGNORED, EventCallbackResult.HANDLED, or EventCallbackResult.CONSUMED.
        """
    def set_on_mouse(self, arg0: typing.Callable[[MouseEvent], int]) -> None:
        """
        Sets a callback for mouse events. This callback is passed a MouseEvent object. The callback must return EventCallbackResult.IGNORED, EventCallbackResult.HANDLED, or EventCallbackResult.CONSUMED.
        """
    def set_on_sun_direction_changed(
        self, arg0: typing.Callable[[Annotated[npt.NDArray[np.float32], (3, 1)]], None]
    ) -> None:
        """
        Callback when user changes sun direction (only called in ROTATE_SUN control mode). Called with one argument, the [i, j, k] vector of the new sun direction
        """
    def set_view_controls(self, arg0: SceneWidget.Controls) -> None:
        """
        Sets mouse interaction, e.g. ROTATE_OBJ
        """
    @typing.overload
    def setup_camera(
        self,
        arg0: Annotated[npt.NDArray[np.float64], (3, 3)],
        arg1: Annotated[npt.NDArray[np.float64], (4, 4)],
        arg2: int,
        arg3: int,
        arg4: open3d.geometry.AxisAlignedBoundingBox,
    ) -> None:
        """
        Configure the camera: setup_camera(field_of_view, model_bounds, center_of_rotation)
        """
    @typing.overload
    def setup_camera(
        self,
        arg0: float,
        arg1: open3d.geometry.AxisAlignedBoundingBox,
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
    ) -> None: ...
    @typing.overload
    def setup_camera(
        self,
        arg0: open3d.camera.PinholeCameraIntrinsic,
        arg1: Annotated[npt.NDArray[np.float64], (4, 4)],
        arg2: open3d.geometry.AxisAlignedBoundingBox,
    ) -> None: ...
    @property
    def center_of_rotation(self) -> Annotated[npt.NDArray[np.float32], (3, 1)]:
        """
        Current center of rotation (for ROTATE_CAMERA and ROTATE_CAMERA_SPHERE)

        :type: Annotated[npt.NDArray[np.float32], (3, 1)]
        """
    @center_of_rotation.setter
    def center_of_rotation(
        self, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        """
        Current center of rotation (for ROTATE_CAMERA and ROTATE_CAMERA_SPHERE)
        """
    @property
    def scene(self) -> open3d.visualization.rendering.Open3DScene:
        """
        The rendering.Open3DScene that the SceneWidget renders

        :type: open3d.visualization.rendering.Open3DScene
        """
    @scene.setter
    def scene(self, arg1: open3d.visualization.rendering.Open3DScene) -> None:
        """
        The rendering.Open3DScene that the SceneWidget renders
        """
    FLY: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.FLY: 2>
    PICK_POINTS: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.PICK_POINTS: 6>
    ROTATE_CAMERA: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_CAMERA: 0>
    ROTATE_CAMERA_SPHERE: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_CAMERA_SPHERE: 1>
    ROTATE_IBL: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_IBL: 4>
    ROTATE_MODEL: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_MODEL: 5>
    ROTATE_SUN: open3d.visualization.gui.SceneWidget.Controls  # value = <Controls.ROTATE_SUN: 3>
    pass

class ScrollableVert(Vert, Layout1D, Widget):
    """
    Scrollable vertical layout
    """

    @typing.overload
    def __init__(self, spacing: float = 0.0, margins: Margins = ...) -> None:
        """
        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the spacing between widgets, the second is the margins. Both default to 0.

        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the spacing between widgets, the second is the margins. Both default to 0.
        """
    @typing.overload
    def __init__(self, spacing: int = 0, margins: Margins = ...) -> None: ...
    pass

class Size:
    """
    Size object
    """

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def height(self) -> int:
        """
        :type: int
        """
    @height.setter
    def height(self, arg0: int) -> None:
        pass
    @property
    def width(self) -> int:
        """
        :type: int
        """
    @width.setter
    def width(self, arg0: int) -> None:
        pass
    pass

class Slider(Widget):
    """
    A slider widget for visually selecting numbers
    """

    class Type:
        """
        Enum class for Slider types.
        """

        def __and__(self, other: object) -> object: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> object: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: object) -> object: ...
        def __rand__(self, other: object) -> object: ...
        def __repr__(self) -> str: ...
        def __ror__(self, other: object) -> object: ...
        def __rxor__(self, other: object) -> object: ...
        def __setstate__(self, state: int) -> None: ...
        def __xor__(self, other: object) -> object: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        DOUBLE: open3d.visualization.gui.Slider.Type  # value = <Type.DOUBLE: 1>
        INT: open3d.visualization.gui.Slider.Type  # value = <Type.INT: 0>
        __members__: dict  # value = {'INT': <Type.INT: 0>, 'DOUBLE': <Type.DOUBLE: 1>}
        pass
    def __init__(self, arg0: Slider.Type) -> None:
        """
        Creates a NumberEdit that is either integers (INT) or floating point (DOUBLE). The initial value is 0 and the limits are +/- infinity.
        """
    def __repr__(self) -> str: ...
    def set_limits(self, arg0: float, arg1: float) -> None:
        """
        Sets the minimum and maximum values for the slider
        """
    def set_on_value_changed(self, arg0: typing.Callable[[float], None]) -> None:
        """
        Sets f(new_value) which is called with a Float when user changes widget's value
        """
    @property
    def double_value(self) -> float:
        """
        Slider value (double)

        :type: float
        """
    @double_value.setter
    def double_value(self, arg1: float) -> None:
        """
        Slider value (double)
        """
    @property
    def get_maximum_value(self) -> float:
        """
        The maximum value number can contain (read-only, use set_limits() to set)

        :type: float
        """
    @property
    def get_minimum_value(self) -> float:
        """
        The minimum value number can contain (read-only, use set_limits() to set)

        :type: float
        """
    @property
    def int_value(self) -> int:
        """
        Slider value (int)

        :type: int
        """
    @int_value.setter
    def int_value(self, arg1: int) -> None:
        """
        Slider value (int)
        """
    DOUBLE: open3d.visualization.gui.Slider.Type  # value = <Type.DOUBLE: 1>
    INT: open3d.visualization.gui.Slider.Type  # value = <Type.INT: 0>
    pass

class StackedWidget(Widget):
    """
    Like a TabControl but without the tabs
    """

    def __init__(self) -> None: ...
    @property
    def selected_index(self) -> int:
        """
        Selects the index of the child to display

        :type: int
        """
    @selected_index.setter
    def selected_index(self, arg1: int) -> None:
        """
        Selects the index of the child to display
        """
    pass

class TabControl(Widget):
    """
    Tab control
    """

    def __init__(self) -> None: ...
    def add_tab(self, arg0: str, arg1: Widget) -> None:
        """
        Adds a tab. The first parameter is the title of the tab, and the second parameter is a widget--normally this is a layout.
        """
    def set_on_selected_tab_changed(self, arg0: typing.Callable[[int], None]) -> None:
        """
        Calls the provided callback function with the index of the currently selected tab whenever the user clicks on a different tab
        """
    @property
    def selected_tab_index(self) -> int:
        """
        The index of the currently selected item

        :type: int
        """
    @selected_tab_index.setter
    def selected_tab_index(self, arg1: int) -> None:
        """
        The index of the currently selected item
        """
    pass

class TextEdit(Widget):
    """
    Allows the user to enter or modify text
    """

    def __init__(self) -> None:
        """
        Creates a TextEdit widget with an initial value of an empty string.
        """
    def __repr__(self) -> str: ...
    def set_on_text_changed(self, arg0: typing.Callable[[str], None]) -> None:
        """
        Sets f(new_text) which is called whenever the the user makes a change to the text
        """
    def set_on_value_changed(self, arg0: typing.Callable[[str], None]) -> None:
        """
        Sets f(new_text) which is called with the new text when the user completes text editing
        """
    @property
    def placeholder_text(self) -> str:
        """
        The placeholder text displayed when text value is empty

        :type: str
        """
    @placeholder_text.setter
    def placeholder_text(self, arg1: str) -> None:
        """
        The placeholder text displayed when text value is empty
        """
    @property
    def text_value(self) -> str:
        """
        The value of text

        :type: str
        """
    @text_value.setter
    def text_value(self, arg1: str) -> None:
        """
        The value of text
        """
    pass

class Theme:
    """
    Theme parameters such as colors used for drawing widgets (read-only)
    """

    @property
    def default_layout_spacing(self) -> int:
        """
        Good value for the spacing parameter in layouts (read-only)

        :type: int
        """
    @property
    def default_margin(self) -> int:
        """
        Good default value for margins, useful for layouts (read-only)

        :type: int
        """
    @property
    def font_size(self) -> int:
        """
        Font size (which is also the conventional size of the em unit) (read-only)

        :type: int
        """
    pass

class ToggleSwitch(Widget):
    """
    ToggleSwitch
    """

    def __init__(self, arg0: str) -> None:
        """
        Creates a toggle switch with the given text
        """
    def __repr__(self) -> str: ...
    def set_on_clicked(self, arg0: typing.Callable[[bool], None]) -> None:
        """
        Sets f(is_on) which is called when the switch changes state.
        """
    @property
    def is_on(self) -> bool:
        """
        True if is one, False otherwise

        :type: bool
        """
    @is_on.setter
    def is_on(self, arg1: bool) -> None:
        """
        True if is one, False otherwise
        """
    pass

class TreeView(Widget):
    """
    Hierarchical list
    """

    def __init__(self) -> None:
        """
        Creates an empty TreeView widget
        """
    def __repr__(self) -> str: ...
    def add_item(self, arg0: int, arg1: Widget) -> int:
        """
        Adds a child item to the parent. add_item(parent, widget)
        """
    def add_text_item(self, arg0: int, arg1: str) -> int:
        """
        Adds a child item to the parent. add_text_item(parent, text)
        """
    def clear(self) -> None:
        """
        Removes all items
        """
    def get_root_item(self) -> int:
        """
        Returns the root item. This item is invisible, so its child are the top-level items
        """
    def remove_item(self, arg0: int) -> None:
        """
        Removes an item and all its children (if any)
        """
    def set_on_selection_changed(self, arg0: typing.Callable[[int], None]) -> None:
        """
        Sets f(new_item_id) which is called when the user changes the selection.
        """
    @property
    def can_select_items_with_children(self) -> bool:
        """
        If set to False, clicking anywhere on an item with will toggle the item open or closed; the item cannot be selected. If set to True, items with children can be selected, and to toggle open/closed requires clicking the arrow or double-clicking the item

        :type: bool
        """
    @can_select_items_with_children.setter
    def can_select_items_with_children(self, arg1: bool) -> None:
        """
        If set to False, clicking anywhere on an item with will toggle the item open or closed; the item cannot be selected. If set to True, items with children can be selected, and to toggle open/closed requires clicking the arrow or double-clicking the item
        """
    @property
    def selected_item(self) -> int:
        """
        The currently selected item

        :type: int
        """
    @selected_item.setter
    def selected_item(self, arg1: int) -> None:
        """
        The currently selected item
        """
    pass

class UIImage:
    """
    A bitmap suitable for displaying with ImageWidget
    """

    class Scaling:
        """
        Members:

          NONE

          ANY

          ASPECT
        """

        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ANY: open3d.visualization.gui.UIImage.Scaling  # value = <Scaling.ANY: 1>
        ASPECT: open3d.visualization.gui.UIImage.Scaling  # value = <Scaling.ASPECT: 2>
        NONE: open3d.visualization.gui.UIImage.Scaling  # value = <Scaling.NONE: 0>
        __members__: dict  # value = {'NONE': <Scaling.NONE: 0>, 'ANY': <Scaling.ANY: 1>, 'ASPECT': <Scaling.ASPECT: 2>}
        pass
    @typing.overload
    def __init__(self, arg0: open3d.geometry.Image) -> None:
        """
        Creates a UIImage from the image at the specified path

        Creates a UIImage from the provided image
        """
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def scaling(self) -> UIImage.Scaling:
        """
        Sets how the image is scaled:
        gui.UIImage.Scaling.NONE: no scaling
        gui.UIImage.Scaling.ANY: scaled to fit
        gui.UIImage.Scaling.ASPECT: scaled to fit but keeping the image's aspect ratio

        :type: UIImage.Scaling
        """
    @scaling.setter
    def scaling(self, arg1: UIImage.Scaling) -> None:
        """
        Sets how the image is scaled:
        gui.UIImage.Scaling.NONE: no scaling
        gui.UIImage.Scaling.ANY: scaled to fit
        gui.UIImage.Scaling.ASPECT: scaled to fit but keeping the image's aspect ratio
        """
    pass

class VGrid(Widget):
    """
    Grid layout
    """

    @typing.overload
    def __init__(self, cols: int, spacing: float = 0.0, margins: Margins = ...) -> None:
        """
        Creates a layout that orders its children in a grid, left to right, top to bottom, according to the number of columns. The first argument is the number of columns, the second is the spacing between items (both vertically and horizontally), and third is the margins. Both spacing and margins default to zero.

        Creates a layout that orders its children in a grid, left to right, top to bottom, according to the number of columns. The first argument is the number of columns, the second is the spacing between items (both vertically and horizontally), and third is the margins. Both spacing and margins default to zero.
        """
    @typing.overload
    def __init__(self, cols: int, spacing: int = 0, margins: Margins = ...) -> None: ...
    @property
    def margins(self) -> Margins:
        """
        Returns the margins

        :type: Margins
        """
    @property
    def preferred_width(self) -> int:
        """
        Sets the preferred width of the layout

        :type: int
        """
    @preferred_width.setter
    def preferred_width(self, arg1: int) -> None:
        """
        Sets the preferred width of the layout
        """
    @property
    def spacing(self) -> int:
        """
        Returns the spacing between rows and columns

        :type: int
        """
    pass

class VectorEdit(Widget):
    """
    Allows the user to edit a 3-space vector
    """

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def set_on_value_changed(
        self, arg0: typing.Callable[[Annotated[npt.NDArray[np.float32], (3, 1)]], None]
    ) -> None:
        """
        Sets f([x, y, z]) which is called whenever the user changes the value of a component
        """
    @property
    def vector_value(self) -> Annotated[npt.NDArray[np.float32], (3, 1)]:
        """
        Returns value [x, y, z]

        :type: Annotated[npt.NDArray[np.float32], (3, 1)]
        """
    @vector_value.setter
    def vector_value(self, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]) -> None:
        """
        Returns value [x, y, z]
        """
    pass

class CollapsableVert(Vert, Layout1D, Widget):
    """
    Vertical layout with title, whose contents are collapsable
    """

    @typing.overload
    def __init__(self, text: str, spacing: float = 0.0, margins: Margins = ...) -> None:
        """
        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the heading text, the second is the spacing between widgets, and the third is the margins. Both the spacing and the margins default to 0.

        Creates a layout that arranges widgets vertically, top to bottom, making their width equal to the layout's width. First argument is the heading text, the second is the spacing between widgets, and the third is the margins. Both the spacing and the margins default to 0.
        """
    @typing.overload
    def __init__(self, text: str, spacing: int = 0, margins: Margins = ...) -> None: ...
    def get_is_open(self) -> bool:
        """
        Check if widget is open.
        """
    def set_is_open(self, is_open: bool) -> None:
        """
        Sets to collapsed (False) or open (True). Requires a call to Window.SetNeedsLayout() afterwards, unless calling before window is visible
        """
    @property
    def font_id(self) -> int:
        """
        Set the font using the FontId returned from Application.add_font()

        :type: int
        """
    @font_id.setter
    def font_id(self, arg1: int) -> None:
        """
        Set the font using the FontId returned from Application.add_font()
        """
    pass

class Button(Widget):
    """
    Button
    """

    def __init__(self, arg0: str) -> None:
        """
        Creates a button with the given text
        """
    def __repr__(self) -> str: ...
    def set_on_clicked(self, arg0: typing.Callable[[], None]) -> None:
        """
        Calls passed function when button is pressed
        """
    @property
    def horizontal_padding_em(self) -> float:
        """
        Horizontal padding in em units

        :type: float
        """
    @horizontal_padding_em.setter
    def horizontal_padding_em(self, arg1: object) -> None:
        """
        Horizontal padding in em units
        """
    @property
    def is_on(self) -> bool:
        """
        True if the button is toggleable and in the on state

        :type: bool
        """
    @is_on.setter
    def is_on(self, arg1: bool) -> None:
        """
        True if the button is toggleable and in the on state
        """
    @property
    def text(self) -> str:
        """
        Gets/sets the button text.

        :type: str
        """
    @text.setter
    def text(self, arg1: str) -> None:
        """
        Gets/sets the button text.
        """
    @property
    def toggleable(self) -> bool:
        """
        True if button is toggleable, False if a push button

        :type: bool
        """
    @toggleable.setter
    def toggleable(self, arg1: bool) -> None:
        """
        True if button is toggleable, False if a push button
        """
    @property
    def vertical_padding_em(self) -> float:
        """
        Vertical padding in em units

        :type: float
        """
    @vertical_padding_em.setter
    def vertical_padding_em(self, arg1: object) -> None:
        """
        Vertical padding in em units
        """
    pass

class WidgetProxy(Widget):
    """
    Widget container to delegate any widget dynamically. Widget can not be managed dynamically. Although it is allowed to add more child widgets, it's impossible to replace some child with new on or remove children. WidgetProxy is designed to solve this problem. When WidgetProxy is created, it's invisible and disabled, so it won't be drawn or layout, seeming like it does not exist. When a widget is set by  set_widget, all  Widget's APIs will be conducted to that child widget. It looks like WidgetProxy is that widget. At any time, a new widget could be set, to replace the old one. and the old widget will be destroyed. Due to the content changing after a new widget is set or cleared, a relayout of Window might be called after set_widget. The delegated widget could be retrieved by  get_widget in case  you need to access it directly, like get check status of a CheckBox. API other than  set_widget and get_widget has completely same functions as Widget.
    """

    def __init__(self) -> None:
        """
        Creates a widget proxy
        """
    def __repr__(self) -> str: ...
    def get_widget(self) -> Widget:
        """
        Retrieve current delegated widget.return instance of current delegated widget set by set_widget. An empty pointer will be returned if there is none.
        """
    def set_widget(self, arg0: Widget) -> None:
        """
        set a new widget to be delegated by this one. After set_widget, the previously delegated widget , will be abandon all calls to Widget's API will be  conducted to widget. Before any set_widget call,  this widget is invisible and disabled, seems it  does not exist because it won't be drawn or in a layout.
        """
    pass

class WidgetStack(WidgetProxy, Widget):
    """
    A widget stack saves all widgets pushed into by push_widget and always shows the top one. The WidgetStack is a subclass of WidgetProxy, in otherwords, the topmost widget will delegate itself to WidgetStack. pop_widget will remove the topmost widget and callback set by set_on_top taking the new topmost widget will be called. The WidgetStack disappears in GUI if there is no widget in stack.
    """

    def __init__(self) -> None:
        """
        Creates a widget stack. The widget stack without anywidget will not be shown in GUI until set_widget iscalled to push a widget.
        """
    def __repr__(self) -> str: ...
    def pop_widget(self) -> Widget:
        """
        pop the topmost widget in the stack. The new topmost widgetof stack will be the widget on the show in GUI.
        """
    def push_widget(self, arg0: Widget) -> None:
        """
        push a new widget onto the WidgetStack's stack, hiding whatever widget was there before and making the new widget visible.
        """
    def set_on_top(self, arg0: typing.Callable[[Widget], None]) -> None:
        """
        Callable[[widget] -> None], called while a widget becomes the topmost of stack after some widget is poppedout. It won't be called if a widget is pushed into stackby set_widget.
        """
    pass

class WindowBase:
    """
    Application window
    """

    pass

class Window(WindowBase):
    """
    Application window. Create with Application.instance.create_window().
    """

    def __repr__(self) -> str: ...
    def add_child(self, arg0: open3d.visualization.gui.Widget) -> None:
        """
        Adds a widget to the window
        """
    def close(self) -> None:
        """
        Closes the window and destroys it, unless an on_close callback cancels the close.
        """
    def close_dialog(self) -> None:
        """
        Closes the current dialog
        """
    def post_redraw(self) -> None:
        """
        Sends a redraw message to the OS message queue
        """
    def set_focus_widget(self, arg0: open3d.visualization.gui.Widget) -> None:
        """
        Makes specified widget have text focus
        """
    def set_needs_layout(self) -> None:
        """
        Flags window to re-layout
        """
    def set_on_close(self, arg0: typing.Callable[[], bool]) -> None:
        """
        Sets a callback that will be called when the window is closed. The callback is given no arguments and should return True to continue closing the window or False to cancel the close
        """
    def set_on_key(self, arg0: typing.Callable[[KeyEvent], bool]) -> None:
        """
        Sets a callback for key events. This callback is passed a KeyEvent object. The callback must return True to stop more dispatching or False to dispatchto focused widget
        """
    def set_on_layout(self, arg0: typing.Callable[[LayoutContext], None]) -> None:
        """
        Sets a callback function that manually sets the frames of children of the window. Callback function will be called with one argument: gui.LayoutContext
        """
    def set_on_menu_item_activated(
        self, arg0: int, arg1: typing.Callable[[], None]
    ) -> None:
        """
        Sets callback function for menu item:  callback()
        """
    def set_on_tick_event(self, arg0: typing.Callable[[], bool]) -> None:
        """
        Sets callback for tick event. Callback takes no arguments and must return True if a redraw is needed (that is, if any widget has changed in any fashion) or False if nothing has changed
        """
    def show(self, arg0: bool) -> None:
        """
        Shows or hides the window
        """
    def show_dialog(self, arg0: open3d.visualization.gui.Dialog) -> None:
        """
        Displays the dialog
        """
    def show_menu(self, arg0: bool) -> None: ...
    def show_message_box(self, arg0: str, arg1: str) -> None:
        """
        Displays a simple dialog with a title and message and okay button
        """
    def size_to_fit(self) -> None:
        """
        Sets the width and height of window to its preferred size
        """
    @property
    def content_rect(self) -> open3d.visualization.gui.Rect:
        """
        Returns the frame in device pixels, relative  to the window, which is available for widgets (read-only)

        :type: open3d.visualization.gui.Rect
        """
    @property
    def is_active_window(self) -> bool:
        """
        True if the window is currently the active window (read-only)

        :type: bool
        """
    @property
    def is_visible(self) -> bool:
        """
        True if window is visible (read-only)

        :type: bool
        """
    @property
    def os_frame(self) -> open3d.visualization.gui.Rect:
        """
        Window rect in OS coords, not device pixels

        :type: open3d.visualization.gui.Rect
        """
    @os_frame.setter
    def os_frame(self, arg1: open3d.visualization.gui.Rect) -> None:
        """
        Window rect in OS coords, not device pixels
        """
    @property
    def renderer(self) -> open3d.visualization.rendering.Renderer:
        """
        Gets the rendering.Renderer object for the Window

        :type: open3d.visualization.rendering.Renderer
        """
    @property
    def scaling(self) -> float:
        """
        Returns the scaling factor between OS pixels and device pixels (read-only)

        :type: float
        """
    @property
    def size(self) -> open3d.visualization.gui.Size:
        """
        The size of the window in device pixels, including menubar (except on macOS)

        :type: open3d.visualization.gui.Size
        """
    @size.setter
    def size(self, arg1: open3d.visualization.gui.Size) -> None:
        """
        The size of the window in device pixels, including menubar (except on macOS)
        """
    @property
    def theme(self) -> open3d.visualization.gui.Theme:
        """
        Get's window's theme info

        :type: open3d.visualization.gui.Theme
        """
    @property
    def title(self) -> str:
        """
        Returns the title of the window

        :type: str
        """
    @title.setter
    def title(self, arg1: str) -> None:
        """
        Returns the title of the window
        """
    pass

A: open3d.visualization.gui.KeyName  # value = <KeyName.A: 97>
ALT: open3d.visualization.gui.KeyName  # value = <KeyName.ALT: 260>
AMPERSAND: open3d.visualization.gui.KeyName  # value = <KeyName.AMPERSAND: 38>
ASTERISK: open3d.visualization.gui.KeyName  # value = <KeyName.ASTERISK: 42>
AT: open3d.visualization.gui.KeyName  # value = <KeyName.AT: 64>
B: open3d.visualization.gui.KeyName  # value = <KeyName.B: 98>
BACKSLASH: open3d.visualization.gui.KeyName  # value = <KeyName.BACKSLASH: 92>
BACKSPACE: open3d.visualization.gui.KeyName  # value = <KeyName.BACKSPACE: 8>
BACKTICK: open3d.visualization.gui.KeyName  # value = <KeyName.BACKTICK: 96>
BUTTON4: open3d.visualization.gui.MouseButton  # value = <MouseButton.BUTTON4: 8>
BUTTON5: open3d.visualization.gui.MouseButton  # value = <MouseButton.BUTTON5: 16>
C: open3d.visualization.gui.KeyName  # value = <KeyName.C: 99>
CAPS_LOCK: open3d.visualization.gui.KeyName  # value = <KeyName.CAPS_LOCK: 262>
CARET: open3d.visualization.gui.KeyName  # value = <KeyName.CARET: 94>
COLON: open3d.visualization.gui.KeyName  # value = <KeyName.COLON: 58>
COMMA: open3d.visualization.gui.KeyName  # value = <KeyName.COMMA: 44>
CTRL: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.CTRL: 2>
D: open3d.visualization.gui.KeyName  # value = <KeyName.D: 100>
DELETE: open3d.visualization.gui.KeyName  # value = <KeyName.DELETE: 127>
DOLLAR_SIGN: open3d.visualization.gui.KeyName  # value = <KeyName.DOLLAR_SIGN: 36>
DOUBLE_QUOTE: open3d.visualization.gui.KeyName  # value = <KeyName.DOUBLE_QUOTE: 34>
DOWN: open3d.visualization.gui.KeyName  # value = <KeyName.DOWN: 266>
E: open3d.visualization.gui.KeyName  # value = <KeyName.E: 101>
EIGHT: open3d.visualization.gui.KeyName  # value = <KeyName.EIGHT: 56>
END: open3d.visualization.gui.KeyName  # value = <KeyName.END: 269>
ENTER: open3d.visualization.gui.KeyName  # value = <KeyName.ENTER: 10>
EQUALS: open3d.visualization.gui.KeyName  # value = <KeyName.EQUALS: 61>
ESCAPE: open3d.visualization.gui.KeyName  # value = <KeyName.ESCAPE: 27>
EXCLAMATION_MARK: open3d.visualization.gui.KeyName  # value = <KeyName.EXCLAMATION_MARK: 33>
F: open3d.visualization.gui.KeyName  # value = <KeyName.F: 102>
F1: open3d.visualization.gui.KeyName  # value = <KeyName.F1: 290>
F10: open3d.visualization.gui.KeyName  # value = <KeyName.F10: 299>
F11: open3d.visualization.gui.KeyName  # value = <KeyName.F11: 300>
F12: open3d.visualization.gui.KeyName  # value = <KeyName.F12: 301>
F2: open3d.visualization.gui.KeyName  # value = <KeyName.F2: 291>
F3: open3d.visualization.gui.KeyName  # value = <KeyName.F3: 292>
F4: open3d.visualization.gui.KeyName  # value = <KeyName.F4: 293>
F5: open3d.visualization.gui.KeyName  # value = <KeyName.F5: 294>
F6: open3d.visualization.gui.KeyName  # value = <KeyName.F6: 295>
F7: open3d.visualization.gui.KeyName  # value = <KeyName.F7: 296>
F8: open3d.visualization.gui.KeyName  # value = <KeyName.F8: 297>
F9: open3d.visualization.gui.KeyName  # value = <KeyName.F9: 298>
FIVE: open3d.visualization.gui.KeyName  # value = <KeyName.FIVE: 53>
FOUR: open3d.visualization.gui.KeyName  # value = <KeyName.FOUR: 52>
G: open3d.visualization.gui.KeyName  # value = <KeyName.G: 103>
GREATER_THAN: open3d.visualization.gui.KeyName  # value = <KeyName.GREATER_THAN: 62>
H: open3d.visualization.gui.KeyName  # value = <KeyName.H: 104>
HASH: open3d.visualization.gui.KeyName  # value = <KeyName.HASH: 35>
HOME: open3d.visualization.gui.KeyName  # value = <KeyName.HOME: 268>
I: open3d.visualization.gui.KeyName  # value = <KeyName.I: 105>
INSERT: open3d.visualization.gui.KeyName  # value = <KeyName.INSERT: 267>
J: open3d.visualization.gui.KeyName  # value = <KeyName.J: 106>
K: open3d.visualization.gui.KeyName  # value = <KeyName.K: 107>
L: open3d.visualization.gui.KeyName  # value = <KeyName.L: 108>
LEFT: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT: 263>
LEFT_BRACE: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_BRACE: 123>
LEFT_BRACKET: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_BRACKET: 91>
LEFT_CONTROL: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_CONTROL: 258>
LEFT_PAREN: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_PAREN: 40>
LEFT_SHIFT: open3d.visualization.gui.KeyName  # value = <KeyName.LEFT_SHIFT: 256>
LESS_THAN: open3d.visualization.gui.KeyName  # value = <KeyName.LESS_THAN: 60>
M: open3d.visualization.gui.KeyName  # value = <KeyName.M: 109>
META: open3d.visualization.gui.KeyName  # value = <KeyName.META: 261>
MIDDLE: open3d.visualization.gui.MouseButton  # value = <MouseButton.MIDDLE: 2>
MINUS: open3d.visualization.gui.KeyName  # value = <KeyName.MINUS: 45>
N: open3d.visualization.gui.KeyName  # value = <KeyName.N: 110>
NINE: open3d.visualization.gui.KeyName  # value = <KeyName.NINE: 57>
NONE: open3d.visualization.gui.KeyName  # value = <KeyName.NONE: 0>
O: open3d.visualization.gui.KeyName  # value = <KeyName.O: 111>
ONE: open3d.visualization.gui.KeyName  # value = <KeyName.ONE: 49>
P: open3d.visualization.gui.KeyName  # value = <KeyName.P: 112>
PAGE_DOWN: open3d.visualization.gui.KeyName  # value = <KeyName.PAGE_DOWN: 271>
PAGE_UP: open3d.visualization.gui.KeyName  # value = <KeyName.PAGE_UP: 270>
PERCENT: open3d.visualization.gui.KeyName  # value = <KeyName.PERCENT: 37>
PERIOD: open3d.visualization.gui.KeyName  # value = <KeyName.PERIOD: 46>
PIPE: open3d.visualization.gui.KeyName  # value = <KeyName.PIPE: 124>
PLUS: open3d.visualization.gui.KeyName  # value = <KeyName.PLUS: 43>
Q: open3d.visualization.gui.KeyName  # value = <KeyName.Q: 113>
QUESTION_MARK: open3d.visualization.gui.KeyName  # value = <KeyName.QUESTION_MARK: 63>
QUOTE: open3d.visualization.gui.KeyName  # value = <KeyName.QUOTE: 39>
R: open3d.visualization.gui.KeyName  # value = <KeyName.R: 114>
RIGHT: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT: 264>
RIGHT_BRACE: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_BRACE: 125>
RIGHT_BRACKET: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_BRACKET: 93>
RIGHT_CONTROL: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_CONTROL: 259>
RIGHT_PAREN: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_PAREN: 41>
RIGHT_SHIFT: open3d.visualization.gui.KeyName  # value = <KeyName.RIGHT_SHIFT: 257>
S: open3d.visualization.gui.KeyName  # value = <KeyName.S: 115>
SEMICOLON: open3d.visualization.gui.KeyName  # value = <KeyName.SEMICOLON: 59>
SEVEN: open3d.visualization.gui.KeyName  # value = <KeyName.SEVEN: 55>
SHIFT: open3d.visualization.gui.KeyModifier  # value = <KeyModifier.SHIFT: 1>
SIX: open3d.visualization.gui.KeyName  # value = <KeyName.SIX: 54>
SLASH: open3d.visualization.gui.KeyName  # value = <KeyName.SLASH: 47>
SPACE: open3d.visualization.gui.KeyName  # value = <KeyName.SPACE: 32>
T: open3d.visualization.gui.KeyName  # value = <KeyName.T: 116>
TAB: open3d.visualization.gui.KeyName  # value = <KeyName.TAB: 9>
THREE: open3d.visualization.gui.KeyName  # value = <KeyName.THREE: 51>
TILDE: open3d.visualization.gui.KeyName  # value = <KeyName.TILDE: 126>
TWO: open3d.visualization.gui.KeyName  # value = <KeyName.TWO: 50>
U: open3d.visualization.gui.KeyName  # value = <KeyName.U: 117>
UNDERSCORE: open3d.visualization.gui.KeyName  # value = <KeyName.UNDERSCORE: 95>
UNKNOWN: open3d.visualization.gui.KeyName  # value = <KeyName.UNKNOWN: 1000>
UP: open3d.visualization.gui.KeyName  # value = <KeyName.UP: 265>
V: open3d.visualization.gui.KeyName  # value = <KeyName.V: 118>
W: open3d.visualization.gui.KeyName  # value = <KeyName.W: 119>
X: open3d.visualization.gui.KeyName  # value = <KeyName.X: 120>
Y: open3d.visualization.gui.KeyName  # value = <KeyName.Y: 121>
Z: open3d.visualization.gui.KeyName  # value = <KeyName.Z: 122>
ZERO: open3d.visualization.gui.KeyName  # value = <KeyName.ZERO: 48>
