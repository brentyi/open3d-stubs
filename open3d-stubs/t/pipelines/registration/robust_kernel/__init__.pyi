"""Tensor-based robust kernel for outlier rejection."""
from __future__ import annotations

import typing

import open3d.t.pipelines.registration.robust_kernel
import typing_extensions
from typing_extensions import Annotated

__all__ = [
    "CauchyLoss",
    "GMLoss",
    "GeneralizedLoss",
    "HuberLoss",
    "L1Loss",
    "L2Loss",
    "RobustKernel",
    "RobustKernelMethod",
    "TukeyLoss",
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

    def __copy__(self) -> RobustKernel: ...
    def __deepcopy__(self, arg0: dict) -> RobustKernel: ...
    @typing.overload
    def __init__(self, arg0: RobustKernel) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(
        self,
        type: RobustKernelMethod = RobustKernelMethod.L2Loss,
        scaling_parameter: float = 1.0,
        shape_parameter: float = 1.0,
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def scaling_parameter(self) -> float:
        """
        Scaling parameter.

        :type: float
        """
    @scaling_parameter.setter
    def scaling_parameter(self, arg0: float) -> None:
        """
        Scaling parameter.
        """
    @property
    def shape_parameter(self) -> float:
        """
        Shape parameter.

        :type: float
        """
    @shape_parameter.setter
    def shape_parameter(self, arg0: float) -> None:
        """
        Shape parameter.
        """
    @property
    def type(self) -> RobustKernelMethod:
        """
        Loss type.

        :type: RobustKernelMethod
        """
    @type.setter
    def type(self, arg0: RobustKernelMethod) -> None:
        """
        Loss type.
        """
    pass

class RobustKernelMethod:
    """
    Robust kernel method for outlier rejection.

    Members:

      L2Loss

      L1Loss

      HuberLoss

      CauchyLoss

      GMLoss

      TukeyLoss

      GeneralizedLoss
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
    CauchyLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.CauchyLoss: 3>
    GMLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.GMLoss: 4>
    GeneralizedLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.GeneralizedLoss: 6>
    HuberLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.HuberLoss: 2>
    L1Loss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.L1Loss: 1>
    L2Loss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.L2Loss: 0>
    TukeyLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.TukeyLoss: 5>
    __members__: dict  # value = {'L2Loss': <RobustKernelMethod.L2Loss: 0>, 'L1Loss': <RobustKernelMethod.L1Loss: 1>, 'HuberLoss': <RobustKernelMethod.HuberLoss: 2>, 'CauchyLoss': <RobustKernelMethod.CauchyLoss: 3>, 'GMLoss': <RobustKernelMethod.GMLoss: 4>, 'TukeyLoss': <RobustKernelMethod.TukeyLoss: 5>, 'GeneralizedLoss': <RobustKernelMethod.GeneralizedLoss: 6>}
    pass

CauchyLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.CauchyLoss: 3>
GMLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.GMLoss: 4>
GeneralizedLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.GeneralizedLoss: 6>
HuberLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.HuberLoss: 2>
L1Loss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.L1Loss: 1>
L2Loss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.L2Loss: 0>
TukeyLoss: open3d.t.pipelines.registration.robust_kernel.RobustKernelMethod  # value = <RobustKernelMethod.TukeyLoss: 5>
