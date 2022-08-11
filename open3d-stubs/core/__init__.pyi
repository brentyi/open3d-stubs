from __future__ import annotations

import typing

import numpy as np
import open3d.core
import typing_extensions
from typing_extensions import Annotated

from . import cuda, kernel, nns

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Blob",
    "Device",
    "Dtype",
    "DynamicSizeVector",
    "HashMap",
    "HashSet",
    "Scalar",
    "SizeVector",
    "Tensor",
    "addmm",
    "append",
    "bool",
    "bool8",
    "concatenate",
    "cuda",
    "det",
    "float32",
    "float64",
    "int16",
    "int32",
    "int64",
    "int8",
    "inv",
    "kernel",
    "lstsq",
    "lu",
    "lu_ipiv",
    "matmul",
    "maximum",
    "minimum",
    "nns",
    "solve",
    "svd",
    "sycl_demo",
    "tril",
    "triu",
    "triul",
    "uint16",
    "uint32",
    "uint64",
    "uint8",
    "undefined",
]

class Blob:
    pass

class Device:
    """
    Device context specifying device type and device id.
    """

    class DeviceType:
        """
        Members:

          CPU

          CUDA
        """

        def __eq__(self, other: object) -> __builtins__.bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> __builtins__.bool: ...
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
        CPU: open3d.core.Device.DeviceType  # value = <DeviceType.CPU: 0>
        CUDA: open3d.core.Device.DeviceType  # value = <DeviceType.CUDA: 1>
        __members__: dict  # value = {'CPU': <DeviceType.CPU: 0>, 'CUDA': <DeviceType.CUDA: 1>}
        pass
    def __ene__(self, arg0: Device) -> __builtins__.bool: ...
    def __eq__(self, arg0: Device) -> __builtins__.bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: open3d.core.Device.DeviceType, arg1: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def get_id(self) -> int: ...
    def get_type(self) -> open3d.core.Device.DeviceType: ...
    CPU: open3d.core.Device.DeviceType  # value = <DeviceType.CPU: 0>
    CUDA: open3d.core.Device.DeviceType  # value = <DeviceType.CUDA: 1>
    __hash__ = None
    pass

