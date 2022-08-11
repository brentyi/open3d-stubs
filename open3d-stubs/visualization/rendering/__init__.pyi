from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.camera
import open3d.geometry
import open3d.t.geometry
import open3d.visualization.rendering
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Camera",
    "ColorGrading",
    "Gradient",
    "MaterialRecord",
    "OffscreenRenderer",
    "Open3DScene",
    "Renderer",
    "Scene",
    "TriangleMeshModel",
    "View",
]

class Camera:
    """
    Camera object
    """

    class FovType:
        """
        Enum class for Camera field of view types.

        Members:

          Vertical

          Horizontal
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
        Horizontal: open3d.visualization.rendering.Camera.FovType  # value = <FovType.Horizontal: 1>
        Vertical: open3d.visualization.rendering.Camera.FovType  # value = <FovType.Vertical: 0>
        __members__: dict  # value = {'Vertical': <FovType.Vertical: 0>, 'Horizontal': <FovType.Horizontal: 1>}
        pass

    class Projection:
        """
        Enum class for Camera projection types.

        Members:

          Perspective

          Ortho
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
        Ortho: open3d.visualization.rendering.Camera.Projection  # value = <Projection.Ortho: 1>
        Perspective: open3d.visualization.rendering.Camera.Projection  # value = <Projection.Perspective: 0>
        __members__: dict  # value = {'Perspective': <Projection.Perspective: 0>, 'Ortho': <Projection.Ortho: 1>}
        pass
    def copy_from(self, arg0: Camera) -> None:
        """
        Copies the settings from the camera passed as the argument into this camera
        """
    def get_far(self) -> float:
        """
        Returns the distance from the camera to the far plane
        """
    def get_field_of_view(self) -> float:
        """
        Returns the field of view of camera, in degrees. Only valid if it was passed to set_projection().
        """
    def get_field_of_view_type(self) -> Camera.FovType:
        """
        Returns the field of view type. Only valid if it was passed to set_projection().
        """
    def get_model_matrix(self) -> Annotated[npt.NDArray[np.float32], (4, 4)]:
        """
        Returns the model matrix of the camera
        """
    def get_near(self) -> float:
        """
        Returns the distance from the camera to the near plane
        """
    def get_projection_matrix(self) -> Annotated[npt.NDArray[np.float32], (4, 4)]:
        """
        Returns the projection matrix of the camera
        """
    def get_view_matrix(self) -> Annotated[npt.NDArray[np.float32], (4, 4)]:
        """
        Returns the view matrix of the camera
        """
    def look_at(
        self,
        arg0: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
    ) -> None:
        """
        Sets the position and orientation of the camera: look_at(center, eye, up)
        """
    @typing.overload
    def set_projection(
        self,
        arg0: Annotated[npt.NDArray[np.float64], (3, 3)],
        arg1: float,
        arg2: float,
        arg3: float,
        arg4: float,
    ) -> None:
        """
        Sets a perspective projection. set_projection(field_of_view, aspect_ratio, far_plane, field_of_view_type)

        Sets the camera projection via a viewing frustum. set_projection(projection_type, left, right, bottom, top, near, far)

        Sets the camera projection via intrinsics matrix. set_projection(intrinsics, near_place, far_plane, image_width, image_height)
        """
    @typing.overload
    def set_projection(
        self,
        arg0: Camera.Projection,
        arg1: float,
        arg2: float,
        arg3: float,
        arg4: float,
        arg5: float,
        arg6: float,
    ) -> None: ...
    @typing.overload
    def set_projection(
        self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: Camera.FovType
    ) -> None: ...
    def unproject(
        self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float
    ) -> Annotated[npt.NDArray[np.float32], (3, 1)]: ...
    Horizontal: open3d.visualization.rendering.Camera.FovType  # value = <FovType.Horizontal: 1>
    Ortho: open3d.visualization.rendering.Camera.Projection  # value = <Projection.Ortho: 1>
    Perspective: open3d.visualization.rendering.Camera.Projection  # value = <Projection.Perspective: 0>
    Vertical: open3d.visualization.rendering.Camera.FovType  # value = <FovType.Vertical: 0>
    pass

