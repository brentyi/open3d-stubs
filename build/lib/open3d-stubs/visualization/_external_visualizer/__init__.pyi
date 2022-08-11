from __future__ import annotations

import typing

import open3d
import open3d.visualization._external_visualizer
import typing_extensions
from typing_extensions import Annotated

__all__ = ["EV", "ExternalVisualizer"]

class ExternalVisualizer:
    """
    This class allows to send data to an external Visualizer

        Example:
            This example sends a point cloud to the visualizer.

                import open3d as o3d
                import numpy as np
                ev = o3d.visualization.ExternalVisualizer()
                pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(np.random.rand(100,3)))
                ev.set(pcd)

        Args:
            address: The address where the visualizer is running.
                The default is localhost.
            timeout: The timeout for sending data in milliseconds.

    """

    pass

EV: open3d.visualization._external_visualizer.ExternalVisualizer
__all__ = ["ExternalVisualizer", "EV"]
