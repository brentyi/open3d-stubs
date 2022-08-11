"""Tensor-based geometry defining module."""
from __future__ import annotations

import typing

import open3d.core
import open3d.geometry
import open3d.t.geometry
import open3d.visualization
import open3d.visualization_extensions
from typing_extensions import Annotated

__all__ = [
    "AxisAlignedBoundingBox",
    "Cubic",
    "DrawableGeometry",
    "Geometry",
    "Image",
    "InterpType",
    "Lanczos",
    "LineSet",
    "Linear",
    "Nearest",
    "PointCloud",
    "RGBDImage",
    "RaycastingScene",
    "Super",
    "TensorMap",
    "TriangleMesh",
    "VoxelBlockGrid",
]

class DrawableGeometry:
    """
    Base class for geometry types which can be visualized.
    """

    def has_valid_material(self) -> bool:
        """
        Returns true if the geometry's material is valid.
        """
    @property
    def material(self) -> open3d.visualization.Material:
        """
        :type: open3d.visualization.Material
        """
    @material.setter
    def material(self, arg1: open3d.visualization.Material) -> None:
        pass
    pass

class Geometry:
    """
    The base geometry class.
    """

    @property
    def device(self) -> open3d.core.Device:
        """
        Returns the device of the geometry.

        :type: open3d.core.Device
        """
    @property
    def is_cpu(self) -> bool:
        """
        Returns true if the geometry is on CPU.

        :type: bool
        """
    @property
    def is_cuda(self) -> bool:
        """
        Returns true if the geometry is on CUDA.

        :type: bool
        """
    pass

