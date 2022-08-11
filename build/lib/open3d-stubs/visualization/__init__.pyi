from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.camera
import open3d.geometry
import open3d.t.geometry
import open3d.utility
import open3d.visualization
import open3d.visualization.gui
import typing_extensions
from typing_extensions import Annotated

from . import app, gui, rendering, webrtc_server

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Color",
    "Default",
    "Material",
    "MeshColorOption",
    "MeshShadeOption",
    "Normal",
    "O3DVisualizer",
    "PickedPoint",
    "PointColorOption",
    "RenderOption",
    "ScalarProperties",
    "SelectedIndex",
    "SelectionPolygonVolume",
    "TextureMaps",
    "VectorProperties",
    "ViewControl",
    "Visualizer",
    "VisualizerWithEditing",
    "VisualizerWithKeyCallback",
    "VisualizerWithVertexSelection",
    "XCoordinate",
    "YCoordinate",
    "ZCoordinate",
    "app",
    "draw_geometries",
    "draw_geometries_with_animation_callback",
    "draw_geometries_with_custom_animation",
    "draw_geometries_with_editing",
    "draw_geometries_with_key_callbacks",
    "draw_geometries_with_vertex_selection",
    "gui",
    "read_selection_polygon_volume",
    "rendering",
    "webrtc_server",
]

class Material:
    """
    Properties (texture maps, scalar and vector) related to visualization. Materials are optionally set for 3D geometries such as TriangleMesh, LineSets, and PointClouds
    """

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: Material) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def is_valid(self) -> bool:
        """
        Returns false if material is an empty material
        """
    def set_default_properties(self) -> None:
        """
        Fills material with defaults for common PBR material properties used by Open3D
        """
    @property
    def material_name(self) -> str:
        """
        :type: str
        """
    @material_name.setter
    def material_name(self, arg1: str) -> None:
        pass
    @property
    def scalar_properties(self) -> ScalarProperties:
        """
        :type: ScalarProperties
        """
    @property
    def texture_maps(self) -> TextureMaps:
        """
        :type: TextureMaps
        """
    @property
    def vector_properties(self) -> VectorProperties:
        """
        :type: VectorProperties
        """
    pass

class MeshColorOption:
    """
    Enum class for color for ``TriangleMesh``.
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
    Color: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Color: 1>
    Default: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Default: 0>
    Normal: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Normal: 9>
    XCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.XCoordinate: 2>
    YCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.YCoordinate: 3>
    ZCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.ZCoordinate: 4>
    __members__: dict  # value = {'Default': <MeshColorOption.Default: 0>, 'Color': <MeshColorOption.Color: 1>, 'XCoordinate': <MeshColorOption.XCoordinate: 2>, 'YCoordinate': <MeshColorOption.YCoordinate: 3>, 'ZCoordinate': <MeshColorOption.ZCoordinate: 4>, 'Normal': <MeshColorOption.Normal: 9>}
    pass

class MeshShadeOption:
    """
    Enum class for mesh shading for ``TriangleMesh``.
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
    Color: open3d.visualization.MeshShadeOption  # value = <MeshShadeOption.Color: 1>
    Default: open3d.visualization.MeshShadeOption  # value = <MeshShadeOption.Default: 0>
    __members__: dict  # value = {'Default': <MeshShadeOption.Default: 0>, 'Color': <MeshShadeOption.Color: 1>}
    pass

