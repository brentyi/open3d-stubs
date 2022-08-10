from __future__ import annotations

import os
import typing

import open3d.ml.vis
import typing_extensions
from typing_extensions import Annotated

__all__ = []

_build_config = {
    "BUILD_TENSORFLOW_OPS": False,
    "BUILD_PYTORCH_OPS": False,
    "BUILD_CUDA_MODULE": False,
    "BUILD_SYCL_MODULE": False,
    "BUILD_AZURE_KINECT": False,
    "BUILD_LIBREALSENSE": False,
    "BUILD_SHARED_LIBS": False,
    "BUILD_GUI": True,
    "ENABLE_HEADLESS_RENDERING": False,
    "BUILD_JUPYTER_EXTENSION": False,
    "BUNDLE_OPEN3D_ML": False,
    "GLIBCXX_USE_CXX11_ABI": False,
    "CMAKE_BUILD_TYPE": "Release",
    "CUDA_VERSION": "",
    "CUDA_GENCODES": "",
    "Tensorflow_VERSION": "",
    "Pytorch_VERSION": "",
    "WITH_OPENMP": True,
}
