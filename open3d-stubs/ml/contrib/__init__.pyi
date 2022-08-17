from typing import Optional, Set

import numpy as np
import numpy.typing as npt
from open3d.cuda.pybind.ml.contrib import *
from open3d.ml.contrib import *
from typing_extensions import Annotated

def iou_3d_cpu(boxes_a: npt.NDArray, boxes_b: npt.NDArray) -> npt.NDArray: ...
def iou_bev_cpu(boxes_a: npt.NDArray, boxes_b: npt.NDArray) -> npt.NDArray: ...
def subsample(
    points: npt.NDArray,
    features: Optional[npt.NDArray] = ...,
    classes: Optional[npt.NDArray] = ...,
    sampleDl: float = ...,
    verbose: int = ...,
) -> object: ...
def subsample_batch(
    points: npt.NDArray,
    batches: npt.NDArray,
    features: Optional[npt.NDArray] = ...,
    classes: Optional[npt.NDArray] = ...,
    sampleDl: float = ...,
    method: str = ...,
    max_p: int = ...,
    verbose: int = ...,
) -> tuple: ...

__all__ = ["iou_3d_cpu", "iou_bev_cpu", "subsample", "subsample_batch"]
