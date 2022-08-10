"""Tensor-based registration pipeline."""
from __future__ import annotations

import typing

import open3d.core
import open3d.t.pipelines.registration
import typing_extensions
from typing_extensions import Annotated

from . import robust_kernel

__all__ = [
    "ICPConvergenceCriteria",
    "RegistrationResult",
    "TransformationEstimation",
    "TransformationEstimationForColoredICP",
    "TransformationEstimationPointToPlane",
    "TransformationEstimationPointToPoint",
    "evaluate_registration",
    "get_information_matrix",
    "icp",
    "multi_scale_icp",
    "robust_kernel",
]

class ICPConvergenceCriteria:
    """
    Convergence criteria of ICP. ICP algorithm stops if the relative change of fitness and rmse hit ``relative_fitness`` and ``relative_rmse`` individually, or the iteration number exceeds ``max_iteration``.
    """

    def __copy__(self) -> ICPConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> ICPConvergenceCriteria: ...
    @typing.overload
    def __init__(self, arg0: ICPConvergenceCriteria) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        relative_fitness: float = 1e-06,
        relative_rmse: float = 1e-06,
        max_iteration: int = 30,
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
        If relative change (difference) of inlier RMSE score is lower than ``relative_rmse``, the iteration stops.

        :type: float
        """
    @relative_rmse.setter
    def relative_rmse(self, arg0: float) -> None:
        """
        If relative change (difference) of inlier RMSE score is lower than ``relative_rmse``, the iteration stops.
        """
    pass

class RegistrationResult:
    """
    Registration results.
    """

    def __copy__(self) -> RegistrationResult: ...
    def __deepcopy__(self, arg0: dict) -> RegistrationResult: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RegistrationResult) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def correspondences_(self) -> open3d.core.Tensor:
        """
        Tensor of type Int64 containing indices of corresponding target points, where the value is the target index and the index of the value itself is the source index. It contains -1 as value at index with no correspondence.

        :type: open3d.core.Tensor
        """
    @correspondences_.setter
    def correspondences_(self, arg0: open3d.core.Tensor) -> None:
        """
        Tensor of type Int64 containing indices of corresponding target points, where the value is the target index and the index of the value itself is the source index. It contains -1 as value at index with no correspondence.
        """
    @property
    def fitness(self) -> float:
        """
        float: The overlapping area (# of inlier correspondences / # of points in source). Higher is better.

        :type: float
        """
    @fitness.setter
    def fitness(self, arg0: float) -> None:
        """
        float: The overlapping area (# of inlier correspondences / # of points in source). Higher is better.
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

class TransformationEstimation:
    """
    Base class that estimates a transformation between two point clouds. The virtual function ComputeTransformation() must be implemented in subclasses.
    """

    pass

RobustKernel = typing.NewType("RobustKernel", object)

class TransformationEstimationForColoredICP(TransformationEstimation):
    """
    Class to estimate a transformation between two point clouds using color information
    """

    def __copy__(self) -> TransformationEstimationForColoredICP: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationForColoredICP: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationForColoredICP) -> None: ...
    @typing.overload
    def __init__(
        self, kernel: open3d.t.pipelines.registration.RobustKernel
    ) -> None: ...
    @typing.overload
    def __init__(self, lambda_geometric: float) -> None: ...
    @typing.overload
    def __init__(
        self,
        lambda_geometric: float,
        kernel: open3d.t.pipelines.registration.RobustKernel,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def kernel(self) -> open3d.t.pipelines.registration.RobustKernel:
        """
        Robust Kernel used in the Optimization

        :type: open3d.t.pipelines.registration.RobustKernel
        """
    @kernel.setter
    def kernel(self, arg0: open3d.t.pipelines.registration.RobustKernel) -> None:
        """
        Robust Kernel used in the Optimization
        """
    @property
    def lambda_geometric(self) -> float:
        """
        lambda_geometric

        :type: float
        """
    @lambda_geometric.setter
    def lambda_geometric(self, arg0: float) -> None:
        """
        lambda_geometric
        """
    pass

class TransformationEstimationPointToPlane(TransformationEstimation):
    """
    Class to estimate a transformation for point to plane distance.
    """

    def __copy__(self) -> TransformationEstimationPointToPlane: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPlane: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationPointToPlane) -> None: ...
    @typing.overload
    def __init__(
        self, kernel: open3d.t.pipelines.registration.RobustKernel
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def kernel(self) -> open3d.t.pipelines.registration.RobustKernel:
        """
        Robust Kernel used in the Optimization

        :type: open3d.t.pipelines.registration.RobustKernel
        """
    @kernel.setter
    def kernel(self, arg0: open3d.t.pipelines.registration.RobustKernel) -> None:
        """
        Robust Kernel used in the Optimization
        """
    pass

class TransformationEstimationPointToPoint(TransformationEstimation):
    """
    Class to estimate a transformation for point to point distance.
    """

    def __copy__(self) -> TransformationEstimationPointToPoint: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPoint: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationPointToPoint) -> None: ...
    def __repr__(self) -> str: ...
    pass
