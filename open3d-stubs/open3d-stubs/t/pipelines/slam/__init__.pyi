from typing import Any, Set, overload

import numpy as np
import numpy.typing as npt
import open3d.core
from typing_extensions import Annotated

class Frame:
    @overload
    def __init__(self, arg0) -> None: ...
    @overload
    def __init__(self, height, width, intrinsics, device) -> None: ...
    def get_data(self, arg0: str) -> open3d.core.Tensor: ...
    def get_data_as_image(self, *args, **kwargs) -> Any: ...
    def height(self) -> int: ...
    def set_data(self, arg0: str, arg1: open3d.core.Tensor) -> None: ...
    def set_data_from_image(self, arg0: str, arg1) -> None: ...
    def width(self) -> int: ...
    def __copy__(self) -> Frame: ...
    def __deepcopy__(self, arg0: dict) -> Frame: ...

class Model:
    frame_id: int
    transformation_frame_to_world: open3d.core.Tensor
    voxel_grid: Any
    @overload
    def __init__(self, arg0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def extract_pointcloud(self, weight_threshold=..., estimated_number=...) -> Any: ...
    def extract_trianglemesh(
        self, weight_threshold=..., estimated_number=...
    ) -> Any: ...
    def get_current_frame_pose(self) -> open3d.core.Tensor: ...
    def get_hashmap(self) -> open3d.core.HashMap: ...
    def integrate(
        self, input_frame, depth_scale=..., depth_max=..., trunc_voxel_multiplier=...
    ) -> Any: ...
    def synthesize_model_frame(
        self,
        model_frame,
        depth_scale=...,
        depth_min=...,
        depth_max=...,
        trunc_voxel_multiplier=...,
        enable_color=...,
    ) -> Any: ...
    def track_frame_to_model(
        self, input_frame, model_frame, depth_scale=..., depth_max=..., depth_diff=...
    ) -> Any: ...
    def update_frame_pose(self, arg0: int, arg1: open3d.core.Tensor) -> None: ...
    def __copy__(self) -> Model: ...
    def __deepcopy__(self, arg0: dict) -> Model: ...

__all__ = ["Frame", "Model"]
