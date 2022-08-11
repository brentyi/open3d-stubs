from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.camera
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Kinect2ColorCameraDefault",
    "Kinect2DepthCameraDefault",
    "PinholeCameraIntrinsic",
    "PinholeCameraIntrinsicParameters",
    "PinholeCameraParameters",
    "PinholeCameraTrajectory",
    "PrimeSenseDefault",
]

class PinholeCameraIntrinsic:
    """
    PinholeCameraIntrinsic class stores intrinsic camera matrix, and image height and width.
    """

    def __copy__(self) -> PinholeCameraIntrinsic: ...
    def __deepcopy__(self, arg0: dict) -> PinholeCameraIntrinsic: ...
    def __repr__(self) -> str: ...
    @property
    def height(self) -> int:
        """
        int: Height of the image.

        :type: int
        """
    @height.setter
    def height(self, arg0: int) -> None:
        """
        int: Height of the image.
        """
    @property
    def intrinsic_matrix(self) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
        """
        3x3 numpy array: Intrinsic camera matrix ``[[fx, 0, cx], [0, fy, cy], [0, 0, 1]]``

        :type: Annotated[npt.NDArray[np.float64], (3, 3)]
        """
    @intrinsic_matrix.setter
    def intrinsic_matrix(
        self, arg0: Annotated[npt.NDArray[np.float64], (3, 3)]
    ) -> None:
        """
        3x3 numpy array: Intrinsic camera matrix ``[[fx, 0, cx], [0, fy, cy], [0, 0, 1]]``
        """
    @property
    def width(self) -> int:
        """
        int: Width of the image.

        :type: int
        """
    @width.setter
    def width(self, arg0: int) -> None:
        """
        int: Width of the image.
        """
    pass

class PinholeCameraIntrinsicParameters:
    """
    Enum class that contains default camera intrinsic parameters for different sensors.
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
    Kinect2ColorCameraDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.Kinect2ColorCameraDefault: 2>
    Kinect2DepthCameraDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.Kinect2DepthCameraDefault: 1>
    PrimeSenseDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.PrimeSenseDefault: 0>
    __members__: dict  # value = {'PrimeSenseDefault': <PinholeCameraIntrinsicParameters.PrimeSenseDefault: 0>, 'Kinect2DepthCameraDefault': <PinholeCameraIntrinsicParameters.Kinect2DepthCameraDefault: 1>, 'Kinect2ColorCameraDefault': <PinholeCameraIntrinsicParameters.Kinect2ColorCameraDefault: 2>}
    pass

class PinholeCameraParameters:
    """
    Contains both intrinsic and extrinsic pinhole camera parameters.
    """

    def __copy__(self) -> PinholeCameraParameters: ...
    def __deepcopy__(self, arg0: dict) -> PinholeCameraParameters: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PinholeCameraParameters) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def extrinsic(self) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        4x4 numpy array: Camera extrinsic parameters.

        :type: Annotated[npt.NDArray[np.float64], (4, 4)]
        """
    @extrinsic.setter
    def extrinsic(self, arg0: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        4x4 numpy array: Camera extrinsic parameters.
        """
    @property
    def intrinsic(self) -> PinholeCameraIntrinsic:
        """
        ``open3d.camera.PinholeCameraIntrinsic``: PinholeCameraIntrinsic object.

        :type: PinholeCameraIntrinsic
        """
    @intrinsic.setter
    def intrinsic(self, arg0: PinholeCameraIntrinsic) -> None:
        """
        ``open3d.camera.PinholeCameraIntrinsic``: PinholeCameraIntrinsic object.
        """
    pass

class PinholeCameraTrajectory:
    """
    Contains a list of ``PinholeCameraParameters``, useful to storing trajectories.
    """

    def __copy__(self) -> PinholeCameraTrajectory: ...
    def __deepcopy__(self, arg0: dict) -> PinholeCameraTrajectory: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PinholeCameraTrajectory) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def parameters(self) -> typing.List[PinholeCameraParameters]:
        """
        ``List(open3d.camera.PinholeCameraParameters)``: List of PinholeCameraParameters objects.

        :type: typing.List[PinholeCameraParameters]
        """
    @parameters.setter
    def parameters(self, arg0: typing.List[PinholeCameraParameters]) -> None:
        """
        ``List(open3d.camera.PinholeCameraParameters)``: List of PinholeCameraParameters objects.
        """
    pass

Kinect2ColorCameraDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.Kinect2ColorCameraDefault: 2>
Kinect2DepthCameraDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.Kinect2DepthCameraDefault: 1>
PrimeSenseDefault: open3d.camera.PinholeCameraIntrinsicParameters  # value = <PinholeCameraIntrinsicParameters.PrimeSenseDefault: 0>
