from typing import Any, Set, overload

import numpy as np
import numpy.typing as npt
import open3d.core
from typing_extensions import Annotated

from . import robust_kernel

class ICPConvergenceCriteria:
    max_iteration: int
    relative_fitness: float
    relative_rmse: float
    @overload
    def __init__(self, arg0: ICPConvergenceCriteria) -> None: ...
    @overload
    def __init__(
        self,
        relative_fitness: float = ...,
        relative_rmse: float = ...,
        max_iteration: int = ...,
    ) -> None: ...
    def __copy__(self) -> ICPConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> ICPConvergenceCriteria: ...

class RegistrationResult:
    correspondences_: open3d.core.Tensor
    fitness: float
    inlier_rmse: float
    transformation: open3d.core.Tensor
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: RegistrationResult) -> None: ...
    def __copy__(self) -> RegistrationResult: ...
    def __deepcopy__(self, arg0: dict) -> RegistrationResult: ...

class TransformationEstimation:
    def __init__(self, *args, **kwargs) -> None: ...
    def compute_rmse(self, source, target, correspondences) -> Any: ...
    def compute_transformation(self, source, target, correspondences) -> Any: ...

class TransformationEstimationForColoredICP(TransformationEstimation):
    kernel: Any
    lambda_geometric: float
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: TransformationEstimationForColoredICP) -> None: ...
    @overload
    def __init__(self, lambda_geometric: float, kernel) -> None: ...
    @overload
    def __init__(self, lambda_geometric: float) -> None: ...
    @overload
    def __init__(self, kernel) -> None: ...
    def __copy__(self) -> TransformationEstimationForColoredICP: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationForColoredICP: ...

class TransformationEstimationPointToPlane(TransformationEstimation):
    kernel: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: TransformationEstimationPointToPlane) -> None: ...
    @overload
    def __init__(self, kernel) -> None: ...
    def __copy__(self) -> TransformationEstimationPointToPlane: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPlane: ...

class TransformationEstimationPointToPoint(TransformationEstimation):
    @overload
    def __init__(self, arg0: TransformationEstimationPointToPoint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __copy__(self) -> TransformationEstimationPointToPoint: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPoint: ...

def evaluate_registration(
    source, target, max_correspondence_distance, transformation=...
) -> Any: ...
def get_information_matrix(
    source, target, max_correspondence_distance, transformation
) -> Any: ...
def icp(*args, **kwargs) -> Any: ...
def multi_scale_icp(*args, **kwargs) -> Any: ...

__all__ = [
    "robust_kernel",
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
]