class AxisAlignedBoundingBox(Geometry, DrawableGeometry):
    """
    A bounding box that is aligned along the coordinate axes
    and defined by the min_bound and max_bound."
    - (min_bound, max_bound): Lower and upper bounds of the bounding box for all
    axes.
        - Usage
            - AxisAlignedBoundingBox.GetMinBound()
            - AxisAlignedBoundingBox.SetMinBound(const core.Tensor &min_bound)
            - AxisAlignedBoundingBox.GetMaxBound()
            - AxisAlignedBoundingBox.SetMaxBound(const core.Tensor &max_bound)
        - Value tensor must have shape {3,}.
        - Value tensor must have the same data type and device.
        - Value tensor can only be float32 (default) or float64.
        - The device of the tensor determines the device of the box.

    - color: Color of the bounding box.
        - Usage
            - AxisAlignedBoundingBox.GetColor()
            - AxisAlignedBoundingBox.SetColor(const core.Tensor &color)
        - Value tensor must have shape {3,}.
        - Value tensor can only be float32 (default) or float64.
        - Value tensor can only be range [0.0, 1.0].
    """

    def __add__(self, arg0: AxisAlignedBoundingBox) -> AxisAlignedBoundingBox:
        """
        Add operation for axis-aligned bounding box.
        The device of ohter box must be the same as the device of the current box.
        """
    def __repr__(self) -> str: ...
    def clone(self) -> AxisAlignedBoundingBox:
        """
        Returns copy of the axis-aligned box on the same device.
        """
    def cpu(self) -> AxisAlignedBoundingBox:
        """
        Transfer the axis-aligned box to CPU. If the axis-aligned box is already on CPU, no copy will be performed.
        """
    def cuda(self, device_id: int = 0) -> AxisAlignedBoundingBox:
        """
        Transfer the axis-aligned box to a CUDA device. If the axis-aligned box is already on the specified CUDA device, no copy will be performed.
        """
    @staticmethod
    def from_legacy(
        box: open3d.geometry.AxisAlignedBoundingBox,
        dtype: open3d.core.Dtype = open3d.core.Dtype.Float32,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> AxisAlignedBoundingBox:
        """
        Create an AxisAlignedBoundingBox from a legacy Open3D axis-aligned box.
        """
    def get_box_points(self) -> open3d.core.Tensor:
        """
        Returns the eight points that define the bounding box. The Return tensor has shape {8, 3} and data type of float32.
        """
    def get_center(self) -> open3d.core.Tensor:
        """
        Returns the center for box coordinates.
        """
    def get_color(self) -> open3d.core.Tensor:
        """
        Returns the color for box.
        """
    def get_extent(self) -> open3d.core.Tensor:
        """
        Get the extent/length of the bounding box in x, y, and z dimension.
        """
    def get_half_extent(self) -> open3d.core.Tensor:
        """
        Returns the half extent of the bounding box.
        """
    def get_max_bound(self) -> open3d.core.Tensor:
        """
        Returns the max bound for box coordinates.
        """
    def get_max_extent(self) -> float:
        """
        Returns the maximum extent, i.e. the maximum of X, Y and Z axis's extents.
        """
    def get_min_bound(self) -> open3d.core.Tensor:
        """
        Returns the min bound for box coordinates.
        """
    def to(
        self, device: open3d.core.Device, copy: bool = False
    ) -> AxisAlignedBoundingBox:
        """
        Transfer the axis-aligned box to a specified device.
        """
    def to_legacy(self) -> open3d.geometry.AxisAlignedBoundingBox:
        """
        Convert to a legacy Open3D axis-aligned box.
        """
    def volume(self) -> float:
        """
        Returns the volume of the bounding box.
        """
    pass

class Image(Geometry):
    """
    The Image class stores image with customizable rols, cols, channels, dtype and device.
    """

    def __repr__(self) -> str: ...
    def as_tensor(self) -> open3d.core.Tensor: ...
    def clip_transform(
        self, scale: float, min_value: float, max_value: float, clip_fill: float = 0.0
    ) -> Image:
        """
        Preprocess a image of shape (rows, cols, channels=1), typically used for a depth image. UInt16 and Float32 Dtypes supported. Each pixel will be transformed by
        x = x / scale
        x = x < min_value ? clip_fill : x
        x = x > max_value ? clip_fill : x
        Use INF, NAN or 0.0 (default) for clip_fill
        """
    def clone(self) -> Image:
        """
        Returns a copy of the Image on the same device.
        """
    def colorize_depth(self, scale: float, min_value: float, max_value: float) -> Image:
        """
        Colorize an input depth image (with Dtype UInt16 or Float32). The image values are divided by scale, then clamped within (min_value, max_value) and finally converted to a 3 channel UInt8 RGB image using the Turbo colormap as a lookup table.
        """
    def cpu(self) -> Image:
        """
        Transfer the image to CPU. If the image is already on CPU, no copy will be performed.
        """
    def create_normal_map(self, invalid_fill: float = 0.0) -> Image:
        """
        Create a normal map of shape (rows, cols, channels=3) in Float32 from a vertex map of shape (rows, cols, channels=1) in Float32 using cross product of V(r, c+1)-V(r, c) and V(r+1, c)-V(r, c). The input vertex map is expected to be the output of create_vertex_map. You may need to start with a filtered depth  image (e.g. with filter_bilateral) to obtain good results.
        """
    def create_vertex_map(
        self, intrinsics: open3d.core.Tensor, invalid_fill: float = 0.0
    ) -> Image:
        """
        Create a vertex map of shape (rows, cols, channels=3) in Float32 from an image of shape (rows, cols, channels=1) in Float32 using unprojection. The input depth is expected to be the output of clip_transform.
        """
    def cuda(self, device_id: int = 0) -> Image:
        """
        Transfer the image to a CUDA device. If the image is already on the specified CUDA device, no copy will be performed.
        """
    def dilate(self, kernel_size: int = 3) -> Image:
        """
        Return a new image after performing morphological dilation. Supported datatypes are UInt8, UInt16 and Float32 with {1, 3, 4} channels. An 8-connected neighborhood is used to create the dilation mask.
        """
    def filter(self, kernel: open3d.core.Tensor) -> Image:
        """
        Return a new image after filtering with the given kernel.
        """
    def filter_bilateral(
        self, kernel_size: int = 3, value_sigma: float = 20.0, dist_sigma: float = 10.0
    ) -> Image:
        """
        Return a new image after bilateral filtering.Note: CPU (IPP) and CUDA (NPP) versions are inconsistent: CPU uses a round kernel (radius = floor(kernel_size / 2)), while CUDA uses a square kernel (width = kernel_size). Make sure to tune parameters accordingly.
        """
    def filter_gaussian(self, kernel_size: int = 3, sigma: float = 1.0) -> Image:
        """
        Return a new image after Gaussian filtering. Possible kernel_size: odd numbers >= 3 are supported.
        """
    def filter_sobel(self, kernel_size: int = 3) -> typing.Tuple[Image, Image]:
        """
        Return a pair of new gradient images (dx, dy) after Sobel filtering. Possible kernel_size: 3 and 5.
        """
    @staticmethod
    def from_legacy(
        image_legacy: open3d.geometry.Image,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> Image:
        """
        Create a Image from a legacy Open3D Image.
        """
    def pyrdown(self) -> Image:
        """
        Return a new downsampled image with pyramid downsampling formed by a chained Gaussian filter (kernel_size = 5, sigma = 1.0) and a resize (ratio = 0.5) operation.
        """
    def resize(
        self, sampling_rate: float = 0.5, interp_type: InterpType = InterpType.Nearest
    ) -> Image:
        """
        Return a new image after resizing with specified interpolation type. Downsample if sampling rate is < 1. Upsample if sampling rate > 1. Aspect ratio is always kept.
        """
    def rgb_to_gray(self) -> Image:
        """
        Converts a 3-channel RGB image to a new 1-channel Grayscale image by I = 0.299 * R + 0.587 * G + 0.114 * B.
        """
    @property
    def channels(self) -> int:
        """
        Get the number of channels of the image.

        :type: int
        """
    @property
    def columns(self) -> int:
        """
        Get the number of columns of the image.

        :type: int
        """
    @property
    def device(self) -> open3d.core.Device:
        """
        Get the device of the image.

        :type: open3d.core.Device
        """
    @property
    def dtype(self) -> open3d.core.Dtype:
        """
        Get dtype of the image

        :type: open3d.core.Dtype
        """
    @property
    def rows(self) -> int:
        """
        Get the number of rows of the image.

        :type: int
        """
    pass

class InterpType:
    """
    Interpolation type.

    Members:

      Nearest

      Linear

      Cubic

      Lanczos

      Super
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
    Cubic: open3d.t.geometry.InterpType  # value = <InterpType.Cubic: 2>
    Lanczos: open3d.t.geometry.InterpType  # value = <InterpType.Lanczos: 3>
    Linear: open3d.t.geometry.InterpType  # value = <InterpType.Linear: 1>
    Nearest: open3d.t.geometry.InterpType  # value = <InterpType.Nearest: 0>
    Super: open3d.t.geometry.InterpType  # value = <InterpType.Super: 4>
    __members__: dict  # value = {'Nearest': <InterpType.Nearest: 0>, 'Linear': <InterpType.Linear: 1>, 'Cubic': <InterpType.Cubic: 2>, 'Lanczos': <InterpType.Lanczos: 3>, 'Super': <InterpType.Super: 4>}
    pass

class LineSet(Geometry, DrawableGeometry):
    """
    A LineSet contains points and lines joining them and optionally attributes on
    the points and lines.  The ``LineSet`` class stores the attribute data in
    key-value maps, where the key is the attribute name and value is a Tensor
    containing the attribute data.  There are two maps: one each for ``point``
    and ``line``.

    The attributes of the line set have different levels.

        import open3d as o3d

        dtype_f = o3d.core.float32
        dtype_i = o3d.core.int32

        # Create an empty line set
        # Use lineset.point to access the point attributes
        # Use lineset.line to access the line attributes
        lineset = o3d.t.geometry.LineSet()

        # Default attribute: point["positions"], line["indices"]
        # These attributes is created by default and are required by all line
        # sets. The shape must be (N, 3) and (N, 2) respectively. The device of
        # "positions" determines the device of the line set.
        lineset.point["positions"] = o3d.core.Tensor([[0, 0, 0],
                                                      [0, 0, 1],
                                                      [0, 1, 0],
                                                      [0, 1, 1]], dtype_f, device)
        lineset.line["indices"] = o3d.core.Tensor([[0, 1],
                                                   [1, 2],
                                                   [2, 3],
                                                   [3, 0]], dtype_i, device)

        # Common attributes: line["colors"]
        # Common attributes are used in built-in line set operations. The
        # spellings must be correct. For example, if "color" is used instead of
        # "color", some internal operations that expects "colors" will not work.
        # "colors" must have shape (N, 3) and must be on the same device as the
        # line set.
        lineset.line["colors"] = o3d.core.Tensor([[0.0, 0.0, 0.0],
                                                  [0.1, 0.1, 0.1],
                                                  [0.2, 0.2, 0.2],
                                                  [0.3, 0.3, 0.3]], dtype_f, device)

        # User-defined attributes
        # You can also attach custom attributes. The value tensor must be on the
        # same device as the line set. The are no restrictions on the shape or
        # dtype, e.g.,
        pcd.point["labels"] = o3d.core.Tensor(...)
        pcd.line["features"] = o3d.core.Tensor(...)
    """

    def __repr__(self) -> str: ...
    def clone(self) -> LineSet:
        """
        Returns copy of the line set on the same device.
        """
    def cpu(self) -> LineSet:
        """
        Transfer the line set to CPU. If the line set is already on CPU, no copy will be performed.
        """
    def cuda(self, device_id: int = 0) -> LineSet:
        """
        Transfer the line set to a CUDA device. If the line set is already on the specified CUDA device, no copy will be performed.
        """
    def get_axis_aligned_bounding_box(self) -> open3d.t.geometry.AxisAlignedBoundingBox:
        """
        Create an axis-aligned bounding box from point attribute 'positions'.
        """
    def get_center(self) -> open3d.core.Tensor:
        """
        Returns the center for point coordinates.
        """
    def get_max_bound(self) -> open3d.core.Tensor:
        """
        Returns the max bound for point coordinates.
        """
    def get_min_bound(self) -> open3d.core.Tensor:
        """
        Returns the min bound for point coordinates.
        """
    def to(self, device: open3d.core.Device, copy: bool = False) -> LineSet:
        """
        Transfer the line set to a specified device.
        """
    def to_legacy(self) -> open3d.geometry.LineSet:
        """
        Convert to a legacy Open3D LineSet.
        """
    @property
    def line(self) -> TensorMap:
        """
        Dictionary containing line attributes. The primary key ``indices`` contains indices of points defining the lines.

        :type: TensorMap
        """
    @property
    def point(self) -> TensorMap:
        """
        Dictionary containing point attributes. The primary key ``positions`` contains point positions.

        :type: TensorMap
        """
    pass

class PointCloud(Geometry, DrawableGeometry):
    """
    A point cloud contains a list of 3D points. The point cloud class stores the
    attribute data in key-value maps, where the key is a string representing the
    attribute name and the value is a Tensor containing the attribute data.

    The attributes of the point cloud have different levels.

        import open3d as o3d

        device = o3d.core.Device("CPU:0")
        dtype = o3d.core.float32

        # Create an empty point cloud
        # Use pcd.point to access the points' attributes
        pcd = o3d.t.geometry.PointCloud(device)

        # Default attribute: "positions".
        # This attribute is created by default and is required by all point clouds.
        # The shape must be (N, 3). The device of "positions" determines the device
        # of the point cloud.
        pcd.point["positions"] = o3d.core.Tensor([[0, 0, 0],
                                                  [1, 1, 1],
                                                  [2, 2, 2]], dtype, device)

        # Common attributes: "normals", "colors".
        # Common attributes are used in built-in point cloud operations. The
        # spellings must be correct. For example, if "normal" is used instead of
        # "normals", some internal operations that expects "normals" will not work.
        # "normals" and "colors" must have shape (N, 3) and must be on the same
        # device as the point cloud.
        pcd.point["normals"] = o3d.core.Tensor([[0, 0, 1],
                                                [0, 1, 0],
                                                [1, 0, 0]], dtype, device)
        pcd.point["colors"] = o3d.core.Tensor([[0.0, 0.0, 0.0],
                                                [0.1, 0.1, 0.1],
                                                [0.2, 0.2, 0.2]], dtype, device)

        # User-defined attributes.
        # You can also attach custom attributes. The value tensor must be on the
        # same device as the point cloud. The are no restrictions on the shape and
        # dtype, e.g.,
        pcd.point["intensities"] = o3d.core.Tensor([0.3, 0.1, 0.4], dtype, device)
        pcd.point["labels"] = o3d.core.Tensor([3, 1, 4], o3d.core.int32, device)
    """

    def __add__(self, arg0: PointCloud) -> PointCloud: ...
    @typing.overload
    def __init__(
        self, device: open3d.core.Device = open3d.core.Device("CPU:0")
    ) -> None:
        """
        Construct an empty pointcloud on the provided ``device`` (default: 'CPU:0').
        """
    @typing.overload
    def __init__(
        self, map_keys_to_tensors: typing.Dict[str, open3d.core.Tensor]
    ) -> None: ...
    @typing.overload
    def __init__(self, positions: open3d.core.Tensor) -> None: ...
    def __repr__(self) -> str: ...
    def append(self, arg0: PointCloud) -> PointCloud: ...
    def clone(self) -> PointCloud:
        """
        Returns a copy of the point cloud on the same device.
        """
    def compute_convex_hull(
        self, joggle_inputs: bool = False
    ) -> open3d.t.geometry.TriangleMesh:
        """
        Compute the convex hull of a triangle mesh using qhull. This runs on the CPU.

        Args:
            joggle_inputs (default False). Handle precision problems by
            randomly perturbing the input data. Set to True if perturbing the input
            iis acceptable but you need convex simplicial output. If False,
            neighboring facets may be merged in case of precision problems. See
            `QHull docs <http://www.qhull.org/html/qh-impre.htm#joggle>`__ for more
            details.

        Return:
            TriangleMesh representing the convexh hull. This contains an
            extra vertex property "point_indices" that contains the index of the
            corresponding vertex in the original mesh.

        Example:
            We will load the Eagle dataset, compute and display it's convex hull.

                eagle = o3d.data.EaglePointCloud()
                pcd = o3d.t.io.read_point_cloud(eagle.path)
                hull = pcd.compute_convex_hull()
                o3d.visualization.draw([{'name': 'eagle', 'geometry': pcd}, {'name': 'convex hull', 'geometry': hull}])

        """
    def cpu(self) -> PointCloud:
        """
        Transfer the point cloud to CPU. If the point cloud is already on CPU, no copy will be performed.
        """
    def cuda(self, device_id: int = 0) -> PointCloud:
        """
        Transfer the point cloud to a CUDA device. If the point cloud is already on the specified CUDA device, no copy will be performed.
        """
    def estimate_color_gradients(
        self, max_nn: int = 30, radius: typing.Optional[float] = None
    ) -> None:
        """
        Function to estimate point color gradients. If radius is provided, then HybridSearch is used, otherwise KNN-Search is used.
        """
    @staticmethod
    def from_legacy(
        pcd_legacy: open3d.geometry.PointCloud,
        dtype: open3d.core.Dtype = open3d.core.Dtype.Float32,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> PointCloud:
        """
        Create a PointCloud from a legacy Open3D PointCloud.
        """
    def get_axis_aligned_bounding_box(self) -> open3d.t.geometry.AxisAlignedBoundingBox:
        """
        Create an axis-aligned bounding box from attribute 'positions'.
        """
    def get_center(self) -> open3d.core.Tensor:
        """
        Returns the center for point coordinates.
        """
    def get_max_bound(self) -> open3d.core.Tensor:
        """
        Returns the max bound for point coordinates.
        """
    def get_min_bound(self) -> open3d.core.Tensor:
        """
        Returns the min bound for point coordinates.
        """
    def remove_non_finite_points(
        self, remove_nan: bool = True, remove_infinite: bool = True
    ) -> typing.Tuple[PointCloud, open3d.core.Tensor]:
        """
        Remove all points from the point cloud that have a nan entry, or infinite value. It also removes the corresponding attributes.
        """
    def rotate(self, R: open3d.core.Tensor, center: open3d.core.Tensor) -> PointCloud:
        """
        Rotate points and normals (if exist).
        """
    def scale(self, scale: float, center: open3d.core.Tensor) -> PointCloud:
        """
        Scale points.
        """
    def to(self, device: open3d.core.Device, copy: bool = False) -> PointCloud:
        """
        Transfer the point cloud to a specified device.
        """
    def to_legacy(self) -> open3d.geometry.PointCloud:
        """
        Convert to a legacy Open3D PointCloud.
        """
    def transform(self, transformation: open3d.core.Tensor) -> PointCloud:
        """
        Transforms the points and normals (if exist).
        """
    def translate(
        self, translation: open3d.core.Tensor, relative: bool = True
    ) -> PointCloud:
        """
        Translates points.
        """
    @property
    def point(self) -> TensorMap:
        """
        Point's attributes: positions, colors, normals, etc.

        :type: TensorMap
        """
    pass

class RGBDImage(Geometry):
    """
    RGBDImage is a pair of color and depth images. For most processing, the image pair should be aligned (same viewpoint and  resolution).
    """

    def __repr__(self) -> str: ...
    def are_aligned(self) -> bool:
        """
        Are the depth and color images aligned (same viewpoint and resolution)?
        """
    def clone(self) -> RGBDImage:
        """
        Returns a copy of the RGBDImage on the same device.
        """
    def cpu(self) -> RGBDImage:
        """
        Transfer the RGBD image to CPU. If the RGBD image is already on CPU, no copy will be performed.
        """
    def cuda(self, device_id: int = 0) -> RGBDImage:
        """
        Transfer the RGBD image to a CUDA device. If the RGBD image is already on the specified CUDA device, no copy will be performed.
        """
    def to(self, device: open3d.core.Device, copy: bool = False) -> RGBDImage:
        """
        Transfer the RGBDImage to a specified device.
        """
    @property
    def aligned_(self) -> bool:
        """
        Are the depth and color images aligned (same viewpoint and resolution)?

        :type: bool
        """
    @aligned_.setter
    def aligned_(self, arg0: bool) -> None:
        """
        Are the depth and color images aligned (same viewpoint and resolution)?
        """
    @property
    def color(self) -> Image:
        """
        The color image.

        :type: Image
        """
    @color.setter
    def color(self, arg0: Image) -> None:
        """
        The color image.
        """
    @property
    def depth(self) -> Image:
        """
        The depth image.

        :type: Image
        """
    @depth.setter
    def depth(self, arg0: Image) -> None:
        """
        The depth image.
        """
    pass

class RaycastingScene:
    """
    A scene class with basic ray casting and closest point queries.

    The RaycastingScene allows to compute ray intersections with triangle meshes
    or compute the closest point on the surface of a mesh with respect to one
    or more query points.
    It builds an internal acceleration structure to speed up those queries.

    This class supports only the CPU device.

    The following shows how to create a scene and compute ray intersections.

        import open3d as o3d
        import matplotlib.pyplot as plt

        cube = o3d.t.geometry.TriangleMesh.from_legacy(
                                            o3d.geometry.TriangleMesh.create_box())

        # Create scene and add the cube mesh
        scene = o3d.t.geometry.RaycastingScene()
        scene.add_triangles(cube)

        # Rays are 6D vectors with origin and ray direction.
        # Here we use a helper function to create rays for a pinhole camera.
        rays = scene.create_rays_pinhole(fov_deg=60,
                                         center=[0.5,0.5,0.5],
                                         eye=[-1,-1,-1],
                                         up=[0,0,1],
                                         width_px=320,
                                         height_px=240)

        # Compute the ray intersections.
        ans = scene.cast_rays(rays)

        # Visualize the hit distance (depth)
        plt.imshow(ans['t_hit'].numpy())
    """

    def __init__(self, nthreads: int = 0) -> None:
        """
        Create a RaycastingScene.

        Args:
            nthreads (int): The number of threads to use for building the scene. Set to 0 for automatic.
        """
    @typing.overload
    def add_triangles(self, mesh: TriangleMesh) -> int:
        """
        Add a triangle mesh to the scene.

        Args:
            vertices (open3d.core.Tensor): Vertices as Tensor of dim {N,3} and dtype
                Float32.
            triangles (open3d.core.Tensor): Triangles as Tensor of dim {M,3} and dtype
                UInt32.

        Returns:
            The geometry ID of the added mesh.


        Add a triangle mesh to the scene.

        Args:
            mesh (open3d.t.geometry.TriangleMesh): A triangle mesh.

        Returns:
            The geometry ID of the added mesh.
        """
    @typing.overload
    def add_triangles(
        self, vertex_positions: open3d.core.Tensor, triangle_indices: open3d.core.Tensor
    ) -> int: ...
    def cast_rays(
        self, rays: open3d.core.Tensor, nthreads: int = 0
    ) -> typing.Dict[str, open3d.core.Tensor]:
        """
        Computes the first intersection of the rays with the scene.

        Args:
            rays (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 6}, and Dtype
                Float32 describing the rays.
                {..} can be any number of dimensions, e.g., to organize rays for
                creating an image the shape can be {height, width, 6}. The last
                dimension must be 6 and has the format [ox, oy, oz, dx, dy, dz]
                with [ox,oy,oz] as the origin and [dx,dy,dz] as the direction. It is
                not necessary to normalize the direction but the returned hit distance
                uses the length of the direction vector as unit.

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A dictionary which contains the following keys

            t_hit
                A tensor with the distance to the first hit. The shape is {..}. If there
                is no intersection the hit distance is *inf*.

            geometry_ids
                A tensor with the geometry IDs. The shape is {..}. If there
                is no intersection the ID is *INVALID_ID*.

            primitive_ids
                A tensor with the primitive IDs, which corresponds to the triangle
                index. The shape is {..}.  If there is no intersection the ID is
                *INVALID_ID*.

            primitive_uvs
                A tensor with the barycentric coordinates of the hit points within the
                hit triangles. The shape is {.., 2}.

            primitive_normals
                A tensor with the normals of the hit triangles. The shape is {.., 3}.
        """
    def compute_closest_points(
        self, query_points: open3d.core.Tensor, nthreads: int = 0
    ) -> typing.Dict[str, open3d.core.Tensor]:
        """
        Computes the closest points on the surfaces of the scene.

        Args:
            query_points (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 3},
                and Dtype Float32 describing the query points.
                {..} can be any number of dimensions, e.g., to organize the query_point
                to create a 3D grid the shape can be {depth, height, width, 3}.
                The last dimension must be 3 and has the format [x, y, z].

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            The returned dictionary contains

            points
                A tensor with the closest surface points. The shape is {..}.

            geometry_ids
                A tensor with the geometry IDs. The shape is {..}.

            primitive_ids
                A tensor with the primitive IDs, which corresponds to the triangle
                index. The shape is {..}.
        """
    def compute_distance(
        self, query_points: open3d.core.Tensor, nthreads: int = 0
    ) -> open3d.core.Tensor:
        """
        Computes the distance to the surface of the scene.

        Args:
            query_points (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 3},
                and Dtype Float32 describing the query points.
                {..} can be any number of dimensions, e.g., to organize the
                query points to create a 3D grid the shape can be
                {depth, height, width, 3}.
                The last dimension must be 3 and has the format [x, y, z].

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A tensor with the distances to the surface. The shape is {..}.
        """
    def compute_occupancy(
        self, query_points: open3d.core.Tensor, nthreads: int = 0
    ) -> open3d.core.Tensor:
        """
        Computes the occupancy at the query point positions.

        This function computes whether the query points are inside or outside.
        The function assumes that all meshes are watertight and that there are
        no intersections between meshes, i.e., inside and outside must be well
        defined. The function determines if a point is inside by counting the
        intersections of a rays starting at the query points.

        Args:
            query_points (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 3},
                and Dtype Float32 describing the query points.
                {..} can be any number of dimensions, e.g., to organize the
                query points to create a 3D grid the shape can be
                {depth, height, width, 3}.
                The last dimension must be 3 and has the format [x, y, z].

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A tensor with the occupancy values. The shape is {..}. Values are either 0
            or 1. A point is occupied or inside if the value is 1.
        """
    def compute_signed_distance(
        self, query_points: open3d.core.Tensor, nthreads: int = 0
    ) -> open3d.core.Tensor:
        """
        Computes the signed distance to the surface of the scene.

        This function computes the signed distance to the meshes in the scene.
        The function assumes that all meshes are watertight and that there are
        no intersections between meshes, i.e., inside and outside must be well
        defined. The function determines the sign of the distance by counting
        the intersections of a rays starting at the query points.

        Args:
            query_points (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 3},
                and Dtype Float32 describing the query_points.
                {..} can be any number of dimensions, e.g., to organize the
                query points to create a 3D grid the shape can be
                {depth, height, width, 3}.
                The last dimension must be 3 and has the format [x, y, z].

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A tensor with the signed distances to the surface. The shape is {..}.
            Negative distances mean a point is inside a closed surface.
        """
    def count_intersections(
        self, rays: open3d.core.Tensor, nthreads: int = 0
    ) -> open3d.core.Tensor:
        """
        Computes the number of intersection of the rays with the scene.

        Args:
            rays (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 6}, and Dtype
                Float32 describing the rays.
                {..} can be any number of dimensions, e.g., to organize rays for
                creating an image the shape can be {height, width, 6}.
                The last dimension must be 6 and has the format [ox, oy, oz, dx, dy, dz]
                with [ox,oy,oz] as the origin and [dx,dy,dz] as the direction. It is not
                necessary to normalize the direction.

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A tensor with the number of intersections. The shape is {..}.
        """
    @staticmethod
    @typing.overload
    def create_rays_pinhole(
        fov_deg: float,
        center: open3d.core.Tensor,
        eye: open3d.core.Tensor,
        up: open3d.core.Tensor,
        width_px: int,
        height_px: int,
    ) -> open3d.core.Tensor:
        """
        Creates rays for the given camera parameters.

        Args:
            intrinsic_matrix (open3d.core.Tensor): The upper triangular intrinsic matrix
                with shape {3,3}.
            extrinsic_matrix (open3d.core.Tensor): The 4x4 world to camera SE(3)
                transformation matrix.
            width_px (int): The width of the image in pixels.
            height_px (int): The height of the image in pixels.

        Returns:
            A tensor of shape {height_px, width_px, 6} with the rays.


        Creates rays for the given camera parameters.

        Args:
            fov_deg (float): The horizontal field of view in degree.
            center (open3d.core.Tensor): The point the camera is looking at with shape
                {3}.
            eye (open3d.core.Tensor): The position of the camera with shape {3}.
            up (open3d.core.Tensor): The up-vector with shape {3}.
            width_px (int): The width of the image in pixels.
            height_px (int): The height of the image in pixels.

        Returns:
            A tensor of shape {height_px, width_px, 6} with the rays.
        """
    @staticmethod
    @typing.overload
    def create_rays_pinhole(
        intrinsic_matrix: open3d.core.Tensor,
        extrinsic_matrix: open3d.core.Tensor,
        width_px: int,
        height_px: int,
    ) -> open3d.core.Tensor: ...
    def test_occlusions(
        self,
        rays: open3d.core.Tensor,
        tnear: float = 0.0,
        tfar: float = float("inf"),
        nthreads: int = 0,
    ) -> open3d.core.Tensor:
        """
        Checks if the rays have any intersection with the scene.

        Args:
            rays (open3d.core.Tensor): A tensor with >=2 dims, shape {.., 6}, and Dtype
                Float32 describing the rays.
                {..} can be any number of dimensions, e.g., to organize rays for
                creating an image the shape can be {height, width, 6}.
                The last dimension must be 6 and has the format [ox, oy, oz, dx, dy, dz]
                with [ox,oy,oz] as the origin and [dx,dy,dz] as the direction. It is not
                necessary to normalize the direction.

            tnear (float): The tnear offset for the rays. The default is 0.

            tfar (float): The tfar value for the ray. The default is infinity.

            nthreads (int): The number of threads to use. Set to 0 for automatic.

        Returns:
            A boolean tensor which indicates if the ray is occluded by the scene (true)
            or not (false).
        """
    INVALID_ID = 4294967295
    pass

class TensorMap:
    """
    Map of String to Tensor with a primary key.
    """

    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> int: ...
    def __getitem__(self, arg0: str) -> open3d.core.Tensor: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, primary_key: str) -> None: ...
    @typing.overload
    def __init__(
        self,
        primary_key: str,
        map_keys_to_tensors: typing.Dict[str, open3d.core.Tensor],
    ) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: open3d.core.Tensor) -> None: ...
    def assert_size_synchronized(self) -> None: ...
    def erase(self, arg0: str) -> int: ...
    def get_primary_key(self) -> str: ...
    def is_size_synchronized(self) -> bool: ...
    def items(self) -> typing.Iterator: ...
    pass

class TriangleMesh(Geometry, DrawableGeometry):
    """
    A triangle mesh contains vertices and triangles. The triangle mesh class stores
    the attribute data in key-value maps. There are two maps: the vertex attributes
    map, and the triangle attribute map.

    The attributes of the triangle mesh have different levels.

        import open3d as o3d

        device = o3d.core.Device("CPU:0")
        dtype_f = o3d.core.float32
        dtype_i = o3d.core.int32

        # Create an empty triangle mesh
        # Use mesh.vertex to access the vertices' attributes
        # Use mesh.triangle to access the triangles' attributes
        mesh = o3d.t.geometry.TriangleMesh(device)

        # Default attribute: vertex["positions"], triangle["indices"]
        # These attributes is created by default and is required by all triangle
        # meshes. The shape of both must be (N, 3). The device of "positions"
        # determines the device of the triangle mesh.
        mesh.vertex["positions"] = o3d.core.Tensor([[0, 0, 0],
                                                    [0, 0, 1],
                                                    [0, 1, 0],
                                                    [0, 1, 1]], dtype_f, device)
        mesh.triangle["indices"] = o3d.core.Tensor([[0, 1, 2],
                                                    [0, 2, 3]]], dtype_i, device)

        # Common attributes: vertex["colors"]  , vertex["normals"]
        #                    triangle["colors"], triangle["normals"]
        # Common attributes are used in built-in triangle mesh operations. The
        # spellings must be correct. For example, if "normal" is used instead of
        # "normals", some internal operations that expects "normals" will not work.
        # "normals" and "colors" must have shape (N, 3) and must be on the same
        # device as the triangle mesh.
        mesh.vertex["normals"] = o3d.core.Tensor([[0, 0, 1],
                                                  [0, 1, 0],
                                                  [1, 0, 0],
                                                  [1, 1, 1]], dtype_f, device)
        mesh.vertex["colors"] = o3d.core.Tensor([[0.0, 0.0, 0.0],
                                                 [0.1, 0.1, 0.1],
                                                 [0.2, 0.2, 0.2],
                                                 [0.3, 0.3, 0.3]], dtype_f, device)
        mesh.triangle["normals"] = o3d.core.Tensor(...)
        mesh.triangle["colors"] = o3d.core.Tensor(...)

        # User-defined attributes
        # You can also attach custom attributes. The value tensor must be on the
        # same device as the triangle mesh. The are no restrictions on the shape and
        # dtype, e.g.,
        pcd.vertex["labels"] = o3d.core.Tensor(...)
        pcd.triangle["features"] = o3d.core.Tensor(...)
    """

    @typing.overload
    def __init__(
        self, device: open3d.core.Device = open3d.core.Device("CPU:0")
    ) -> None:
        """
        Construct an empty trianglemesh on the provided ``device`` (default: 'CPU:0').
        """
    @typing.overload
    def __init__(
        self, vertex_positions: open3d.core.Tensor, triangle_indices: open3d.core.Tensor
    ) -> None: ...
    def __repr__(self) -> str: ...
    def boolean_difference(
        self, mesh: TriangleMesh, tolerance: float = 1e-06
    ) -> TriangleMesh:
        """
        Computes the mesh that encompasses the volume after subtracting the volume of the second operand.
        Both meshes should be manifold.

        This function always uses the CPU device.

        Args:
            mesh (open3d.t.geometry.TriangleMesh): This is the second operand for the
                boolean operation.

            tolerance (float): Threshold which determines when point distances are
                considered to be 0.

        Returns:
            The mesh describing the difference volume.

        Example:
            This subtracts the sphere from the cube volume.

                box = o3d.geometry.TriangleMesh.create_box()
                box = o3d.t.geometry.TriangleMesh.from_legacy(box)
                sphere = o3d.geometry.TriangleMesh.create_sphere(0.8)
                sphere = o3d.t.geometry.TriangleMesh.from_legacy(sphere)

                ans = box.boolean_difference(sphere)

                o3d.visualization.draw([{'name': 'difference', 'geometry': ans}])
        """
    def boolean_intersection(
        self, mesh: TriangleMesh, tolerance: float = 1e-06
    ) -> TriangleMesh:
        """
        Computes the mesh that encompasses the intersection of the volumes of two meshes.
        Both meshes should be manifold.

        This function always uses the CPU device.

        Args:
            mesh (open3d.t.geometry.TriangleMesh): This is the second operand for the
                boolean operation.

            tolerance (float): Threshold which determines when point distances are
                considered to be 0.

        Returns:
            The mesh describing the intersection volume.

        Example:
            This copmutes the intersection of a sphere and a cube.

                box = o3d.geometry.TriangleMesh.create_box()
                box = o3d.t.geometry.TriangleMesh.from_legacy(box)
                sphere = o3d.geometry.TriangleMesh.create_sphere(0.8)
                sphere = o3d.t.geometry.TriangleMesh.from_legacy(sphere)

                ans = box.boolean_intersection(sphere)

                o3d.visualization.draw([{'name': 'intersection', 'geometry': ans}])
        """
    def boolean_union(
        self, mesh: TriangleMesh, tolerance: float = 1e-06
    ) -> TriangleMesh:
        """
        Computes the mesh that encompasses the union of the volumes of two meshes.
        Both meshes should be manifold.

        This function always uses the CPU device.

        Args:
            mesh (open3d.t.geometry.TriangleMesh): This is the second operand for the
                boolean operation.

            tolerance (float): Threshold which determines when point distances are
                considered to be 0.

        Returns:
            The mesh describing the union volume.

        Example:
            This copmutes the union of a sphere and a cube.

                box = o3d.geometry.TriangleMesh.create_box()
                box = o3d.t.geometry.TriangleMesh.from_legacy(box)
                sphere = o3d.geometry.TriangleMesh.create_sphere(0.8)
                sphere = o3d.t.geometry.TriangleMesh.from_legacy(sphere)

                ans = box.boolean_union(sphere)

                o3d.visualization.draw([{'name': 'union', 'geometry': ans}])
        """
    def clip_plane(
        self, point: open3d.core.Tensor, normal: open3d.core.Tensor
    ) -> TriangleMesh:
        """
        Returns a new triangle mesh clipped with the plane.

        This method clips the triangle mesh with the specified plane.
        Parts of the mesh on the positive side of the plane will be kept and triangles
        intersected by the plane will be cut.

        Args:
            point (open3d.core.Tensor): A point on the plane.

            normal (open3d.core.Tensor): The normal of the plane. The normal points to
                the positive side of the plane for which the geometry will be kept.

        Returns:
            New triangle mesh clipped with the plane.


        This example shows how to create a hemisphere from a sphere.

            import open3d as o3d

            sphere = o3d.t.geometry.TriangleMesh.from_legacy(o3d.geometry.TriangleMesh.create_sphere())
            hemisphere = sphere.clip_plane(point=[0,0,0], normal=[1,0,0])

            o3d.visualization.draw(hemisphere)
        """
    def clone(self) -> TriangleMesh:
        """
        Returns copy of the triangle mesh on the same device.
        """
    def compute_convex_hull(self, joggle_inputs: bool = False) -> TriangleMesh:
        """
        Compute the convex hull of a point cloud using qhull. This runs on the CPU.

        Args:
            joggle_inputs (default False). Handle precision problems by
            randomly perturbing the input data. Set to True if perturbing the input
            iis acceptable but you need convex simplicial output. If False,
            neighboring facets may be merged in case of precision problems. See
            `QHull docs <http://www.qhull.org/html/qh-impre.htm#joggle`__ for more
            details.

        Returns:
            TriangleMesh representing the convexh hull. This contains an
            extra vertex property "point_indices" that contains the index of the
            corresponding vertex in the original mesh.

        Example:
            We will load the Stanford Bunny dataset, compute and display it's convex hull.

                bunny = o3d.data.BunnyMesh()
                mesh = o3d.t.geometry.TriangleMesh.from_legacy(o3d.io.read_triangle_mesh(bunny.path))
                hull = mesh.compute_convex_hull()
                o3d.visualization.draw([{'name': 'bunny', 'geometry': mesh}, {'name': 'convex hull', 'geometry': hull}])
        """
    def cpu(self) -> TriangleMesh:
        """
        Transfer the triangle mesh to CPU. If the triangle mesh is already on CPU, no copy will be performed.
        """
    @staticmethod
    def create_text(
        text: str,
        depth: float = 0.0,
        float_dtype: open3d.core.Dtype = open3d.core.Dtype.Float32,
        int_dtype: open3d.core.Dtype = open3d.core.Dtype.Int64,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> TriangleMesh:
        """
        Create a triangle mesh from a text string.

        Args:
            text (str): The text for generating the mesh. ASCII characters 32-126 are
                supported (includes alphanumeric characters and punctuation). In
                addition the line feed '\n' is supported to start a new line.
            depth (float): The depth of the generated mesh. If depth is 0 then a flat mesh will be generated.
            float_dtype (o3d.core.Dtype): Float type for the vertices. Either Float32 or Float64.
            int_dtype (o3d.core.Dtype): Int type for the triangle indices. Either Int32 or Int64.
            device (o3d.core.Device): The device for the returned mesh.

        Returns:
            Text as triangle mesh.

        Example:
            This shows how to simplifify the Stanford Bunny mesh.

                import open3d as o3d

                mesh = o3d.t.geometry.TriangleMesh.create_text('Open3D', depth=1)
                o3d.visualization.draw([{'name': 'text', 'geometry': mesh}])
        """
    def cuda(self, device_id: int = 0) -> TriangleMesh:
        """
        Transfer the triangle mesh to a CUDA device. If the triangle mesh is already on the specified CUDA device, no copy will be performed.
        """
    def fill_holes(self, hole_size: float = 1000000.0) -> TriangleMesh:
        """
        Fill holes by triangulating boundary edges.

        This function always uses the CPU device.

        Args:
            hole_size (float): This is the approximate threshold for filling holes.
                The value describes the maximum radius of holes to be filled.

        Returns:
            New mesh after filling holes.

        Example:
            Fill holes at the bottom of the Stanford Bunny mesh.

                bunny = o3d.data.BunnyMesh()
                mesh = o3d.t.geometry.TriangleMesh.from_legacy(o3d.io.read_triangle_mesh(bunny.path))
                filled = mesh.fill_holes()
                o3d.visualization.draw([{'name': 'filled', 'geometry': ans}])
        """
    @staticmethod
    def from_legacy(
        mesh_legacy: open3d.geometry.TriangleMesh,
        vertex_dtype: open3d.core.Dtype = open3d.core.Dtype.Float32,
        triangle_dtype: open3d.core.Dtype = open3d.core.Dtype.Int64,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> TriangleMesh:
        """
        Create a TriangleMesh from a legacy Open3D TriangleMesh.
        """
    def get_axis_aligned_bounding_box(self) -> open3d.t.geometry.AxisAlignedBoundingBox:
        """
        Create an axis-aligned bounding box from vertex attribute 'positions'.
        """
    def get_center(self) -> open3d.core.Tensor:
        """
        Returns the center for point coordinates.
        """
    def get_max_bound(self) -> open3d.core.Tensor:
        """
        Returns the max bound for point coordinates.
        """
    def get_min_bound(self) -> open3d.core.Tensor:
        """
        Returns the min bound for point coordinates.
        """
    def rotate(self, R: open3d.core.Tensor, center: open3d.core.Tensor) -> TriangleMesh:
        """
        Rotate points and normals (if exist).
        """
    def scale(self, scale: float, center: open3d.core.Tensor) -> TriangleMesh:
        """
        Scale points.
        """
    def simplify_quadric_decimation(
        self, target_reduction: float, preserve_volume: bool = True
    ) -> TriangleMesh:
        """
        Function to simplify mesh using Quadric Error Metric Decimation by Garland and Heckbert.

        This function always uses the CPU device.

        Args:
            target_reduction (float): The factor of triangles to delete, i.e., setting
                this to 0.9 will return a mesh with about 10% of the original triangle
                count. It is not guaranteed that the target reduction factor will be
                reached.

            preserve_volume (bool): If set to True this enables volume preservation
                which reduces the error in triangle normal direction.

        Returns:
            Simplified TriangleMesh.

        Example:
            This shows how to simplifify the Stanford Bunny mesh.

                bunny = o3d.data.BunnyMesh()
                mesh = o3d.t.geometry.TriangleMesh.from_legacy(o3d.io.read_triangle_mesh(bunny.path))
                simplified = mesh.simplify_quadric_decimation(0.99)
                o3d.visualization.draw([{'name': 'bunny', 'geometry': simplified}])
        """
    def slice_plane(
        self,
        point: open3d.core.Tensor,
        normal: open3d.core.Tensor,
        contour_values: typing.List[float] = [0.0],
    ) -> LineSet:
        """
        Returns a line set with the contour slices defined by the plane and values.

        This method generates slices as LineSet from the mesh at specific contour
        values with respect to a plane.

        Args:
            point (open3d.core.Tensor): A point on the plane.
            normal (open3d.core.Tensor): The normal of the plane.
            contour_values (list): A list of contour values at which slices will be
                generated. The value describes the signed distance to the plane.

        Returns:
            LineSet with he extracted contours.


        This example shows how to create a hemisphere from a sphere.

            import open3d as o3d
            import numpy as np

            bunny = o3d.data.BunnyMesh()
            mesh = o3d.t.geometry.TriangleMesh.from_legacy(o3d.io.read_triangle_mesh(bunny.path))
            contours = mesh.slice_plane([0,0,0], [0,1,0], np.linspace(0,0.2))
            o3d.visualization.draw([{'name': 'bunny', 'geometry': contours}])
        """
    def to(self, device: open3d.core.Device, copy: bool = False) -> TriangleMesh:
        """
        Transfer the triangle mesh to a specified device.
        """
    def to_legacy(self) -> open3d.geometry.TriangleMesh:
        """
        Convert to a legacy Open3D TriangleMesh.
        """
    def transform(self, transformation: open3d.core.Tensor) -> TriangleMesh:
        """
        Transforms the points and normals (if exist).
        """
    def translate(
        self, translation: open3d.core.Tensor, relative: bool = True
    ) -> TriangleMesh:
        """
        Translates points.
        """
    @property
    def triangle(self) -> TensorMap:
        """
        :type: TensorMap
        """
    @property
    def vertex(self) -> TensorMap:
        """
        :type: TensorMap
        """
    pass

class VoxelBlockGrid:
    """
    A voxel block grid is a sparse grid of voxel blocks. Each voxel block is a dense 3D array, preserving local data distribution. If the block_resolution is set to 1, then the VoxelBlockGrid degenerates to a sparse voxel grid.
    """

    def __init__(
        self,
        attr_names: typing.List[str],
        attr_dtypes: typing.List[open3d.core.Dtype],
        attr_channels: typing.List[open3d.core.SizeVector],
        voxel_size: float = 0.0058,
        block_resolution: int = 16,
        block_count: int = 10000,
        device: open3d.core.Device = open3d.core.Device("CPU:0"),
    ) -> None: ...
    def attribute(self, attribute_name: str) -> open3d.core.Tensor:
        """
        Get the attribute tensor to be indexed with voxel_indices.
        """
    @typing.overload
    def compute_unique_block_coordinates(
        self,
        depth: Image,
        intrinsic: open3d.core.Tensor,
        extrinsic: open3d.core.Tensor,
        depth_scale: float = 1000.0,
        depth_max: float = 3.0,
        trunc_voxel_multiplier: float = 8.0,
    ) -> open3d.core.Tensor:
        """
        Get a (3, M) active block coordinates from a depth image, with potential duplicates removed.Note: these coordinates are not activated in the internal sparse voxel block. They need to be inserted in the hash map.

        Obtain active block coordinates from a point cloud.
        """
    @typing.overload
    def compute_unique_block_coordinates(
        self, pcd: PointCloud, trunc_voxel_multiplier: float = 8.0
    ) -> open3d.core.Tensor: ...
    def extract_point_cloud(
        self, weight_threshold: float = 3.0, estimated_point_number: int = -1
    ) -> PointCloud:
        """
        Specific operation for TSDF volumes.Extract point cloud at isosurface points.
        """
    def extract_triangle_mesh(
        self, weight_threshold: float = 3.0, estimated_vertex_number: int = -1
    ) -> TriangleMesh:
        """
        Specific operation for TSDF volumes.Extract triangle mesh at isosurface points.
        """
    def hashmap(self) -> open3d.core.HashMap:
        """
        Get the underlying hash map from 3d block coordinates to block voxel grids.
        """
    @typing.overload
    def integrate(
        self,
        block_coords: open3d.core.Tensor,
        depth: Image,
        color: Image,
        depth_intrinsic: open3d.core.Tensor,
        color_intrinsic: open3d.core.Tensor,
        extrinsic: open3d.core.Tensor,
        depth_scale: float = 1000.0,
        depth_max: float = 3.0,
        trunc_voxel_multiplier: float = 8.0,
    ) -> None:
        """
        Specific operation for TSDF volumes.Integrate an RGB-D frame in the selected block coordinates using pinhole camera model.

        Specific operation for TSDF volumes.Integrate an RGB-D frame in the selected block coordinates using pinhole camera model.

        Specific operation for TSDF volumes.Similar to RGB-D integration, but only applied to depth images.
        """
    @typing.overload
    def integrate(
        self,
        block_coords: open3d.core.Tensor,
        depth: Image,
        color: Image,
        intrinsic: open3d.core.Tensor,
        extrinsic: open3d.core.Tensor,
        depth_scale: float = 1000.0,
        depth_max: float = 3.0,
        trunc_voxel_multiplier: float = 8.0,
    ) -> None: ...
    @typing.overload
    def integrate(
        self,
        block_coords: open3d.core.Tensor,
        depth: Image,
        intrinsic: open3d.core.Tensor,
        extrinsic: open3d.core.Tensor,
        depth_scale: float = 1000.0,
        depth_max: float = 3.0,
        trunc_voxel_multiplier: float = 8.0,
    ) -> None: ...
    @staticmethod
    def load(file_name: str) -> VoxelBlockGrid:
        """
        Load a voxel block grid from a npz file.
        """
    def ray_cast(
        self,
        block_coords: open3d.core.Tensor,
        intrinsic: open3d.core.Tensor,
        extrinsic: open3d.core.Tensor,
        width: int,
        height: int,
        render_attributes: typing.List[str] = ["depth", "color"],
        depth_scale: float = 1000.0,
        depth_min: float = 0.10000000149011612,
        depth_max: float = 3.0,
        weight_threshold: float = 3.0,
        trunc_voxel_multiplier: float = 8.0,
        range_map_down_factor: int = 8,
    ) -> TensorMap:
        """
        Specific operation for TSDF volumes.Perform volumetric ray casting in the selected block coordinates.The block coordinates in the frustum can be taken fromcompute_unique_block_coordinatesAll the block coordinates can be taken from hashmap().key_tensor()
        """
    def save(self, file_name: str) -> None:
        """
        Save the voxel block grid to a npz file.
        """
    def voxel_coordinates(
        self, voxel_indices: open3d.core.Tensor
    ) -> open3d.core.Tensor:
        """
        Get a (3, hashmap.Size() * resolution^3) coordinate tensor of activevoxels per block, used for geometry transformation jointly with   indices from voxel_indices.                                       Example:                                                          For a voxel block grid with (2, 2, 2) block resolution,           if the active block coordinates are {(-1, 3, 2), (0, 2, 4)},      the returned result will be a (3, 2 x 8) tensor given by:         {                                                                 key_tensor[voxel_indices[0]] * block_resolution_ + voxel_indices[1] key_tensor[voxel_indices[0]] * block_resolution_ + voxel_indices[2] key_tensor[voxel_indices[0]] * block_resolution_ + voxel_indices[3] }                                                                 Note: the coordinates are VOXEL COORDINATES in Int64. To access metriccoordinates, multiply by voxel size.
        """
    @typing.overload
    def voxel_coordinates_and_flattened_indices(
        self,
    ) -> typing.Tuple[open3d.core.Tensor, open3d.core.Tensor]:
        """
        Get a (buf_indices.shape[0] * resolution^3, 3), Float32 voxel coordinate tensor,and a (buf_indices.shape[0] * resolution^3, 1), Int64 voxel index tensor.

        Get a (hashmap.size() * resolution^3, 3), Float32 voxel coordinate tensor,and a (hashmap.size() * resolution^3, 1), Int64 voxel index tensor.
        """
    @typing.overload
    def voxel_coordinates_and_flattened_indices(
        self, buf_indices: open3d.core.Tensor
    ) -> typing.Tuple[open3d.core.Tensor, open3d.core.Tensor]: ...
    @typing.overload
    def voxel_indices(self) -> open3d.core.Tensor:
        """
        Get a (4, N), Int64 index tensor for input buffer indices, used for advanced indexing.   Returned index tensor can access selected value bufferin the order of  (buf_index, index_voxel_x, index_voxel_y, index_voxel_z).       Example:                                                        For a voxel block grid with (2, 2, 2) block resolution,         if the active block coordinates are at buffer index {(2, 4)} given by active_indices() from the underlying hash map,         the returned result will be a (4, 2 x 8) tensor:                {                                                               (2, 0, 0, 0), (2, 1, 0, 0), (2, 0, 1, 0), (2, 1, 1, 0),         (2, 0, 0, 1), (2, 1, 0, 1), (2, 0, 1, 1), (2, 1, 1, 1),         (4, 0, 0, 0), (4, 1, 0, 0), (4, 0, 1, 0), (4, 1, 1, 0),         (4, 0, 0, 1), (4, 1, 0, 1), (4, 0, 1, 1), (4, 1, 1, 1),         }Note: the slicing order is z-y-x.

        Get a (4, N) Int64 idnex tensor for all the active voxels stored in the hash map, used for advanced indexing.
        """
    @typing.overload
    def voxel_indices(self, arg0: open3d.core.Tensor) -> open3d.core.Tensor: ...
    pass

Cubic: open3d.t.geometry.InterpType  # value = <InterpType.Cubic: 2>
Lanczos: open3d.t.geometry.InterpType  # value = <InterpType.Lanczos: 3>
Linear: open3d.t.geometry.InterpType  # value = <InterpType.Linear: 1>
Nearest: open3d.t.geometry.InterpType  # value = <InterpType.Nearest: 0>
Super: open3d.t.geometry.InterpType  # value = <InterpType.Super: 4>
