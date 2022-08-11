"""Registration pipeline."""
from __future__ import annotations

import typing

import np.typing as npt
import numpy as np
import open3d.pipelines.registration
import open3d.utility
import typing_extensions
from typing_extensions import Annotated

_Shape = typing.Tuple[int, ...]

__all__ = [
    "CauchyLoss",
    "CorrespondenceChecker",
    "CorrespondenceCheckerBasedOnDistance",
    "CorrespondenceCheckerBasedOnEdgeLength",
    "CorrespondenceCheckerBasedOnNormal",
    "FastGlobalRegistrationOption",
    "Feature",
    "GMLoss",
    "GlobalOptimizationConvergenceCriteria",
    "GlobalOptimizationGaussNewton",
    "GlobalOptimizationLevenbergMarquardt",
    "GlobalOptimizationMethod",
    "GlobalOptimizationOption",
    "HuberLoss",
    "ICPConvergenceCriteria",
    "L1Loss",
    "L2Loss",
    "PoseGraph",
    "PoseGraphEdge",
    "PoseGraphEdgeVector",
    "PoseGraphNode",
    "PoseGraphNodeVector",
    "RANSACConvergenceCriteria",
    "RegistrationResult",
    "RobustKernel",
    "TransformationEstimation",
    "TransformationEstimationForColoredICP",
    "TransformationEstimationForGeneralizedICP",
    "TransformationEstimationPointToPlane",
    "TransformationEstimationPointToPoint",
    "TukeyLoss",
    "compute_fpfh_feature",
    "evaluate_registration",
    "get_information_matrix_from_point_clouds",
    "global_optimization",
    "registration_colored_icp",
    "registration_fgr_based_on_correspondence",
    "registration_fgr_based_on_feature_matching",
    "registration_generalized_icp",
    "registration_icp",
    "registration_ransac_based_on_correspondence",
    "registration_ransac_based_on_feature_matching",
]

class RobustKernel:
    """
    Base class that models a robust kernel for outlier rejection. The virtual
    function ``weight()`` must be implemented in derived classes.

    The main idea of a robust loss is to downweight large residuals that are
    assumed to be caused from outliers such that their influence on the solution
    is reduced. This is achieved by optimizing:

    .. math.
      \def\argmin{\mathop{\rm argmin}}
      \begin{equation}
        x^{*} = \argmin_{x} \sum_{i=1}^{N} \rho({r_i(x)})
      \end{equation}
      :label: robust_loss

    where :math:`\rho(r)` is also called the robust loss or kernel and
    :math:`r_i(x)` is the residual.

    Several robust kernels have been proposed to deal with different kinds of
    outliers such as Huber, Cauchy, and others.

    The optimization problem in :eq:`robust_loss` can be solved using the
    iteratively reweighted least squares (IRLS) approach, which solves a sequence
    of weighted least squares problems. We can see the relation between the least
    squares optimization in stanad non-linear least squares and robust loss
    optimization by comparing the respective gradients which go to zero at the
    optimum (illustrated only for the :math:`i^\mathrm{th}` residual):

    .. math.
      \begin{eqnarray}
        \frac{1}{2}\frac{\partial (w_i r^2_i(x))}{\partial{x}}
        &=&
        w_i r_i(x) \frac{\partial r_i(x)}{\partial{x}} \\
        \label{eq:gradient_ls}
        \frac{\partial(\rho(r_i(x)))}{\partial{x}}
        &=&
        \rho'(r_i(x)) \frac{\partial r_i(x)}{\partial{x}}.
      \end{eqnarray}

    By setting the weight :math:`w_i= \frac{1}{r_i(x)}\rho'(r_i(x))`, we
    can solve the robust loss optimization problem by using the existing techniques
    for weighted least-squares. This scheme allows standard solvers using
    Gauss-Newton and Levenberg-Marquardt algorithms to optimize for robust losses
    and is the one implemented in Open3D.

    Then we minimize the objective function using Gauss-Newton and determine
    increments by iteratively solving:

    .. math.
      \newcommand{\mat}[1]{\mathbf{#1}}
      \newcommand{\veca}[1]{\vec{#1}}
      \renewcommand{\vec}[1]{\mathbf{#1}}
      \begin{align}
       \left(\mat{J}^\top \mat{W} \mat{J}\right)^{-1}\mat{J}^\top\mat{W}\vec{r},
      \end{align}

    where :math:`\mat{W} \in \mathbb{R}^{n\times n}` is a diagonal matrix containing
    weights :math:`w_i` for each residual :math:`r_i`

    The different loss functions will only impact in the weight for each residual
    during the optimization step.
    Therefore, the only impact of the choice on the kernel is through its first
    order derivate.

    The kernels implemented so far, and the notation has been inspired by the
    publication: **"Analysis of Robust Functions for Registration Algorithms"**, by
    Philippe Babin et al.

    For more information please also see: **"Adaptive Robust Kernels for
    Non-Linear Least Squares Problems"**, by Nived Chebrolu et al.
    """

    pass

