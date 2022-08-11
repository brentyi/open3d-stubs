"""Color map optimization pipeline"""
from __future__ import annotations

import typing

import open3d.camera
import open3d.geometry
import open3d.pipelines.color_map
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "NonRigidOptimizerOption",
    "RigidOptimizerOption",
    "run_non_rigid_optimizer",
    "run_rigid_optimizer",
]

class NonRigidOptimizerOption:
    """
    Non Rigid optimizer option class.
    """

    pass

class RigidOptimizerOption:
    """
    Rigid optimizer option class.
    """

    pass

def run_non_rigid_optimizer(
    arg0: open3d.geometry.TriangleMesh,
    arg1: typing.List[open3d.geometry.RGBDImage],
    arg2: open3d.camera.PinholeCameraTrajectory,
    arg3: NonRigidOptimizerOption,
) -> typing.Tuple[open3d.geometry.TriangleMesh, open3d.camera.PinholeCameraTrajectory]:
    """
    Run non-rigid optimization.
    """

def run_rigid_optimizer(
    arg0: open3d.geometry.TriangleMesh,
    arg1: typing.List[open3d.geometry.RGBDImage],
    arg2: open3d.camera.PinholeCameraTrajectory,
    arg3: RigidOptimizerOption,
) -> typing.Tuple[open3d.geometry.TriangleMesh, open3d.camera.PinholeCameraTrajectory]:
    """
    Run rigid optimization.
    """