class Dtype:
    """
    Open3D data types.
    """

    def __ene__(self, arg0: Dtype) -> __builtins__.bool: ...
    def __eq__(self, arg0: Dtype) -> __builtins__.bool: ...
    def __hash__(self) -> int: ...
    def __init__(
        self, arg0: open3d.core.Dtype.DtypeCode, arg1: int, arg2: str
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def byte_code(self) -> open3d.core.Dtype.DtypeCode: ...
    def byte_size(self) -> int: ...
    DtypeCode = typing.NewType("DtypeCode", object)
    Bool: open3d.core.Dtype  # value = Bool
    Float32: open3d.core.Dtype  # value = open3d.core.Dtype.Float32
    Float64: open3d.core.Dtype  # value = Float64
    Int16: open3d.core.Dtype  # value = Int16
    Int32: open3d.core.Dtype  # value = Int32
    Int64: open3d.core.Dtype  # value = open3d.core.Dtype.Int64
    Int8: open3d.core.Dtype  # value = Int8
    UInt16: open3d.core.Dtype  # value = UInt16
    UInt32: open3d.core.Dtype  # value = UInt32
    UInt64: open3d.core.Dtype  # value = UInt64
    UInt8: open3d.core.Dtype  # value = UInt8
    Undefined: open3d.core.Dtype  # value = Undefined
    pass

class DynamicSizeVector:
    """
    A vector of integers for specifying shape, strides, etc. Some elements can be None.
    """

    def __bool__(self) -> __builtins__.bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: typing.Optional[int]) -> __builtins__.bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: DynamicSizeVector) -> __builtins__.bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> typing.Optional[int]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> DynamicSizeVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: DynamicSizeVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: DynamicSizeVector) -> __builtins__.bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: typing.Optional[int]) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: DynamicSizeVector) -> None: ...
    def append(self, x: typing.Optional[int]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: typing.Optional[int]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: DynamicSizeVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: typing.Optional[int]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> typing.Optional[int]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> typing.Optional[int]: ...
    def remove(self, x: typing.Optional[int]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class HashMap:
    """
    A HashMap is an unordered map from key to value wrapped by Tensors.
    """

    def active_buf_indices(self) -> Tensor:
        """
        Get the buffer indices corresponding to active entries in the hash map.
        """
    def capacity(self) -> int:
        """
        Get the capacity of the hash map.
        """
    def clone(self) -> HashMap:
        """
        Clone the hash map, including the data structure and the data buffers.
        """
    def cpu(self) -> HashMap:
        """
        Transfer the hash map to CPU. If the hash map is already on CPU, no copy will be performed.
        """
    def key_tensor(self) -> Tensor:
        """
        Get the key tensor stored in the buffer.
        """
    def size(self) -> int:
        """
        Get the size of the hash map.
        """
    def value_tensors(self) -> typing.List[Tensor]:
        """
        Get the list of value tensors stored in the buffer.
        """
    @property
    def device(self) -> Device:
        """
        :type: Device
        """
    @property
    def is_cpu(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    @property
    def is_cuda(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    pass

class HashSet:
    """
    A HashSet is an unordered set of keys wrapped by Tensors.
    """

    def active_buf_indices(self) -> Tensor:
        """
        Get the buffer indices corresponding to active entries in the hash set.
        """
    def capacity(self) -> int:
        """
        Get the capacity of the hash set.
        """
    def clone(self) -> HashSet:
        """
        Clone the hash set, including the data structure and the data buffers.
        """
    def cpu(self) -> HashSet:
        """
        Transfer the hash set to CPU. If the hash set is already on CPU, no copy will be performed.
        """
    def key_tensor(self) -> Tensor:
        """
        Get the key tensor stored in the buffer.
        """
    def size(self) -> int:
        """
        Get the size of the hash set.
        """
    @property
    def device(self) -> Device:
        """
        :type: Device
        """
    @property
    def is_cpu(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    @property
    def is_cuda(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    pass

class Scalar:
    """
    A Scalar can store one of {double, int64, bool}.
    """

    @typing.overload
    def __init__(self, arg0: __builtins__.bool) -> None: ...
    @typing.overload
    def __init__(self, arg0: float) -> None: ...
    @typing.overload
    def __init__(self, arg0: int) -> None: ...
    pass

class SizeVector:
    """
    A vector of integers for specifying shape, strides, etc.
    """

    def __bool__(self) -> __builtins__.bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: int) -> __builtins__.bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: SizeVector) -> __builtins__.bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> SizeVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: SizeVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: SizeVector) -> __builtins__.bool: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: int) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: SizeVector) -> None: ...
    def append(self, x: int) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: int) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: SizeVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: int) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> int:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> int: ...
    def remove(self, x: int) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

DLPackCapsule = typing.NewType("DLPackCapsule", object)

