Spontaneous intracerebral hemorrhage (ICH) and perihematomal edema (PHE) volumes serve as biomarkers for functional outcomes and mortality. An application use CNN model for the accurate segmenting of ICH and PHE from non-contrast head CT scans.

Data: ATACH-2
Train data: 1782 CTs ATACH-2
Independent test data: 400 CT patients Yale
Unseen independent test data: 900 CT patients Charite

A full pipeline using a deep learning method is proposed for ICH and PHE segmentation. First, we apply the skull stripping method, extract the brain window from 3D brain non-contrast head CT, and crop the objects inside the image. Second, we resample all the images to the same spacing. Then, SinNET, a combination of Swin UNEt Transformers (SwinUNETR) with no new UNET (nn-UNET) is used

Download the standalone application Ubuntu>=20 (size>5GB) with all library:
