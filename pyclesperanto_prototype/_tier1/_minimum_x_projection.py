from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_2d_zy

@plugin_function(output_creator=create_2d_zy)
def minimum_x_projection(input : Image, output : Image = None):
    """Determines the minimum projection of an image along X.

    Available for: 3D

    Parameters
    ----------
    (Image source, ByRef Image destination_sum)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_minimumXProjection


    Returns
    -------

    """


    parameters = {
        "dst_min":output,
        "src":input,
    }

    execute(__file__, 'minimum_x_projection_x.cl', 'minimum_x_projection', output.shape, parameters)
    return output