class ColorGrading:
    """
    Parameters to control color grading options
    """

    class Quality:
        """
        Quality level of color grading operations

        Members:

          LOW

          MEDIUM

          HIGH

          ULTRA
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
        HIGH: open3d.visualization.rendering.ColorGrading.Quality  # value = <Quality.HIGH: 2>
        LOW: open3d.visualization.rendering.ColorGrading.Quality  # value = <Quality.LOW: 0>
        MEDIUM: open3d.visualization.rendering.ColorGrading.Quality  # value = <Quality.MEDIUM: 1>
        ULTRA: open3d.visualization.rendering.ColorGrading.Quality  # value = <Quality.ULTRA: 3>
        __members__: dict  # value = {'LOW': <Quality.LOW: 0>, 'MEDIUM': <Quality.MEDIUM: 1>, 'HIGH': <Quality.HIGH: 2>, 'ULTRA': <Quality.ULTRA: 3>}
        pass

    class ToneMapping:
        """
        Specifies the tone-mapping algorithm

        Members:

          LINEAR

          ACES_LEGACY

          ACES

          FILMIC

          UCHIMURA

          REINHARD

          DISPLAY_RANGE
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
        ACES: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.ACES: 2>
        ACES_LEGACY: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.ACES_LEGACY: 1>
        DISPLAY_RANGE: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.DISPLAY_RANGE: 6>
        FILMIC: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.FILMIC: 3>
        LINEAR: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.LINEAR: 0>
        REINHARD: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.REINHARD: 5>
        UCHIMURA: open3d.visualization.rendering.ColorGrading.ToneMapping  # value = <ToneMapping.UCHIMURA: 4>
        __members__: dict  # value = {'LINEAR': <ToneMapping.LINEAR: 0>, 'ACES_LEGACY': <ToneMapping.ACES_LEGACY: 1>, 'ACES': <ToneMapping.ACES: 2>, 'FILMIC': <ToneMapping.FILMIC: 3>, 'UCHIMURA': <ToneMapping.UCHIMURA: 4>, 'REINHARD': <ToneMapping.REINHARD: 5>, 'DISPLAY_RANGE': <ToneMapping.DISPLAY_RANGE: 6>}
        pass
    def __init__(
        self, arg0: ColorGrading.Quality, arg1: ColorGrading.ToneMapping
    ) -> None: ...
    @property
    def quality(self) -> ColorGrading.Quality:
        """
        Quality of color grading operations. High quality is more accurate but slower

        :type: ColorGrading.Quality
        """
    @quality.setter
    def quality(self, arg1: ColorGrading.Quality) -> None:
        """
        Quality of color grading operations. High quality is more accurate but slower
        """
    @property
    def temperature(self) -> float:
        """
        White balance color temperature

        :type: float
        """
    @temperature.setter
    def temperature(self, arg1: float) -> None:
        """
        White balance color temperature
        """
    @property
    def tint(self) -> float:
        """
        Tint on the green/magenta axis. Ranges from -1.0 to 1.0.

        :type: float
        """
    @tint.setter
    def tint(self, arg1: float) -> None:
        """
        Tint on the green/magenta axis. Ranges from -1.0 to 1.0.
        """
    @property
    def tone_mapping(self) -> ColorGrading.ToneMapping:
        """
        The tone mapping algorithm to apply. Must be one of Linear, AcesLegacy, Aces, Filmic, Uchimura, Rienhard, Display Range(for debug)

        :type: ColorGrading.ToneMapping
        """
    @tone_mapping.setter
    def tone_mapping(self, arg1: ColorGrading.ToneMapping) -> None:
        """
        The tone mapping algorithm to apply. Must be one of Linear, AcesLegacy, Aces, Filmic, Uchimura, Rienhard, Display Range(for debug)
        """
    pass

