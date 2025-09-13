# mandelbrot.py
# Python 3, mobile-friendly (Juno). Vectorized, no deprecated APIs.

import numpy as np
import matplotlib.pyplot as plt

try:
    import plotly.express as px
    _HAS_PLOTLY = True
except Exception:
    _HAS_PLOTLY = False

def mandelbrot(
    x_min=-2.5, x_max=1.0, y_min=-1.5, y_max=1.5,
    width=1000, height=800, max_iter=300, escape_radius=2.0
):
    """
    Compute escape-time for the Mandelbrot set over a rectangular region.
    Returns (escape_iterations, X_extent, Y_extent).
    """
    # Grid of complex numbers
    xs = np.linspace(x_min, x_max, width, dtype=np.float64)
    ys = np.linspace(y_min, y_max, height, dtype=np.float64)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y

    Z = np.zeros_like(C, dtype=np.complex128)
    esc = np.full(C.shape, max_iter, dtype=np.int32)  # default: never escaped
    mask = np.ones(C.shape, dtype=bool)

    r2 = escape_radius * escape_radius

    for k in range(max_iter):
        # z = z^2 + c on the subset that hasn't escaped
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        # Newly escaped points (|z|^2 > r^2)
        escaped_now = (Z.real * Z.real + Z.imag * Z.imag) > r2
        newly = mask & escaped_now
        esc[newly] = k
        mask &= ~escaped_now
        if not mask.any():
            break

    return esc, (x_min, x_max), (y_min, y_max)

def show_matplotlib(esc, xext, yext, cmap="turbo"):
    """
    Render with Matplotlib. esc==max_iter are inside-set points.
    """
    plt.figure(figsize=(6, 5), dpi=160)
    # Smooth-ish coloring: normalize by max to accentuate gradients
    im = plt.imshow(
        esc,
        extent=(xext[0], xext[1], yext[0], yext[1]),
        origin="lower",
        interpolation="nearest",
        cmap=cmap
    )
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.title("Mandelbrot Escape-Time")
    plt.colorbar(im, label="Iterations to escape")
    plt.tight_layout()
    plt.show()

def show_plotly(esc, xext, yext):
    """
    Render with Plotly for interactive pan/zoom in Juno.
    """
    if not _HAS_PLOTLY:
        raise RuntimeError("Plotly not installed. `pip install plotly`")
    # Plotly expects image data with y increasing downward; flip vertically
    esc_img = np.flipud(esc)
    fig = px.imshow(
        esc_img,
        origin="upper",
        aspect="equal",
        color_continuous_scale="Turbo",
        labels=dict(color="Iterations"),
    )
    fig.update_xaxes(
        tickmode="array",
        tickvals=[0, esc.shape[1]//2, esc.shape[1]-1],
        ticktext=[f"{xext[0]:.2f}", f"{(xext[0]+xext[1])/2:.2f}", f"{xext[1]:.2f}"],
        title="Re(c)",
    )
    fig.update_yaxes(
        tickmode="array",
        tickvals=[0, esc.shape[0]//2, esc.shape[0]-1],
        ticktext=[f"{yext[1]:.2f}", f"{(yext[0]+yext[1])/2:.2f}", f"{yext[0]:.2f}"],  # inverted
        title="Im(c)",
        scaleanchor="x",
        scaleratio=1,
    )
    fig.update_layout(
        title="Mandelbrot Escape-Time (interactive)",
        margin=dict(l=10, r=10, t=40, b=10),
        coloraxis_colorbar=dict(title="Iter"),
    )
    fig.show()

def main(
    x_min=-2.5, x_max=1.0, y_min=-1.5, y_max=1.5,
    width=900, height=700, max_iter=300, escape_radius=2.0,
    backend="mpl"
):
    esc, xext, yext = mandelbrot(
        x_min, x_max, y_min, y_max, width, height, max_iter, escape_radius
    )
    if backend == "mpl":
        show_matplotlib(esc, xext, yext)
    elif backend == "plotly":
        show_plotly(esc, xext, yext)
    else:
        raise ValueError("backend must be 'mpl' or 'plotly'")

if __name__ == "__main__":
    # Good defaults for mobile. Increase width/height or max_iter if your device handles it.
    main(backend="mpl")   # change to "plotly" for interactive in Juno