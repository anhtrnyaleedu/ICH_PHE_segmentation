Spontaneous intracerebral hemorrhage (ICH) and perihematomal edema (PHE) volumes serve as biomarkers for functional outcomes and mortality. An application use CNN model for the accurate segmenting of ICH and PHE from non-contrast head CT scans.

Data: ATACH-2
Train data: 1782 CTs ATACH-2
Independent test data: 400 CT patients Yale
Unseen independent test data: 900 CT patients Charite

A full pipeline using a deep learning method is proposed for ICH and PHE segmentation. First, we apply the skull stripping method, extract the brain window from 3D brain non-contrast head CT, and crop the objects inside the image. Second, we resample all the images to the same spacing. Then, SinuNET, a combination of Swin UNEt Transformers (SwinUNETR) with no new UNET (nn-UNET) and uncertainty segmentation detection are used.
1) Weights of model: folder in application with name=Dataset506_xxx
2) Code: please update the our files to the same in nnunetv2
3) The code and standalone application Ubuntu>=20 (size>5GB) with all library: https://drive.google.com/file/d/1fH99dmt4HI75x02RpdoB7tSh0PMRDfko/view?usp=sharing