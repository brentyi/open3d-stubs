from __future__ import annotations

import typing

import open3d.core
import open3d.core.nns
import typing_extensions
from typing_extensions import Annotated

__all__ = ["NearestNeighborSearch"]

class NearestNeighborSearch:
    """
    NearestNeighborSearch class for nearest neighbor search. Construct a NearestNeighborSearch object with input dataset_points of shape {n_dataset, d}.
    """

    def __init__(
        self,
        dataset_points: open3d.core.Tensor,
        index_dtype: open3d.core.Dtype = open3d.core.Dtype.Int64,
    ) -> None: ...
    def fixed_radius_index(self, radius: typing.Optional[float] = None) -> bool: ...
    def hybrid_index(self, radius: typing.Optional[float] = None) -> bool: ...
    def knn_index(self) -> bool:
        """
        Set index for knn search.
        """
    def multi_radius_index(self) -> bool:
        """
        Set index for multi-radius search.
        """
    pass
