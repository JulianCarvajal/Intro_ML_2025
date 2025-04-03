import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.stats import multivariate_normal
from matplotlib.patches import Ellipse
from scipy.stats import multivariate_normal


def plot_ellipse(ax, mu, sigma):

    vals, vecs = np.linalg.eigh(sigma)

    x, y = vecs[:, 0]
    theta = np.degrees(np.arctan2(y, x))

    w, h = 4 * np.sqrt(vals)

    ax.tick_params(axis="both", which="major", labelsize=20)
    ellipse = Ellipse(mu, w, h, angle=theta, color="k")
    ellipse.set_alpha(0.5)
    ax.add_artist(ellipse)


def plot_contour(ax, mu, sigma, levels=6):
    # Create a grid of points
    x, y = np.meshgrid(
        np.linspace(
            mu[0] - 3 * np.sqrt(sigma[0, 0]), mu[0] + 3 * np.sqrt(sigma[0, 0]), 100
        ),
        np.linspace(
            mu[1] - 3 * np.sqrt(sigma[1, 1]), mu[1] + 3 * np.sqrt(sigma[1, 1]), 100
        ),
    )

    pos = np.dstack((x, y))
    rv = multivariate_normal(mu, sigma)

    # Compute the PDF values
    pdf_values = rv.pdf(pos)

    # Define contour levels correctly
    contour_levels = np.linspace(pdf_values.min(), pdf_values.max(), levels + 2)[
        1:-1
    ]  # Ensure increasing order

    # Plot contour lines with color
    contours = ax.contour(x, y, pdf_values, levels=contour_levels, cmap="viridis")

    # Mask values outside the highest contour level
    max_level = contour_levels[-1]
    pdf_masked = np.ma.masked_where(pdf_values > max_level, pdf_values)

    # Plot filled contour with white outside the contours
    # ax.contourf(x, y, pdf_masked, levels=[pdf_values.min()] + list(contour_levels),
    #            cmap='bone', alpha=0.5, extend='neither')
    ax.set_facecolor("white")  # Set background color to white

    ax.tick_params(axis="both", which="major", labelsize=20)

    return contours


def Plot_Gaussian_3D_2D():
    N = 60
    X = np.linspace(-3, 3, N)
    Y = np.linspace(-3, 4, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu = np.array([0.0, 1.0])
    Sigma = np.array([[1.0, -0.5], [-0.5, 1.5]])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    # The distribution on the variables X, Y packed into pos.
    F = multivariate_normal(mu, Sigma)
    Z = F.pdf(pos)

    # Create a surface plot and projected filled contour plot under it.
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(
        X, Y, Z, rstride=3, cstride=3, linewidth=1, antialiased=True, cmap=cm.viridis
    )

    _ = ax.contourf(X, Y, Z, zdir="z", offset=-0.15, cmap=cm.viridis)

    # Adjust the limits, ticks and view angle
    ax.set_zlim(-0.15, 0.2)
    ax.set_zticks(np.linspace(0, 0.2, 5))
    ax.view_init(27, -21)

    plt.show()
