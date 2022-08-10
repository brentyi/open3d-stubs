"""Tensor DenseSLAM pipeline."""
from __future__ import annotations

import typing

import open3d.core
import open3d.t.geometry
import open3d.t.geometry_extensions
import open3d.t.pipelines.slam
from typing_extensions import Annotated

__all__ = ["Frame", "Model"]

class Frame:
    """
    A frame container that stores a map from keys (color, depth) to tensor images.
    """

    def __copy__(self) -> Frame: ...
    def __deepcopy__(self, arg0: dict) -> Frame: ...
    def get_data(self, arg0: str) -> open3d.core.Tensor:
        """
        Get a 2D tensor from a image from the given key in the map.
        """
    def get_data_as_image(self, arg0: str) -> open3d.t.geometry.Image:
        """
        Get a 2D image from from the given key in the map.
        """
    def height(self) -> int: ...
    def set_data(self, arg0: str, arg1: open3d.core.Tensor) -> None:
        """
        Set a 2D tensor to a image to the given key in the map.
        """
    def set_data_from_image(self, arg0: str, arg1: open3d.t.geometry.Image) -> None:
        """
        Set a 2D image to the given key in the map.
        """
    def width(self) -> int: ...
    pass

class Model:
    """
    Volumetric model for Dense SLAM.
    """

    def __copy__(self) -> Model: ...
    def __deepcopy__(self, arg0: dict) -> Model: ...
    def get_current_frame_pose(self) -> open3d.core.Tensor: ...
    def get_hashmap(self) -> open3d.core.HashMap:
        """
        Get the underlying hash map from 3D coordinates to voxel blocks.
        """
    def update_frame_pose(self, arg0: int, arg1: open3d.core.Tensor) -> None: ...
    @property
    def frame_id(self) -> int:
        """
        Get the current frame index in a sequence.

        :type: int
        """
    @frame_id.setter
    def frame_id(self, arg0: int) -> None:
        """
        Get the current frame index in a sequence.
        """
    @property
    def transformation_frame_to_world(self) -> open3d.core.Tensor:
        """
        Get the 4x4 transformation matrix from the current frame to the world frame.

        :type: open3d.core.Tensor
        """
    @transformation_frame_to_world.setter
    def transformation_frame_to_world(self, arg0: open3d.core.Tensor) -> None:
        """
        Get the 4x4 transformation matrix from the current frame to the world frame.
        """
    @property
    def voxel_grid(self) -> open3d.t.geometry.VoxelBlockGrid:
        """
        Get the maintained VoxelBlockGrid.

        :type: open3d.t.geometry.VoxelBlockGrid
        """
    @voxel_grid.setter
    def voxel_grid(self, arg0: open3d.t.geometry.VoxelBlockGrid) -> None:
        """
        Get the maintained VoxelBlockGrid.
        """
    pass
