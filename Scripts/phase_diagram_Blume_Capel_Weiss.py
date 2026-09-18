import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import brentq


# ============================================================
# BLUME-CAPEL CURIE-WEISS
#
# Dimensionless variables:
#
#     t = k_B T / J
#     d = D / J
#
# Free energy:
#
#     g(m) =
#         m^2/2
#         - t log[1 + 2 exp(-d/t) cosh(m/t)]
#
# ============================================================


# ============================================================
# PARAMETERS
# ============================================================

T_MAX = 0.70
D_MAX = 0.60

N_SECOND = 600
N_FIRST = 120

# Resolution used to find nonzero stationary points
N_M = 1200

# Number of temperatures tested when locating coexistence
N_T = 700

# Avoid exactly T = 0
T_MIN = 1e-5


# ============================================================
# TRICRITICAL POINT
# ============================================================

t_tc = 1.0 / 3.0
d_tc = (2.0 / 3.0) * np.log(2.0)

print("================================================")
print("Tricritical point")
print("================================================")
print(f"t_tc = {t_tc:.10f}")
print(f"d_tc = {d_tc:.10f}")
print()


# ============================================================
# NUMERICALLY STABLE LOG(COSH(x))
# ============================================================

def logcosh(x):
    """
    Numerically stable evaluation of log(cosh(x)).
    """

    ax = np.abs(x)

    return (
        ax
        + np.log1p(np.exp(-2.0 * ax))
        - np.log(2.0)
    )


# ============================================================
# FREE ENERGY
# ============================================================

def free_energy(m, t, d):
    """
    Dimensionless free energy per spin:

        g(m) =
            m^2/2
            - t log[1 + 2 exp(-d/t) cosh(m/t)]

    The logarithm is evaluated using logaddexp to avoid
    overflow/underflow problems.
    """

    m = np.asarray(m)

    if t <= 0:
        raise ValueError("t must be positive.")

    y = m / t

    log_x = np.log(2.0) - d / t

    # log[x cosh(y)]
    log_xcosh = log_x + logcosh(y)

    # log(1 + x cosh(y))
    log_partition = np.logaddexp(
        0.0,
        log_xcosh
    )

    return (
        0.5 * m**2
        - t * log_partition
    )


# ============================================================
# EQUATION OF STATE
#
# dg/dm = 0
#
# m =
#     x sinh(m/t)
#     ------------------
#     1 + x cosh(m/t)
#
# where
#
# x = 2 exp(-d/t)
#
# ============================================================

def equation_of_state(m, t, d):
    """
    Returns dg/dm.

    Implemented in a numerically stable way.
    """

    m = np.asarray(m)

    y = m / t

    # log[x] = log(2) - d/t
    log_x = np.log(2.0) - d / t

    # We rewrite the ratio as

    # x sinh(y)
    # ----------------
    # 1 + x cosh(y)

    # using exp(y) as the dominant exponential.

    q = log_x + y - np.log(2.0)

    exp_minus_2y = np.exp(-2.0 * y)

    # r = exp(q)
    #
    # x sinh(y) =
    # r [1 - exp(-2y)]
    #
    # x cosh(y) =
    # r [1 + exp(-2y)]

    r = np.exp(np.clip(q, -700.0, 700.0))

    numerator = (
        r * (1.0 - exp_minus_2y)
    )

    denominator = (
        1.0
        + r * (1.0 + exp_minus_2y)
    )

    ratio = numerator / denominator

    return m - ratio


# ============================================================
# FIND NONZERO LOCAL MINIMA
# ============================================================

