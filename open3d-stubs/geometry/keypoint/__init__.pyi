from typing import Any, Set

import numpy as np
import numpy.typing as npt
from typing_extensions import Annotated

def compute_iss_keypoints(
    input,
    salient_radius=...,
    non_max_radius=...,
    gamma_21=...,
    gamma_32=...,
    min_neighbors=...,
) -> Any: ...

__all__ = ["compute_iss_keypoints"]
