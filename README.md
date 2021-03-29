# py-clEsperanto
[![Image.sc forum](https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftag%2Fclesperanto.json&query=%24.topic_list.tags.0.topic_count&colorB=brightgreen&suffix=%20topics&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABPklEQVR42m3SyyqFURTA8Y2BER0TDyExZ+aSPIKUlPIITFzKeQWXwhBlQrmFgUzMMFLKZeguBu5y+//17dP3nc5vuPdee6299gohUYYaDGOyyACq4JmQVoFujOMR77hNfOAGM+hBOQqB9TjHD36xhAa04RCuuXeKOvwHVWIKL9jCK2bRiV284QgL8MwEjAneeo9VNOEaBhzALGtoRy02cIcWhE34jj5YxgW+E5Z4iTPkMYpPLCNY3hdOYEfNbKYdmNngZ1jyEzw7h7AIb3fRTQ95OAZ6yQpGYHMMtOTgouktYwxuXsHgWLLl+4x++Kx1FJrjLTagA77bTPvYgw1rRqY56e+w7GNYsqX6JfPwi7aR+Y5SA+BXtKIRfkfJAYgj14tpOF6+I46c4/cAM3UhM3JxyKsxiOIhH0IO6SH/A1Kb1WBeUjbkAAAAAElFTkSuQmCC)](https://forum.image.sc/tag/clesperanto)
[![website](https://img.shields.io/website?url=https%3A%2F%2Fclesperanto.net)](https://clesperanto.net)
[![Licence: BSD v3](https://img.shields.io/github/licenseclEsperanto/pyclesperanto_prototype)](https://github.com/clEsperanto/pyclesperanto_prototype/blob/master/LICENSE)
[![Contributors](https://img.shields.io/github/contributors-anon/clEsperanto/pyclesperanto_prototype)](https://github.com/clEsperanto/pyclesperanto_prototype/graphs/contributors)
[![Coverage Status](https://coveralls.io/repos/github/clEsperanto/pyclesperanto_prototype/badge.svg?branch=master)](https://coveralls.io/github/clEsperanto/pyclesperanto_prototype?branch=master)
[![PyPI version](https://badge.fury.io/py/pyclesperanto_prototype.svg)](https://badge.fury.io/py/pyclesperanto_prototype)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyclesperanto_prototype)](https://pypistats.org/packages/pyclesperanto_prototype)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto_prototype?style=social)](https://github.com/clEsperanto/pyclesperanto_prototype/)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto_prototype?style=social)](https://github.com/clEsperanto/pyclesperanto_prototype/)

py-clEsperanto is a prototype for [clEsperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image processing. 
It uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/).

For users convenience, there are code generators available for [napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/) and [Fiji](https://clij.github.io/assistant/).

![](https://clesperanto.github.io/napari_pyclesperanto_assistant/docs/images/screenshot_5.png)

## Reference
The [full reference](https://clij.github.io/clij2-docs/reference__pyclesperanto) is available as part of the CLIJ2 documentation.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html). If you never used python/conda environments before, please follow the instructions [here](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments) first.
* Install [pyopencl](https://documen.tician.de/pyopencl/). 

If installation of pyopencl for Windows fails, consider downloading a precompiled wheel (e.g. from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl) ) and installing it manually. Note that "cl12" and "cp38" in the filename matter: They allow you using OpenCL 1.2 compatible GPU devices from Python 3.8.

```
pip install pyopencl-2019.1.1+cl12-cp37-cp37m-win_amd64.whl
```
Alternatively, installing via conda also works:
```
conda install -c conda-forge pyopencl=2020.3.1
```

Afterwards, install pyclesperanto:

```
pip install pyclesperanto-prototype
```

### Troubleshooting installation
If you receive an error like 
```
DLL load failed: The specified procedure could not be found.
```
Try downloading and installing a pyopencl with a lower cl version, e.g. cl12 : pyopencl-2020.1+cl12-cp37-cp37m-win_amd64

## Example code
A basic image procressing workflow loads blobs.gif and counts the number of gold particles:

```python
import pyclesperanto_prototype as cle

from skimage.io import imread, imsave

# initialize GPU
cle.select_device("GTX")
print("Used GPU: " + cle.get_device().name)

# load data
image = imread('https://imagej.nih.gov/ij/images/blobs.gif')
print("Loaded image size: " + str(image.shape))

# push image to GPU memory
input = cle.push(image)
print("Image size in GPU: " + str(input.shape))

# process the image
inverted = cle.subtract_image_from_scalar(image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# for debugging: print out image
print(labeled)

# for debugging: save image to disc
imsave("result.tif", cle.pull(labeled))
```

## Example gallery 

<table border="0">
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_select_GPU.png" width="300"/>

</td><td>

[Select GPU](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/select_GPU.py)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_count_blobs.png" width="300"/>

</td><td>

[Counting blobs](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/count_blobs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/voronoi_otsu_labeling.png" width="300"/>

</td><td>

[Voronoi-Otsu labeling](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/voronoi_otsu_labeling.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/segmentation_3d.png" width="300"/>

</td><td>

[3D Image segmentation ](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/Segmentation_3D.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/segmentation_2d_membranes.png" width="300"/>

</td><td>

[Cell segmentation based on membranes](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/segmentation_2d_membranes.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_crop_and_paste_images.png" width="300"/>

</td><td>

[Crop and paste images](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/crop_and_paste_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_inspecting_3d_images.png" width="300"/>

</td><td>

[Inspecting 3D image data](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/inspecting_3d_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_affine_transforms.png" width="300"/>

</td><td>

[Rotation, scaling, translation, affine transforms](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/transforms/affine_transforms.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_vectors_and_matrices.png" width="300"/>

</td><td>

[Multiply vectors and matrices](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_vectors_and_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_matrices.png" width="300"/>

</td><td>

[Matrix multiplication](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_spots_pointlists_matrices_tables.png" width="300"/>

</td><td>

[Working with spots, pointlist and matrices](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/spots_pointlists_matrices_tables.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_centroids.png" width="300"/>

</td><td>

[Mesh between centroids](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_centroids.ipynb)

</td></tr><tr><td>


<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_touching_neighbors.png" width="300"/>

</td><td>

[Mesh between touching neighbors](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_touching_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_with_distances.png" width="300"/>

</td><td>

[Mesh with distances](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_with_distances.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_nearest_neighbors.png" width="300"/>

</td><td>

[Mesh nearest_neighbors](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_nearest_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighborhood_definitions.png" width="300"/>

</td><td>

[Neighborhood definitions](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighborhood_definitions.ipynb)


</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/tissue_neighborhood_quantification.png" width="300"/>

</td><td>

[Tissue neighborhood quantification](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/tissues/tissue_neighborhood_quantification.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighbors_of_neighbors.png" width="300"/>

</td><td>

[Neighbors of neighbors](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighbors_of_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_voronoi_diagrams.png" width="300"/>

</td><td>

[Voronoi diagrams](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/voronoi_diagrams.ipynb)

</td></tr><tr><td>

</td><td>

[Shape descriptors based on neighborhood graphs](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/shape_descriptors_based_on_neighborhood_graphs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_napari.png" width="300"/>

</td><td>

[Tribolium morphometry + Napari](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium.py)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_morphometry.png" width="300"/>

</td><td>

[Tribolium morphometry](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium_morphometry.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_napari_dask.png" width="300"/>

</td><td>

[napari+dask timelapse processing](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/napari_gui/napari_dask.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clesperanto/napari_pyclesperanto_assistant/raw/master/docs/images/screenshot.png" width="300"/>

</td><td>

[pyclesperanto assistant](https://github.com/clesperanto/napari_pyclesperanto_assistant)

</td></tr></table>

## Benchmarking
We implemented some basic benchmarking notebooks allowing to see performance differences between pyclesperanto and 
some other image processing libraries, typically using the CPU. Such benchmarking results vary heavily depending on 
image size, kernel size, used operations, parameters and used hardware. Feel free to use those notebooks, adapt them to 
your use-case scenario and benchmark on your target hardware. If you have different scenarios or use-cases, you are very 
welcome to submit your notebook as pull-request!

* [Affine transforms](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/affine_transforms.ipynb)
* [Gaussian blur](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/gaussian_blur.ipynb)
* [Convolution](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/convolution.ipynb)
* [Otsu's thresholding](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/threshold_otsu.ipynb)
* [Connected component labeling](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/connected_component_labeling.ipynb)  
* [Extend labels](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/extend_labels.ipynb)
* [Statistics of labeled pixels / regionprops](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/statistics_of_labeled_pixels.ipynb)
* [Matrix multiplication](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/matrix_multiplication.ipynb)
* [Pixel-wise comparison](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/pixelwise_comparison.ipynb)
* [Intensity projections](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/intensity_projections.ipynb)
* [Axis transposition](http://nbviewer.jupyter.org/github/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/transpose.ipynb)

## Feedback welcome!
clEsperanto is developed in the open because we believe in the open source community. See our [community guidelines](https://clij.github.io/clij2-docs/community_guidelines). Feel free to drop feedback as [github issue](https://github.com/clEsperanto/pyclesperanto_prototype/issues) or via [image.sc](https://image.sc)