class Gradient:
    """
    Manages a gradient for the unlitGradient shader.In gradient mode, the array of points specifies points along the gradient, from 0 to 1 (inclusive). These do need to be evenly spaced.Simple greyscale:    [ ( 0.0, black ),      ( 1.0, white ) ]Rainbow (note the gaps around green):    [ ( 0.000, blue ),      ( 0.125, cornflower blue ),      ( 0.250, cyan ),      ( 0.500, green ),      ( 0.750, yellow ),      ( 0.875, orange ),      ( 1.000, red ) ]The gradient will generate a largish texture, so it should be fairly smooth, but the boundaries may not be exactly as specified due to quantization imposed by the fixed size of the texture.  The points *must* be sorted from the smallest value to the largest. The values must be in the range [0, 1].
    """

    class Mode:
        """
        Members:

          GRADIENT

          LUT
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
        GRADIENT: open3d.visualization.rendering.Gradient.Mode  # value = <Mode.GRADIENT: 0>
        LUT: open3d.visualization.rendering.Gradient.Mode  # value = <Mode.LUT: 1>
        __members__: dict  # value = {'GRADIENT': <Mode.GRADIENT: 0>, 'LUT': <Mode.LUT: 1>}
        pass

    class Point:
        def __init__(
            self, arg0: float, arg1: Annotated[npt.NDArray[np.float32], (4, 1)]
        ) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def color(self) -> Annotated[npt.NDArray[np.float32], (4, 1)]:
            """
            [R, G, B, A]. Color values must be in [0.0, 1.0]

            :type: Annotated[npt.NDArray[np.float32], (4, 1)]
            """
        @color.setter
        def color(self, arg0: Annotated[npt.NDArray[np.float32], (4, 1)]) -> None:
            """
            [R, G, B, A]. Color values must be in [0.0, 1.0]
            """
        @property
        def value(self) -> float:
            """
            Must be within 0.0 and 1.0

            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            """
            Must be within 0.0 and 1.0
            """
        pass
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.List[Gradient.Point]) -> None: ...
    @property
    def mode(self) -> Gradient.Mode:
        """
        :type: Gradient.Mode
        """
    @mode.setter
    def mode(self, arg1: Gradient.Mode) -> None:
        pass
    @property
    def points(self) -> typing.List[Gradient.Point]:
        """
        :type: typing.List[Gradient.Point]
        """
    @points.setter
    def points(self, arg1: typing.List[Gradient.Point]) -> None:
        pass
    GRADIENT: open3d.visualization.rendering.Gradient.Mode  # value = <Mode.GRADIENT: 0>
    LUT: open3d.visualization.rendering.Gradient.Mode  # value = <Mode.LUT: 1>
    pass