def find_nonzero_minima(t, d):
    """
    Find all nonzero stationary points m > 0 and return
    those corresponding to local minima.

    We exploit symmetry and only consider m >= 0.
    """

    # m is physically bounded by 1
    m_grid = np.linspace(
        1e-7,
        1.0,
        N_M
    )

    f_grid = equation_of_state(
        m_grid,
        t,
        d
    )

    minima = []

    # Look for sign changes in dg/dm.
    #
    # minimum:
    #
    #       dg/dm : - -> +
    #

    for i in range(len(m_grid) - 1):

        f1 = f_grid[i]
        f2 = f_grid[i + 1]

        if not (
            np.isfinite(f1)
            and np.isfinite(f2)
        ):
            continue

        if f1 < 0.0 and f2 > 0.0:

            try:

                m_root = brentq(
                    lambda m:
                        equation_of_state(
                            m, t, d
                        ),
                    m_grid[i],
                    m_grid[i + 1],
                    xtol=1e-12,
                    rtol=1e-12
                )

                if m_root > 1e-5:

                    minima.append(m_root)

            except ValueError:
                pass

    return minima


# ============================================================
# NONZERO MINIMUM WITH LOWEST FREE ENERGY
# ============================================================

def nonzero_minimum(t, d):
    """
    Find the nonzero local minimum with the lowest free energy.

    Returns

        m_star
        Delta_g

    where

        Delta_g = g(m_star) - g(0)
    """

    minima = find_nonzero_minima(
        t,
        d
    )

    if len(minima) == 0:
        return np.nan, np.nan

    energies = np.array([
        free_energy(m, t, d)
        for m in minima
    ])

    i = np.argmin(energies)

    m_star = minima[i]

    delta_g = (
        free_energy(m_star, t, d)
        - free_energy(0.0, t, d)
    )

    return m_star, delta_g


# ============================================================
# FIND FIRST-ORDER TRANSITION FOR FIXED d
# ============================================================

def first_order_temperature(d):
    """
    For a fixed d > d_tc, find the temperature at which

        g(m*) = g(0)

    with m* > 0.

    This is the first-order coexistence temperature.
    """

    # At d -> 1/2, the transition temperature -> 0.
    #
    # At d -> d_tc, the transition temperature -> 1/3.

    t_grid = np.linspace(
        T_MIN,
        t_tc - 1e-7,
        N_T
    )

    delta_g = np.full_like(
        t_grid,
        np.nan
    )

    # --------------------------------------------------------
    # Evaluate free-energy difference
    # --------------------------------------------------------

    for i, t in enumerate(t_grid):

        _, dg = nonzero_minimum(
            t,
            d
        )

        delta_g[i] = dg

    # --------------------------------------------------------
    # Search for a sign change
    #
    # Low T:
    #
    #     ordered phase stable
    #     Delta g < 0
    #
    # High T:
    #
    #     disordered phase stable
    #     Delta g > 0
    #
    # --------------------------------------------------------

    for i in range(len(t_grid) - 1):

        f1 = delta_g[i]
        f2 = delta_g[i + 1]

        if not (
            np.isfinite(f1)
            and np.isfinite(f2)
        ):
            continue

        if f1 * f2 < 0.0:

            try:

                t_transition = brentq(
                    lambda t:
                        nonzero_minimum(
                            t, d
                        )[1],
                    t_grid[i],
                    t_grid[i + 1],
                    xtol=1e-10,
                    rtol=1e-10
                )

                m_transition, _ = (
                    nonzero_minimum(
                        t_transition,
                        d
                    )
                )

                return (
                    t_transition,
                    m_transition
                )

            except ValueError:
                pass

    return np.nan, np.nan


# ============================================================
# SECOND-ORDER TRANSITION LINE
# ============================================================
#
# For m -> 0:
#
#     1 =
#     x/t
#     -----
#     1+x
#
# with
#
#     x = 2 exp(-d/t)
#
# Hence:
#
#     t = x/(1+x)
#
#     d = -t log(x/2)
#
# ============================================================

x_vals = np.linspace(
    0.5,
    2.0,
    N_SECOND
)

t_second = (
    x_vals
    / (1.0 + x_vals)
)

d_second = (
    -t_second
    * np.log(x_vals / 2.0)
)


# Sort by d
idx = np.argsort(d_second)

d_second = d_second[idx]
t_second = t_second[idx]


# ============================================================
# FIRST-ORDER TRANSITION LINE
# ============================================================

# Avoid exactly d_tc because the nonzero minimum becomes
# infinitesimally small there.

