"""Tensor odometry pipeline."""
from __future__ import annotations

import typing

import open3d.core
import open3d.t.pipelines.odometry
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "Hybrid",
    "Intensity",
    "Method",
    "OdometryConvergenceCriteria",
    "OdometryLossParams",
    "OdometryResult",
    "PointToPlane",
    "compute_odometry_result_hybrid",
    "compute_odometry_result_intensity",
    "compute_odometry_result_point_to_plane",
    "rgbd_odometry_multi_scale",
]

class Method:
    """
    Tensor odometry estimation method.

    Members:

      PointToPlane

      Intensity

      Hybrid
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
    Hybrid: open3d.t.pipelines.odometry.Method  # value = <Method.Hybrid: 2>
    Intensity: open3d.t.pipelines.odometry.Method  # value = <Method.Intensity: 1>
    PointToPlane: open3d.t.pipelines.odometry.Method  # value = <Method.PointToPlane: 0>
    __members__: dict  # value = {'PointToPlane': <Method.PointToPlane: 0>, 'Intensity': <Method.Intensity: 1>, 'Hybrid': <Method.Hybrid: 2>}
    pass

class OdometryConvergenceCriteria:
    """
    Convergence criteria of odometry. Odometry algorithm stops if the relative change of fitness and rmse hit ``relative_fitness`` and ``relative_rmse`` individually, or the iteration number exceeds ``max_iteration``.
    """

    def __copy__(self) -> OdometryConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> OdometryConvergenceCriteria: ...
    @typing.overload
    def __init__(self, arg0: OdometryConvergenceCriteria) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        max_iteration: int,
        relative_rmse: float = 1e-06,
        relative_fitness: float = 1e-06,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def max_iteration(self) -> int:
        """
        Maximum iteration before iteration stops.

        :type: int
        """
    @max_iteration.setter
    def max_iteration(self, arg0: int) -> None:
        """
        Maximum iteration before iteration stops.
        """
    @property
    def relative_fitness(self) -> float:
        """
        If relative change (difference) of fitness score is lower than ``relative_fitness``, the iteration stops.

        :type: float
        """
    @relative_fitness.setter
    def relative_fitness(self, arg0: float) -> None:
        """
        If relative change (difference) of fitness score is lower than ``relative_fitness``, the iteration stops.
        """
    @property
    def relative_rmse(self) -> float:
        """
        If relative change (difference) of inliner RMSE score is lower than ``relative_rmse``, the iteration stops.

        :type: float
        """
    @relative_rmse.setter
    def relative_rmse(self, arg0: float) -> None:
        """
        If relative change (difference) of inliner RMSE score is lower than ``relative_rmse``, the iteration stops.
        """
    pass

class OdometryLossParams:
    """
    Odometry loss parameters.
    """

    def __copy__(self) -> OdometryLossParams: ...
    def __deepcopy__(self, arg0: dict) -> OdometryLossParams: ...
    @typing.overload
    def __init__(self, arg0: OdometryLossParams) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        depth_outlier_trunc: float = 0.07,
        depth_huber_delta: float = 0.05,
        intensity_huber_delta: float = 0.1,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def depth_huber_delta(self) -> float:
        """
        float: Huber norm parameter used in depth loss.

        :type: float
        """
    @depth_huber_delta.setter
    def depth_huber_delta(self, arg0: float) -> None:
        """
        float: Huber norm parameter used in depth loss.
        """
    @property
    def depth_outlier_trunc(self) -> float:
        """
        float: Depth difference threshold used to filter projective associations.

        :type: float
        """
    @depth_outlier_trunc.setter
    def depth_outlier_trunc(self, arg0: float) -> None:
        """
        float: Depth difference threshold used to filter projective associations.
        """
    @property
    def intensity_huber_delta(self) -> float:
        """
        float: Huber norm parameter used in intensity loss.

        :type: float
        """
    @intensity_huber_delta.setter
    def intensity_huber_delta(self, arg0: float) -> None:
        """
        float: Huber norm parameter used in intensity loss.
        """
    pass

class OdometryResult:
    """
    Odometry results.
    """

    def __copy__(self) -> OdometryResult: ...
    def __deepcopy__(self, arg0: dict) -> OdometryResult: ...
    def __init__(self, arg0: OdometryResult) -> None:
        """
        Copy constructor

        2. __init__(self: open3d.t.pipelines.odometry.OdometryResult, transformation: open3d.core.Tensor = [[1.0 0.0 0.0 0.0],
         [0.0 1.0 0.0 0.0],
         [0.0 0.0 1.0 0.0],
         [0.0 0.0 0.0 1.0]]
        Tensor[shape={4, 4}, stride={4, 1}, Float64, CPU:0, 0x55ebf8ea8f80], inlier_rmse: float = 0.0, fitness: float = 0.0) -> None
        """
    def __repr__(self) -> str: ...
    @property
    def fitness(self) -> float:
        """
        float: The overlapping area (# of inlier correspondences / # of points in target). Higher is better.

        :type: float
        """
    @fitness.setter
    def fitness(self, arg0: float) -> None:
        """
        float: The overlapping area (# of inlier correspondences / # of points in target). Higher is better.
        """
    @property
    def inlier_rmse(self) -> float:
        """
        float: RMSE of all inlier correspondences. Lower is better.

        :type: float
        """
    @inlier_rmse.setter
    def inlier_rmse(self, arg0: float) -> None:
        """
        float: RMSE of all inlier correspondences. Lower is better.
        """
    @property
    def transformation(self) -> open3d.core.Tensor:
        """
        ``4 x 4`` float64 tensor on CPU: The estimated transformation matrix.

        :type: open3d.core.Tensor
        """
    @transformation.setter
    def transformation(self, arg0: open3d.core.Tensor) -> None:
        """
        ``4 x 4`` float64 tensor on CPU: The estimated transformation matrix.
        """
    pass

Hybrid: open3d.t.pipelines.odometry.Method  # value = <Method.Hybrid: 2>
Intensity: open3d.t.pipelines.odometry.Method  # value = <Method.Intensity: 1>
PointToPlane: open3d.t.pipelines.odometry.Method  # value = <Method.PointToPlane: 0>
