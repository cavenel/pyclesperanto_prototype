from .._tier0 import execute


from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def draw_sphere(dst : Image, x : float = 0, y : float = 0, z : float = 0, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1, value : float = 1):
    """Draws a sphere around a given point with given radii in x, y and z (if 3D). 
    
     All pixels other than in the sphere are untouched. Consider using `set(buffer, 0);` in advance.

    Available for: 2D, 3D

    Parameters
    ----------
    (ByRef Image destination, Number x, Number y, Number z, Number radius_x, Number radius_y, Number radius_z, Number value)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_drawSphere


    Returns
    -------

    """


    if (len(dst.shape) == 2):
        parameters = {
            "dst": dst,
            "cx": float(x),
            "cy": float(y),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": dst,
            "cx": float(x),
            "cy": float(y),
            "cz": float(z),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rz": float(radius_z),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "rzsq": float(radius_z * radius_z),
            "value": float(value)
        }

    execute(__file__, 'draw_sphere_' + str(len(dst.shape)) + 'd_x.cl', 'draw_sphere_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
