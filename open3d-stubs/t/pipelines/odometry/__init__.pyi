from typing import Any, ClassVar, Set, overload

import numpy as np
import numpy.typing as npt
import open3d.core
from typing_extensions import Annotated

Hybrid: Method
Intensity: Method
PointToPlane: Method

class Method:
    __members__: ClassVar[dict] = ...  # read-only
    Hybrid: ClassVar[Method] = ...
    Intensity: ClassVar[Method] = ...
    PointToPlane: ClassVar[Method] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OdometryConvergenceCriteria:
    max_iteration: int
    relative_fitness: float
    relative_rmse: float
    @overload
    def __init__(self, arg0: OdometryConvergenceCriteria) -> None: ...
    @overload
    def __init__(
        self,
        max_iteration: int,
        relative_rmse: float = ...,
        relative_fitness: float = ...,
    ) -> None: ...
    def __copy__(self) -> OdometryConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> OdometryConvergenceCriteria: ...

class OdometryLossParams:
    depth_huber_delta: float
    depth_outlier_trunc: float
    intensity_huber_delta: float
    @overload
    def __init__(self, arg0: OdometryLossParams) -> None: ...
    @overload
    def __init__(
        self,
        depth_outlier_trunc: float = ...,
        depth_huber_delta: float = ...,
        intensity_huber_delta: float = ...,
    ) -> None: ...
    def __copy__(self) -> OdometryLossParams: ...
    def __deepcopy__(self, arg0: dict) -> OdometryLossParams: ...

class OdometryResult:
    fitness: float
    inlier_rmse: float
    transformation: open3d.core.Tensor
    @overload
    def __init__(self, arg0: OdometryResult) -> None: ...
    @overload
    def __init__(
        self,
        transformation: open3d.core.Tensor = ...,
        inlier_rmse: float = ...,
        fitness: float = ...,
    ) -> None: ...
    def __copy__(self) -> OdometryResult: ...
    def __deepcopy__(self, arg0: dict) -> OdometryResult: ...

def compute_odometry_result_hybrid(
    source_depth,
    target_depth,
    source_intensity,
    target_intensity,
    target_depth_dx,
    target_depth_dy,
    target_intensity_dx,
    target_intensity_dy,
    source_vertex_map,
    intrinsics,
    init_source_to_target,
    depth_outlier_trunc,
    depth_huber_delta,
    intensity_huber_delta,
) -> Any: ...
def compute_odometry_result_intensity(
    source_depth,
    target_depth,
    source_intensity,
    target_intensity,
    target_intensity_dx,
    target_intensity_dy,
    source_vertex_map,
    intrinsics,
    init_source_to_target,
    depth_outlier_trunc,
    intensity_huber_delta,
) -> Any: ...
def compute_odometry_result_point_to_plane(
    source_vertex_map,
    target_vertex_map,
    target_normal_map,
    intrinsics,
    init_source_to_target,
    depth_outlier_trunc,
    depth_huber_delta,
) -> Any: ...
def rgbd_odometry_multi_scale(*args, **kwargs) -> Any: ...

__all__ = [
    "Hybrid",
    "Intensity",
    "PointToPlane",
    "Method",
    "OdometryConvergenceCriteria",
    "OdometryLossParams",
    "OdometryResult",
    "compute_odometry_result_hybrid",
    "compute_odometry_result_intensity",
    "compute_odometry_result_point_to_plane",
    "rgbd_odometry_multi_scale",
]