class MaterialRecord:
    """
    Describes the real-world, physically based (PBR) material used to render a geometry
    """

    def __init__(self) -> None: ...
    @property
    def absorption_color(self) -> Annotated[npt.NDArray[np.float32], (3, 1)]:
        """
        :type: Annotated[npt.NDArray[np.float32], (3, 1)]
        """
    @absorption_color.setter
    def absorption_color(
        self, arg0: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        pass
    @property
    def absorption_distance(self) -> float:
        """
        :type: float
        """
    @absorption_distance.setter
    def absorption_distance(self, arg0: float) -> None:
        pass
    @property
    def albedo_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @albedo_img.setter
    def albedo_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def anisotropy_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @anisotropy_img.setter
    def anisotropy_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def ao_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @ao_img.setter
    def ao_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def ao_rough_metal_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @ao_rough_metal_img.setter
    def ao_rough_metal_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def aspect_ratio(self) -> float:
        """
        :type: float
        """
    @aspect_ratio.setter
    def aspect_ratio(self, arg0: float) -> None:
        pass
    @property
    def base_anisotropy(self) -> float:
        """
        :type: float
        """
    @base_anisotropy.setter
    def base_anisotropy(self, arg0: float) -> None:
        pass
    @property
    def base_clearcoat(self) -> float:
        """
        :type: float
        """
    @base_clearcoat.setter
    def base_clearcoat(self, arg0: float) -> None:
        pass
    @property
    def base_clearcoat_roughness(self) -> float:
        """
        :type: float
        """
    @base_clearcoat_roughness.setter
    def base_clearcoat_roughness(self, arg0: float) -> None:
        pass
    @property
    def base_color(self) -> Annotated[npt.NDArray[np.float32], (4, 1)]:
        """
        :type: Annotated[npt.NDArray[np.float32], (4, 1)]
        """
    @base_color.setter
    def base_color(self, arg0: Annotated[npt.NDArray[np.float32], (4, 1)]) -> None:
        pass
    @property
    def base_metallic(self) -> float:
        """
        :type: float
        """
    @base_metallic.setter
    def base_metallic(self, arg0: float) -> None:
        pass
    @property
    def base_reflectance(self) -> float:
        """
        :type: float
        """
    @base_reflectance.setter
    def base_reflectance(self, arg0: float) -> None:
        pass
    @property
    def base_roughness(self) -> float:
        """
        :type: float
        """
    @base_roughness.setter
    def base_roughness(self, arg0: float) -> None:
        pass
    @property
    def clearcoat_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @clearcoat_img.setter
    def clearcoat_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def clearcoat_roughness_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @clearcoat_roughness_img.setter
    def clearcoat_roughness_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def generic_imgs(self) -> typing.Dict[str, open3d.geometry.Image]:
        """
        :type: typing.Dict[str, open3d.geometry.Image]
        """
    @generic_imgs.setter
    def generic_imgs(self, arg0: typing.Dict[str, open3d.geometry.Image]) -> None:
        pass
    @property
    def generic_params(
        self,
    ) -> typing.Dict[str, Annotated[npt.NDArray[np.float32], (4, 1)]]:
        """
        :type: typing.Dict[str, Annotated[npt.NDArray[np.float32], (4, 1)]]
        """
    @generic_params.setter
    def generic_params(
        self, arg0: typing.Dict[str, Annotated[npt.NDArray[np.float32], (4, 1)]]
    ) -> None:
        pass
    @property
    def gradient(self) -> Gradient:
        """
        :type: Gradient
        """
    @gradient.setter
    def gradient(self, arg0: Gradient) -> None:
        pass
    @property
    def ground_plane_axis(self) -> float:
        """
        :type: float
        """
    @ground_plane_axis.setter
    def ground_plane_axis(self, arg0: float) -> None:
        pass
    @property
    def has_alpha(self) -> bool:
        """
        :type: bool
        """
    @has_alpha.setter
    def has_alpha(self, arg0: bool) -> None:
        pass
    @property
    def line_width(self) -> float:
        """
        Requires 'shader' to be 'unlitLine'

        :type: float
        """
    @line_width.setter
    def line_width(self, arg0: float) -> None:
        """
        Requires 'shader' to be 'unlitLine'
        """
    @property
    def metallic_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @metallic_img.setter
    def metallic_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def normal_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @normal_img.setter
    def normal_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def point_size(self) -> float:
        """
        :type: float
        """
    @point_size.setter
    def point_size(self, arg0: float) -> None:
        pass
    @property
    def reflectance_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @reflectance_img.setter
    def reflectance_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def roughness_img(self) -> open3d.geometry.Image:
        """
        :type: open3d.geometry.Image
        """
    @roughness_img.setter
    def roughness_img(self, arg0: open3d.geometry.Image) -> None:
        pass
    @property
    def sRGB_color(self) -> bool:
        """
        :type: bool
        """
    @sRGB_color.setter
    def sRGB_color(self, arg0: bool) -> None:
        pass
    @property
    def scalar_max(self) -> float:
        """
        :type: float
        """
    @scalar_max.setter
    def scalar_max(self, arg0: float) -> None:
        pass
    @property
    def scalar_min(self) -> float:
        """
        :type: float
        """
    @scalar_min.setter
    def scalar_min(self, arg0: float) -> None:
        pass
    @property
    def shader(self) -> str:
        """
        :type: str
        """
    @shader.setter
    def shader(self, arg0: str) -> None:
        pass
    @property
    def thickness(self) -> float:
        """
        :type: float
        """
    @thickness.setter
    def thickness(self, arg0: float) -> None:
        pass
    @property
    def transmission(self) -> float:
        """
        :type: float
        """
    @transmission.setter
    def transmission(self, arg0: float) -> None:
        pass
    pass

class OffscreenRenderer:
    """
    Renderer instance that can be used for rendering to an image
    """

    def __init__(
        self, width: int, height: int, resource_path: str = "", headless: bool = False
    ) -> None:
        """
        Takes width, height and optionally a resource_path and headless flag. If unspecified, resource_path will use the resource path from the installed Open3D library. By default a running windowing session is required. To enable headless rendering set headless to True
        """
    def render_to_depth_image(
        self, z_in_view_space: bool = False
    ) -> open3d.geometry.Image:
        """
        Renders scene depth buffer to a float image, blocking until the image is returned. Pixels range from 0 (near plane) to 1 (far plane). If z_in_view_space is set to True then pixels are pre-transformed into view space (i.e., distance from camera).
        """
    def render_to_image(self) -> open3d.geometry.Image:
        """
        Renders scene to an image, blocking until the image is returned
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
    @property
    def scene(self) -> open3d.visualization.rendering.Open3DScene:
        """
        Returns the Open3DScene for this renderer. This scene is destroyed when the renderer is destroyed and should not be accessed after that point.

        :type: open3d.visualization.rendering.Open3DScene
        """
    pass

class Open3DScene:
    """
    High-level scene for rending
    """

    class LightingProfile:
        """
        Enum for conveniently setting lighting

        Members:

          HARD_SHADOWS

          DARK_SHADOWS

          MED_SHADOWS

          SOFT_SHADOWS

          NO_SHADOWS
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
        DARK_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.DARK_SHADOWS: 1>
        HARD_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.HARD_SHADOWS: 0>
        MED_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.MED_SHADOWS: 2>
        NO_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.NO_SHADOWS: 4>
        SOFT_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.SOFT_SHADOWS: 3>
        __members__: dict  # value = {'HARD_SHADOWS': <LightingProfile.HARD_SHADOWS: 0>, 'DARK_SHADOWS': <LightingProfile.DARK_SHADOWS: 1>, 'MED_SHADOWS': <LightingProfile.MED_SHADOWS: 2>, 'SOFT_SHADOWS': <LightingProfile.SOFT_SHADOWS: 3>, 'NO_SHADOWS': <LightingProfile.NO_SHADOWS: 4>}
        pass
    def __init__(self, arg0: Renderer) -> None: ...
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.geometry.Geometry3D,
        material: MaterialRecord,
        add_downsampled_copy_for_fast_rendering: bool = True,
    ) -> None: ...
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.t.geometry.Geometry,
        material: MaterialRecord,
        add_downsampled_copy_for_fast_rendering: bool = True,
    ) -> None: ...
    def add_model(self, arg0: str, arg1: TriangleMeshModel) -> None:
        """
        Adds TriangleMeshModel to the scene.
        """
    def clear_geometry(self) -> None: ...
    def geometry_is_visible(self, arg0: str) -> bool: ...
    def get_geometry_transform(
        self, arg0: str
    ) -> Annotated[npt.NDArray[np.float64], (4, 4)]: ...
    def has_geometry(self, arg0: str) -> bool: ...
    def modify_geometry_material(self, arg0: str, arg1: MaterialRecord) -> None: ...
    def remove_geometry(self, arg0: str) -> None:
        """
        Removes the geometry with the given name
        """
    def set_background(
        self,
        color: Annotated[npt.NDArray[np.float32], (4, 1)],
        image: open3d.geometry.Image = None,
    ) -> None: ...
    def set_background_color(
        self, arg0: Annotated[npt.NDArray[np.float32], (4, 1)]
    ) -> None:
        """
        This function has been deprecated. Please use set_background() instead.
        """
    def set_geometry_transform(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float64], (4, 4)]
    ) -> None: ...
    def set_lighting(
        self,
        arg0: Open3DScene.LightingProfile,
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
    ) -> None:
        """
        Sets a simple lighting model. set_lighting(profile, sun_dir). The default value is set_lighting(Open3DScene.LightingProfile.MED_SHADOWS, (0.577, -0.577, -0.577))
        """
    def set_view_size(self, arg0: int, arg1: int) -> None:
        """
        Sets the view size. This should not be used except for rendering to an image
        """
    def show_axes(self, arg0: bool) -> None:
        """
        Toggles display of xyz axes
        """
    def show_geometry(self, arg0: str, arg1: bool) -> None:
        """
        Shows or hides the geometry with the given name
        """
    def show_ground_plane(self, arg0: bool, arg1: Scene.GroundPlane) -> None:
        """
        Toggles display of ground plane
        """
    def show_skybox(self, arg0: bool) -> None:
        """
        Toggles display of the skybox
        """
    def update_material(self, arg0: MaterialRecord) -> None:
        """
        Applies the passed material to all the geometries
        """
    @property
    def background_color(self) -> Annotated[npt.NDArray[np.float32], (4, 1)]:
        """
        The background color (read-only)

        :type: Annotated[npt.NDArray[np.float32], (4, 1)]
        """
    @property
    def bounding_box(self) -> open3d.geometry.AxisAlignedBoundingBox:
        """
        The bounding box of all the items in the scene, visible and invisible

        :type: open3d.geometry.AxisAlignedBoundingBox
        """
    @property
    def camera(self) -> Camera:
        """
        The camera object (read-only)

        :type: Camera
        """
    @property
    def downsample_threshold(self) -> int:
        """
        Minimum number of points before downsampled point clouds are created and used when rendering speed is important

        :type: int
        """
    @downsample_threshold.setter
    def downsample_threshold(self, arg1: int) -> None:
        """
        Minimum number of points before downsampled point clouds are created and used when rendering speed is important
        """
    @property
    def scene(self) -> Scene:
        """
        The low-level rendering scene object (read-only)

        :type: Scene
        """
    @property
    def view(self) -> View:
        """
        The low level view associated with the scene

        :type: View
        """
    DARK_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.DARK_SHADOWS: 1>
    HARD_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.HARD_SHADOWS: 0>
    MED_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.MED_SHADOWS: 2>
    NO_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.NO_SHADOWS: 4>
    SOFT_SHADOWS: open3d.visualization.rendering.Open3DScene.LightingProfile  # value = <LightingProfile.SOFT_SHADOWS: 3>
    pass