class CorrespondenceChecker:
    """
    Base class that checks if two (small) point clouds can be aligned. This class is used in feature based matching algorithms (such as RANSAC and FastGlobalRegistration) to prune out outlier correspondences. The virtual function Check() must be implemented in subclasses.
    """

    @property
    def require_pointcloud_alignment_(self) -> bool:
        """
        Some checkers do not require point clouds to be aligned, e.g., the edge length checker. Some checkers do, e.g., the distance checker.

        :type: bool
        """
    @require_pointcloud_alignment_.setter
    def require_pointcloud_alignment_(self, arg0: bool) -> None:
        """
        Some checkers do not require point clouds to be aligned, e.g., the edge length checker. Some checkers do, e.g., the distance checker.
        """
    pass

class CorrespondenceCheckerBasedOnDistance(CorrespondenceChecker):
    """
    Class to check if aligned point clouds are close (less than specified threshold).
    """

    def __copy__(self) -> CorrespondenceCheckerBasedOnDistance: ...
    def __deepcopy__(self, arg0: dict) -> CorrespondenceCheckerBasedOnDistance: ...
    @typing.overload
    def __init__(self, arg0: CorrespondenceCheckerBasedOnDistance) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, distance_threshold: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def distance_threshold(self) -> float:
        """
        Distance threshold for the check.

        :type: float
        """
    @distance_threshold.setter
    def distance_threshold(self, arg0: float) -> None:
        """
        Distance threshold for the check.
        """
    pass

class CorrespondenceCheckerBasedOnEdgeLength(CorrespondenceChecker):
    """
    Check if two point clouds build the polygons with similar edge lengths. That is, checks if the lengths of any two arbitrary edges (line formed by two vertices) individually drawn withinin source point cloud and within the target point cloud with correspondences are similar. The only parameter similarity_threshold is a number between 0 (loose) and 1 (strict)
    """

    def __copy__(self) -> CorrespondenceCheckerBasedOnEdgeLength: ...
    def __deepcopy__(self, arg0: dict) -> CorrespondenceCheckerBasedOnEdgeLength: ...
    @typing.overload
    def __init__(self, arg0: CorrespondenceCheckerBasedOnEdgeLength) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, similarity_threshold: float = 0.9) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def similarity_threshold(self) -> float:
        """
        float value between 0 (loose) and 1 (strict): For the
        check to be true,

        :math:`||\text{edge}_{\text{source}}|| > \text{similarity_threshold} \times ||\text{edge}_{\text{target}}||` and

        :math:`||\text{edge}_{\text{target}}|| > \text{similarity_threshold} \times ||\text{edge}_{\text{source}}||`

        must hold true for all edges.

        :type: float
        """
    @similarity_threshold.setter
    def similarity_threshold(self, arg0: float) -> None:
        """
        float value between 0 (loose) and 1 (strict): For the
        check to be true,

        :math:`||\text{edge}_{\text{source}}|| > \text{similarity_threshold} \times ||\text{edge}_{\text{target}}||` and

        :math:`||\text{edge}_{\text{target}}|| > \text{similarity_threshold} \times ||\text{edge}_{\text{source}}||`

        must hold true for all edges.
        """
    pass

class CorrespondenceCheckerBasedOnNormal(CorrespondenceChecker):
    """
    Class to check if two aligned point clouds have similar normals. It considers vertex normal affinity of any correspondences. It computes dot product of two normal vectors. It takes radian value for the threshold.
    """

    def __copy__(self) -> CorrespondenceCheckerBasedOnNormal: ...
    def __deepcopy__(self, arg0: dict) -> CorrespondenceCheckerBasedOnNormal: ...
    @typing.overload
    def __init__(self, arg0: CorrespondenceCheckerBasedOnNormal) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, normal_angle_threshold: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def normal_angle_threshold(self) -> float:
        """
        Radian value for angle threshold.

        :type: float
        """
    @normal_angle_threshold.setter
    def normal_angle_threshold(self, arg0: float) -> None:
        """
        Radian value for angle threshold.
        """
    pass

