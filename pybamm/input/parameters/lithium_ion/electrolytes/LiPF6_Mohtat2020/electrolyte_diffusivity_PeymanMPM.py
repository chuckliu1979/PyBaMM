from pybamm import exp, constants, Scalar


def electrolyte_diffusivity_PeymanMPM(c_e, T):
    """
    Diffusivity of LiPF6 in EC:DMC as a function of ion concentration. The original data
    is from [1]. The fit from Dualfoil [2].

    References
    ----------
    .. [1] C Capiglia et al. 7Li and 19F diffusion coefficients and thermal
    properties of non-aqueous electrolyte solutions for rechargeable lithium batteries.
    Journal of power sources 81 (1999): 859-862.
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature


    Returns
    -------
    :class:`pybamm.Symbol`
        Electrolyte diffusivity
    """

    D_c_e = Scalar(5.35 * 10 ** (-10), "[m2.s-1]")
    E_D_e = Scalar(37040, "[J.mol-1]")
    arrhenius = exp(E_D_e / constants.R * (1 / Scalar(298.15, "[K]") - 1 / T))

    return D_c_e * arrhenius