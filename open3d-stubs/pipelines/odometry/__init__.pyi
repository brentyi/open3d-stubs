"""Odometry pipeline."""
from __future__ import annotations

import typing

import open3d.pipelines.odometry
import open3d.utility
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "OdometryOption",
    "RGBDOdometryJacobian",
    "RGBDOdometryJacobianFromColorTerm",
    "RGBDOdometryJacobianFromHybridTerm",
    "compute_rgbd_odometry",
]

class OdometryOption:
    """
    Class that defines Odometry options.
    """

    def __init__(
        self,
        iteration_number_per_pyramid_level: open3d.utility.IntVector = open3d.utility.IntVector(
            [20, 10, 5]
        ),
        depth_diff_max: float = 0.03,
        depth_min: float = 0.0,
        depth_max: float = 4.0,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def depth_diff_max(self) -> float:
        """
        Maximum depth difference to be considered as correspondence. In depth image domain, if two aligned pixels have a depth difference less than specified value, they are considered as a correspondence. Larger value induce more aggressive search, but it is prone to unstable result.

        :type: float
        """
    @depth_diff_max.setter
    def depth_diff_max(self, arg0: float) -> None:
        """
        Maximum depth difference to be considered as correspondence. In depth image domain, if two aligned pixels have a depth difference less than specified value, they are considered as a correspondence. Larger value induce more aggressive search, but it is prone to unstable result.
        """
    @property
    def depth_max(self) -> float:
        """
        Pixels that has larger than specified depth values are ignored.

        :type: float
        """
    @depth_max.setter
    def depth_max(self, arg0: float) -> None:
        """
        Pixels that has larger than specified depth values are ignored.
        """
    @property
    def depth_min(self) -> float:
        """
        Pixels that has smaller than specified depth values are ignored.

        :type: float
        """
    @depth_min.setter
    def depth_min(self, arg0: float) -> None:
        """
        Pixels that has smaller than specified depth values are ignored.
        """
    @property
    def iteration_number_per_pyramid_level(self) -> open3d.utility.IntVector:
        """
        :type: open3d.utility.IntVector
        """
    @iteration_number_per_pyramid_level.setter
    def iteration_number_per_pyramid_level(
        self, arg0: open3d.utility.IntVector
    ) -> None:
        pass
    pass

class RGBDOdometryJacobian:
    """
    Base class that computes Jacobian from two RGB-D images.
    """

    pass

class RGBDOdometryJacobianFromColorTerm(RGBDOdometryJacobian):
    """
    Class to Compute Jacobian using color term.

    Energy: :math:`(I_p-I_q)^2.`

    Reference:

    F. Steinbrucker, J. Sturm, and D. Cremers.

    Real-time visual odometry from dense RGB-D images.

    In ICCV Workshops, 2011.
    """

    def __copy__(self) -> RGBDOdometryJacobianFromColorTerm: ...
    def __deepcopy__(self, arg0: dict) -> RGBDOdometryJacobianFromColorTerm: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RGBDOdometryJacobianFromColorTerm) -> None: ...
    def __repr__(self) -> str: ...
    pass

class RGBDOdometryJacobianFromHybridTerm(RGBDOdometryJacobian):
    """
    Class to compute Jacobian using hybrid term

    Energy: :math:`(I_p-I_q)^2 + \lambda(D_p-D_q')^2`

    Reference:

    J. Park, Q.-Y. Zhou, and V. Koltun

    Anonymous submission.
    """

    def __copy__(self) -> RGBDOdometryJacobianFromHybridTerm: ...
    def __deepcopy__(self, arg0: dict) -> RGBDOdometryJacobianFromHybridTerm: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RGBDOdometryJacobianFromHybridTerm) -> None: ...
    def __repr__(self) -> str: ...
    pass