class O3DVisualizer(open3d.visualization.gui.WindowBase):
    """
    Visualization object used by draw()
    """

    class DrawObject:
        """
        Information about an object that is drawn. Do not modify this, it can lead to unexpected results.
        """

        @property
        def geometry(self) -> object:
            """
            The geometry. Modifying this will not result in any visible change. Use remove_geometry() and then add_geometry()to change the geometry

            :type: object
            """
        @property
        def group(self) -> str:
            """
            The group that the object belongs to

            :type: str
            """
        @property
        def is_visible(self) -> bool:
            """
            True if the object is checked in the list. If the object's group is unchecked or an animation is playing, the object's visibility may not correspond with this value

            :type: bool
            """
        @property
        def name(self) -> str:
            """
            The name of the object

            :type: str
            """
        @property
        def time(self) -> float:
            """
            The object's timestamp

            :type: float
            """
        pass

    class Shader:
        """
        Scene-level rendering options

        Members:

          STANDARD : Pixel colors from standard lighting model

          UNLIT : Normals will be ignored (useful for point clouds)

          NORMALS : Pixel colors correspond to surface normal

          DEPTH : Pixel colors correspond to depth buffer value
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
        DEPTH: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.DEPTH: 3>
        NORMALS: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.NORMALS: 2>
        STANDARD: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.STANDARD: 0>
        UNLIT: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.UNLIT: 1>
        __members__: dict  # value = {'STANDARD': <Shader.STANDARD: 0>, 'UNLIT': <Shader.UNLIT: 1>, 'NORMALS': <Shader.NORMALS: 2>, 'DEPTH': <Shader.DEPTH: 3>}
        pass

    class TickResult:
        """
        Return value from animation tick callback

        Members:

          NO_CHANGE : Signals that no change happened and no redraw is required

          REDRAW : Signals that a redraw is required
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
        NO_CHANGE: open3d.visualization.O3DVisualizer.TickResult  # value = <TickResult.NO_CHANGE: 0>
        REDRAW: open3d.visualization.O3DVisualizer.TickResult  # value = <TickResult.REDRAW: 1>
        __members__: dict  # value = {'NO_CHANGE': <TickResult.NO_CHANGE: 0>, 'REDRAW': <TickResult.REDRAW: 1>}
        pass
    def __init__(
        self, title: str = "Open3D", width: int = 1024, height: int = 768
    ) -> None:
        """
        Creates a O3DVisualizer object
        """
    def add_3d_label(
        self, arg0: Annotated[npt.NDArray[np.float32], (3, 1)], arg1: str
    ) -> None: ...
    def add_action(
        self, arg0: str, arg1: typing.Callable[[O3DVisualizer], None]
    ) -> None:
        """
        Adds a button to the custom actions section of the UI and a corresponding menu item in the "Actions" menu. add_action(name, callback). The callback will be given one parameter, the O3DVisualizer instance, and does not return any value.
        """
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.geometry.Geometry3D,
        material: open3d.visualization.rendering.MaterialRecord = None,
        group: str = "",
        time: float = 0.0,
        is_visible: bool = True,
    ) -> None:
        """
        Adds a geometry: add_geometry(name, geometry, material=None, group='', time=0.0, is_visible=True). 'name' must be unique.

        Adds a Tensor-based add_geometry: geometry(name, geometry, material=None, group='', time=0.0, is_visible=True). 'name' must be unique.

        Adds a TriangleMeshModel: add_geometry(name, model, material=None, group='', time=0.0, is_visible=True). 'name' must be unique. 'material' is ignored.

        Adds a geometry from a dictionary. The dictionary has the following elements:
        name: unique name of the object (required)
        geometry: the geometry or t.geometry object (required)
        material: a visualization.rendering.Material object (optional)
        group: a string declaring the group it is a member of (optional)
        time: a time value
        """
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.t.geometry.Geometry,
        material: open3d.visualization.rendering.MaterialRecord = None,
        group: str = "",
        time: float = 0.0,
        is_visible: bool = True,
    ) -> None: ...
    @typing.overload
    def add_geometry(
        self,
        name: str,
        model: open3d.visualization.rendering.TriangleMeshModel,
        material: open3d.visualization.rendering.MaterialRecord = None,
        group: str = "",
        time: float = 0.0,
        is_visible: bool = True,
    ) -> None: ...
    @typing.overload
    def add_geometry(self, arg0: dict) -> None: ...
    def clear_3d_labels(self) -> None:
        """
        Clears all 3D text
        """
    def close(self) -> None:
        """
        Closes the window and destroys it, unless an on_close callback cancels the close.
        """
    def close_dialog(self) -> None:
        """
        Closes the current dialog
        """
    def enable_raw_mode(self, arg0: bool) -> None: ...
    def export_current_image(self, arg0: str) -> None: ...
    def get_geometry(self, arg0: str) -> O3DVisualizer.DrawObject: ...
    def get_geometry_material(
        self, arg0: str
    ) -> open3d.visualization.rendering.MaterialRecord: ...
    def get_selection_sets(
        self,
    ) -> typing.List[typing.Dict[str, typing.Set[SelectedIndex]]]:
        """
        Returns the selection sets, as [{'obj_name', [SelectedIndex]}]
        """
    def modify_geometry_material(
        self, arg0: str, arg1: open3d.visualization.rendering.MaterialRecord
    ) -> None: ...
    def post_redraw(self) -> None:
        """
        Tells the window to redraw
        """
    def remove_geometry(self, arg0: str) -> None: ...
    def reset_camera_to_default(self) -> None:
        """
        Sets camera to default position
        """
    def set_background(
        self,
        arg0: Annotated[npt.NDArray[np.float32], (4, 1)],
        arg1: open3d.geometry.Image,
    ) -> None: ...
    def set_ibl(self, arg0: str) -> None: ...
    def set_ibl_intensity(self, arg0: float) -> None: ...
    def set_on_animation_frame(
        self, arg0: typing.Callable[[O3DVisualizer, float], None]
    ) -> None: ...
    def set_on_animation_tick(
        self,
        arg0: typing.Callable[[O3DVisualizer, float, float], O3DVisualizer.TickResult],
    ) -> None: ...
    def set_on_close(self, arg0: typing.Callable[[], bool]) -> None:
        """
        Sets a callback that will be called when the window is closed. The callback is given no arguments and should return True to continue closing the window or False to cancel the close
        """
    @typing.overload
    def setup_camera(
        self,
        arg0: Annotated[npt.NDArray[np.float64], (3, 3)],
        arg1: Annotated[npt.NDArray[np.float64], (4, 4)],
        arg2: int,
        arg3: int,
    ) -> None: ...
    @typing.overload
    def setup_camera(
        self,
        arg0: float,
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg3: Annotated[npt.NDArray[np.float32], (3, 1)],
    ) -> None: ...
    @typing.overload
    def setup_camera(
        self,
        arg0: open3d.camera.PinholeCameraIntrinsic,
        arg1: Annotated[npt.NDArray[np.float64], (4, 4)],
    ) -> None: ...
    def show(self, arg0: bool) -> None:
        """
        Shows or hides the window
        """
    def show_dialog(self, arg0: open3d.visualization.gui.Dialog) -> None:
        """
        Displays the dialog
        """
    def show_geometry(self, arg0: str, arg1: bool) -> None:
        """
        Checks or unchecks the named geometry in the list. Note that even if show_geometry(name, True) is called, the object may not actually be visible if its group is unchecked, or if an animation is in progress.
        """
    def show_menu(self, arg0: bool) -> None: ...
    def show_message_box(self, arg0: str, arg1: str) -> None:
        """
        Displays a simple dialog with a title and message and okay button
        """
    def show_skybox(self, arg0: bool) -> None:
        """
        Show/Hide the skybox
        """
    def size_to_fit(self) -> None:
        """
        Sets the width and height of window to its preferred size
        """
    def start_rpc_interface(self, address: str, timeout: int) -> None:
        """
        Starts the RPC interface.
        address: str with the address to listen on.
        timeout: int timeout in milliseconds for sending the reply.
        """
    def stop_rpc_interface(self) -> None:
        """
        Stops the RPC interface.
        """
    def update_geometry(
        self, arg0: str, arg1: open3d.t.geometry.Geometry, arg2: int
    ) -> None: ...
    @property
    def animation_duration(self) -> float:
        """
        Gets/sets the duration (in seconds) of the animation. This is automatically computed to be the difference between the minimum and maximum time values, but this is useful if no time values have been specified (that is, all objects are at the default t=0)

        :type: float
        """
    @animation_duration.setter
    def animation_duration(self, arg1: float) -> None:
        """
        Gets/sets the duration (in seconds) of the animation. This is automatically computed to be the difference between the minimum and maximum time values, but this is useful if no time values have been specified (that is, all objects are at the default t=0)
        """
    @property
    def animation_frame_delay(self) -> float:
        """
        Gets/sets the length of time a frame is visible.

        :type: float
        """
    @animation_frame_delay.setter
    def animation_frame_delay(self, arg1: float) -> None:
        """
        Gets/sets the length of time a frame is visible.
        """
    @property
    def animation_time_step(self) -> float:
        """
        Gets/sets the time step for animations. Default is 1.0 sec

        :type: float
        """
    @animation_time_step.setter
    def animation_time_step(self, arg1: float) -> None:
        """
        Gets/sets the time step for animations. Default is 1.0 sec
        """
    @property
    def content_rect(self) -> open3d.visualization.gui.Rect:
        """
        Returns the frame in device pixels, relative  to the window, which is available for widgets (read-only)

        :type: open3d.visualization.gui.Rect
        """
    @property
    def current_time(self) -> float:
        """
        Gets/sets the current time. If setting, only the objects belonging to the current time-step will be displayed

        :type: float
        """
    @current_time.setter
    def current_time(self, arg1: float) -> None:
        """
        Gets/sets the current time. If setting, only the objects belonging to the current time-step will be displayed
        """
    @property
    def ground_plane(self) -> open3d.visualization.rendering.Scene.GroundPlane:
        """
        Sets the plane for ground plane, XZ, XY, or YZ

        :type: open3d.visualization.rendering.Scene.GroundPlane
        """
    @ground_plane.setter
    def ground_plane(
        self, arg1: open3d.visualization.rendering.Scene.GroundPlane
    ) -> None:
        """
        Sets the plane for ground plane, XZ, XY, or YZ
        """
    @property
    def is_animating(self) -> bool:
        """
        Gets/sets the status of the animation. Changing value will start or stop the animating.

        :type: bool
        """
    @is_animating.setter
    def is_animating(self, arg1: bool) -> None:
        """
        Gets/sets the status of the animation. Changing value will start or stop the animating.
        """
    @property
    def is_visible(self) -> bool:
        """
        True if window is visible (read-only)

        :type: bool
        """
    @property
    def line_width(self) -> int:
        """
        Gets/sets width of lines (in units of pixels)

        :type: int
        """
    @line_width.setter
    def line_width(self, arg1: int) -> None:
        """
        Gets/sets width of lines (in units of pixels)
        """
    @property
    def mouse_mode(self) -> open3d.visualization.gui.SceneWidget.Controls:
        """
        Gets/sets the control mode being used for the mouse

        :type: open3d.visualization.gui.SceneWidget.Controls
        """
    @mouse_mode.setter
    def mouse_mode(self, arg1: open3d.visualization.gui.SceneWidget.Controls) -> None:
        """
        Gets/sets the control mode being used for the mouse
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
    def point_size(self) -> int:
        """
        Gets/sets size of points (in units of pixels)

        :type: int
        """
    @point_size.setter
    def point_size(self, arg1: int) -> None:
        """
        Gets/sets size of points (in units of pixels)
        """
    @property
    def scaling(self) -> float:
        """
        Returns the scaling factor between OS pixels and device pixels (read-only)

        :type: float
        """
    @property
    def scene(self) -> open3d.visualization.rendering.Open3DScene:
        """
        Returns the rendering.Open3DScene object for low-level manipulation

        :type: open3d.visualization.rendering.Open3DScene
        """
    @property
    def scene_shader(self) -> O3DVisualizer.Shader:
        """
        Gets/sets the shading model for the scene

        :type: O3DVisualizer.Shader
        """
    @scene_shader.setter
    def scene_shader(self, arg1: O3DVisualizer.Shader) -> None:
        """
        Gets/sets the shading model for the scene
        """
    @property
    def show_axes(self) -> bool:
        """
        Gets/sets if axes are visible

        :type: bool
        """
    @show_axes.setter
    def show_axes(self, arg1: bool) -> None:
        """
        Gets/sets if axes are visible
        """
    @property
    def show_ground(self) -> bool:
        """
        Gets/sets if ground plane is visible

        :type: bool
        """
    @show_ground.setter
    def show_ground(self, arg1: bool) -> None:
        """
        Gets/sets if ground plane is visible
        """
    @property
    def show_settings(self) -> bool:
        """
        Gets/sets if settings panel is visible

        :type: bool
        """
    @show_settings.setter
    def show_settings(self, arg1: bool) -> None:
        """
        Gets/sets if settings panel is visible
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
    @property
    def uid(self) -> str:
        """
        Window's unique ID when WebRTCWindowSystem is use.Returns 'window_undefined' otherwise.

        :type: str
        """
    DEPTH: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.DEPTH: 3>
    NORMALS: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.NORMALS: 2>
    STANDARD: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.STANDARD: 0>
    UNLIT: open3d.visualization.O3DVisualizer.Shader  # value = <Shader.UNLIT: 1>
    pass

