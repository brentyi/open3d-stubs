"""Tensor-based input-output handling module."""
from __future__ import annotations

import typing

import open3d.camera
import open3d.core
import open3d.t.io
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "RGBDSensor",
    "RGBDVideoMetadata",
    "RGBDVideoReader",
    "SensorType",
    "read_image",
    "read_point_cloud",
    "write_image",
    "write_point_cloud",
]

class RGBDSensor:
    """
    Interface class for control of RGBD cameras.
    """

    def __repr__(self) -> str: ...
    pass

class RGBDVideoMetadata:
    """
    RGBD Video metadata.
    """

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def color_channels(self) -> int:
        """
        Number of color channels.

        :type: int
        """
    @color_channels.setter
    def color_channels(self, arg0: int) -> None:
        """
        Number of color channels.
        """
    @property
    def color_dt(self) -> open3d.core.Dtype:
        """
        Pixel Dtype for color data.

        :type: open3d.core.Dtype
        """
    @color_dt.setter
    def color_dt(self, arg0: open3d.core.Dtype) -> None:
        """
        Pixel Dtype for color data.
        """
    @property
    def color_format(self) -> str:
        """
        Pixel format for color data

        :type: str
        """
    @color_format.setter
    def color_format(self, arg0: str) -> None:
        """
        Pixel format for color data
        """
    @property
    def depth_dt(self) -> open3d.core.Dtype:
        """
        Pixel Dtype for depth data.

        :type: open3d.core.Dtype
        """
    @depth_dt.setter
    def depth_dt(self, arg0: open3d.core.Dtype) -> None:
        """
        Pixel Dtype for depth data.
        """
    @property
    def depth_format(self) -> str:
        """
        Pixel format for depth data

        :type: str
        """
    @depth_format.setter
    def depth_format(self, arg0: str) -> None:
        """
        Pixel format for depth data
        """
    @property
    def depth_scale(self) -> float:
        """
        Number of depth units per meter (depth in m = depth_pixel_value/depth_scale).

        :type: float
        """
    @depth_scale.setter
    def depth_scale(self, arg0: float) -> None:
        """
        Number of depth units per meter (depth in m = depth_pixel_value/depth_scale).
        """
    @property
    def device_name(self) -> str:
        """
        Capture device name

        :type: str
        """
    @device_name.setter
    def device_name(self, arg0: str) -> None:
        """
        Capture device name
        """
    @property
    def fps(self) -> float:
        """
        Video frame rate (common for both color and depth)

        :type: float
        """
    @fps.setter
    def fps(self, arg0: float) -> None:
        """
        Video frame rate (common for both color and depth)
        """
    @property
    def height(self) -> int:
        """
        Height of the video

        :type: int
        """
    @height.setter
    def height(self, arg0: int) -> None:
        """
        Height of the video
        """
    @property
    def intrinsics(self) -> open3d.camera.PinholeCameraIntrinsic:
        """
        Shared intrinsics between RGB & depth

        :type: open3d.camera.PinholeCameraIntrinsic
        """
    @intrinsics.setter
    def intrinsics(self, arg0: open3d.camera.PinholeCameraIntrinsic) -> None:
        """
        Shared intrinsics between RGB & depth
        """
    @property
    def serial_number(self) -> str:
        """
        Capture device serial number

        :type: str
        """
    @serial_number.setter
    def serial_number(self, arg0: str) -> None:
        """
        Capture device serial number
        """
    @property
    def stream_length_usec(self) -> int:
        """
        Length of the video (usec). 0 for live capture.

        :type: int
        """
    @stream_length_usec.setter
    def stream_length_usec(self, arg0: int) -> None:
        """
        Length of the video (usec). 0 for live capture.
        """
    @property
    def width(self) -> int:
        """
        Width of the video

        :type: int
        """
    @width.setter
    def width(self, arg0: int) -> None:
        """
        Width of the video
        """
    pass

class RGBDVideoReader:
    """
    RGBD Video file reader.
    """

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    pass

class SensorType:
    """
    Sensor type

    Members:

      AZURE_KINECT

      REAL_SENSE
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
    AZURE_KINECT: open3d.t.io.SensorType  # value = <SensorType.AZURE_KINECT: 0>
    REAL_SENSE: open3d.t.io.SensorType  # value = <SensorType.REAL_SENSE: 1>
    __members__: dict  # value = {'AZURE_KINECT': <SensorType.AZURE_KINECT: 0>, 'REAL_SENSE': <SensorType.REAL_SENSE: 1>}
    pass
