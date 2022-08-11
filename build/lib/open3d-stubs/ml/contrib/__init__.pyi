from __future__ import annotations

import typing

import numpy as np
import open3d.ml.contrib
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = ["iou_3d_cpu", "iou_bev_cpu", "subsample", "subsample_batch"]

def iou_3d_cpu(boxes_a: np.ndarray, boxes_b: np.ndarray) -> np.ndarray:
    pass

def iou_bev_cpu(boxes_a: np.ndarray, boxes_b: np.ndarray) -> np.ndarray:
    pass

def subsample(
    points: np.ndarray,
    features: typing.Optional[np.ndarray] = None,
    classes: typing.Optional[np.ndarray] = None,
    sampleDl: float = 0.1,
    verbose: int = 0,
) -> object:
    pass

def subsample_batch(
    points: np.ndarray,
    batches: np.ndarray,
    features: typing.Optional[np.ndarray] = None,
    classes: typing.Optional[np.ndarray] = None,
    sampleDl: float = 0.1,
    method: str = "barycenters",
    max_p: int = 0,
    verbose: int = 0,
) -> tuple:
    pass
