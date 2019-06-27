%matplotlib inline
%load_ext autoreload
%autoreload 2

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from showit import image
import pprint
from starfish import data, FieldOfView
from starfish.types import Features, Axes
from starfish import Experiment
from starfish.util.argparse import FsExistsType

def RNAscope(input_json: FsExistsType()):
	return Experiment.from_json(input_json)
experiment = RNAscope("/Users/sbergenholtz/Applications/starfish/rnascope/formatted/experiment.json")

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(experiment._src_doc)

fov = experiment.fov()
primary_image = fov[FieldOfView.PRIMARY_IMAGES]
dots = fov['dots']
nuclei = fov['nuclei']
images = [primary_image, nuclei, dots]
primary_image.xarray.shape

dots_mp = dots.max_proj(Axes.ROUND, Axes.CH, Axes.ZPLANE)
dots_mp_numpy = dots_mp._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)
image(dots_mp_numpy)

nuclei_mp = nuclei.max_proj(Axes.ROUND, Axes.CH, Axes.ZPLANE)
nuclei_mp_numpy = nuclei_mp._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)
image(nuclei_mp_numpy)

experiment.codebook

from starfish.image import Filter

# filter raw data
masking_radius = 15
filt = Filter.WhiteTophat(masking_radius, is_volume=False)
for img in images:
    filt.run(img, verbose=True, in_place=True)
from starfish.image import Registration

registration = Registration.FourierShiftRegistration(
    upsampling=1000,
    reference_stack=dots,
    verbose=True)
registered_image = registration.run(primary_image, in_place=False)
from starfish.spots import SpotFinder
import warnings

# parameters to define the allowable gaussian sizes (parameter space)
min_sigma = 1
max_sigma = 10
num_sigma = 30
threshold = 0.01

p = SpotFinder.BlobDetector(
    min_sigma=min_sigma,
    max_sigma=max_sigma,
    num_sigma=num_sigma,
    threshold=threshold,
    measurement_type='mean',
)

# detect triggers some numpy warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    # blobs = dots; define the spots in the dots image, but then find them again in the stack.
    dots = dots.max_proj(Axes.ROUND, Axes.ZPLANE)
    dots_numpy = dots._squeezed_numpy(Axes.ROUND, Axes.ZPLANE)
    blobs_image = dots_numpy
    intensities = p.run(registered_image, blobs_image=blobs_image)
decoded = experiment.codebook.decode_per_round_max(intensities)
genes, counts = np.unique(decoded.loc[decoded[Features.PASSES_THRESHOLDS]][Features.TARGET], return_counts=True)
table = pd.Series(counts, index=genes).sort_values(ascending=False)

from starfish.image import Segmentation

dapi_thresh = .24  # binary mask for cell (nuclear) locations
stain_thresh = .22  # binary mask for overall cells // binarization of stain
min_dist = 57

registered_mp = registered_image.max_proj(Axes.CH, Axes.ZPLANE)
registered_mp_numpy = registered_mp._squeezed_numpy(Axes.CH, Axes.ZPLANE)
stain = np.mean(registered_mp_numpy, axis=0)
stain = stain/stain.max()
nuclei = nuclei.max_proj(Axes.ROUND, Axes.CH, Axes.ZPLANE)
nuclei_numpy = nuclei._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)

seg = Segmentation.Watershed(
    nuclei_threshold=dapi_thresh,
    input_threshold=stain_thresh,
    min_distance=min_dist
)
label_image = seg.run(registered_image, nuclei)
seg.show()

from skimage.color import rgb2gray
rgb = np.zeros(registered_image.tile_shape + (3,))
nuclei_mp = nuclei.max_proj(Axes.ROUND, Axes.CH, Axes.ZPLANE)
nuclei_numpy = nuclei_mp._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)
rgb[:,:,0] = nuclei_numpy
dots_mp = dots.max_proj(Axes.ROUND, Axes.CH, Axes.ZPLANE)
dots_mp_numpy = dots_mp._squeezed_numpy(Axes.ROUND, Axes.CH, Axes.ZPLANE)
rgb[:,:,1] = dots_mp_numpy
do = rgb2gray(rgb)
do = do/(do.max())
print("The number of spots in the image is:", str(counts[0]))
image(do,size=10)