class FastGlobalRegistrationOption:
    """
    Options for FastGlobalRegistration.
    """

    def __copy__(self) -> FastGlobalRegistrationOption: ...
    def __deepcopy__(self, arg0: dict) -> FastGlobalRegistrationOption: ...
    @typing.overload
    def __init__(self, arg0: FastGlobalRegistrationOption) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        division_factor: float = 1.4,
        use_absolute_scale: bool = False,
        decrease_mu: bool = False,
        maximum_correspondence_distance: float = 0.025,
        iteration_number: int = 64,
        tuple_scale: float = 0.95,
        maximum_tuple_count: int = 1000,
        tuple_test: bool = True,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def decrease_mu(self) -> bool:
        """
        bool: Set to ``True`` to decrease scale mu by ``division_factor`` for graduated non-convexity.

        :type: bool
        """
    @decrease_mu.setter
    def decrease_mu(self, arg0: bool) -> None:
        """
        bool: Set to ``True`` to decrease scale mu by ``division_factor`` for graduated non-convexity.
        """
    @property
    def division_factor(self) -> float:
        """
        float: Division factor used for graduated non-convexity.

        :type: float
        """
    @division_factor.setter
    def division_factor(self, arg0: float) -> None:
        """
        float: Division factor used for graduated non-convexity.
        """
    @property
    def iteration_number(self) -> int:
        """
        int: Maximum number of iterations.

        :type: int
        """
    @iteration_number.setter
    def iteration_number(self, arg0: int) -> None:
        """
        int: Maximum number of iterations.
        """
    @property
    def maximum_correspondence_distance(self) -> float:
        """
        float: Maximum correspondence distance.

        :type: float
        """
    @maximum_correspondence_distance.setter
    def maximum_correspondence_distance(self, arg0: float) -> None:
        """
        float: Maximum correspondence distance.
        """
    @property
    def maximum_tuple_count(self) -> int:
        """
        float: Maximum tuple numbers.

        :type: int
        """
    @maximum_tuple_count.setter
    def maximum_tuple_count(self, arg0: int) -> None:
        """
        float: Maximum tuple numbers.
        """
    @property
    def tuple_scale(self) -> float:
        """
        float: Similarity measure used for tuples of feature points.

        :type: float
        """
    @tuple_scale.setter
    def tuple_scale(self, arg0: float) -> None:
        """
        float: Similarity measure used for tuples of feature points.
        """
    @property
    def tuple_test(self) -> bool:
        """
        bool: Set to `true` to perform geometric compatibility tests on initial set of correspondences.

        :type: bool
        """
    @tuple_test.setter
    def tuple_test(self, arg0: bool) -> None:
        """
        bool: Set to `true` to perform geometric compatibility tests on initial set of correspondences.
        """
    @property
    def use_absolute_scale(self) -> bool:
        """
        bool: Measure distance in absolute scale (1) or in scale relative to the diameter of the model (0).

        :type: bool
        """
    @use_absolute_scale.setter
    def use_absolute_scale(self, arg0: bool) -> None:
        """
        bool: Measure distance in absolute scale (1) or in scale relative to the diameter of the model (0).
        """
    pass

class Feature:
    """
    Class to store featrues for registration.
    """

    def __copy__(self) -> Feature: ...
    def __deepcopy__(self, arg0: dict) -> Feature: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: Feature) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def data(self) -> Annotated[npt.NDArray[np.float64], ("m, n")]:
        """
        ``dim x n`` float64 numpy array: Data buffer storing features.

        :type: Annotated[npt.NDArray[np.float64], ("m, n")]
        """
    @data.setter
    def data(self, arg0: Annotated[npt.NDArray[np.float64], ("m, n")]) -> None:
        """
        ``dim x n`` float64 numpy array: Data buffer storing features.
        """
    pass

