# Remote-Sensing-Homework
This repository contains homework for Southern University of Science and Technology(SUSTech) Environment Remote Sensing postgraduate course. The Tutor in this class is [Feng Lian](https://faculty.sustech.edu.cn/fengl/). Thanks for his work. This repository will be updated until the end of this class. 

## Getting Started

### Dependencies

* Python3.x
* numpy, pandas, matplotlib, tqdm
### Executing program

```python
python data_matching.py
```

## Help

If anyone has any problem about this repository, it’s welcomed to put forward issues in Github or email me.

## Authors

* Yu bin: 12232254@mail.sustech.edu.cn

[TOC]

### Update HW1 2022/9/24

The structure of HW1 is:

```python
└─hw1# homework1 folder
    │  data_matching.py#main
    │  matched_object_spectral_cosine.png#matched object in cosine distance
    │  matched_object_spectral_euclidean.png#matched object in euclidean distance
    │  matched_object_spectral_mahalanobis.png#matched object in mahalanobis distance
    │  spec_array.npy#numpy array format of all materials' spectrals in USGS spectral lib07
    │  spec_name.npy#numpy array format of all materials' names in USGS spectral lib07
    │  utils.py#some function used in data_matching.py
    │  
    ├─spectral_experiment#three objects measured in the experiment,object3 is the standard whiteboard, object4 is grass, object5 is a road
    │      17B60A4_00003.raw
    │      17B60A4_00003.sed
    │      17B60A4_00004.raw
    │      17B60A4_00004.sed
    │      17B60A4_00005.raw
    │      17B60A4_00005.sed
    │      White_plaque_reference_白板反射率.txt
    │      
    ├─usgs_splib07#USGS spectral lib version7
    │  │  README.htm#some description about the data
    │  │  
    │  └─ASCIIdata_splib07b_cvASD#spectral measured by ASD
    │      │  s07_ASD_Bandpass_(FWHM)_ASDFR_StandardResolution.txt
    │      │  s07_ASD_Wavelengths_ASD_0.35-2.5_microns_2151_ch.txt#wave length
    │      └─all_material#all materials' spectral in text form

    └─__pycache__
            utils.cpython-38.pyc
            
```

##### the matching result in cosine distance:

![matched_object_spectral_cosine](hw1/matched_object_spectral_cosine.png)

##### the matching result in euclidean distance: 

![matched_object_spectral_euclidean](hw1/matched_object_spectral_euclidean.png)

##### the matching result in mahalanobis distance:

![matched_object_spectral_mahalanobis](hw1/matched_object_spectral_mahalanobis.png)

### Next update is coming soon~



## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Here acknowledge the author, i.e. myself, for his time and effort and you for your effort to finish this homework:)