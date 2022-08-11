from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.camera
import open3d.geometry
import open3d.utility
import typing_extensions
from typing_extensions import Annotated

from . import keypoint

_Shape = typing.Tuple[int, ...]

__all__ = [
    "All",
    "Average",
    "AxisAlignedBoundingBox",
    "Color",
    "DeformAsRigidAsPossibleEnergy",
    "FilterScope",
    "Gaussian3",
    "Gaussian5",
    "Gaussian7",
    "Geometry",
    "Geometry2D",
    "Geometry3D",
    "HalfEdge",
    "HalfEdgeTriangleMesh",
    "Image",
    "ImageFilterType",
    "KDTreeFlann",
    "KDTreeSearchParam",
    "KDTreeSearchParamHybrid",
    "KDTreeSearchParamKNN",
    "KDTreeSearchParamRadius",
    "LineSet",
    "MeshBase",
    "Normal",
    "Octree",
    "OctreeColorLeafNode",
    "OctreeInternalNode",
    "OctreeInternalPointNode",
    "OctreeLeafNode",
    "OctreeNode",
    "OctreeNodeInfo",
    "OctreePointColorLeafNode",
    "OrientedBoundingBox",
    "PointCloud",
    "Quadric",
    "RGBDImage",
    "SimplificationContraction",
    "Smoothed",
    "Sobel3dx",
    "Sobel3dy",
    "Spokes",
    "TetraMesh",
    "TriangleMesh",
    "Vertex",
    "Voxel",
    "VoxelGrid",
    "get_rotation_matrix_from_axis_angle",
    "get_rotation_matrix_from_quaternion",
    "get_rotation_matrix_from_xyz",
    "get_rotation_matrix_from_xzy",
    "get_rotation_matrix_from_yxz",
    "get_rotation_matrix_from_yzx",
    "get_rotation_matrix_from_zxy",
    "get_rotation_matrix_from_zyx",
    "keypoint",
]

class Geometry:
    """
    The base geometry class.
    """

    class Type:
        """
        Enum class for Geometry types.
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
        HalfEdgeTriangleMesh: open3d.geometry.Geometry.Type  # value = <Type.HalfEdgeTriangleMesh: 7>
        Image: open3d.geometry.Geometry.Type  # value = <Type.Image: 8>
        LineSet: open3d.geometry.Geometry.Type  # value = <Type.LineSet: 4>
        PointCloud: open3d.geometry.Geometry.Type  # value = <Type.PointCloud: 1>
        RGBDImage: open3d.geometry.Geometry.Type  # value = <Type.RGBDImage: 9>
        TetraMesh: open3d.geometry.Geometry.Type  # value = <Type.TetraMesh: 10>
        TriangleMesh: open3d.geometry.Geometry.Type  # value = <Type.TriangleMesh: 6>
        Unspecified: open3d.geometry.Geometry.Type  # value = <Type.Unspecified: 0>
        VoxelGrid: open3d.geometry.Geometry.Type  # value = <Type.VoxelGrid: 2>
        __members__: dict  # value = {'Unspecified': <Type.Unspecified: 0>, 'PointCloud': <Type.PointCloud: 1>, 'VoxelGrid': <Type.VoxelGrid: 2>, 'LineSet': <Type.LineSet: 4>, 'TriangleMesh': <Type.TriangleMesh: 6>, 'HalfEdgeTriangleMesh': <Type.HalfEdgeTriangleMesh: 7>, 'Image': <Type.Image: 8>, 'RGBDImage': <Type.RGBDImage: 9>, 'TetraMesh': <Type.TetraMesh: 10>}
        pass
    HalfEdgeTriangleMesh: open3d.geometry.Geometry.Type  # value = <Type.HalfEdgeTriangleMesh: 7>
    Image: open3d.geometry.Geometry.Type  # value = <Type.Image: 8>
    LineSet: open3d.geometry.Geometry.Type  # value = <Type.LineSet: 4>
    PointCloud: open3d.geometry.Geometry.Type  # value = <Type.PointCloud: 1>
    RGBDImage: open3d.geometry.Geometry.Type  # value = <Type.RGBDImage: 9>
    TetraMesh: open3d.geometry.Geometry.Type  # value = <Type.TetraMesh: 10>
    TriangleMesh: open3d.geometry.Geometry.Type  # value = <Type.TriangleMesh: 6>
    Unspecified: open3d.geometry.Geometry.Type  # value = <Type.Unspecified: 0>
    VoxelGrid: open3d.geometry.Geometry.Type  # value = <Type.VoxelGrid: 2>
    pass

class DeformAsRigidAsPossibleEnergy:
    """
    Members:

      Spokes : is the original energy as formulated in orkine and Alexa, "As-Rigid-As-Possible Surface Modeling", 2007.

      Smoothed : adds a rotation smoothing term to the rotations.
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
    Smoothed: open3d.geometry.DeformAsRigidAsPossibleEnergy  # value = <DeformAsRigidAsPossibleEnergy.Smoothed: 1>
    Spokes: open3d.geometry.DeformAsRigidAsPossibleEnergy  # value = <DeformAsRigidAsPossibleEnergy.Spokes: 0>
    __members__: dict  # value = {'Spokes': <DeformAsRigidAsPossibleEnergy.Spokes: 0>, 'Smoothed': <DeformAsRigidAsPossibleEnergy.Smoothed: 1>}
    pass

