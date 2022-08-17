from typing import Any, Set, overload

import numpy as np
import numpy.typing as npt
from typing_extensions import Annotated

@overload
def seed(seed) -> Any: ...
@overload
def seed(int) -> Any: ...

__all__ = ["seed", "seed"]
