from typing import Any, Set, overload

import numpy as np
import numpy.typing as npt
import open3d.utility
from typing_extensions import Annotated

class OdometryOption:
    depth_diff_max: float
    depth_max: float
    depth_min: float
    iteration_number_per_pyramid_level: open3d.utility.IntVector
    def __init__(
        self,
        iteration_number_per_pyramid_level: open3d.utility.IntVector = ...,
        depth_diff_max: float = ...,
        depth_min: float = ...,
        depth_max: float = ...,
    ) -> None: ...

class RGBDOdometryJacobian:
    def __init__(self, *args, **kwargs) -> None: ...

class RGBDOdometryJacobianFromColorTerm(RGBDOdometryJacobian):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: RGBDOdometryJacobianFromColorTerm) -> None: ...
    def __copy__(self) -> RGBDOdometryJacobianFromColorTerm: ...
    def __deepcopy__(self, arg0: dict) -> RGBDOdometryJacobianFromColorTerm: ...

class RGBDOdometryJacobianFromHybridTerm(RGBDOdometryJacobian):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: RGBDOdometryJacobianFromHybridTerm) -> None: ...
    def __copy__(self) -> RGBDOdometryJacobianFromHybridTerm: ...
    def __deepcopy__(self, arg0: dict) -> RGBDOdometryJacobianFromHybridTerm: ...

def compute_rgbd_odometry(
    rgbd_source,
    rgbd_target,
    pinhole_camera_intrinsic=...,
    odo_init=...,
    jacobian=...,
    option=...,
) -> Any: ...

__all__ = [
    "OdometryOption",
    "RGBDOdometryJacobian",
    "RGBDOdometryJacobianFromColorTerm",
    "RGBDOdometryJacobianFromHybridTerm",
    "compute_rgbd_odometry",
]