REHandle = typing.NewType("REHandle", object)

class Renderer:
    """
    Renderer class that manages 3D resources. Get from gui.Window.
    """

    def add_texture(
        self, image: open3d.geometry.Image, is_sRGB: bool = False
    ) -> REHandle:
        """
        Adds a texture: add_texture(geometry.Image, bool). The first parameter is the image, the second parameter is optional and is True if the image is in the sRGB colorspace and False otherwise
        """
    def remove_texture(self, arg0: REHandle) -> None:
        """
        Deletes the texture. This does not remove the texture from any existing materials or GUI widgets, and must be done prior to this call.
        """
    def set_clear_color(self, arg0: Annotated[npt.NDArray[np.float32], (4, 1)]) -> None:
        """
        Sets the background color for the renderer, [r, g, b, a]. Applies to everything being rendered, so it essentially acts as the background color of the window
        """
    def update_texture(
        self, texture: REHandle, image: open3d.geometry.Image, is_sRGB: bool = False
    ) -> bool:
        """
        Updates the contents of the texture to be the new image, or returns False and does nothing if the image is a different size. It is more efficient to call update_texture() rather than removing and adding a new texture, especially when changes happen frequently, such as when implementing video. add_texture(geometry.Image, bool). The first parameter is the image, the second parameter is optional and is True if the image is in the sRGB colorspace and False otherwise
        """
    pass

