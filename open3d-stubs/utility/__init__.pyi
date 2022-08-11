from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.utility
import typing_extensions
from typing_extensions import Annotated

from . import random

_Shape = typing.Tuple[int, ...]

__all__ = [
    "Debug",
    "DoubleVector",
    "Error",
    "Info",
    "IntVector",
    "Matrix3dVector",
    "Matrix4dVector",
    "Vector2dVector",
    "Vector2iVector",
    "Vector3dVector",
    "Vector3iVector",
    "Vector4iVector",
    "VerbosityContextManager",
    "VerbosityLevel",
    "Warning",
    "get_verbosity_level",
    "random",
    "reset_print_function",
    "set_verbosity_level",
]

class DoubleVector:
    """
    Convert float64 numpy array of shape ``(n,)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: float) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> DoubleVector: ...
    def __deepcopy__(self, arg0: dict) -> DoubleVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: DoubleVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> DoubleVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: DoubleVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: DoubleVector) -> bool: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: float) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: DoubleVector) -> None: ...
    def append(self, x: float) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: float) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: DoubleVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: float) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> float:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> float: ...
    def remove(self, x: float) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class IntVector:
    """
    Convert int32 numpy array of shape ``(n,)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: int) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> IntVector: ...
    def __deepcopy__(self, arg0: dict) -> IntVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: IntVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> IntVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: IntVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: IntVector) -> bool: ...
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
    def __setitem__(self, arg0: slice, arg1: IntVector) -> None: ...
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
    def extend(self, L: IntVector) -> None:
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

