from typing import Any, List, Set, Tuple

import numpy as np
import numpy.typing as npt
import open3d.camera
import open3d.geometry
from typing_extensions import Annotated

class NonRigidOptimizerOption:
    def __init__(
        self,
        number_of_vertical_anchors=...,
        non_rigid_anchor_point_weight=...,
        maximum_iteration=...,
        maximum_allowable_depth=...,
        depth_threshold_for_visibility_check=...,
        depth_threshold_for_discontinuity_check=...,
        half_dilation_kernel_size_for_discontinuity_map=...,
        image_boundary_margin=...,
        invisible_vertex_color_knn=...,
        debug_output_dir=...,
    ) -> None: ...

class RigidOptimizerOption:
    def __init__(
        self,
        maximum_iteration=...,
        maximum_allowable_depth=...,
        depth_threshold_for_visibility_check=...,
        depth_threshold_for_discontinuity_check=...,
        half_dilation_kernel_size_for_discontinuity_map=...,
        image_boundary_margin=...,
        invisible_vertex_color_knn=...,
        debug_output_dir=...,
    ) -> None: ...

def run_non_rigid_optimizer(
    arg0: open3d.geometry.TriangleMesh,
    arg1: List[open3d.geometry.RGBDImage],
    arg2: open3d.camera.PinholeCameraTrajectory,
    arg3: NonRigidOptimizerOption,
) -> Tuple[open3d.geometry.TriangleMesh, open3d.camera.PinholeCameraTrajectory]: ...
def run_rigid_optimizer(
    arg0: open3d.geometry.TriangleMesh,
    arg1: List[open3d.geometry.RGBDImage],
    arg2: open3d.camera.PinholeCameraTrajectory,
    arg3: RigidOptimizerOption,
) -> Tuple[open3d.geometry.TriangleMesh, open3d.camera.PinholeCameraTrajectory]: ...

__all__ = [
    "NonRigidOptimizerOption",
    "RigidOptimizerOption",
    "run_non_rigid_optimizer",
    "run_rigid_optimizer",
]