class GMLoss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is:

    .. math.
      \begin{equation}
        \rho(r)=
        \frac{r^2/ 2}{k + r^2}
      \end{equation}

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math.
      \begin{equation}
        w(r)=
        \frac{k}{\left(k + r^2\right)^2}
      \end{equation}
    """

    def __copy__(self) -> GMLoss: ...
    def __deepcopy__(self, arg0: dict) -> GMLoss: ...
    @typing.overload
    def __init__(self, arg0: GMLoss) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, k: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def k(self) -> float:
        """
        Parameter of the loss.

        :type: float
        """
    @k.setter
    def k(self, arg0: float) -> None:
        """
        Parameter of the loss.
        """
    pass

class GlobalOptimizationConvergenceCriteria:
    """
    Convergence criteria of GlobalOptimization.
    """

    def __copy__(self) -> GlobalOptimizationConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> GlobalOptimizationConvergenceCriteria: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: GlobalOptimizationConvergenceCriteria) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def lower_scale_factor(self) -> float:
        """
        float: Lower scale factor value.

        :type: float
        """
    @lower_scale_factor.setter
    def lower_scale_factor(self, arg0: float) -> None:
        """
        float: Lower scale factor value.
        """
    @property
    def max_iteration(self) -> int:
        """
        int: Maximum iteration number for iterative optimization module.

        :type: int
        """
    @max_iteration.setter
    def max_iteration(self, arg0: int) -> None:
        """
        int: Maximum iteration number for iterative optimization module.
        """
    @property
    def max_iteration_lm(self) -> int:
        """
        int: Maximum iteration number for Levenberg Marquardt method. max_iteration_lm is used for additional Levenberg-Marquardt inner loop that automatically changes steepest gradient gain.

        :type: int
        """
    @max_iteration_lm.setter
    def max_iteration_lm(self, arg0: int) -> None:
        """
        int: Maximum iteration number for Levenberg Marquardt method. max_iteration_lm is used for additional Levenberg-Marquardt inner loop that automatically changes steepest gradient gain.
        """
    @property
    def min_relative_increment(self) -> float:
        """
        float: Minimum relative increments.

        :type: float
        """
    @min_relative_increment.setter
    def min_relative_increment(self, arg0: float) -> None:
        """
        float: Minimum relative increments.
        """
    @property
    def min_relative_residual_increment(self) -> float:
        """
        float: Minimum relative residual increments.

        :type: float
        """
    @min_relative_residual_increment.setter
    def min_relative_residual_increment(self, arg0: float) -> None:
        """
        float: Minimum relative residual increments.
        """
    @property
    def min_residual(self) -> float:
        """
        float: Minimum residual value.

        :type: float
        """
    @min_residual.setter
    def min_residual(self, arg0: float) -> None:
        """
        float: Minimum residual value.
        """
    @property
    def min_right_term(self) -> float:
        """
        float: Minimum right term value.

        :type: float
        """
    @min_right_term.setter
    def min_right_term(self, arg0: float) -> None:
        """
        float: Minimum right term value.
        """
    @property
    def upper_scale_factor(self) -> float:
        """
        float: Upper scale factor value. Scaling factors are used for levenberg marquardt algorithm these are scaling factors that increase/decrease lambda used in H_LM = H + lambda * I

        :type: float
        """
    @upper_scale_factor.setter
    def upper_scale_factor(self, arg0: float) -> None:
        """
        float: Upper scale factor value. Scaling factors are used for levenberg marquardt algorithm these are scaling factors that increase/decrease lambda used in H_LM = H + lambda * I
        """
    pass

class GlobalOptimizationMethod:
    """
    Base class for global optimization method.
    """

    pass

class GlobalOptimizationLevenbergMarquardt(GlobalOptimizationMethod):
    """
    Global optimization with Levenberg-Marquardt algorithm. Recommended over the Gauss-Newton method since the LM has better convergence characteristics.
    """

    def __copy__(self) -> GlobalOptimizationLevenbergMarquardt: ...
    def __deepcopy__(self, arg0: dict) -> GlobalOptimizationLevenbergMarquardt: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: GlobalOptimizationLevenbergMarquardt) -> None: ...
    def __repr__(self) -> str: ...
    pass

class GlobalOptimizationGaussNewton(GlobalOptimizationMethod):
    """
    Global optimization with Gauss-Newton algorithm.
    """

    def __copy__(self) -> GlobalOptimizationGaussNewton: ...
    def __deepcopy__(self, arg0: dict) -> GlobalOptimizationGaussNewton: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: GlobalOptimizationGaussNewton) -> None: ...
    def __repr__(self) -> str: ...
    pass

class GlobalOptimizationOption:
    """
    Option for GlobalOptimization.
    """

    def __copy__(self) -> GlobalOptimizationOption: ...
    def __deepcopy__(self, arg0: dict) -> GlobalOptimizationOption: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: GlobalOptimizationOption) -> None: ...
    @typing.overload
    def __init__(
        self,
        max_correspondence_distance: float = 0.03,
        edge_prune_threshold: float = 0.25,
        preference_loop_closure: float = 1.0,
        reference_node: int = -1,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def edge_prune_threshold(self) -> float:
        """
        float: According to [Choi et al 2015], line_process weight < edge_prune_threshold (0.25) is pruned.

        :type: float
        """
    @edge_prune_threshold.setter
    def edge_prune_threshold(self, arg0: float) -> None:
        """
        float: According to [Choi et al 2015], line_process weight < edge_prune_threshold (0.25) is pruned.
        """
    @property
    def max_correspondence_distance(self) -> float:
        """
        float: Identifies which distance value is used for finding neighboring points when making information matrix. According to [Choi et al 2015], this distance is used for determining $mu, a line process weight.

        :type: float
        """
    @max_correspondence_distance.setter
    def max_correspondence_distance(self, arg0: float) -> None:
        """
        float: Identifies which distance value is used for finding neighboring points when making information matrix. According to [Choi et al 2015], this distance is used for determining $mu, a line process weight.
        """
    @property
    def preference_loop_closure(self) -> float:
        """
        float: Balancing parameter to decide which one is more reliable: odometry vs loop-closure. [0,1] -> try to unchange odometry edges, [1) -> try to utilize loop-closure. Recommendation: 0.1 for RGBD Odometry, 2.0 for fragment registration.

        :type: float
        """
    @preference_loop_closure.setter
    def preference_loop_closure(self, arg0: float) -> None:
        """
        float: Balancing parameter to decide which one is more reliable: odometry vs loop-closure. [0,1] -> try to unchange odometry edges, [1) -> try to utilize loop-closure. Recommendation: 0.1 for RGBD Odometry, 2.0 for fragment registration.
        """
    @property
    def reference_node(self) -> int:
        """
        int: The pose of this node is unchanged after optimization.

        :type: int
        """
    @reference_node.setter
    def reference_node(self, arg0: int) -> None:
        """
        int: The pose of this node is unchanged after optimization.
        """
    pass

class HuberLoss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is:

    .. math.
      \begin{equation}
        \rho(r)=
        \begin{cases}
          \frac{r^{2}}{2}, & |r| \leq k.\\
          k(|r|-k / 2), & \text{otherwise}.
        \end{cases}
      \end{equation}

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math.
      \begin{equation}
        w(r)=
        \begin{cases}
          1,              & |r| \leq k.       \\
          \frac{k}{|r|} , & \text{otherwise}.
        \end{cases}
      \end{equation}
    """

    def __copy__(self) -> HuberLoss: ...
    def __deepcopy__(self, arg0: dict) -> HuberLoss: ...
    @typing.overload
    def __init__(self, arg0: HuberLoss) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, k: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def k(self) -> float:
        """
        Parameter of the loss

        :type: float
        """
    @k.setter
    def k(self, arg0: float) -> None:
        """
        Parameter of the loss
        """
    pass