class Tensor:
    """
    A Tensor is a view of a data Blob with shape, stride, data_ptr.
    """

    def T(self) -> Tensor:
        """
        Transpose <=2-D tensor by swapping dimension 0 and 1.0-D and 1-D Tensor remains the same.
        """
    @typing.overload
    def __add__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __add__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __add__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __add__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __and__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __and__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __and__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __and__(self, arg0: int) -> Tensor: ...
    def __bool__(self) -> __builtins__.bool: ...
    @typing.overload
    def __div__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __div__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __div__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __div__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __eq__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __eq__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __eq__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __eq__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __floordiv__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __floordiv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __floordiv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __floordiv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ge__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __ge__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ge__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ge__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: list) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: np.ndarray) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Tensor: ...
    @typing.overload
    def __getitem__(self, arg0: tuple) -> Tensor: ...
    @typing.overload
    def __gt__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __gt__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __gt__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __gt__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __iadd__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __iadd__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __iadd__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __iadd__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __iand__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __iand__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __iand__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __iand__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __idiv__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __idiv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __idiv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __idiv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ifloordiv__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __ifloordiv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ifloordiv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ifloordiv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __imul__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __imul__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __imul__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __imul__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ior__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __ior__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ior__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ior__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __isub__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __isub__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __isub__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __isub__(self, arg0: int) -> Tensor: ...
    def __iter__(self) -> typing.Iterator: ...
    @typing.overload
    def __itruediv__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __itruediv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __itruediv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __itruediv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ixor__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __ixor__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ixor__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ixor__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __le__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __le__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __le__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __le__(self, arg0: int) -> Tensor: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __lt__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __lt__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __lt__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __lt__(self, arg0: int) -> Tensor: ...
    def __matmul__(self, arg0: Tensor) -> Tensor:
        """
        Computes matrix multiplication of a 2D tensor with another tensor of compatible shape.
        """
    @typing.overload
    def __mul__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __mul__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __mul__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __mul__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ne__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __ne__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ne__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ne__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __or__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __or__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __or__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __or__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __radd__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __radd__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __radd__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rand__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rand__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rand__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rdiv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rdiv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rdiv__(self, arg0: int) -> Tensor: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __rfloordiv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rfloordiv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rfloordiv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rmul__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rmul__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rmul__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __ror__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __ror__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __ror__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rsub__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rsub__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rsub__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rtruediv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rtruediv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rtruediv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __rxor__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __rxor__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __rxor__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: Tensor, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: __builtins__.bool, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: list, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: np.ndarray, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: typing.Any) -> Tensor: ...
    @typing.overload
    def __setitem__(self, arg0: tuple, arg1: typing.Any) -> Tensor: ...
    def __str__(self) -> str: ...
    @typing.overload
    def __sub__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __sub__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __sub__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __sub__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __truediv__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __truediv__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __truediv__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __truediv__(self, arg0: int) -> Tensor: ...
    @typing.overload
    def __xor__(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def __xor__(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def __xor__(self, arg0: float) -> Tensor: ...
    @typing.overload
    def __xor__(self, arg0: int) -> Tensor: ...
    def abs(self) -> Tensor: ...
    def abs_(self) -> Tensor: ...
    @typing.overload
    def add(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def add(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def add(self, arg0: float) -> Tensor: ...
    @typing.overload
    def add(self, arg0: int) -> Tensor: ...
    @typing.overload
    def add_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def add_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def add_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def add_(self, arg0: int) -> Tensor: ...
    def all(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor:
        """
        Returns true if all elements in the tensor are true. Only works for boolean tensors.
        """
    def any(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor:
        """
        Returns true if any elements in the tensor are true. Only works for boolean tensors.
        """
    def append(self, values: Tensor, axis: typing.Optional[int] = None) -> Tensor:
        """
        Appends the `values` tensor, along the given axis and returns
        a copy of the original tensor. Both the tensors must have same data-type
        device, and number of dimensions. All dimensions must be the same, except the
        dimension along the axis the tensors are to be appended.

        This is the similar to NumPy's semantics:
        - https://np.org/doc/stable/reference/generated/np.append.html

        Returns:
            A copy of the tensor with `values` appended to axis. Note that append
            does not occur in-place: a new array is allocated and filled. If axis
            is None, out is a flattened tensor.

        Example:
            >>> a = o3d.core.Tensor([[0, 1], [2, 3]])
            >>> b = o3d.core.Tensor([[4, 5]])
            >>> a.append(b, axis = 0)
            [[0 1],
             [2 3],
             [4 5]]
            Tensor[shape={3, 2}, stride={2, 1}, Int64, CPU:0, 0x55555abc6b00]

            >>> a.append(b)
            [0 1 2 3 4 5]
            Tensor[shape={6}, stride={1}, Int64, CPU:0, 0x55555abc6b70]
        """
    @staticmethod
    @typing.overload
    def arange(
        start: typing.Optional[float],
        stop: float,
        step: typing.Optional[float] = None,
        dtype: typing.Optional[Dtype] = None,
        device: typing.Optional[Device] = None,
    ) -> Tensor:
        """
        Create a 1D tensor with evenly spaced values in the given interval.

        Create a 1D tensor with evenly spaced values in the given interval.

        Create a 1D tensor with evenly spaced values in the given interval.

        Create a 1D tensor with evenly spaced values in the given interval.
        """
    @staticmethod
    @typing.overload
    def arange(
        start: typing.Optional[int],
        stop: int,
        step: typing.Optional[int] = None,
        dtype: typing.Optional[Dtype] = None,
        device: typing.Optional[Device] = None,
    ) -> Tensor: ...
    @staticmethod
    @typing.overload
    def arange(
        stop: float,
        dtype: typing.Optional[Dtype] = None,
        device: typing.Optional[Device] = None,
    ) -> Tensor: ...
    @staticmethod
    @typing.overload
    def arange(
        stop: int,
        dtype: typing.Optional[Dtype] = None,
        device: typing.Optional[Device] = None,
    ) -> Tensor: ...
    def argmax(self, dim: typing.Optional[SizeVector] = None) -> Tensor: ...
    def argmin(self, dim: typing.Optional[SizeVector] = None) -> Tensor: ...
    def ceil(self) -> Tensor: ...
    @typing.overload
    def clip(self, arg0: __builtins__.bool, arg1: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def clip(self, arg0: float, arg1: float) -> Tensor: ...
    @typing.overload
    def clip(self, arg0: int, arg1: int) -> Tensor: ...
    @typing.overload
    def clip_(self, arg0: __builtins__.bool, arg1: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def clip_(self, arg0: float, arg1: float) -> Tensor: ...
    @typing.overload
    def clip_(self, arg0: int, arg1: int) -> Tensor: ...
    def clone(self) -> Tensor:
        """
        Copy Tensor to the same device.
        """
    def contiguous(self) -> Tensor:
        """
        Returns a contiguous tensor containing the same data in the same device.  If the tensor is already contiguous, the same underlying memory will be used.
        """
    def cos(self) -> Tensor: ...
    def cos_(self) -> Tensor: ...
    def cpu(self) -> Tensor:
        """
        Transfer the tensor to CPU. If the tensor is already on CPU, no copy will be performed.
        """
    def cuda(self, device_id: int = 0) -> Tensor:
        """
        Transfer the tensor to a CUDA device. If the tensor is already on the specified CUDA device, no copy will be performed.
        """
    def det(self) -> float:
        """
        Compute the determinant of a 2D square tensor.
        """
    @staticmethod
    def diag(arg0: Tensor) -> Tensor: ...
    @typing.overload
    def div(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def div(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def div(self, arg0: float) -> Tensor: ...
    @typing.overload
    def div(self, arg0: int) -> Tensor: ...
    @typing.overload
    def div_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def div_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def div_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def div_(self, arg0: int) -> Tensor: ...
    @typing.overload
    def eq(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def eq(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def eq(self, arg0: float) -> Tensor: ...
    @typing.overload
    def eq(self, arg0: int) -> Tensor: ...
    @typing.overload
    def eq_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def eq_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def eq_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def eq_(self, arg0: int) -> Tensor: ...
    def exp(self) -> Tensor: ...
    def exp_(self) -> Tensor: ...
    @staticmethod
    def eye(
        n: int,
        dtype: typing.Optional[Dtype] = None,
        device: typing.Optional[Device] = None,
    ) -> Tensor:
        """
        Create an identity matrix of size n x n.
        """
    def floor(self) -> Tensor: ...
    @staticmethod
    def from_dlpack(arg0: DLPackCapsule) -> Tensor: ...
    @staticmethod
    def from_numpy(arg0: np.ndarray) -> Tensor: ...
    @typing.overload
    def ge(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def ge(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def ge(self, arg0: float) -> Tensor: ...
    @typing.overload
    def ge(self, arg0: int) -> Tensor: ...
    @typing.overload
    def ge_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def ge_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def ge_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def ge_(self, arg0: int) -> Tensor: ...
    @typing.overload
    def gt(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def gt(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def gt(self, arg0: float) -> Tensor: ...
    @typing.overload
    def gt(self, arg0: int) -> Tensor: ...
    @typing.overload
    def gt_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def gt_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def gt_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def gt_(self, arg0: int) -> Tensor: ...
    def inv(self) -> Tensor:
        """
        Computes the matrix inverse of the square matrix self with LU factorization and returns the result.
        """
    def is_contiguous(self) -> __builtins__.bool:
        """
        Returns True if the underlying memory buffer is contiguous.
        """
    def isfinite(self) -> Tensor: ...
    def isinf(self) -> Tensor: ...
    def isnan(self) -> Tensor: ...
    def issame(self, arg0: Tensor) -> __builtins__.bool:
        """
        Returns true iff the tensor is the other tensor. This means that, the two tensors have the same underlying memory, device, dtype, shape, strides and etc.
        """
    def item(self) -> object:
        """
        Helper function to return the scalar value of a scalar tensor. The tensor must be 0 - dimensional (i.e. have an empty shape).
        """
    @typing.overload
    def le(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def le(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def le(self, arg0: float) -> Tensor: ...
    @typing.overload
    def le(self, arg0: int) -> Tensor: ...
    @typing.overload
    def le_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def le_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def le_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def le_(self, arg0: int) -> Tensor: ...
    @staticmethod
    def load(file_name: str) -> Tensor:
        """
        Load tensor from Numpy's npy format.
        """
    @typing.overload
    def logical_and(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_and(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_and(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_and(self, arg0: int) -> Tensor: ...
    @typing.overload
    def logical_and_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_and_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_and_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_and_(self, arg0: int) -> Tensor: ...
    def logical_not(self) -> Tensor: ...
    def logical_not_(self) -> Tensor: ...
    @typing.overload
    def logical_or(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_or(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_or(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_or(self, arg0: int) -> Tensor: ...
    @typing.overload
    def logical_or_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_or_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_or_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_or_(self, arg0: int) -> Tensor: ...
    @typing.overload
    def logical_xor(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_xor(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_xor(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_xor(self, arg0: int) -> Tensor: ...
    @typing.overload
    def logical_xor_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def logical_xor_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def logical_xor_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def logical_xor_(self, arg0: int) -> Tensor: ...
    def lstsq(self, B: Tensor) -> Tensor:
        """
        Solves the linear system AX = B with QR decomposition and returns X. A is a (m, n) matrix with m >= n.
        """
    @typing.overload
    def lt(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def lt(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def lt(self, arg0: float) -> Tensor: ...
    @typing.overload
    def lt(self, arg0: int) -> Tensor: ...
    @typing.overload
    def lt_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def lt_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def lt_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def lt_(self, arg0: int) -> Tensor: ...
    def lu_ipiv(self) -> typing.Tuple[Tensor, Tensor]:
        """
        Computes LU factorisation of the 2D square tensor, using A = P * L * U;
        where P is the permutation matrix, L is the lower-triangular matrix with
        diagonal elements as 1.0 and U is the upper-triangular matrix, and returns
        tuple `output` tensor of shape {n,n} and `ipiv` tensor of shape {n}, where
        {n,n} is the shape of input tensor.

        Returns:
            ipiv: ipiv is a 1D integer pivot indices tensor. It contains the pivot
                indices, indicating row i of the matrix was interchanged with row
                ipiv[i]
            output: It has L as lower triangular values and U as upper triangle
                values including the main diagonal (diagonal elements of L to be
                taken as unity).

        Example:
            >>> ipiv, output = a.lu_ipiv()
        """
    def matmul(self, arg0: Tensor) -> Tensor:
        """
        Computes matrix multiplication of a 2D tensor with another tensor of compatible shape.
        """
    def max(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor: ...
    def mean(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor: ...
    def min(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor: ...
    @typing.overload
    def mul(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def mul(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def mul(self, arg0: float) -> Tensor: ...
    @typing.overload
    def mul(self, arg0: int) -> Tensor: ...
    @typing.overload
    def mul_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def mul_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def mul_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def mul_(self, arg0: int) -> Tensor: ...
    @typing.overload
    def ne(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def ne(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def ne(self, arg0: float) -> Tensor: ...
    @typing.overload
    def ne(self, arg0: int) -> Tensor: ...
    @typing.overload
    def ne_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def ne_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def ne_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def ne_(self, arg0: int) -> Tensor: ...
    def neg(self) -> Tensor: ...
    def neg_(self) -> Tensor: ...
    def num_elements(self) -> int: ...
    def numpy(self) -> np.ndarray: ...
    def prod(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor: ...
    def round(self) -> Tensor: ...
    def save(self, file_name: str) -> None:
        """
        Save tensor to Numpy's npy format.
        """
    def sin(self) -> Tensor: ...
    def sin_(self) -> Tensor: ...
    def solve(self, B: Tensor) -> Tensor:
        """
        Solves the linear system AX = B with LU decomposition and returns X.  A must be a square matrix.
        """
    def sqrt(self) -> Tensor: ...
    def sqrt_(self) -> Tensor: ...
    @typing.overload
    def sub(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def sub(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def sub(self, arg0: float) -> Tensor: ...
    @typing.overload
    def sub(self, arg0: int) -> Tensor: ...
    @typing.overload
    def sub_(self, arg0: Tensor) -> Tensor: ...
    @typing.overload
    def sub_(self, arg0: __builtins__.bool) -> Tensor: ...
    @typing.overload
    def sub_(self, arg0: float) -> Tensor: ...
    @typing.overload
    def sub_(self, arg0: int) -> Tensor: ...
    def sum(
        self,
        dim: typing.Optional[SizeVector] = None,
        keepdim: __builtins__.bool = False,
    ) -> Tensor: ...
    def svd(self) -> typing.Tuple[Tensor, Tensor, Tensor]:
        """
        Computes the matrix SVD decomposition :math:`A = U S V^T` and returns the result.  Note :math:`V^T` (V transpose) is returned instead of :math:`V`.
        """
    def to_dlpack(self) -> DLPackCapsule: ...
    def trunc(self) -> Tensor: ...
    @property
    def blob(self) -> Blob:
        """
        :type: Blob
        """
    @property
    def device(self) -> Device:
        """
        :type: Device
        """
    @property
    def dtype(self) -> Dtype:
        """
        :type: Dtype
        """
    @property
    def is_cpu(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    @property
    def is_cuda(self) -> __builtins__.bool:
        """
        :type: __builtins__.bool
        """
    @property
    def ndim(self) -> int:
        """
        :type: int
        """
    @property
    def shape(self) -> SizeVector:
        """
        :type: SizeVector
        """
    @property
    def strides(self) -> SizeVector:
        """
        :type: SizeVector
        """
    __hash__ = None
    pass

def addmm(input: Tensor, A: Tensor, B: Tensor, alpha: float, beta: float) -> Tensor:
    """
    Function to perform addmm of two 2D tensors with compatible shapes. Specifically this function returns output = alpha * A @ B + beta * input.
    """

def append(self: Tensor, values: Tensor, axis: typing.Optional[int] = None) -> Tensor:
    """
    Appends the `values` tensor to the `self` tensor, along the
    given axis and returns a new tensor. Both the tensors must have same data-type
    device, and number of dimensions. All dimensions must be the same, except the
    dimension along the axis the tensors are to be appended.

    This is the same as NumPy's semantics:
    - https://np.org/doc/stable/reference/generated/np.append.html

    Returns:
        A copy of the `self` tensor with `values` appended to axis. Note that
        append does not occur in-place: a new array is allocated and filled.
        If axis is null, out is a flattened tensor.

    Example:
        >>> o3d.core.append([[0, 1], [2, 3]], [[4, 5]], axis = 0)
        [[0 1],
         [2 3],
         [4 5]]
        Tensor[shape={3, 2}, stride={2, 1}, Int64, CPU:0, 0x55555abc6b00]

        >>> o3d.core.append([[0, 1], [2, 3]], [[4, 5]])
        [0 1 2 3 4 5]
        Tensor[shape={6}, stride={1}, Int64, CPU:0, 0x55555abc6b70]
    """

def concatenate(tensors: typing.List[Tensor], axis: typing.Optional[int] = 0) -> Tensor:
    """
    Concatenates the list of tensors in their order, along the given
    axis into a new tensor. All the tensors must have same data-type, device, and
    number of dimensions. All dimensions must be the same, except the dimension
    along the axis the tensors are to be concatenated.
    Using Concatenate for a single tensor, the tensor is split along its first
    dimension (length), and concatenated along the axis.

    This is the same as NumPy's semantics:
    - https://np.org/doc/stable/reference/generated/np.concatenate.html

    Returns:
         A new tensor with the values of list of tensors concatenated in order,
         along the given axis.

    Example:
        >>> a = o3d.core.Tensor([[0, 1], [2, 3]])
        >>> b = o3d.core.Tensor([[4, 5]])
        >>> c = o3d.core.Tensor([[6, 7])
        >>> o3d.core.concatenate((a, b, c), 0)
        [[0 1],
         [2 3],
         [4 5],
         [6 7],
         [8 9]]
        Tensor[shape={5, 2}, stride={2, 1}, Int64, CPU:0, 0x55b454b09390]
    """

def det(A: Tensor) -> float:
    """
    Function to compute determinant of a 2D square tensor.
    """

def inv(A: Tensor) -> Tensor:
    """
    Function to inverse a square 2D tensor.
    """

def lstsq(A: Tensor, B: Tensor) -> Tensor:
    """
    Function to solve X for a linear system AX = B where A is a full rank matrix.
    """

def lu(A: Tensor, permute_l: __builtins__.bool = False) -> tuple:
    """
    Function to compute LU factorisation of a square 2D tensor.
    """

def lu_ipiv(A: Tensor) -> tuple:
    """
    Function to compute LU factorisation of a square 2D tensor.
    """

def matmul(A: Tensor, B: Tensor) -> Tensor:
    """
    Function to perform matrix multiplication of two 2D tensors with compatible shapes.
    """

def maximum(input: Tensor, other: Tensor) -> Tensor:
    """
    Computes the element-wise maximum of input and other. The tensors
    must have same data type and device.
    If input.GetShape() != other.GetShape(), then they will be broadcasted to a
    common shape (which becomes the shape of the output).
    """

def minimum(input: Tensor, other: Tensor) -> Tensor:
    """
    Computes the element-wise minimum of input and other. The tensors
    must have same data type and device.
    If input.GetShape() != other.GetShape(), then they will be broadcasted to a
    common shape (which becomes the shape of the output).
    """

def solve(A: Tensor, B: Tensor) -> Tensor:
    """
    Function to solve X for a linear system AX = B where A is a square matrix
    """

def svd(A: Tensor) -> tuple:
    """
    Function to decompose A with A = U S VT.
    """

def sycl_demo() -> int:
    pass

def tril(A: Tensor, diagonal: int = 0) -> Tensor:
    """
    Function to get lower triangular matrix, below diagonal
    """

def triu(A: Tensor, diagonal: int = 0) -> Tensor:
    """
    Function to get upper triangular matrix, above diagonal
    """

def triul(A: Tensor, diagonal: int = 0) -> tuple:
    """
    Function to get both upper and lower triangular matrix
    """

bool: open3d.core.Dtype  # value = Bool
bool8: open3d.core.Dtype  # value = Bool
float32: open3d.core.Dtype  # value = open3d.core.Dtype.Float32
float64: open3d.core.Dtype  # value = Float64
int16: open3d.core.Dtype  # value = Int16
int32: open3d.core.Dtype  # value = Int32
int64: open3d.core.Dtype  # value = open3d.core.Dtype.Int64
int8: open3d.core.Dtype  # value = Int8
uint16: open3d.core.Dtype  # value = UInt16
uint32: open3d.core.Dtype  # value = UInt32
uint64: open3d.core.Dtype  # value = UInt64
uint8: open3d.core.Dtype  # value = UInt8
undefined: open3d.core.Dtype  # value = Undefined