d_first_grid = np.linspace(
    d_tc + 2e-4,
    0.49995,
    N_FIRST
)

t_first = []
d_first = []
m_first = []


print("================================================")
print("Calculating first-order transition line")
print("================================================")

for j, d in enumerate(d_first_grid):

    t, m = first_order_temperature(d)

    if np.isfinite(t):

        d_first.append(d)
        t_first.append(t)
        m_first.append(m)

    if (j + 1) % 10 == 0:

        print(
            f"{j+1:4d}/{len(d_first_grid)} "
            f"| d = {d:.5f} "
            f"| t = {t:.6f} "
            f"| m = {m:.6f}"
        )


d_first = np.array(d_first)
t_first = np.array(t_first)
m_first = np.array(m_first)


# ============================================================
# SORT FIRST-ORDER DATA
# ============================================================

idx = np.argsort(d_first)

d_first = d_first[idx]
t_first = t_first[idx]
m_first = m_first[idx]


# ============================================================
# ADD THE LIMITING ENDPOINT
# ============================================================
#
# The first-order line satisfies
#
#     t -> 0
#     d -> 1/2
#
# It is a limiting point, not obtained by solving at t = 0.
#
# ============================================================

d_first_plot = np.concatenate([
    d_first,
    [0.5]
])

t_first_plot = np.concatenate([
    t_first,
    [0.0]
])


# ============================================================
# PLOT
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 6)
)


# ------------------------------------------------------------
# Second order
# ------------------------------------------------------------

ax.plot(
    t_second,
    d_second,
    color='tab:blue',
    linewidth=2.5,
    label=r'2ª ordem ($m\rightarrow0$)'
)


# ------------------------------------------------------------
# First order
# ------------------------------------------------------------

ax.plot(
    t_first_plot,
    d_first_plot,
    color='tab:red',
    linewidth=2.5,
    linestyle='--',
    label=r'1ª ordem (coexistência)'
)


# ------------------------------------------------------------
# Tricritical point
# ------------------------------------------------------------

ax.plot(
    t_tc,
    d_tc,
    marker='o',
    markersize=9,
    color='tab:green',
    markeredgecolor='black',
    label='Ponto tricrítico'
)


# ------------------------------------------------------------
# T = 0 endpoint
# ------------------------------------------------------------

ax.plot(
    0.0,
    0.5,
    marker='o',
    markersize=9,
    color='black',
    label=r'$(t,d)=(0,1/2)$'
)


# ------------------------------------------------------------
# Labels
# ------------------------------------------------------------

ax.set_xlabel(
    r'$t = k_B T/J$',
    fontsize=14
)

ax.set_ylabel(
    r'$d = D/J$',
    fontsize=14
)

ax.set_title(
    'Diagrama de fases — Blume–Capel Curie–Weiss',
    fontsize=14
)


# ------------------------------------------------------------
# Limits
# ------------------------------------------------------------

ax.set_xlim(
    0.0,
    0.70
)

ax.set_ylim(
    0.0,
    0.60
)


# ------------------------------------------------------------
# Grid / legend
# ------------------------------------------------------------

ax.grid(
    True,
    alpha=0.3
)

ax.legend(
    fontsize=11
)


plt.tight_layout()
plt.show()


# ============================================================
# PRINT SOME CHECK VALUES
# ============================================================

print()
print("================================================")
print("Checks")
print("================================================")

print(
    f"Tricritical point:"
    f"  t = {t_tc:.8f},"
    f"  d = {d_tc:.8f}"
)

print()

if len(d_first) > 0:

    print(
        "First-order line:"
    )

    for d_test in [
        0.463,
        0.470,
        0.480,
        0.490,
        0.499,
        0.4999
    ]:

        if d_test <= d_first.max():

            i = np.argmin(
                np.abs(
                    d_first - d_test
                )
            )

            print(
                f"d = {d_first[i]:.6f} "
                f"-> t = {t_first[i]:.6f}, "
                f"m = {m_first[i]:.6f}"
            )

print()
print(
    "Endpoint T -> 0:"
)

print(
    "t -> 0, d -> 1/2"
)