class ICPConvergenceCriteria:
    """
    Class that defines the convergence criteria of ICP. ICP algorithm stops if the relative change of fitness and rmse hit ``relative_fitness`` and ``relative_rmse`` individually, or the iteration number exceeds ``max_iteration``.
    """

    def __copy__(self) -> ICPConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> ICPConvergenceCriteria: ...
    @typing.overload
    def __init__(self, arg0: ICPConvergenceCriteria) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        relative_fitness: float = 1e-06,
        relative_rmse: float = 1e-06,
        max_iteration: int = 30,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def max_iteration(self) -> int:
        """
        Maximum iteration before iteration stops.

        :type: int
        """
    @max_iteration.setter
    def max_iteration(self, arg0: int) -> None:
        """
        Maximum iteration before iteration stops.
        """
    @property
    def relative_fitness(self) -> float:
        """
        If relative change (difference) of fitness score is lower than ``relative_fitness``, the iteration stops.

        :type: float
        """
    @relative_fitness.setter
    def relative_fitness(self, arg0: float) -> None:
        """
        If relative change (difference) of fitness score is lower than ``relative_fitness``, the iteration stops.
        """
    @property
    def relative_rmse(self) -> float:
        """
        If relative change (difference) of inliner RMSE score is lower than ``relative_rmse``, the iteration stops.

        :type: float
        """
    @relative_rmse.setter
    def relative_rmse(self, arg0: float) -> None:
        """
        If relative change (difference) of inliner RMSE score is lower than ``relative_rmse``, the iteration stops.
        """
    pass

class L1Loss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is given by:

    .. math. \rho(r) = |r|

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math. w(r) = \frac{1}{|r|}
    """

    def __copy__(self) -> L1Loss: ...
    def __deepcopy__(self, arg0: dict) -> L1Loss: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: L1Loss) -> None: ...
    def __repr__(self) -> str: ...
    pass

class L2Loss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is given by:

    .. math. \rho(r) = \frac{r^2}{2}

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math. w(r) = 1
    """

    def __copy__(self) -> L2Loss: ...
    def __deepcopy__(self, arg0: dict) -> L2Loss: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: L2Loss) -> None: ...
    def __repr__(self) -> str: ...
    pass

class PoseGraph:
    """
    Data structure defining the pose graph.
    """

    def __copy__(self) -> PoseGraph: ...
    def __deepcopy__(self, arg0: dict) -> PoseGraph: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PoseGraph) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def edges(self) -> PoseGraphEdgeVector:
        """
        ``List(PoseGraphEdge)``: List of ``PoseGraphEdge``.

        :type: PoseGraphEdgeVector
        """
    @edges.setter
    def edges(self, arg0: PoseGraphEdgeVector) -> None:
        """
        ``List(PoseGraphEdge)``: List of ``PoseGraphEdge``.
        """
    @property
    def nodes(self) -> PoseGraphNodeVector:
        """
        ``List(PoseGraphNode)``: List of ``PoseGraphNode``.

        :type: PoseGraphNodeVector
        """
    @nodes.setter
    def nodes(self, arg0: PoseGraphNodeVector) -> None:
        """
        ``List(PoseGraphNode)``: List of ``PoseGraphNode``.
        """
    pass