class PickedPoint:
    def __init__(self) -> None: ...
    @property
    def coord(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @coord.setter
    def coord(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        pass
    @property
    def index(self) -> int:
        """
        :type: int
        """
    @index.setter
    def index(self, arg0: int) -> None:
        pass
    pass

class PointColorOption:
    """
    Enum class for point color for ``PointCloud``.
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
    Color: open3d.visualization.PointColorOption  # value = <PointColorOption.Color: 1>
    Default: open3d.visualization.PointColorOption  # value = <PointColorOption.Default: 0>
    Normal: open3d.visualization.PointColorOption  # value = <PointColorOption.Normal: 9>
    XCoordinate: open3d.visualization.PointColorOption  # value = <PointColorOption.XCoordinate: 2>
    YCoordinate: open3d.visualization.PointColorOption  # value = <PointColorOption.YCoordinate: 3>
    ZCoordinate: open3d.visualization.PointColorOption  # value = <PointColorOption.ZCoordinate: 4>
    __members__: dict  # value = {'Default': <PointColorOption.Default: 0>, 'Color': <PointColorOption.Color: 1>, 'XCoordinate': <PointColorOption.XCoordinate: 2>, 'YCoordinate': <PointColorOption.YCoordinate: 3>, 'ZCoordinate': <PointColorOption.ZCoordinate: 4>, 'Normal': <PointColorOption.Normal: 9>}
    pass

class RenderOption:
    """
    Defines rendering options for visualizer.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    @property
    def background_color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        float numpy array of size ``(3,)``: Background RGB color.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @background_color.setter
    def background_color(
        self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> None:
        """
        float numpy array of size ``(3,)``: Background RGB color.
        """
    @property
    def light_on(self) -> bool:
        """
        bool: Whether to turn on Phong lighting.

        :type: bool
        """
    @light_on.setter
    def light_on(self, arg0: bool) -> None:
        """
        bool: Whether to turn on Phong lighting.
        """
    @property
    def line_width(self) -> float:
        """
        float: Line width for ``LineSet``.

        :type: float
        """
    @line_width.setter
    def line_width(self, arg0: float) -> None:
        """
        float: Line width for ``LineSet``.
        """
    @property
    def mesh_color_option(self) -> open3d.visualization.MeshColorOption:
        """
        ``MeshColorOption``: Color option for ``TriangleMesh``.

        :type: open3d.visualization.MeshColorOption
        """
    @mesh_color_option.setter
    def mesh_color_option(self, arg0: open3d.visualization.MeshColorOption) -> None:
        """
        ``MeshColorOption``: Color option for ``TriangleMesh``.
        """
    @property
    def mesh_shade_option(self) -> open3d.visualization.MeshShadeOption:
        """
        ``MeshShadeOption``: Mesh shading option for ``TriangleMesh``.

        :type: open3d.visualization.MeshShadeOption
        """
    @mesh_shade_option.setter
    def mesh_shade_option(self, arg0: open3d.visualization.MeshShadeOption) -> None:
        """
        ``MeshShadeOption``: Mesh shading option for ``TriangleMesh``.
        """
    @property
    def mesh_show_back_face(self) -> bool:
        """
        bool: Whether to show back faces for ``TriangleMesh``.

        :type: bool
        """
    @mesh_show_back_face.setter
    def mesh_show_back_face(self, arg0: bool) -> None:
        """
        bool: Whether to show back faces for ``TriangleMesh``.
        """
    @property
    def mesh_show_wireframe(self) -> bool:
        """
        bool: Whether to show wireframe for ``TriangleMesh``.

        :type: bool
        """
    @mesh_show_wireframe.setter
    def mesh_show_wireframe(self, arg0: bool) -> None:
        """
        bool: Whether to show wireframe for ``TriangleMesh``.
        """
    @property
    def point_color_option(self) -> open3d.visualization.PointColorOption:
        """
        ``PointColorOption``: Point color option for ``PointCloud``.

        :type: open3d.visualization.PointColorOption
        """
    @point_color_option.setter
    def point_color_option(self, arg0: open3d.visualization.PointColorOption) -> None:
        """
        ``PointColorOption``: Point color option for ``PointCloud``.
        """
    @property
    def point_show_normal(self) -> bool:
        """
        bool: Whether to show normal for ``PointCloud``.

        :type: bool
        """
    @point_show_normal.setter
    def point_show_normal(self, arg0: bool) -> None:
        """
        bool: Whether to show normal for ``PointCloud``.
        """
    @property
    def point_size(self) -> float:
        """
        float: Point size for ``PointCloud``.

        :type: float
        """
    @point_size.setter
    def point_size(self, arg0: float) -> None:
        """
        float: Point size for ``PointCloud``.
        """
    @property
    def show_coordinate_frame(self) -> bool:
        """
        bool: Whether to show coordinate frame.

        :type: bool
        """
    @show_coordinate_frame.setter
    def show_coordinate_frame(self, arg0: bool) -> None:
        """
        bool: Whether to show coordinate frame.
        """
    pass

class ScalarProperties:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> float: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this map.
        """
    def __setitem__(self, arg0: str, arg1: float) -> None: ...
    def items(self) -> typing.Iterator: ...
    pass

class SelectedIndex:
    """
    Information about a point or vertex that was selected
    """

    def __repr__(self) -> str: ...
    @property
    def index(self) -> int:
        """
        The index of this point in the point/vertex array

        :type: int
        """
    @property
    def order(self) -> int:
        """
        A monotonically increasing value that can be used to determine in what order the points were selected

        :type: int
        """
    @property
    def point(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    pass

class SelectionPolygonVolume:
    """
    Select a polygon volume for cropping.
    """

    def __copy__(self) -> SelectionPolygonVolume: ...
    def __deepcopy__(self, arg0: dict) -> SelectionPolygonVolume: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: SelectionPolygonVolume) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def axis_max(self) -> float:
        """
        float: Maximum axis value.

        :type: float
        """
    @axis_max.setter
    def axis_max(self, arg0: float) -> None:
        """
        float: Maximum axis value.
        """
    @property
    def axis_min(self) -> float:
        """
        float: Minimum axis value.

        :type: float
        """
    @axis_min.setter
    def axis_min(self, arg0: float) -> None:
        """
        float: Minimum axis value.
        """
    @property
    def bounding_polygon(self) -> open3d.utility.Vector3dVector:
        """
        ``(n, 3)`` float64 numpy array: Bounding polygon boundary.

        :type: open3d.utility.Vector3dVector
        """
    @bounding_polygon.setter
    def bounding_polygon(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``(n, 3)`` float64 numpy array: Bounding polygon boundary.
        """
    @property
    def orthogonal_axis(self) -> str:
        """
        string: one of ``{x, y, z}``.

        :type: str
        """
    @orthogonal_axis.setter
    def orthogonal_axis(self, arg0: str) -> None:
        """
        string: one of ``{x, y, z}``.
        """
    pass

class TextureMaps:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> open3d.t.geometry.Image: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: open3d.t.geometry.Image) -> None: ...
    def items(self) -> typing.Iterator: ...
    pass

class VectorProperties:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> Annotated[npt.NDArray[np.float32], (4, 1)]: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this map.
        """
    def __setitem__(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float32], (4, 1)]
    ) -> None: ...
    def items(self) -> typing.Iterator: ...
    pass

class ViewControl:
    """
    View controller for visualizer.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    def camera_local_rotate(
        self, x: float, y: float, xo: float = 0.0, yo: float = 0.0
    ) -> None:
        """
        Function to process rotation of camera in a localcoordinate frame
        """
    def camera_local_translate(self, forward: float, right: float, up: float) -> None:
        """
        Function to process translation of camera
        """
    def reset_camera_local_rotate(self) -> None:
        """
        Resets the coordinate frame for local camera rotations
        """
    def set_front(self, front: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Set the front vector of the visualizer
        """
    def set_lookat(self, lookat: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Set the lookat vector of the visualizer
        """
    def set_up(self, up: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Set the up vector of the visualizer
        """
    def set_zoom(self, zoom: float) -> None:
        """
        Set the zoom of the visualizer
        """
    pass

class Visualizer:
    """
    The main Visualizer class.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    def clear_geometries(self) -> bool:
        """
        Function to clear geometries from the visualizer
        """
    pass

class VisualizerWithEditing(Visualizer):
    """
    Visualizer with editing capabilities.
    """

    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor
        """
    @typing.overload
    def __init__(self, arg0: float, arg1: bool, arg2: str) -> None: ...
    def __repr__(self) -> str: ...
    def get_cropped_geometry(self) -> open3d.geometry.Geometry:
        """
        Function to get cropped geometry
        """
    def get_picked_points(self) -> typing.List[int]:
        """
        Function to get picked points
        """
    pass

class VisualizerWithKeyCallback(Visualizer):
    """
    Visualizer with custom key callback capabilities.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    def register_key_action_callback(
        self, key: int, callback_func: typing.Callable[[Visualizer, int, int], bool]
    ) -> None:
        """
        Function to register a callback function for a key action event. The callback function takes Visualizer, action and mods as input and returns a boolean indicating if UpdateGeometry() needs to be run.
        """
    def register_key_callback(
        self, key: int, callback_func: typing.Callable[[Visualizer], bool]
    ) -> None:
        """
        Function to register a callback function for a key press event
        """
    pass

class VisualizerWithVertexSelection(Visualizer):
    """
    Visualizer with vertex selection capabilities.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    def add_picked_points(self, arg0: open3d.utility.IntVector) -> None:
        """
        Function to add picked points
        """
    def clear_picked_points(self) -> None:
        """
        Function to clear picked points
        """
    def get_picked_points(self) -> typing.List[open3d.visualization.PickedPoint]:
        """
        Function to get picked points
        """
    def pick_points(
        self, arg0: float, arg1: float, arg2: float, arg3: float
    ) -> open3d.utility.IntVector:
        """
        Function to pick points
        """
    def register_selection_changed_callback(
        self, arg0: typing.Callable[[], None]
    ) -> None:
        """
        Registers a function to be called when selection changes
        """
    def register_selection_moved_callback(
        self, arg0: typing.Callable[[], None]
    ) -> None:
        """
        Registers a function to be called after selection moves
        """
    def register_selection_moving_callback(
        self, arg0: typing.Callable[[], None]
    ) -> None:
        """
        Registers a function to be called while selection moves. Geometry's vertex values can be changed, but do not changethe number of vertices.
        """
    def remove_picked_points(self, arg0: open3d.utility.IntVector) -> None:
        """
        Function to remove picked points
        """
    pass

Color: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Color: 1>
Default: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Default: 0>
Normal: open3d.visualization.MeshColorOption  # value = <MeshColorOption.Normal: 9>
XCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.XCoordinate: 2>
YCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.YCoordinate: 3>
ZCoordinate: open3d.visualization.MeshColorOption  # value = <MeshColorOption.ZCoordinate: 4>