class FilterScope:
    """
    Members:

      All : All properties (color, normal, vertex position) are filtered.

      Color : Only the color values are filtered.

      Normal : Only the normal values are filtered.

      Vertex : Only the vertex positions are filtered.
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
    All: open3d.geometry.FilterScope  # value = <FilterScope.All: 0>
    Color: open3d.geometry.FilterScope  # value = <FilterScope.Color: 1>
    Normal: open3d.geometry.FilterScope  # value = <FilterScope.Normal: 2>
    Vertex: open3d.geometry.FilterScope  # value = <FilterScope.Vertex: 3>
    __members__: dict  # value = {'All': <FilterScope.All: 0>, 'Color': <FilterScope.Color: 1>, 'Normal': <FilterScope.Normal: 2>, 'Vertex': <FilterScope.Vertex: 3>}
    pass

class Geometry3D(Geometry):
    """
    The base geometry class for 3D geometries.
    """

    def get_oriented_bounding_box(
        self, robust: bool = False
    ) -> open3d.geometry.OrientedBoundingBox:
        """
        Returns the oriented bounding box for the geometry.

        Computes the oriented bounding box based on the PCA of the convex hull.
        The returned bounding box is an approximation to the minimal bounding box.

        Args:
             robust (bool): If set to true uses a more robust method which works in
                  degenerate cases but introduces noise to the points coordinates.

        Returns:
             open3d.geometry.OrientedBoundingBox: The oriented bounding box. The
             bounding box is oriented such that the axes are ordered with respect to
             the principal components.
        """
    @staticmethod
    def get_rotation_matrix_from_axis_angle(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_quaternion(
        rotation: Annotated[npt.NDArray[np.float64], (4, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_xyz(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_xzy(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_yxz(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_yzx(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_zxy(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    @staticmethod
    def get_rotation_matrix_from_zyx(
        rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> Annotated[npt.NDArray[np.float64], (3, 3)]: ...
    pass

class Geometry2D(Geometry):
    """
    The base geometry class for 2D geometries.
    """

    pass

class AxisAlignedBoundingBox(Geometry3D, Geometry):
    """
    Class that defines an axis_aligned box that can be computed from 3D geometries, The axis aligned bounding box uses the coordinate axes for bounding box generation.
    """

    def __copy__(self) -> AxisAlignedBoundingBox: ...
    def __deepcopy__(self, arg0: dict) -> AxisAlignedBoundingBox: ...
    def __iadd__(self, arg0: AxisAlignedBoundingBox) -> AxisAlignedBoundingBox: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create an AxisAlignedBoundingBox from min bounds and max bounds in x, y and z
        """
    @typing.overload
    def __init__(self, arg0: AxisAlignedBoundingBox) -> None: ...
    @typing.overload
    def __init__(
        self,
        min_bound: Annotated[npt.NDArray[np.float64], (3, 1)],
        max_bound: Annotated[npt.NDArray[np.float64], (3, 1)],
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @color.setter
    def color(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    @property
    def max_bound(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @max_bound.setter
    def max_bound(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    @property
    def min_bound(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @min_bound.setter
    def min_bound(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    pass

class HalfEdge:
    """
    HalfEdge class contains vertex, triangle info about a half edge, as well as relations of next and twin half edge.
    """

    def __copy__(self) -> HalfEdge: ...
    def __deepcopy__(self, arg0: dict) -> HalfEdge: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: HalfEdge) -> None: ...
    def __repr__(self) -> str: ...
    def is_boundary(self) -> bool:
        """
        Returns ``True`` iff the half edge is the boundary (has not twin, i.e. twin index == -1).
        """
    @property
    def next(self) -> int:
        """
        int: Index of the next HalfEdge in the same triangle.

        :type: int
        """
    @next.setter
    def next(self, arg0: int) -> None:
        """
        int: Index of the next HalfEdge in the same triangle.
        """
    @property
    def triangle_index(self) -> int:
        """
        int: Index of the triangle containing this half edge

        :type: int
        """
    @triangle_index.setter
    def triangle_index(self, arg0: int) -> None:
        """
        int: Index of the triangle containing this half edge
        """
    @property
    def twin(self) -> int:
        """
        int: Index of the twin HalfEdge

        :type: int
        """
    @twin.setter
    def twin(self, arg0: int) -> None:
        """
        int: Index of the twin HalfEdge
        """
    @property
    def vertex_indices(self) -> Annotated[npt.NDArray[np.int32], (2, 1)]:
        """
        :type: Annotated[npt.NDArray[np.int32], (2, 1)]
        """
    @vertex_indices.setter
    def vertex_indices(self, arg0: Annotated[npt.NDArray[np.int32], (2, 1)]) -> None:
        pass
    pass

class MeshBase(Geometry3D, Geometry):
    """
    MeshBase class. Triangle mesh contains vertices. Optionally, the mesh may also contain vertex normals and vertex colors.
    """

    def __add__(self, arg0: MeshBase) -> MeshBase: ...
    def __copy__(self) -> MeshBase: ...
    def __deepcopy__(self, arg0: dict) -> MeshBase: ...
    def __iadd__(self, arg0: MeshBase) -> MeshBase: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: MeshBase) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def vertex_colors(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of vertices.

        :type: open3d.utility.Vector3dVector
        """
    @vertex_colors.setter
    def vertex_colors(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of vertices.
        """
    @property
    def vertex_normals(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex normals.

        :type: open3d.utility.Vector3dVector
        """
    @vertex_normals.setter
    def vertex_normals(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex normals.
        """
    @property
    def vertices(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.

        :type: open3d.utility.Vector3dVector
        """
    @vertices.setter
    def vertices(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.
        """
    pass

class Image(Geometry2D, Geometry):
    """
    The image class stores image with customizable width, height, num of channels and bytes per channel.
    """

    def __copy__(self) -> Image: ...
    def __deepcopy__(self, arg0: dict) -> Image: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Image) -> None: ...
    def __repr__(self) -> str: ...
    def flip_horizontal(self) -> Image:
        """
        Function to flip image horizontally (from left to right)
        """
    def flip_vertical(self) -> Image:
        """
        Function to flip image vertically (upside down)
        """
    pass

class ImageFilterType:
    """
    Enum class for Image filter types.
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
    Gaussian3: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian3: 0>
    Gaussian5: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian5: 1>
    Gaussian7: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian7: 2>
    Sobel3dx: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Sobel3dx: 3>
    Sobel3dy: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Sobel3dy: 4>
    __members__: dict  # value = {'Gaussian3': <ImageFilterType.Gaussian3: 0>, 'Gaussian5': <ImageFilterType.Gaussian5: 1>, 'Gaussian7': <ImageFilterType.Gaussian7: 2>, 'Sobel3dx': <ImageFilterType.Sobel3dx: 3>, 'Sobel3dy': <ImageFilterType.Sobel3dy: 4>}
    pass

class KDTreeFlann:
    """
    KDTree with FLANN for nearest neighbor search.
    """

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, data: Annotated[npt.NDArray[np.float64], ("m, n")]) -> None: ...
    @typing.overload
    def __init__(self, feature: open3d.pipelines.registration.Feature) -> None: ...
    @typing.overload
    def __init__(self, geometry: Geometry) -> None: ...
    pass

class KDTreeSearchParam:
    """
    Base class for KDTree search parameters.
    """

    class Type:
        """
        Enum class for Geometry types.
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
        HybridSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.HybridSearch: 2>
        KNNSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.KNNSearch: 0>
        RadiusSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.RadiusSearch: 1>
        __members__: dict  # value = {'KNNSearch': <Type.KNNSearch: 0>, 'RadiusSearch': <Type.RadiusSearch: 1>, 'HybridSearch': <Type.HybridSearch: 2>}
        pass
    HybridSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.HybridSearch: 2>
    KNNSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.KNNSearch: 0>
    RadiusSearch: open3d.geometry.KDTreeSearchParam.Type  # value = <Type.RadiusSearch: 1>
    pass

class KDTreeSearchParamHybrid(KDTreeSearchParam):
    """
    KDTree search parameters for hybrid KNN and radius search.
    """

    def __init__(self, radius: float, max_nn: int) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def max_nn(self) -> int:
        """
        At maximum, ``max_nn`` neighbors will be searched.

        :type: int
        """
    @max_nn.setter
    def max_nn(self, arg0: int) -> None:
        """
        At maximum, ``max_nn`` neighbors will be searched.
        """
    @property
    def radius(self) -> float:
        """
        Search radius.

        :type: float
        """
    @radius.setter
    def radius(self, arg0: float) -> None:
        """
        Search radius.
        """
    pass

class KDTreeSearchParamKNN(KDTreeSearchParam):
    """
    KDTree search parameters for pure KNN search.
    """

    def __init__(self, knn: int = 30) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def knn(self) -> int:
        """
        Number of the neighbors that will be searched.

        :type: int
        """
    @knn.setter
    def knn(self, arg0: int) -> None:
        """
        Number of the neighbors that will be searched.
        """
    pass

class KDTreeSearchParamRadius(KDTreeSearchParam):
    """
    KDTree search parameters for pure radius search.
    """

    def __init__(self, radius: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def radius(self) -> float:
        """
        Search radius.

        :type: float
        """
    @radius.setter
    def radius(self, arg0: float) -> None:
        """
        Search radius.
        """
    pass

class LineSet(Geometry3D, Geometry):
    """
    LineSet define a sets of lines in 3D. A typical application is to display the point cloud correspondence pairs.
    """

    def __add__(self, arg0: LineSet) -> LineSet: ...
    def __copy__(self) -> LineSet: ...
    def __deepcopy__(self, arg0: dict) -> LineSet: ...
    def __iadd__(self, arg0: LineSet) -> LineSet: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create a LineSet from given points and line indices
        """
    @typing.overload
    def __init__(self, arg0: LineSet) -> None: ...
    @typing.overload
    def __init__(
        self,
        points: open3d.utility.Vector3dVector,
        lines: open3d.utility.Vector2iVector,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    @typing.overload
    def create_camera_visualization(
        intrinsic: open3d.camera.PinholeCameraIntrinsic,
        extrinsic: Annotated[npt.NDArray[np.float64], (4, 4)],
        scale: float = 1.0,
    ) -> LineSet:
        """
        Factory function to create a LineSet from intrinsic and extrinsic camera matrices

        Factory function to create a LineSet from intrinsic and extrinsic camera matrices
        """
    @staticmethod
    @typing.overload
    def create_camera_visualization(
        view_width_px: int,
        view_height_px: int,
        intrinsic: Annotated[npt.NDArray[np.float64], (3, 3)],
        extrinsic: Annotated[npt.NDArray[np.float64], (4, 4)],
        scale: float = 1.0,
    ) -> LineSet: ...
    @property
    def colors(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_lines, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of lines.

        :type: open3d.utility.Vector3dVector
        """
    @colors.setter
    def colors(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_lines, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of lines.
        """
    @property
    def lines(self) -> open3d.utility.Vector2iVector:
        """
        ``int`` array of shape ``(num_lines, 2)``, use ``np.asarray()`` to access data: Lines denoted by the index of points forming the line.

        :type: open3d.utility.Vector2iVector
        """
    @lines.setter
    def lines(self, arg0: open3d.utility.Vector2iVector) -> None:
        """
        ``int`` array of shape ``(num_lines, 2)``, use ``np.asarray()`` to access data: Lines denoted by the index of points forming the line.
        """
    @property
    def points(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points coordinates.

        :type: open3d.utility.Vector3dVector
        """
    @points.setter
    def points(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points coordinates.
        """
    pass

class HalfEdgeTriangleMesh(MeshBase, Geometry3D, Geometry):
    """
    HalfEdgeTriangleMesh inherits TriangleMesh class with the addition of HalfEdge data structure for each half edge in the mesh as well as related functions.
    """

    def __copy__(self) -> HalfEdgeTriangleMesh: ...
    def __deepcopy__(self, arg0: dict) -> HalfEdgeTriangleMesh: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: HalfEdgeTriangleMesh) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def half_edges(self) -> typing.List[HalfEdge]:
        """
        List of HalfEdge in the mesh

        :type: typing.List[HalfEdge]
        """
    @half_edges.setter
    def half_edges(self, arg0: typing.List[HalfEdge]) -> None:
        """
        List of HalfEdge in the mesh
        """
    @property
    def ordered_half_edge_from_vertex(self) -> typing.List[open3d.utility.IntVector]:
        """
        Counter-clockwise ordered half-edges started from each vertex

        :type: typing.List[open3d.utility.IntVector]
        """
    @ordered_half_edge_from_vertex.setter
    def ordered_half_edge_from_vertex(
        self, arg0: typing.List[open3d.utility.IntVector]
    ) -> None:
        """
        Counter-clockwise ordered half-edges started from each vertex
        """
    @property
    def triangle_normals(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: Triangle normals.

        :type: open3d.utility.Vector3dVector
        """
    @triangle_normals.setter
    def triangle_normals(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: Triangle normals.
        """
    @property
    def triangles(self) -> open3d.utility.Vector3iVector:
        """
        ``int`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: List of triangles denoted by the index of points forming the triangle.

        :type: open3d.utility.Vector3iVector
        """
    @triangles.setter
    def triangles(self, arg0: open3d.utility.Vector3iVector) -> None:
        """
        ``int`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: List of triangles denoted by the index of points forming the triangle.
        """
    pass

class Octree(Geometry3D, Geometry):
    """
    Octree datastructure.
    """

    def __copy__(self) -> Octree: ...
    def __deepcopy__(self, arg0: dict) -> Octree: ...
    def __repr__(self) -> str: ...
    def traverse(self, f: typing.Callable[[OctreeNode, OctreeNodeInfo], bool]) -> None:
        """
        DFS traversal of the octree from the root, with a callback function f being called for each node.
        """
    @property
    def max_depth(self) -> int:
        """
        int: Maximum depth of the octree. The depth is defined as the distance from the deepest leaf node to root. A tree with only the root node has depth 0.

        :type: int
        """
    @max_depth.setter
    def max_depth(self, arg0: int) -> None:
        """
        int: Maximum depth of the octree. The depth is defined as the distance from the deepest leaf node to root. A tree with only the root node has depth 0.
        """
    @property
    def origin(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        (3, 1) float numpy array: Global min bound (include). A point is within bound iff origin <= point < origin + size.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @origin.setter
    def origin(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        (3, 1) float numpy array: Global min bound (include). A point is within bound iff origin <= point < origin + size.
        """
    @property
    def root_node(self) -> OctreeNode:
        """
        OctreeNode: The root octree node.

        :type: OctreeNode
        """
    @root_node.setter
    def root_node(self, arg0: OctreeNode) -> None:
        """
        OctreeNode: The root octree node.
        """
    @property
    def size(self) -> float:
        """
        float: Outer bounding box edge size for the whole octree. A point is within bound iff origin <= point < origin + size.

        :type: float
        """
    @size.setter
    def size(self, arg0: float) -> None:
        """
        float: Outer bounding box edge size for the whole octree. A point is within bound iff origin <= point < origin + size.
        """
    pass

class OctreeNode:
    """
    The base class for octree node.
    """

    def __repr__(self) -> str: ...
    pass

class OctreeInternalNode(OctreeNode):
    """
    OctreeInternalNode class, containing OctreeNode children.
    """

    def __copy__(self) -> OctreeInternalNode: ...
    def __deepcopy__(self, arg0: dict) -> OctreeInternalNode: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def get_init_function() -> typing.Callable[[], OctreeInternalNode]:
        """
        Get lambda function for initializing OctreeInternalNode. When the init function is called, an empty OctreeInternalNode is created.
        """
    @staticmethod
    def get_update_function() -> typing.Callable[[OctreeInternalNode], None]:
        """
        Get lambda function for updating OctreeInternalNode. This update function does nothing.
        """
    @property
    def children(self) -> typing.List[OctreeNode]:
        """
        List of children Nodes.

        :type: typing.List[OctreeNode]
        """
    @children.setter
    def children(self, arg0: typing.List[OctreeNode]) -> None:
        """
        List of children Nodes.
        """
    pass

class OctreeInternalPointNode(OctreeInternalNode, OctreeNode):
    """
    OctreeInternalPointNode class is an OctreeInternalNode with a list of point indices (from point cloud) belonging to children of this node.
    """

    def __copy__(self) -> OctreeInternalPointNode: ...
    def __deepcopy__(self, arg0: dict) -> OctreeInternalPointNode: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def get_init_function() -> typing.Callable[[], OctreeInternalNode]:
        """
        Get lambda function for initializing OctreeInternalPointNode. When the init function is called, an empty OctreeInternalPointNode is created.
        """
    @staticmethod
    def get_update_function(arg0: int) -> typing.Callable[[OctreeInternalNode], None]:
        """
        Get lambda function for updating OctreeInternalPointNode. When called, the update function adds the input point index to the corresponding node's list of indices of children points.
        """
    @property
    def children(self) -> typing.List[OctreeNode]:
        """
        List of children Nodes.

        :type: typing.List[OctreeNode]
        """
    @children.setter
    def children(self, arg0: typing.List[OctreeNode]) -> None:
        """
        List of children Nodes.
        """
    @property
    def indices(self) -> typing.List[int]:
        """
        List of point cloud point indices contained in children nodes.

        :type: typing.List[int]
        """
    @indices.setter
    def indices(self, arg0: typing.List[int]) -> None:
        """
        List of point cloud point indices contained in children nodes.
        """
    pass

class OctreeLeafNode(OctreeNode):
    """
    OctreeLeafNode base class.
    """

    def __eq__(self, other: OctreeLeafNode) -> bool:
        """
        Check equality of OctreeLeafNode.
        """
    def __repr__(self) -> str: ...
    def clone(self) -> OctreeLeafNode:
        """
        Clone this OctreeLeafNode.
        """
    __hash__ = None
    pass

class OctreeColorLeafNode(OctreeLeafNode, OctreeNode):
    """
    OctreeColorLeafNode class is an OctreeLeafNode containing color.
    """

    def __copy__(self) -> OctreeColorLeafNode: ...
    def __deepcopy__(self, arg0: dict) -> OctreeColorLeafNode: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: OctreeColorLeafNode) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def get_init_function() -> typing.Callable[[], OctreeLeafNode]:
        """
        Get lambda function for initializing OctreeLeafNode. When the init function is called, an empty OctreeColorLeafNode is created.
        """
    @staticmethod
    def get_update_function(
        color: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> typing.Callable[[OctreeLeafNode], None]:
        """
        Get lambda function for updating OctreeLeafNode. When called, the update function updates the corresponding node with the input color.
        """
    @property
    def color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        (3, 1) float numpy array: Color of the node.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @color.setter
    def color(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        (3, 1) float numpy array: Color of the node.
        """
    pass

class OctreeNodeInfo:
    """
    OctreeNode's information. OctreeNodeInfo is computed on the fly, not stored with the Node.
    """

    def __repr__(self) -> str: ...
    @property
    def child_index(self) -> int:
        """
        int: Node's child index of itself. For non-root nodes, child_index is 0~7; root node's child_index is -1.

        :type: int
        """
    @child_index.setter
    def child_index(self, arg0: int) -> None:
        """
        int: Node's child index of itself. For non-root nodes, child_index is 0~7; root node's child_index is -1.
        """
    @property
    def depth(self) -> int:
        """
        int: Depth of the node to the root. The root is of depth 0.

        :type: int
        """
    @depth.setter
    def depth(self, arg0: int) -> None:
        """
        int: Depth of the node to the root. The root is of depth 0.
        """
    @property
    def origin(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        (3, 1) float numpy array: Origin coordinate of the node.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @origin.setter
    def origin(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        (3, 1) float numpy array: Origin coordinate of the node.
        """
    @property
    def size(self) -> float:
        """
        float: Size of the node.

        :type: float
        """
    @size.setter
    def size(self, arg0: float) -> None:
        """
        float: Size of the node.
        """
    pass

class OctreePointColorLeafNode(OctreeLeafNode, OctreeNode):
    """
    OctreePointColorLeafNode class is an OctreeLeafNode containing color.
    """

    def __copy__(self) -> OctreePointColorLeafNode: ...
    def __deepcopy__(self, arg0: dict) -> OctreePointColorLeafNode: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: OctreePointColorLeafNode) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def get_init_function() -> typing.Callable[[], OctreeLeafNode]:
        """
        Get lambda function for initializing OctreeLeafNode. When the init function is called, an empty OctreePointColorLeafNode is created.
        """
    @staticmethod
    def get_update_function(
        idx: int, color: Annotated[npt.NDArray[np.float64], (3, 1)]
    ) -> typing.Callable[[OctreeLeafNode], None]:
        """
        Get lambda function for updating OctreeLeafNode. When called, the update function updates the corresponding node with the new point index and the input color.
        """
    @property
    def color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        (3, 1) float numpy array: Color of the node.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @color.setter
    def color(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        (3, 1) float numpy array: Color of the node.
        """
    @property
    def indices(self) -> typing.List[int]:
        """
        List of point cloud point indices contained in this leaf node.

        :type: typing.List[int]
        """
    @indices.setter
    def indices(self, arg0: typing.List[int]) -> None:
        """
        List of point cloud point indices contained in this leaf node.
        """
    pass

class OrientedBoundingBox(Geometry3D, Geometry):
    """
    Class that defines an oriented box that can be computed from 3D geometries.
    """

    def __copy__(self) -> OrientedBoundingBox: ...
    def __deepcopy__(self, arg0: dict) -> OrientedBoundingBox: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create OrientedBoudingBox from center, rotation R and extent in x, y and z direction
        """
    @typing.overload
    def __init__(self, arg0: OrientedBoundingBox) -> None: ...
    @typing.overload
    def __init__(
        self,
        center: Annotated[npt.NDArray[np.float64], (3, 1)],
        R: Annotated[npt.NDArray[np.float64], (3, 3)],
        extent: Annotated[npt.NDArray[np.float64], (3, 1)],
    ) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def create_from_points(
        points: open3d.utility.Vector3dVector, robust: bool = False
    ) -> OrientedBoundingBox:
        """
        Creates the oriented bounding box that encloses the set of points.

        Computes the oriented bounding box based on the PCA of the convex hull.
        The returned bounding box is an approximation to the minimal bounding box.

        Args:
             points (open3d.utility.Vector3dVector): Input points.
             robust (bool): If set to true uses a more robust method which works in
                  degenerate cases but introduces noise to the points coordinates.

        Returns:
             open3d.geometry.OrientedBoundingBox: The oriented bounding box. The
             bounding box is oriented such that the axes are ordered with respect to
             the principal components.
        """
    @property
    def R(self) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
        """
        ``float64`` array of shape ``(3,3 )``

        :type: Annotated[npt.NDArray[np.float64], (3, 3)]
        """
    @R.setter
    def R(self, arg0: Annotated[npt.NDArray[np.float64], (3, 3)]) -> None:
        """
        ``float64`` array of shape ``(3,3 )``
        """
    @property
    def center(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @center.setter
    def center(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    @property
    def color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @color.setter
    def color(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    @property
    def extent(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` array of shape ``(3, )``

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @extent.setter
    def extent(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` array of shape ``(3, )``
        """
    pass

class PointCloud(Geometry3D, Geometry):
    """
    PointCloud class. A point cloud consists of point coordinates, and optionally point colors and point normals.
    """

    def __add__(self, arg0: PointCloud) -> PointCloud: ...
    def __copy__(self) -> PointCloud: ...
    def __deepcopy__(self, arg0: dict) -> PointCloud: ...
    def __iadd__(self, arg0: PointCloud) -> PointCloud: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create a PointCloud from points
        """
    @typing.overload
    def __init__(self, arg0: PointCloud) -> None: ...
    @typing.overload
    def __init__(self, points: open3d.utility.Vector3dVector) -> None: ...
    def __repr__(self) -> str: ...
    def compute_convex_hull(
        self, joggle_inputs: bool = False
    ) -> typing.Tuple[open3d.geometry.TriangleMesh, typing.List[int]]:
        """
        Computes the convex hull of the point cloud.

        Args:
             joggle_inputs (bool): If True allows the algorithm to add random noise to
                  the points to work around degenerate inputs. This adds the 'QJ'
                  option to the qhull command.

        Returns:
             tuple(open3d.geometry.TriangleMesh, list): The triangle mesh of the convex
             hull and the list of point indices that are part of the convex hull.
        """
    def farthest_point_down_sample(self, num_samples: int) -> PointCloud:
        """
        Downsamples input pointcloud into output pointcloud with a set of points has farthest distance. The sample is performed by selecting the farthest point from previous selected points iteratively.
        """
    def has_covariances(self) -> bool:
        """
        Returns ``True`` if the point cloud contains covariances.
        """
    @property
    def colors(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_points, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of points.

        :type: open3d.utility.Vector3dVector
        """
    @colors.setter
    def colors(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_points, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of points.
        """
    @property
    def covariances(self) -> open3d.utility.Matrix3dVector:
        """
        ``float64`` array of shape ``(num_points, 3, 3)``, use ``np.asarray()`` to access data: Points covariances.

        :type: open3d.utility.Matrix3dVector
        """
    @covariances.setter
    def covariances(self, arg0: open3d.utility.Matrix3dVector) -> None:
        """
        ``float64`` array of shape ``(num_points, 3, 3)``, use ``np.asarray()`` to access data: Points covariances.
        """
    @property
    def normals(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points normals.

        :type: open3d.utility.Vector3dVector
        """
    @normals.setter
    def normals(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points normals.
        """
    @property
    def points(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points coordinates.

        :type: open3d.utility.Vector3dVector
        """
    @points.setter
    def points(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_points, 3)``, use ``np.asarray()`` to access data: Points coordinates.
        """
    pass

class RGBDImage(Geometry2D, Geometry):
    """
    RGBDImage is for a pair of registered color and depth images, viewed from the same view, of the same resolution. If you have other format, convert it first.
    """

    def __init__(self) -> None:
        """
        Default constructor
        """
    def __repr__(self) -> str: ...
    @property
    def color(self) -> Image:
        """
        open3d.geometry.Image: The color image.

        :type: Image
        """
    @color.setter
    def color(self, arg0: Image) -> None:
        """
        open3d.geometry.Image: The color image.
        """
    @property
    def depth(self) -> Image:
        """
        open3d.geometry.Image: The depth image.

        :type: Image
        """
    @depth.setter
    def depth(self, arg0: Image) -> None:
        """
        open3d.geometry.Image: The depth image.
        """
    pass

class SimplificationContraction:
    """
    Members:

      Average : The vertex positions are computed by the averaging.

      Quadric : The vertex positions are computed by minimizing the distance to the adjacent triangle planes.
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
    Average: open3d.geometry.SimplificationContraction  # value = <SimplificationContraction.Average: 0>
    Quadric: open3d.geometry.SimplificationContraction  # value = <SimplificationContraction.Quadric: 1>
    __members__: dict  # value = {'Average': <SimplificationContraction.Average: 0>, 'Quadric': <SimplificationContraction.Quadric: 1>}
    pass

class TetraMesh(MeshBase, Geometry3D, Geometry):
    """
    TetraMesh class. Tetra mesh contains vertices and tetrahedra represented by the indices to the vertices.
    """

    def __add__(self, arg0: TetraMesh) -> TetraMesh: ...
    def __copy__(self) -> TetraMesh: ...
    def __deepcopy__(self, arg0: dict) -> TetraMesh: ...
    def __iadd__(self, arg0: TetraMesh) -> TetraMesh: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create a tetrahedra mesh from vertices and tetra indices
        """
    @typing.overload
    def __init__(self, arg0: TetraMesh) -> None: ...
    @typing.overload
    def __init__(
        self,
        vertices: open3d.utility.Vector3dVector,
        tetras: open3d.utility.Vector4iVector,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def tetras(self) -> open3d.utility.Vector4iVector:
        """
        ``int64`` array of shape ``(num_tetras, 4)``, use ``np.asarray()`` to access data: List of tetras denoted by the index of points forming the tetra.

        :type: open3d.utility.Vector4iVector
        """
    @tetras.setter
    def tetras(self, arg0: open3d.utility.Vector4iVector) -> None:
        """
        ``int64`` array of shape ``(num_tetras, 4)``, use ``np.asarray()`` to access data: List of tetras denoted by the index of points forming the tetra.
        """
    @property
    def vertices(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.

        :type: open3d.utility.Vector3dVector
        """
    @vertices.setter
    def vertices(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.
        """
    pass

class TriangleMesh(MeshBase, Geometry3D, Geometry):
    """
    TriangleMesh class. Triangle mesh contains vertices and triangles represented by the indices to the vertices. Optionally, the mesh may also contain triangle normals, vertex normals and vertex colors.
    """

    def __add__(self, arg0: TriangleMesh) -> TriangleMesh: ...
    def __copy__(self) -> TriangleMesh: ...
    def __deepcopy__(self, arg0: dict) -> TriangleMesh: ...
    def __iadd__(self, arg0: TriangleMesh) -> TriangleMesh: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        Create a triangle mesh from vertices and triangle indices
        """
    @typing.overload
    def __init__(self, arg0: TriangleMesh) -> None: ...
    @typing.overload
    def __init__(
        self,
        vertices: open3d.utility.Vector3dVector,
        triangles: open3d.utility.Vector3iVector,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def get_surface_area(self) -> float:
        """
        Function that computes the surface area of the mesh, i.e. the sum of the individual triangle surfaces.
        """
    def get_volume(self) -> float:
        """
        Function that computes the volume of the mesh, under the condition that it is watertight and orientable.
        """
    @property
    def adjacency_list(self) -> typing.List[typing.Set[int]]:
        """
        List of Sets: The set ``adjacency_list[i]`` contains the indices of adjacent vertices of vertex i.

        :type: typing.List[typing.Set[int]]
        """
    @adjacency_list.setter
    def adjacency_list(self, arg0: typing.List[typing.Set[int]]) -> None:
        """
        List of Sets: The set ``adjacency_list[i]`` contains the indices of adjacent vertices of vertex i.
        """
    @property
    def textures(self) -> typing.List[open3d.geometry.Image]:
        """
        open3d.geometry.Image: The texture images.

        :type: typing.List[open3d.geometry.Image]
        """
    @textures.setter
    def textures(self, arg0: typing.List[open3d.geometry.Image]) -> None:
        """
        open3d.geometry.Image: The texture images.
        """
    @property
    def triangle_material_ids(self) -> open3d.utility.IntVector:
        """
        `int` array of shape ``(num_trianges, 1)``, use ``np.asarray()`` to access data: material index associated with each triangle

        :type: open3d.utility.IntVector
        """
    @triangle_material_ids.setter
    def triangle_material_ids(self, arg0: open3d.utility.IntVector) -> None:
        """
        `int` array of shape ``(num_trianges, 1)``, use ``np.asarray()`` to access data: material index associated with each triangle
        """
    @property
    def triangle_normals(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: Triangle normals.

        :type: open3d.utility.Vector3dVector
        """
    @triangle_normals.setter
    def triangle_normals(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: Triangle normals.
        """
    @property
    def triangle_uvs(self) -> open3d.utility.Vector2dVector:
        """
        ``float64`` array of shape ``(3 * num_triangles, 2)``, use ``np.asarray()`` to access data: List of uvs denoted by the index of points forming the triangle.

        :type: open3d.utility.Vector2dVector
        """
    @triangle_uvs.setter
    def triangle_uvs(self, arg0: open3d.utility.Vector2dVector) -> None:
        """
        ``float64`` array of shape ``(3 * num_triangles, 2)``, use ``np.asarray()`` to access data: List of uvs denoted by the index of points forming the triangle.
        """
    @property
    def triangles(self) -> open3d.utility.Vector3iVector:
        """
        ``int`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: List of triangles denoted by the index of points forming the triangle.

        :type: open3d.utility.Vector3iVector
        """
    @triangles.setter
    def triangles(self, arg0: open3d.utility.Vector3iVector) -> None:
        """
        ``int`` array of shape ``(num_triangles, 3)``, use ``np.asarray()`` to access data: List of triangles denoted by the index of points forming the triangle.
        """
    @property
    def vertex_colors(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of vertices.

        :type: open3d.utility.Vector3dVector
        """
    @vertex_colors.setter
    def vertex_colors(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, range ``[0, 1]`` , use ``np.asarray()`` to access data: RGB colors of vertices.
        """
    @property
    def vertex_normals(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex normals.

        :type: open3d.utility.Vector3dVector
        """
    @vertex_normals.setter
    def vertex_normals(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex normals.
        """
    @property
    def vertices(self) -> open3d.utility.Vector3dVector:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.

        :type: open3d.utility.Vector3dVector
        """
    @vertices.setter
    def vertices(self, arg0: open3d.utility.Vector3dVector) -> None:
        """
        ``float64`` array of shape ``(num_vertices, 3)``, use ``np.asarray()`` to access data: Vertex coordinates.
        """
    pass

class Voxel:
    """
    Base Voxel class, containing grid id and color
    """

    def __copy__(self) -> Voxel: ...
    def __deepcopy__(self, arg0: dict) -> Voxel: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Voxel) -> None: ...
    @typing.overload
    def __init__(
        self, grid_index: Annotated[npt.NDArray[np.int32], (3, 1)]
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        grid_index: Annotated[npt.NDArray[np.int32], (3, 1)],
        color: Annotated[npt.NDArray[np.float64], (3, 1)],
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def color(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        Float64 numpy array of shape (3,): Color of the voxel.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @color.setter
    def color(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        Float64 numpy array of shape (3,): Color of the voxel.
        """
    @property
    def grid_index(self) -> Annotated[npt.NDArray[np.int32], (3, 1)]:
        """
        Int numpy array of shape (3,): Grid coordinate index of the voxel.

        :type: Annotated[npt.NDArray[np.int32], (3, 1)]
        """
    @grid_index.setter
    def grid_index(self, arg0: Annotated[npt.NDArray[np.int32], (3, 1)]) -> None:
        """
        Int numpy array of shape (3,): Grid coordinate index of the voxel.
        """
    pass

class VoxelGrid(Geometry3D, Geometry):
    """
    VoxelGrid is a collection of voxels which are aligned in grid.
    """

    def __add__(self, arg0: VoxelGrid) -> VoxelGrid: ...
    def __copy__(self) -> VoxelGrid: ...
    def __deepcopy__(self, arg0: dict) -> VoxelGrid: ...
    def __iadd__(self, arg0: VoxelGrid) -> VoxelGrid: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: VoxelGrid) -> None: ...
    def __repr__(self) -> str: ...
    def get_voxels(self) -> typing.List[Voxel]:
        """
        Returns List of ``Voxel``: Voxels contained in voxel grid. Changes to the voxels returned from this methodare not reflected in the voxel grid.
        """
    @property
    def origin(self) -> Annotated[npt.NDArray[np.float64], (3, 1)]:
        """
        ``float64`` vector of length 3: Coorindate of the origin point.

        :type: Annotated[npt.NDArray[np.float64], (3, 1)]
        """
    @origin.setter
    def origin(self, arg0: Annotated[npt.NDArray[np.float64], (3, 1)]) -> None:
        """
        ``float64`` vector of length 3: Coorindate of the origin point.
        """
    @property
    def voxel_size(self) -> float:
        """
        ``float64`` Size of the voxel.

        :type: float
        """
    @voxel_size.setter
    def voxel_size(self, arg0: float) -> None:
        """
        ``float64`` Size of the voxel.
        """
    pass

def get_rotation_matrix_from_axis_angle(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_quaternion(
    rotation: Annotated[npt.NDArray[np.float64], (4, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_xyz(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_xzy(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_yxz(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_yzx(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_zxy(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

def get_rotation_matrix_from_zyx(
    rotation: Annotated[npt.NDArray[np.float64], (3, 1)]
) -> Annotated[npt.NDArray[np.float64], (3, 3)]:
    pass

All: open3d.geometry.FilterScope  # value = <FilterScope.All: 0>
Average: open3d.geometry.SimplificationContraction  # value = <SimplificationContraction.Average: 0>
Color: open3d.geometry.FilterScope  # value = <FilterScope.Color: 1>
Gaussian3: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian3: 0>
Gaussian5: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian5: 1>
Gaussian7: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Gaussian7: 2>
Normal: open3d.geometry.FilterScope  # value = <FilterScope.Normal: 2>
Quadric: open3d.geometry.SimplificationContraction  # value = <SimplificationContraction.Quadric: 1>
Smoothed: open3d.geometry.DeformAsRigidAsPossibleEnergy  # value = <DeformAsRigidAsPossibleEnergy.Smoothed: 1>
Sobel3dx: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Sobel3dx: 3>
Sobel3dy: open3d.geometry.ImageFilterType  # value = <ImageFilterType.Sobel3dy: 4>
Spokes: open3d.geometry.DeformAsRigidAsPossibleEnergy  # value = <DeformAsRigidAsPossibleEnergy.Spokes: 0>
Vertex: open3d.geometry.FilterScope  # value = <FilterScope.Vertex: 3>
