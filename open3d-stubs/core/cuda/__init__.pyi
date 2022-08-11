from __future__ import annotations

import typing

import open3d.core.cuda
import typing_extensions
from typing_extensions import Annotated

__all__ = ["device_count", "is_available", "release_cache", "synchronize"]

def device_count() -> int:
    """
    Returns the number of available CUDA devices. Returns 0 if Open3D is not compiled with CUDA support.
    """

def is_available() -> bool:
    """
    Returns true if Open3D is compiled with CUDA support and at least one compatible CUDA device is detected.
    """

def release_cache() -> None:
    """
    Releases CUDA memory manager cache. This is typically used for debugging.
    """

def synchronize(device: typing.Optional[open3d.core.Device] = None) -> None:
    """
    Synchronizes CUDA devices. If no device is specified, all CUDA devices will be synchronized. No effect if the specified device is not a CUDA device. No effect if Open3D is not compiled with CUDA support.
    """
