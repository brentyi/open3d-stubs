from typing import Any, ClassVar, Set, overload

import integration
import numpy as np
import numpy.typing as npt
import open3d.geometry
import open3d.utility
from typing_extensions import Annotated

Gray32: TSDFVolumeColorType
NoColor: TSDFVolumeColorType
RGB8: TSDFVolumeColorType

class ScalableTSDFVolume(TSDFVolume):
    @overload
    def __init__(self, arg0: ScalableTSDFVolume) -> None: ...
    @overload
    def __init__(
        self,
        voxel_length: float,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        volume_unit_resolution: int = ...,
        depth_sampling_stride: int = ...,
    ) -> None: ...
    def extract_voxel_point_cloud(self) -> Any: ...
    def __copy__(self) -> ScalableTSDFVolume: ...
    def __deepcopy__(self, arg0: dict) -> ScalableTSDFVolume: ...

class TSDFVolume:
    color_type: integration.TSDFVolumeColorType
    sdf_trunc: float
    voxel_length: float
    def __init__(self, *args, **kwargs) -> None: ...
    def extract_point_cloud(self) -> Any: ...
    def extract_triangle_mesh(self) -> Any: ...
    def integrate(self, image, intrinsic, extrinsic) -> Any: ...
    def reset(self) -> Any: ...

class TSDFVolumeColorType:
    __members__: ClassVar[dict] = ...  # read-only
    Gray32: ClassVar[TSDFVolumeColorType] = ...
    NoColor: ClassVar[TSDFVolumeColorType] = ...
    RGB8: ClassVar[TSDFVolumeColorType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class UniformTSDFVolume(TSDFVolume):
    length: float
    resolution: int
    @overload
    def __init__(self, arg0: UniformTSDFVolume) -> None: ...
    @overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        origin: npt.NDArray[Annotated[np.float64, "3,1"]],
    ) -> None: ...
    def extract_volume_color(self) -> open3d.utility.Vector3dVector: ...
    def extract_volume_tsdf(self) -> open3d.utility.Vector2dVector: ...
    def extract_voxel_grid(self) -> open3d.geometry.VoxelGrid: ...
    def extract_voxel_point_cloud(self) -> Any: ...
    def inject_volume_color(self, color: open3d.utility.Vector3dVector) -> None: ...
    def inject_volume_tsdf(self, tsdf: open3d.utility.Vector2dVector) -> None: ...
    def __copy__(self) -> UniformTSDFVolume: ...
    def __deepcopy__(self, arg0: dict) -> UniformTSDFVolume: ...

__all__ = [
    "Gray32",
    "NoColor",
    "RGB8",
    "ScalableTSDFVolume",
    "TSDFVolume",
    "TSDFVolumeColorType",
    "UniformTSDFVolume",
]
