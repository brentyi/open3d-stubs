"""Data handling module."""
from __future__ import annotations

import typing

import open3d.data
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "ArmadilloMesh",
    "BedroomRGBDImages",
    "BunnyMesh",
    "CrateModel",
    "Dataset",
    "DemoColoredICPPointClouds",
    "DemoCropPointCloud",
    "DemoCustomVisualization",
    "DemoFeatureMatchingPointClouds",
    "DemoICPPointClouds",
    "DemoPoseGraphOptimization",
    "EaglePointCloud",
    "FlightHelmetModel",
    "JackJackL515Bag",
    "JuneauImage",
    "KnotMesh",
    "LivingRoomPointClouds",
    "LoungeRGBDImages",
    "MetalTexture",
    "MonkeyModel",
    "MultiDownloadDataset",
    "OfficePointClouds",
    "PCDPointCloud",
    "PLYPointCloud",
    "PaintedPlasterTexture",
    "SampleFountainRGBDImages",
    "SampleL515Bag",
    "SampleNYURGBDImage",
    "SampleRedwoodRGBDImages",
    "SampleSUNRGBDImage",
    "SampleTUMRGBDImage",
    "SingleDownloadDataset",
    "SwordModel",
    "TerrazzoTexture",
    "TilesTexture",
    "WoodFloorTexture",
    "WoodTexture",
]

class Dataset:
    """
    The base dataset class.
    """

    def __init__(self, prefix: str, data_root: str = "") -> None: ...
    @property
    def data_root(self) -> str:
        """
        Get data root directory. The data root is set at construction time or automatically determined.

        :type: str
        """
    @property
    def download_dir(self) -> str:
        """
        Get absolute path to download directory. i.e. ${data_root}/${download_prefix}/${prefix}

        :type: str
        """
    @property
    def extract_dir(self) -> str:
        """
        Get absolute path to extract directory. i.e. ${data_root}/${extract_prefix}/${prefix}

        :type: str
        """
    @property
    def prefix(self) -> str:
        """
        Get prefix for the dataset.

        :type: str
        """
    pass

class MultiDownloadDataset(Dataset):
    """
    Multiple files download dataset class.
    """

    def __init__(
        self,
        prefix: str,
        url_mirrors_list: typing.List[typing.List[str]],
        md5_list: typing.List[str],
        no_extract: bool = False,
        data_root: str = "",
    ) -> None:
        """
        This class allows user to create simple dataset which includes multiple files downloading and extracting / copying.
        """
    pass

class SingleDownloadDataset(Dataset):
    """
    Single file download dataset class.
    """

    def __init__(
        self,
        prefix: str,
        url_mirrors: typing.List[str],
        md5: str,
        no_extract: bool = False,
        data_root: str = "",
    ) -> None:
        """
        This class allows user to create simple dataset which includes single file downloading and extracting / copying.
        """
    pass

class CrateModel(SingleDownloadDataset, Dataset):
    """
    Data class for `CrateModel` contains a crate model file, along with material and various other texture files. The model file can be accessed using `path`, however in order to access the paths to the texture files one may use path_map["filename"]` method.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Returns the `crate` model file.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path. Refer documentation page for available options.

        :type: typing.Dict[str, str]
        """
    pass

class ArmadilloMesh(SingleDownloadDataset, Dataset):
    """
    Data class for `ArmadilloMesh` contains the `ArmadilloMesh.ply` from the `Stanford 3D Scanning Repository`.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `ArmadilloMesh.ply` file.

        :type: str
        """
    pass

