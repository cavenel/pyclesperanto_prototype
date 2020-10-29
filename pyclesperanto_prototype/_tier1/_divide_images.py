from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def divide_images(src : Image, src1 : Image, dst : Image = None):
    """Divides two images X and Y by each other pixel wise.
    
    <pre>f(x, y) = x / y</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image divident, Image divisor, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_divideImages


    Returns
    -------

    """


    parameters = {
        "src":src,
        "src1":src1,
        "dst":dst
    }

    execute(__file__, 'divide_images_' + str(len(dst.shape)) + 'd_x.cl', 'divide_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