class PoseGraphEdge:
    """
    Edge of ``PoseGraph``.
    """

    def __copy__(self) -> PoseGraphEdge: ...
    def __deepcopy__(self, arg0: dict) -> PoseGraphEdge: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor

        3. __init__(self: open3d.pipelines.registration.PoseGraphEdge, source_node_id: int = -1, target_node_id: int = -1, transformation: np.ndarray[np.float64[4, 4]] = array([[1., 0., 0., 0.],
               [0., 1., 0., 0.],
               [0., 0., 1., 0.],
               [0., 0., 0., 1.]]), information: np.ndarray[np.float64[6, 6]] = array([[1., 0., 0., 0., 0., 0.],
               [0., 1., 0., 0., 0., 0.],
               [0., 0., 1., 0., 0., 0.],
               [0., 0., 0., 1., 0., 0.],
               [0., 0., 0., 0., 1., 0.],
               [0., 0., 0., 0., 0., 1.]]), uncertain: bool = False, confidence: float = 1.0) -> None
        """
    @typing.overload
    def __init__(self, arg0: PoseGraphEdge) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def confidence(self) -> float:
        """
        float from 0 to 1: Confidence value of the edge. if uncertain is true, it has confidence bounded in [0,1].   1 means reliable, and 0 means unreliable edge. This correspondence to line process value in [Choi et al 2015] See core/registration/globaloptimization.h for more details.

        :type: float
        """
    @confidence.setter
    def confidence(self, arg0: float) -> None:
        """
        float from 0 to 1: Confidence value of the edge. if uncertain is true, it has confidence bounded in [0,1].   1 means reliable, and 0 means unreliable edge. This correspondence to line process value in [Choi et al 2015] See core/registration/globaloptimization.h for more details.
        """
    @property
    def information(self) -> Annotated[npt.NDArray[np.float64], (6, 6)]:
        """
        ``6 x 6`` float64 numpy array: Information matrix.

        :type: Annotated[npt.NDArray[np.float64], (6, 6)]
        """
    @information.setter
    def information(self, arg0: Annotated[npt.NDArray[np.float64], (6, 6)]) -> None:
        """
        ``6 x 6`` float64 numpy array: Information matrix.
        """
    @property
    def source_node_id(self) -> int:
        """
        int: Source ``PoseGraphNode`` id.

        :type: int
        """
    @source_node_id.setter
    def source_node_id(self, arg0: int) -> None:
        """
        int: Source ``PoseGraphNode`` id.
        """
    @property
    def target_node_id(self) -> int:
        """
        int: Target ``PoseGraphNode`` id.

        :type: int
        """
    @target_node_id.setter
    def target_node_id(self, arg0: int) -> None:
        """
        int: Target ``PoseGraphNode`` id.
        """
    @property
    def transformation(self) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        ``4 x 4`` float64 numpy array: Transformation matrix.

        :type: Annotated[npt.NDArray[np.float64], (4, 4)]
        """
    @transformation.setter
    def transformation(self, arg0: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        ``4 x 4`` float64 numpy array: Transformation matrix.
        """
    @property
    def uncertain(self) -> bool:
        """
        bool: Whether the edge is uncertain. Odometry edge has uncertain == false, loop closure edges has uncertain == true

        :type: bool
        """
    @uncertain.setter
    def uncertain(self, arg0: bool) -> None:
        """
        bool: Whether the edge is uncertain. Odometry edge has uncertain == false, loop closure edges has uncertain == true
        """
    pass

class PoseGraphEdgeVector:
    """
    Vector of PoseGraphEdge
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> PoseGraphEdge:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> PoseGraphEdgeVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PoseGraphEdgeVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: PoseGraphEdge) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: PoseGraphEdgeVector) -> None: ...
    def append(self, x: PoseGraphEdge) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: PoseGraphEdgeVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: PoseGraphEdge) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> PoseGraphEdge:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> PoseGraphEdge: ...
    pass