class Scene:
    """
    Low-level rendering scene
    """

    class GroundPlane:
        """
        Plane on which to show ground plane: XZ, XY, or YZ

        Members:

          XZ

          XY

          YZ
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
        XY: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.XY: 1>
        XZ: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.XZ: 0>
        YZ: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.YZ: 2>
        __members__: dict  # value = {'XZ': <GroundPlane.XZ: 0>, 'XY': <GroundPlane.XY: 1>, 'YZ': <GroundPlane.YZ: 2>}
        pass
    def add_camera(self, arg0: str, arg1: Camera) -> None:
        """
        Adds a camera to the scene
        """
    def add_directional_light(
        self,
        arg0: str,
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg3: float,
        arg4: bool,
    ) -> bool:
        """
        Adds a directional light to the scene: add_point_light(name, color, intensity, cast_shadows)
        """
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.geometry.Geometry3D,
        material: MaterialRecord,
        downsampled_name: str = "",
        downsample_threshold: int = 18446744073709551615,
    ) -> bool:
        """
        Adds a Geometry with a material to the scene

        Adds a Geometry with a material to the scene
        """
    @typing.overload
    def add_geometry(
        self,
        name: str,
        geometry: open3d.t.geometry.Geometry,
        material: MaterialRecord,
        downsampled_name: str = "",
        downsample_threshold: int = 18446744073709551615,
    ) -> bool: ...
    def add_point_light(
        self,
        arg0: str,
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg3: float,
        arg4: float,
        arg5: bool,
    ) -> bool:
        """
        Adds a point light to the scene: add_point_light(name, color, position, intensity, falloff, cast_shadows)
        """
    def add_spot_light(
        self,
        arg0: str,
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg3: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg4: float,
        arg5: float,
        arg6: float,
        arg7: float,
        arg8: bool,
    ) -> bool:
        """
        Adds a spot light to the scene: add_point_light(name, color, position, direction, intensity, falloff, inner_cone_angle, outer_cone_angle, cast_shadows)
        """
    def enable_indirect_light(self, arg0: bool) -> None:
        """
        Enables or disables indirect lighting
        """
    def enable_light_shadow(self, arg0: str, arg1: bool) -> None:
        """
        Changes whether a point, spot, or directional light can cast shadows:  enable_light_shadow(name, can_cast_shadows)
        """
    def enable_sun_light(self, arg0: bool) -> None: ...
    def has_geometry(self, arg0: str) -> bool:
        """
        Returns True if a geometry with the provided name exists in the scene.
        """
    def remove_camera(self, arg0: str) -> None:
        """
        Removes the camera with the given name
        """
    def remove_light(self, arg0: str) -> None:
        """
        Removes the named light from the scene: remove_light(name)
        """
    def render_to_depth_image(
        self, arg0: typing.Callable[[open3d.geometry.Image], None]
    ) -> None:
        """
        Renders the scene to a depth image. This can only be used in GUI app. To render without a window, use Application.render_to_depth_image. Pixels range from 0.0 (near plane) to 1.0 (far plane)
        """
    def render_to_image(
        self, arg0: typing.Callable[[open3d.geometry.Image], None]
    ) -> None:
        """
        Renders the scene to an image. This can only be used in a GUI app. To render without a window, use Application.render_to_image
        """
    def set_active_camera(self, arg0: str) -> None:
        """
        Sets the camera with the given name as the active camera for the scene
        """
    def set_indirect_light(self, arg0: str) -> bool:
        """
        Loads the indirect light. The name parameter is the name of the file to load
        """
    def set_indirect_light_intensity(self, arg0: float) -> None:
        """
        Sets the brightness of the indirect light
        """
    def set_sun_light(
        self,
        arg0: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg1: Annotated[npt.NDArray[np.float32], (3, 1)],
        arg2: float,
    ) -> None:
        """
        Sets the parameters of the sun light: direction, color, intensity
        """
    def update_geometry(
        self, arg0: str, arg1: open3d.t.geometry.PointCloud, arg2: int
    ) -> None:
        """
        Updates the flagged arrays from the tgeometry.PointCloud. The flags should be ORed from Scene.UPDATE_POINTS_FLAG, Scene.UPDATE_NORMALS_FLAG, Scene.UPDATE_COLORS_FLAG, and Scene.UPDATE_UV0_FLAG
        """
    def update_light_color(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        """
        Changes a point, spot, or directional light's color
        """
    def update_light_cone_angles(self, arg0: str, arg1: float, arg2: float) -> None:
        """
        Changes a spot light's inner and outer cone angles
        """
    def update_light_direction(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        """
        Changes a spot or directional light's direction
        """
    def update_light_falloff(self, arg0: str, arg1: float) -> None:
        """
        Changes a point or spot light's falloff
        """
    def update_light_intensity(self, arg0: str, arg1: float) -> None:
        """
        Changes a point, spot or directional light's intensity
        """
    def update_light_position(
        self, arg0: str, arg1: Annotated[npt.NDArray[np.float32], (3, 1)]
    ) -> None:
        """
        Changes a point or spot light's position
        """
    UPDATE_COLORS_FLAG = 4
    UPDATE_NORMALS_FLAG = 2
    UPDATE_POINTS_FLAG = 1
    UPDATE_UV0_FLAG = 8
    XY: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.XY: 1>
    XZ: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.XZ: 0>
    YZ: open3d.visualization.rendering.Scene.GroundPlane  # value = <GroundPlane.YZ: 2>
    pass

class TriangleMeshModel:
    """
    A list of geometry.TriangleMesh and Material that can describe a complex model with multiple meshes, such as might be stored in an FBX, OBJ, or GLTF file
    """

    class MeshInfo:
        def __init__(
            self, arg0: open3d.geometry.TriangleMesh, arg1: str, arg2: int
        ) -> None: ...
        @property
        def material_idx(self) -> int:
            """
            :type: int
            """
        @material_idx.setter
        def material_idx(self, arg0: int) -> None:
            pass
        @property
        def mesh(self) -> open3d.geometry.TriangleMesh:
            """
            :type: open3d.geometry.TriangleMesh
            """
        @mesh.setter
        def mesh(self, arg0: open3d.geometry.TriangleMesh) -> None:
            pass
        @property
        def mesh_name(self) -> str:
            """
            :type: str
            """
        @mesh_name.setter
        def mesh_name(self, arg0: str) -> None:
            pass
        pass
    def __init__(self) -> None: ...
    @property
    def materials(self) -> typing.List[MaterialRecord]:
        """
        :type: typing.List[MaterialRecord]
        """
    @materials.setter
    def materials(self, arg0: typing.List[MaterialRecord]) -> None:
        pass
    @property
    def meshes(self) -> typing.List[TriangleMeshModel.MeshInfo]:
        """
        :type: typing.List[TriangleMeshModel.MeshInfo]
        """
    @meshes.setter
    def meshes(self, arg0: typing.List[TriangleMeshModel.MeshInfo]) -> None:
        pass
    pass

class View:
    """
    Low-level view class
    """

    class ShadowType:
        """
        Available shadow mapping algorithm options

        Members:

          PCF

          VSM
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
        PCF: open3d.visualization.rendering.View.ShadowType  # value = <ShadowType.PCF: 0>
        VSM: open3d.visualization.rendering.View.ShadowType  # value = <ShadowType.VSM: 1>
        __members__: dict  # value = {'PCF': <ShadowType.PCF: 0>, 'VSM': <ShadowType.VSM: 1>}
        pass
    def get_camera(self) -> Camera:
        """
        Returns the Camera associated with this View.
        """
    def set_ambient_occlusion(self, enabled: bool, ssct_enabled: bool = False) -> None:
        """
        True to enable, False to disable ambient occlusion. Optionally, screen-space cone tracing may be enabled with ssct_enabled=True.
        """
    def set_antialiasing(self, enabled: bool, temporal: bool = False) -> None:
        """
        True to enable, False to disable anti-aliasing. Note that this only impacts anti-aliasing post-processing. MSAA is controlled separately by `set_sample_count`. Temporal anti-aliasing may be optionally enabled with temporal=True.
        """
    def set_color_grading(self, arg0: ColorGrading) -> None:
        """
        Sets the parameters to be used for the color grading algorithms
        """
    def set_post_processing(self, arg0: bool) -> None:
        """
        True to enable, False to disable post processing. Post processing effects include: color grading, ambient occlusion (and other screen space effects), and anti-aliasing.
        """
    def set_sample_count(self, arg0: int) -> None:
        """
        Sets the sample count for MSAA. Set to 1 to disable MSAA. Typical values are 2, 4 or 8. The maximum possible value depends on the underlying GPU and OpenGL driver.
        """
    def set_shadowing(
        self, enabled: bool, type: View.ShadowType = ShadowType.PCF
    ) -> None:
        """
        True to enable, false to enable all shadow mapping when rendering this View. When enabling shadow mapping you may also specify one of two shadow mapping algorithms: PCF (default) or VSM. Note: shadowing is enabled by default with PCF shadow mapping.
        """
    pass
