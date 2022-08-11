from __future__ import annotations

import typing

import open3d.io
import typing_extensions
from typing_extensions import Annotated

from . import rpc

__all__ = [
    "CONTAINS_LINES",
    "CONTAINS_POINTS",
    "CONTAINS_TRIANGLES",
    "CONTENTS_UNKNOWN",
    "FileGeometry",
    "read_feature",
    "read_file_geometry_type",
    "read_image",
    "read_line_set",
    "read_octree",
    "read_pinhole_camera_intrinsic",
    "read_pinhole_camera_parameters",
    "read_pinhole_camera_trajectory",
    "read_point_cloud",
    "read_pose_graph",
    "read_triangle_mesh",
    "read_triangle_model",
    "read_voxel_grid",
    "rpc",
    "write_feature",
    "write_image",
    "write_line_set",
    "write_octree",
    "write_pinhole_camera_intrinsic",
    "write_pinhole_camera_parameters",
    "write_pinhole_camera_trajectory",
    "write_point_cloud",
    "write_pose_graph",
    "write_triangle_mesh",
    "write_voxel_grid",
]

class FileGeometry:
    """
    Geometry types
    """

    def __and__(self, other: object) -> object: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __invert__(self) -> object: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __or__(self, other: object) -> object: ...
    def __rand__(self, other: object) -> object: ...
    def __repr__(self) -> str: ...
    def __ror__(self, other: object) -> object: ...
    def __rxor__(self, other: object) -> object: ...
    def __setstate__(self, state: int) -> None: ...
    def __xor__(self, other: object) -> object: ...
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
    CONTAINS_LINES: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_LINES: 2>
    CONTAINS_POINTS: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_POINTS: 1>
    CONTAINS_TRIANGLES: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_TRIANGLES: 4>
    CONTENTS_UNKNOWN: open3d.io.FileGeometry  # value = <FileGeometry.CONTENTS_UNKNOWN: 0>
    __members__: dict  # value = {'CONTENTS_UNKNOWN': <FileGeometry.CONTENTS_UNKNOWN: 0>, 'CONTAINS_POINTS': <FileGeometry.CONTAINS_POINTS: 1>, 'CONTAINS_LINES': <FileGeometry.CONTAINS_LINES: 2>, 'CONTAINS_TRIANGLES': <FileGeometry.CONTAINS_TRIANGLES: 4>}
    pass

def read_file_geometry_type(arg0: str) -> FileGeometry:
    """
    Returns the type of geometry of the file. This is a faster way of determining the file type than attempting to read the file as a point cloud, mesh, or line set in turn.
    """

CONTAINS_LINES: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_LINES: 2>
CONTAINS_POINTS: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_POINTS: 1>
CONTAINS_TRIANGLES: open3d.io.FileGeometry  # value = <FileGeometry.CONTAINS_TRIANGLES: 4>
CONTENTS_UNKNOWN: open3d.io.FileGeometry  # value = <FileGeometry.CONTENTS_UNKNOWN: 0>