class PoseGraphNode:
    """
    Node of ``PoseGraph``.
    """

    def __copy__(self) -> PoseGraphNode: ...
    def __deepcopy__(self, arg0: dict) -> PoseGraphNode: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PoseGraphNode) -> None: ...
    @typing.overload
    def __init__(self, pose: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def pose(self) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        :type: Annotated[npt.NDArray[np.float64], (4, 4)]
        """
    @pose.setter
    def pose(self, arg0: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        pass
    pass

class PoseGraphNodeVector:
    """
    Vector of PoseGraphNode
    """

    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> PoseGraphNode:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> PoseGraphNodeVector: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: PoseGraphNodeVector) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: PoseGraphNode) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: PoseGraphNodeVector) -> None: ...
    def append(self, x: PoseGraphNode) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: PoseGraphNodeVector) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: PoseGraphNode) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> PoseGraphNode:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> PoseGraphNode: ...
    pass

class RANSACConvergenceCriteria:
    """
    Class that defines the convergence criteria of RANSAC. RANSAC algorithm stops if the iteration number hits ``max_iteration``, or the fitness measured during validation suggests that the algorithm can be terminated early with some ``confidence``. Early termination takes place when the number of iterations reaches ``k = log(1 - confidence)/log(1 - fitness^{ransac_n})``, where ``ransac_n`` is the number of points used during a ransac iteration. Use confidence=1.0 to avoid early termination.
    """

    def __copy__(self) -> RANSACConvergenceCriteria: ...
    def __deepcopy__(self, arg0: dict) -> RANSACConvergenceCriteria: ...
    @typing.overload
    def __init__(self, arg0: RANSACConvergenceCriteria) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self, max_iteration: int = 100000, confidence: float = 0.999
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def confidence(self) -> float:
        """
        Desired probability of success. Used for estimating early termination. Use 1.0 to avoid early termination.

        :type: float
        """
    @confidence.setter
    def confidence(self, arg0: float) -> None:
        """
        Desired probability of success. Used for estimating early termination. Use 1.0 to avoid early termination.
        """
    @property
    def max_iteration(self) -> int:
        """
        Maximum iteration before iteration stops.

        :type: int
        """
    @max_iteration.setter
    def max_iteration(self, arg0: int) -> None:
        """
        Maximum iteration before iteration stops.
        """
    pass

class RegistrationResult:
    """
    Class that contains the registration results.
    """

    def __copy__(self) -> RegistrationResult: ...
    def __deepcopy__(self, arg0: dict) -> RegistrationResult: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RegistrationResult) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def correspondence_set(self) -> open3d.utility.Vector2iVector:
        """
        ``n x 2`` int numpy array: Correspondence set between source and target point cloud.

        :type: open3d.utility.Vector2iVector
        """
    @correspondence_set.setter
    def correspondence_set(self, arg0: open3d.utility.Vector2iVector) -> None:
        """
        ``n x 2`` int numpy array: Correspondence set between source and target point cloud.
        """
    @property
    def fitness(self) -> float:
        """
        float: The overlapping area (# of inlier correspondences / # of points in source). Higher is better.

        :type: float
        """
    @fitness.setter
    def fitness(self, arg0: float) -> None:
        """
        float: The overlapping area (# of inlier correspondences / # of points in source). Higher is better.
        """
    @property
    def inlier_rmse(self) -> float:
        """
        float: RMSE of all inlier correspondences. Lower is better.

        :type: float
        """
    @inlier_rmse.setter
    def inlier_rmse(self, arg0: float) -> None:
        """
        float: RMSE of all inlier correspondences. Lower is better.
        """
    @property
    def transformation(self) -> Annotated[npt.NDArray[np.float64], (4, 4)]:
        """
        ``4 x 4`` float64 numpy array: The estimated transformation matrix.

        :type: Annotated[npt.NDArray[np.float64], (4, 4)]
        """
    @transformation.setter
    def transformation(self, arg0: Annotated[npt.NDArray[np.float64], (4, 4)]) -> None:
        """
        ``4 x 4`` float64 numpy array: The estimated transformation matrix.
        """
    pass

class CauchyLoss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is:

    .. math.
      \begin{equation}
        \rho(r)=
        \frac{k^2}{2} \log\left(1 + \left(\frac{r}{k}\right)^2\right)
      \end{equation}

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math.
      \begin{equation}
        w(r)=
        \frac{1}{1 + \left(\frac{r}{k}\right)^2}
      \end{equation}
    """

    def __copy__(self) -> CauchyLoss: ...
    def __deepcopy__(self, arg0: dict) -> CauchyLoss: ...
    @typing.overload
    def __init__(self, arg0: CauchyLoss) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, k: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def k(self) -> float:
        """
        Parameter of the loss.

        :type: float
        """
    @k.setter
    def k(self, arg0: float) -> None:
        """
        Parameter of the loss.
        """
    pass

class TransformationEstimation:
    """
    Base class that estimates a transformation between two point clouds. The virtual function ComputeTransformation() must be implemented in subclasses.
    """

    pass

class TransformationEstimationForColoredICP(TransformationEstimation):
    """
    Class to estimate a transformation between two point clouds using color information
    """

    def __copy__(self) -> TransformationEstimationForColoredICP: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationForColoredICP: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationForColoredICP) -> None: ...
    @typing.overload
    def __init__(self, kernel: open3d.pipelines.registration.RobustKernel) -> None: ...
    @typing.overload
    def __init__(self, lambda_geometric: float) -> None: ...
    @typing.overload
    def __init__(
        self,
        lambda_geometric: float,
        kernel: open3d.pipelines.registration.RobustKernel,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def kernel(self) -> open3d.pipelines.registration.RobustKernel:
        """
        Robust Kernel used in the Optimization

        :type: open3d.pipelines.registration.RobustKernel
        """
    @kernel.setter
    def kernel(self, arg0: open3d.pipelines.registration.RobustKernel) -> None:
        """
        Robust Kernel used in the Optimization
        """
    @property
    def lambda_geometric(self) -> float:
        """
        lambda_geometric

        :type: float
        """
    @lambda_geometric.setter
    def lambda_geometric(self, arg0: float) -> None:
        """
        lambda_geometric
        """
    pass

class TransformationEstimationForGeneralizedICP(TransformationEstimation):
    """
    Class to estimate a transformation for Generalized ICP.
    """

    def __copy__(self) -> TransformationEstimationForGeneralizedICP: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationForGeneralizedICP: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationForGeneralizedICP) -> None: ...
    @typing.overload
    def __init__(self, epsilon: float) -> None: ...
    @typing.overload
    def __init__(
        self, epsilon: float, kernel: open3d.pipelines.registration.RobustKernel
    ) -> None: ...
    @typing.overload
    def __init__(self, kernel: open3d.pipelines.registration.RobustKernel) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def epsilon(self) -> float:
        """
        epsilon

        :type: float
        """
    @epsilon.setter
    def epsilon(self, arg0: float) -> None:
        """
        epsilon
        """
    @property
    def kernel(self) -> open3d.pipelines.registration.RobustKernel:
        """
        Robust Kernel used in the Optimization

        :type: open3d.pipelines.registration.RobustKernel
        """
    @kernel.setter
    def kernel(self, arg0: open3d.pipelines.registration.RobustKernel) -> None:
        """
        Robust Kernel used in the Optimization
        """
    pass

class TransformationEstimationPointToPlane(TransformationEstimation):
    """
    Class to estimate a transformation for point to plane distance.
    """

    def __copy__(self) -> TransformationEstimationPointToPlane: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPlane: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor

        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TransformationEstimationPointToPlane) -> None: ...
    @typing.overload
    def __init__(self, kernel: open3d.pipelines.registration.RobustKernel) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def kernel(self) -> open3d.pipelines.registration.RobustKernel:
        """
        Robust Kernel used in the Optimization

        :type: open3d.pipelines.registration.RobustKernel
        """
    @kernel.setter
    def kernel(self, arg0: open3d.pipelines.registration.RobustKernel) -> None:
        """
        Robust Kernel used in the Optimization
        """
    pass

class TransformationEstimationPointToPoint(TransformationEstimation):
    """
    Class to estimate a transformation for point to point distance.
    """

    def __copy__(self) -> TransformationEstimationPointToPoint: ...
    def __deepcopy__(self, arg0: dict) -> TransformationEstimationPointToPoint: ...
    @typing.overload
    def __init__(self, arg0: TransformationEstimationPointToPoint) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, with_scaling: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def with_scaling(self) -> bool:
        """
        Set to ``True`` to estimate scaling, ``False`` to force
        scaling to be ``1``.

        The homogeneous transformation is given by

        :math:`T = \begin{bmatrix} c\mathbf{R} & \mathbf{t} \\ \mathbf{0} & 1 \end{bmatrix}`

        Sets :math:`c = 1` if ``with_scaling`` is ``False``.

        :type: bool
        """
    @with_scaling.setter
    def with_scaling(self, arg0: bool) -> None:
        """
        Set to ``True`` to estimate scaling, ``False`` to force
        scaling to be ``1``.

        The homogeneous transformation is given by

        :math:`T = \begin{bmatrix} c\mathbf{R} & \mathbf{t} \\ \mathbf{0} & 1 \end{bmatrix}`

        Sets :math:`c = 1` if ``with_scaling`` is ``False``.
        """
    pass

class TukeyLoss(RobustKernel):
    """
    The loss :math:`\rho(r)` for a given residual ``r`` is:

    .. math.
      \begin{equation}
        \rho(r)=
        \begin{cases}
          \frac{k^2\left[1-\left(1-\left(\frac{e}{k}\right)^2\right)^3\right]}{2}, & |r| \leq k.       \\
          \frac{k^2}{2},                                                           & \text{otherwise}.
        \end{cases}
      \end{equation}

    The weight :math:`w(r)` for a given residual ``r`` is given by:

    .. math.
      \begin{equation}
        w(r)=
        \begin{cases}
          \left(1 - \left(\frac{r}{k}\right)^2\right)^2, & |r| \leq k.       \\
          0 ,                                            & \text{otherwise}.
        \end{cases}
      \end{equation}
    """

    def __copy__(self) -> TukeyLoss: ...
    def __deepcopy__(self, arg0: dict) -> TukeyLoss: ...
    @typing.overload
    def __init__(self, arg0: TukeyLoss) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, k: float) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def k(self) -> float:
        """
        ``k`` Is a running constant for the loss.

        :type: float
        """
    @k.setter
    def k(self, arg0: float) -> None:
        """
        ``k`` Is a running constant for the loss.
        """
    pass