class Matrix3dVector:
    """
    Convert float64 numpy array of shape ``(n, 3, 3)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.float64], (3, 3)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Matrix3dVector: ...
    def __deepcopy__(self, arg0: dict) -> Matrix3dVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Matrix3dVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Matrix3dVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Matrix3dVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Matrix3dVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.float64], (3, 3)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Matrix3dVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.float64], (3, 3)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.float64], (3, 3)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Matrix3dVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.float64], (3, 3)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.float64], (3, 3)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Matrix4dVector:
    """
    Convert float64 numpy array of shape ``(n, 4, 4)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.float64], (4, 4)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Matrix4dVector: ...
    def __deepcopy__(self, arg0: dict) -> Matrix4dVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Matrix4dVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Matrix4dVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Matrix4dVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Matrix4dVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.float64], (4, 4)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Matrix4dVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.float64], (4, 4)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Matrix4dVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.float64], (4, 4)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Vector2dVector:
    """
    Convert float64 numpy array of shape ``(n, 2)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.float64], (2, 1)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Vector2dVector: ...
    def __deepcopy__(self, arg0: dict) -> Vector2dVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Vector2dVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.float64], (2, 1)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Vector2dVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Annotated[npt.NDArray[np.float64]]) -> None: ...
    @typing.overload
    def __init__(self, arg0: Vector2dVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Vector2dVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.float64], (2, 1)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Vector2dVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.float64], (2, 1)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.float64], (2, 1)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Vector2dVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.float64], (2, 1)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.float64], (2, 1)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.float64], (2, 1)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.float64], (2, 1)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Vector2iVector:
    """
    Convert int32 numpy array of shape ``(n, 2)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.int32], (2, 1)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Vector2iVector: ...
    def __deepcopy__(self, arg0: dict) -> Vector2iVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Vector2iVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.int32], (2, 1)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Vector2iVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Annotated[npt.NDArray[np.int32]]) -> None: ...
    @typing.overload
    def __init__(self, arg0: Vector2iVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Vector2iVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.int32], (2, 1)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Vector2iVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.int32], (2, 1)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.int32], (2, 1)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Vector2iVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.int32], (2, 1)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.int32], (2, 1)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.int32], (2, 1)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.int32], (2, 1)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Vector3dVector:
    """
    Convert float64 numpy array of shape ``(n, 3)`` to Open3D format.

    Example usage

    .. code-block. python

        import open3d
        import numpy as np

        pcd = open3d.geometry.PointCloud()
        np_points = np.random.rand(100, 3)

        # From numpy to Open3D
        pcd.points = open3d.utility.Vector3dVector(np_points)

        # From Open3D to numpy
        np_points = np.asarray(pcd.points)
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.float64], (3, 1)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Vector3dVector: ...
    def __deepcopy__(self, arg0: dict) -> Vector3dVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Vector3dVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Vector3dVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Annotated[npt.NDArray[np.float64]]) -> None: ...
    @typing.overload
    def __init__(self, arg0: Vector3dVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Vector3dVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Vector3dVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.float64], (3, 1)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Vector3dVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.float64], (3, 1)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Vector3iVector:
    """
    Convert int32 numpy array of shape ``(n, 3)`` to Open3D format..

    Example usage

    .. code-block. python

        import open3d
        import numpy as np

        # Example mesh
        # x, y coordinates:
        # [0: (-1, 2)]__________[1: (1, 2)]
        #             \        /\
        #              \  (0) /  \
        #               \    / (1)\
        #                \  /      \
        #      [2: (0, 0)]\/________\[3: (2, 0)]
        #
        # z coordinate: 0

        mesh = open3d.geometry.TriangleMesh()
        np_vertices = np.array([[-1, 2, 0],
                                [1, 2, 0],
                                [0, 0, 0],
                                [2, 0, 0]])
        np_triangles = np.array([[0, 2, 1],
                                 [1, 2, 3]]).astype(np.int32)
        mesh.vertices = open3d.Vector3dVector(np_vertices)

        # From numpy to Open3D
        mesh.triangles = open3d.Vector3iVector(np_triangles)

        # From Open3D to numpy
        np_triangles = np.asarray(mesh.triangles)
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.int32], (3, 1)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Vector3iVector: ...
    def __deepcopy__(self, arg0: dict) -> Vector3iVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Vector3iVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.int32], (3, 1)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Vector3iVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Annotated[npt.NDArray[np.int32]]) -> None: ...
    @typing.overload
    def __init__(self, arg0: Vector3iVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Vector3iVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.int32], (3, 1)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Vector3iVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.int32], (3, 1)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.int32], (3, 1)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Vector3iVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.int32], (3, 1)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.int32], (3, 1)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.int32], (3, 1)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.int32], (3, 1)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class Vector4iVector:
    """
    Convert int numpy array of shape ``(n, 4)`` to Open3D format.
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Annotated[npt.NDArray[np.int32], (4, 1)]) -> bool:
        """
        Return true the container contains ``x``
        """
    def __copy__(self) -> Vector4iVector: ...
    def __deepcopy__(self, arg0: dict) -> Vector4iVector: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: Vector4iVector) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Annotated[npt.NDArray[np.int32], (4, 1)]:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> Vector4iVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Annotated[npt.NDArray[np.int32]]) -> None: ...
    @typing.overload
    def __init__(self, arg0: Vector4iVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: Vector4iVector) -> bool: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def __setitem__(
        self, arg0: int, arg1: Annotated[npt.NDArray[np.int32], (4, 1)]
    ) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: Vector4iVector) -> None: ...
    def append(self, x: Annotated[npt.NDArray[np.int32], (4, 1)]) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Annotated[npt.NDArray[np.int32], (4, 1)]) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: Vector4iVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Annotated[npt.NDArray[np.int32], (4, 1)]) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Annotated[npt.NDArray[np.int32], (4, 1)]:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Annotated[npt.NDArray[np.int32], (4, 1)]: ...
    def remove(self, x: Annotated[npt.NDArray[np.int32], (4, 1)]) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None
    pass

class VerbosityContextManager:
    """
    A context manager to temporally change the verbosity level of Open3D
    """

    def __enter__(self) -> None:
        """
        Enter the context manager
        """
    def __exit__(self, arg0: object, arg1: object, arg2: object) -> None:
        """
        Exit the context manager
        """
    def __init__(self, level: VerbosityLevel) -> None:
        """
        Create a VerbosityContextManager with a given VerbosityLevel
        """
    pass

class VerbosityLevel:
    """
    Enum class for VerbosityLevel.
    """

    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
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
    Debug: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Debug: 3>
    Error: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Error: 0>
    Info: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Info: 2>
    Warning: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Warning: 1>
    __members__: dict  # value = {'Error': <VerbosityLevel.Error: 0>, 'Warning': <VerbosityLevel.Warning: 1>, 'Info': <VerbosityLevel.Info: 2>, 'Debug': <VerbosityLevel.Debug: 3>}
    pass

def reset_print_function() -> None:
    pass

Debug: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Debug: 3>
Error: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Error: 0>
Info: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Info: 2>
Warning: open3d.utility.VerbosityLevel  # value = <VerbosityLevel.Warning: 1>
