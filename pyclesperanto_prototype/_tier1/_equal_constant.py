from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def equal_constant(src1 : Image, dst : Image = None, scalar : float = 0):
    """Determines if an image A and a constant b are equal.
    
    <pre>f(a, b) = 1 if a == b; 0 otherwise.</pre> 

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number constant)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_equalConstant


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'equal_constant_' + str(len(dst.shape)) + 'd_x.cl', 'equal_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