class DemoColoredICPPointClouds(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoColoredICPPointClouds` contains 2 point clouds of `ply` format. This dataset is used in Open3D for colored ICP demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def paths(self) -> typing.List[str]:
        """
        List of 2 point cloud paths. Use `paths[0]`, and `paths[1]`, to access the paths.

        :type: typing.List[str]
        """
    pass

class DemoCropPointCloud(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoCropPointCloud` contains a point cloud, and `cropped.json` (a saved selected polygon volume file). This dataset is used in Open3D for point cloud crop demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def cropped_json_path(self) -> str:
        """
        Path to the saved selected polygon volume file.

        :type: str
        """
    @property
    def point_cloud_path(self) -> str:
        """
        Path to the example point cloud.

        :type: str
        """
    pass

class DemoCustomVisualization(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoCustomVisualization` contains an example point-cloud, camera trajectory (json file), rendering options (json file). This data is used in Open3D for custom visualization with camera trajectory demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def camera_trajectory_path(self) -> str:
        """
        Returns path to the camera_trajectory.json.

        :type: str
        """
    @property
    def point_cloud_path(self) -> str:
        """
        Returns path to the point cloud (ply).

        :type: str
        """
    @property
    def render_option_path(self) -> str:
        """
        Returns path to the renderoption.json.

        :type: str
        """
    pass

class DemoFeatureMatchingPointClouds(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoFeatureMatchingPointClouds` contains 2 pointcloud fragments and their respective FPFH features and L32D features. This dataset is used in Open3D for point cloud feature matching demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def fpfh_feature_paths(self) -> typing.List[str]:
        """
        List of 2 saved FPFH feature binary of the respective point cloud paths. Use `fpfh_feature_paths[0]`, and `fpfh_feature_paths[1]`, to access the paths.

        :type: typing.List[str]
        """
    @property
    def l32d_feature_paths(self) -> typing.List[str]:
        """
        List of 2 saved L32D feature binary of the respective point cloud paths. Use `l32d_feature_paths[0]`, and `l32d_feature_paths[1]`, to access the paths.

        :type: typing.List[str]
        """
    @property
    def point_cloud_paths(self) -> typing.List[str]:
        """
        List of 2 point cloud paths. Use `point_cloud_paths[0]`, and `point_cloud_paths[1]`, to access the paths.

        :type: typing.List[str]
        """
    pass

class DemoICPPointClouds(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoICPPointClouds` contains 3 point clouds of binary PCD format. This dataset is used in Open3D for ICP demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def paths(self) -> typing.List[str]:
        """
        List of 3 point cloud paths. Use `paths[0]`, `paths[1]`, and `paths[2]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def transformation_log_path(self) -> str:
        """
        Path to the transformation metadata log file, containing transformation between frame 0 and 1, and frame 1 and 2.

        :type: str
        """
    pass

class DemoPoseGraphOptimization(SingleDownloadDataset, Dataset):
    """
    Data class for `DemoPoseGraphOptimization` contains an example fragment pose graph, and global pose graph. This dataset is used in Open3D for pose graph optimization demo.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def pose_graph_fragment_path(self) -> str:
        """
        Path to example global pose graph (json).

        :type: str
        """
    @property
    def pose_graph_global_path(self) -> str:
        """
        Path to example fragment pose graph (json).

        :type: str
        """
    pass

class EaglePointCloud(SingleDownloadDataset, Dataset):
    """
    Data class for `EaglePointCloud` contains the `EaglePointCloud.ply` file.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `EaglePointCloud.ply` file.

        :type: str
        """
    pass

class FlightHelmetModel(SingleDownloadDataset, Dataset):
    """
    Data class for `FlightHelmetModel` contains a flight helmet GLTF model file, along with material and various other texture files. The model file can be accessed using `path`, however in order to access the paths to the texture files one may use path_map["filename"]` method.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Returns the `FlightHelmet.gltf` model file.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path. Refer documentation page for available options.

        :type: typing.Dict[str, str]
        """
    pass

class JackJackL515Bag(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleL515Bag` contains the `JackJackL515Bag.bag` file.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `JackJackL515Bag.bag` file.

        :type: str
        """
    pass

class JuneauImage(SingleDownloadDataset, Dataset):
    """
    Data class for `JuneauImage` contains the `JuneauImage.jpg` file.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `JuneauImage.jgp` file.

        :type: str
        """
    pass

class KnotMesh(SingleDownloadDataset, Dataset):
    """
    Data class for `KnotMesh` contains the `KnotMesh.ply`.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `KnotMesh.ply` file.

        :type: str
        """
    pass

class LivingRoomPointClouds(SingleDownloadDataset, Dataset):
    """
    Dataset class for `LivingRoomPointClouds` contains 57 point clouds of binary PLY format.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def paths(self) -> typing.List[str]:
        """
        List of paths to ply point-cloud fragments of size 57. Use `paths[0]`, `paths[1]` ... `paths[56]` to access the paths.

        :type: typing.List[str]
        """
    pass

class LoungeRGBDImages(SingleDownloadDataset, Dataset):
    """
    Data class for `LoungeRGBDImages` contains a sample set of 3000 color and depth images from Stanford Lounge RGBD dataset. Additionally it also contains camera trajectory log, and mesh reconstruction.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_paths(self) -> typing.List[str]:
        """
        List of paths to color image samples of size 3000. Use `color_paths[0]`, `color_paths[1]` ... `color_paths[2999]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def depth_paths(self) -> typing.List[str]:
        """
        List of paths to depth image samples of size 3000. Use `depth_paths[0]`, `depth_paths[1]` ... `depth_paths[2999]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def reconstruction_path(self) -> str:
        """
        Path to mesh reconstruction.

        :type: str
        """
    @property
    def trajectory_log_path(self) -> str:
        """
        Path to camera trajectory log file `trajectory.log`.

        :type: str
        """
    pass

class MetalTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `MetalTexture` contains albedo, normal, roughness and metallic texture files for metal based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def metallic_texture_path(self) -> str:
        """
        Path to metallic texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass

class MonkeyModel(SingleDownloadDataset, Dataset):
    """
    Data class for `MonkeyModel` contains a monkey model file, along with material and various other texture files. The model file can be accessed using `path`, however in order to access the paths to the texture files one may use path_map["filename"]` method.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Returns the `monkey` model file.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path. Refer documentation page for available options.

        :type: typing.Dict[str, str]
        """
    pass

class BedroomRGBDImages(MultiDownloadDataset, Dataset):
    """
    Data class for `BedroomRGBDImages` contains a sample set of 21931 color and depth images from Redwood Bedroom RGBD dataset. Additionally it also contains camera trajectory log, and mesh reconstruction.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_paths(self) -> typing.List[str]:
        """
        List of paths to color image samples of size 21931. Use `color_paths[0]`, `color_paths[1]` ... `color_paths[21930]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def depth_paths(self) -> typing.List[str]:
        """
        List of paths to depth image samples of size 21931. Use `depth_paths[0]`, `depth_paths[1]` ... `depth_paths[21930]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def reconstruction_path(self) -> str:
        """
        Path to mesh reconstruction.

        :type: str
        """
    @property
    def trajectory_log_path(self) -> str:
        """
        Path to camera trajectory log file `trajectory.log`.

        :type: str
        """
    pass

class OfficePointClouds(SingleDownloadDataset, Dataset):
    """
    Dataset class for `OfficePointClouds` contains 53 point clouds of binary PLY format.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def paths(self) -> typing.List[str]:
        """
        List of paths to ply point-cloud fragments of size 53. Use `paths[0]`, `paths[1]` ... `paths[52]` to access the paths.

        :type: typing.List[str]
        """
    pass

class PCDPointCloud(SingleDownloadDataset, Dataset):
    """
    Data class for `PCDPointCloud` contains the `fragment.pcd` point cloud mesh from the `Redwood Living Room` dataset.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `pcd` format point cloud.

        :type: str
        """
    pass

class PLYPointCloud(SingleDownloadDataset, Dataset):
    """
    Data class for `PLYPointCloud` contains the `fragment.pcd` point cloud mesh from the `Redwood Living Room` dataset.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `ply` format point cloud.

        :type: str
        """
    pass

class PaintedPlasterTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `PaintedPlasterTexture` contains albedo, normal and roughness texture files for painted plaster based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass

class SampleFountainRGBDImages(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleFountainRGBDImages` contains a sample set of 33 color and depth images from the `Fountain RGBD dataset`. It also contains `camera poses at keyframes log` and `mesh reconstruction`. It is used in demo of `Color Map Optimization`.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_paths(self) -> typing.List[str]:
        """
        List of paths to color image samples of size 33. Use `color_paths[0]`, `color_paths[1]` ... `color_paths[32]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def depth_paths(self) -> typing.List[str]:
        """
        List of paths to depth image samples of size 33. Use `depth_paths[0]`, `depth_paths[1]` ... `depth_paths[32]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def keyframe_poses_log_path(self) -> str:
        """
        Path to camera poses at keyfragmes log file `key.log`.

        :type: str
        """
    @property
    def reconstruction_path(self) -> str:
        """
        Path to mesh reconstruction.

        :type: str
        """
    pass

class SampleL515Bag(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleL515Bag` contains the `SampleL515Bag.bag` file.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `SampleL515Bag.bag` file.

        :type: str
        """
    pass

class SampleNYURGBDImage(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleNYURGBDImage` contains a color image `NYU_color.ppm` and a depth image `NYU_depth.pgm` sample from NYU RGBD dataset.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_path(self) -> str:
        """
        Path to color image sample.

        :type: str
        """
    @property
    def depth_path(self) -> str:
        """
        Path to depth image sample.

        :type: str
        """
    pass

class SampleRedwoodRGBDImages(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleRedwoodRGBDImages` contains a sample set of 5 color and depth images from Redwood RGBD dataset living-room1. Additionally it also contains camera trajectory log, camera odometry log, rgbd match, and point cloud reconstruction obtained using TSDF.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def camera_intrinsic_path(self) -> str:
        """
        Path to pinhole camera intrinsic (json).

        :type: str
        """
    @property
    def color_paths(self) -> typing.List[str]:
        """
        List of paths to color image samples of size 5. Use `color_paths[0]`, `color_paths[1]` ... `color_paths[4]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def depth_paths(self) -> typing.List[str]:
        """
        List of paths to depth image samples of size 5. Use `depth_paths[0]`, `depth_paths[1]` ... `depth_paths[4]` to access the paths.

        :type: typing.List[str]
        """
    @property
    def odometry_log_path(self) -> str:
        """
        Path to camera odometry log file `odometry.log`.

        :type: str
        """
    @property
    def reconstruction_path(self) -> str:
        """
        Path to pointcloud reconstruction from TSDF.

        :type: str
        """
    @property
    def rgbd_match_path(self) -> str:
        """
        Path to color and depth image match file `rgbd.match`.

        :type: str
        """
    @property
    def trajectory_log_path(self) -> str:
        """
        Path to camera trajectory log file `trajectory.log`.

        :type: str
        """
    pass

class SampleSUNRGBDImage(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleSUNRGBDImage` contains a color image `SUN_color.jpg` and a depth image `SUN_depth.png` sample from SUN RGBD dataset.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_path(self) -> str:
        """
        Path to color image sample.

        :type: str
        """
    @property
    def depth_path(self) -> str:
        """
        Path to depth image sample.

        :type: str
        """
    pass

class SampleTUMRGBDImage(SingleDownloadDataset, Dataset):
    """
    Data class for `SampleTUMRGBDImage` contains a color image `TUM_color.png` and a depth image `TUM_depth.png` sample from TUM RGBD dataset.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def color_path(self) -> str:
        """
        Path to color image sample.

        :type: str
        """
    @property
    def depth_path(self) -> str:
        """
        Path to depth image sample.

        :type: str
        """
    pass

class BunnyMesh(SingleDownloadDataset, Dataset):
    """
    Data class for `BunnyMesh` contains the `BunnyMesh.ply` from the `Stanford 3D Scanning Repository`.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Path to the `BunnyMesh.ply` file.

        :type: str
        """
    pass

class SwordModel(SingleDownloadDataset, Dataset):
    """
    Data class for `SwordModel` contains a monkey model file, along with material and various other texture files. The model file can be accessed using `path`, however in order to access the paths to the texture files one may use path_map["filename"]` method.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def path(self) -> str:
        """
        Returns the `sword` model file.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path. Refer documentation page for available options.

        :type: typing.Dict[str, str]
        """
    pass

class TerrazzoTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `TerrazzoTexture` contains albedo, normal and roughness texture files for terrazzo based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass

class TilesTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `TilesTexture` contains albedo, normal and roughness texture files for tiles based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass

class WoodFloorTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `WoodFloorTexture` contains albedo, normal and roughness texture files for wooden floor based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass

class WoodTexture(SingleDownloadDataset, Dataset):
    """
    Data class for `WoodTexture` contains albedo, normal and roughness texture files for wood based material.
    """

    def __init__(self, data_root: str = "") -> None: ...
    @property
    def albedo_texture_path(self) -> str:
        """
        Path to albedo color texture image.

        :type: str
        """
    @property
    def normal_texture_path(self) -> str:
        """
        Path to normal texture image.

        :type: str
        """
    @property
    def path_map(self) -> typing.Dict[str, str]:
        """
        Returns the map of filename to path.

        :type: typing.Dict[str, str]
        """
    @property
    def roughness_texture_path(self) -> str:
        """
        Path to roughness texture image.

        :type: str
        """
    pass
