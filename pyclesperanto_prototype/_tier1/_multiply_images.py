from .._tier0 import execute

from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def multiply_images(src1 : Image, src2 : Image, dst : Image = None):
    """Multiplies all pairs of pixel values x and y from two image X and Y.
    
    <pre>f(x, y) = x * y</pre>
    
    Parameters
    ----------
    factor1 : Image
        The first input image to be multiplied.
    factor2 : Image
        The second image to be multiplied.
    destination : Image
        The output image where results are written into.
         
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.multiply_images(factor1, factor2, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImages    

    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'multiply_images_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return dst