from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def subtract_image_from_scalar(input : Image, output : Image = None, scalar : float = 0):
    """Subtracts one image X from a scalar s pixel wise.
    
    <pre>f(x, s) = s - x</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_subtractImageFromScalar


    Returns
    -------

    """


    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    }
    execute(__file__, 'subtract_image_from_scalar_' + str(len(output.shape)) + 'd_x.cl', 'subtract_image_from_scalar_' + str(len(output.shape)) + 'd', output.shape, parameters)
    return output
