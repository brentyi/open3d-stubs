"""Integration pipeline."""
from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.geometry
import open3d.pipelines.integration
import open3d.utility
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Gray32",
    "NoColor",
    "RGB8",
    "ScalableTSDFVolume",
    "TSDFVolume",
    "TSDFVolumeColorType",
    "UniformTSDFVolume",
]

class TSDFVolume:
    """
    Base class of the Truncated
    Signed Distance Function (TSDF) volume This volume is usually used to integrate
    surface data (e.g., a series of RGB-D images) into a Mesh or PointCloud. The
    basic technique is presented in the following paper:

    A volumetric method for building complex models from range images

    B. Curless and M. Levoy

    In SIGGRAPH, 1996
    """

    @property
    def color_type(self) -> TSDFVolumeColorType:
        """
        integration.TSDFVolumeColorType: Color type of the TSDF volume.

        :type: TSDFVolumeColorType
        """
    @color_type.setter
    def color_type(self, arg0: TSDFVolumeColorType) -> None:
        """
        integration.TSDFVolumeColorType: Color type of the TSDF volume.
        """
    @property
    def sdf_trunc(self) -> float:
        """
        float: Truncation value for signed distance function (SDF).

        :type: float
        """
    @sdf_trunc.setter
    def sdf_trunc(self, arg0: float) -> None:
        """
        float: Truncation value for signed distance function (SDF).
        """
    @property
    def voxel_length(self) -> float:
        """
        float: Length of the voxel in meters.

        :type: float
        """
    @voxel_length.setter
    def voxel_length(self, arg0: float) -> None:
        """
        float: Length of the voxel in meters.
        """
    pass

class ScalableTSDFVolume(TSDFVolume):
    """
    The
    ScalableTSDFVolume implements a more memory efficient data structure for
    volumetric integration.

    This implementation is based on the following repository:
    https://github.com/qianyizh/ElasticReconstruction/tree/master/Integrate

    An observed depth pixel gives two types of information: (a) an approximation
    of the nearby surface, and (b) empty space from the camera to the surface.
    They induce two core concepts of volumetric integration: weighted average of
    a truncated signed distance function (TSDF), and carving. The weighted
    average of TSDF is great in addressing the Gaussian noise along surface
    normal and producing a smooth surface output. The carving is great in
    removing outlier structures like floating noise pixels and bumps along
    structure edges.

    Ref: Dense Scene Reconstruction with Points of Interest

    Q.-Y. Zhou and V. Koltun

    In SIGGRAPH, 2013
    """

    def __copy__(self) -> ScalableTSDFVolume: ...
    def __deepcopy__(self, arg0: dict) -> ScalableTSDFVolume: ...
    @typing.overload
    def __init__(self, arg0: ScalableTSDFVolume) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        voxel_length: float,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        volume_unit_resolution: int = 16,
        depth_sampling_stride: int = 4,
    ) -> None: ...
    def __repr__(self) -> str: ...
    pass

class TSDFVolumeColorType:
    """
    Enum class for TSDFVolumeColorType.
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
    Gray32: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.Gray32: 2>
    NoColor: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.NoColor: 0>
    RGB8: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.RGB8: 1>
    __members__: dict  # value = {'NoColor': <TSDFVolumeColorType.NoColor: 0>, 'RGB8': <TSDFVolumeColorType.RGB8: 1>, 'Gray32': <TSDFVolumeColorType.Gray32: 2>}
    pass

class UniformTSDFVolume(TSDFVolume):
    """
    UniformTSDFVolume implements the classic TSDF volume with uniform voxel grid (Curless and Levoy 1996).
    """

    def __copy__(self) -> UniformTSDFVolume: ...
    def __deepcopy__(self, arg0: dict) -> UniformTSDFVolume: ...
    @typing.overload
    def __init__(self, arg0: UniformTSDFVolume) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        origin: Annotated[npt.NDArray[np.float64], (3, 1)],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def extract_volume_color(self) -> open3d.utility.Vector3dVector:
        """
        Debug function to extract the volume color data.
        """
    def extract_volume_tsdf(self) -> open3d.utility.Vector2dVector:
        """
        Debug function to extract the volume TSDF data.
        """
    def extract_voxel_grid(self) -> open3d.geometry.VoxelGrid:
        """
        Debug function to extract the voxel data VoxelGrid.
        """
    def inject_volume_color(self, color: open3d.utility.Vector3dVector) -> None:
        """
        Debug function to inject the voxel Color data.
        """
    def inject_volume_tsdf(self, tsdf: open3d.utility.Vector2dVector) -> None:
        """
        Debug function to inject the voxel TSDF data.
        """
    @property
    def length(self) -> float:
        """
        Total length, where ``voxel_length = length / resolution``.

        :type: float
        """
    @length.setter
    def length(self, arg0: float) -> None:
        """
        Total length, where ``voxel_length = length / resolution``.
        """
    @property
    def resolution(self) -> int:
        """
        Resolution over the total length, where ``voxel_length = length / resolution``

        :type: int
        """
    @resolution.setter
    def resolution(self, arg0: int) -> None:
        """
        Resolution over the total length, where ``voxel_length = length / resolution``
        """
    pass

Gray32: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.Gray32: 2>
NoColor: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.NoColor: 0>
RGB8: open3d.pipelines.integration.TSDFVolumeColorType  # value = <TSDFVolumeColorType.RGB8: 1>
