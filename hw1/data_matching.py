# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:05:15 2022
E-mail: 3181780875@qq.com
@author: Dell

"""
import numpy as np
from utils import read_database,cal_euclidean,cal_mahalanobis,cal_cosine,plot_result
import re
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

'''
database_path='./usgs_splib07/ASCIIdata_splib07b_cvASD/all_material/'
wvl=np.loadtxt('./usgs_splib07/ASCIIdata_splib07b_cvASD/s07_ASD_Wavelengths_ASD_0.35-2.5_microns_2151_ch.txt',skiprows=1)

database_list=read_database(database_path)
spec_list=[]
spec_name=[]
pattern1=re.compile('s07_ASD_(.*?)\.txt')
for i in tqdm(range(len(database_list))):
    # print(i)
    spec_name.append(re.findall(pattern1, database_list[i])[0])
    spec_list.append(np.loadtxt(database_path+database_list[i],skiprows=1))

spec_ary=np.array(spec_list).T
spec_ary=np.where(spec_ary==-1.23e+34,0,spec_ary)
spec_ary=spec_ary[:1500,:]

spec_sum=spec_ary.sum(axis=0)
spec_sum=~(spec_sum==0)
spec_ary=spec_ary[:,spec_sum]
spec_name=np.array(spec_name)
spec_name=spec_name[spec_sum]
np.save("spec_array.npy",spec_ary)
np.save("spec_name.npy",spec_name)
# '''

spec_ary=np.load("spec_array.npy")
spec_name=np.load("spec_name.npy")
wb_radian=pd.read_csv('./spectral_experiment./17B60A4_00003.sed',skiprows=26,delimiter='	',usecols=[0,2],index_col=0).values
obj1_radian=pd.read_csv('./spectral_experiment./17B60A4_00004.sed',skiprows=26,delimiter='	',usecols=[0,2],index_col=0).values
obj2_radian=pd.read_csv('./spectral_experiment./17B60A4_00005.sed',skiprows=26,delimiter='	',usecols=[0,2],index_col=0).values

wb_refle=pd.read_csv('./spectral_experiment./White_plaque_reference_白板反射率.txt',skiprows=2,delimiter='	',index_col=0)
wb_refle=wb_refle.loc[350:,:].values

obj1_refle=obj1_radian/wb_radian*wb_refle
obj2_refle=obj2_radian/wb_radian*wb_refle
obj1_refle=obj1_refle[:1500,:]
obj2_refle=obj2_refle[:1500,:]

plt.plot(obj1_refle)
plt.plot(obj2_refle)

obj1_index,obj2_index=cal_euclidean(obj1_refle,obj2_refle,spec_ary)
plot_result(obj1_refle,obj2_refle,obj1_index,obj2_index,spec_ary,spec_name,'euclidean')
print('the most similar obj in euclidean distance with obj1 is',spec_name[obj1_index])
print('the most similar obj in euclidean distance with obj2 is',spec_name[obj2_index])

obj1_index,obj2_index=cal_mahalanobis(obj1_refle,obj2_refle,spec_ary)
plot_result(obj1_refle,obj2_refle,obj1_index,obj2_index,spec_ary,spec_name,'mahalanobis')
print('the most similar obj in mahalanobis distance with obj1 is',spec_name[obj1_index])
print('the most similar obj in mahalanobis distance with obj2 is',spec_name[obj2_index])

obj1_index,obj2_index=cal_cosine(obj1_refle,obj2_refle,spec_ary)
plot_result(obj1_refle,obj2_refle,obj1_index,obj2_index,spec_ary,spec_name,'cosine')
print('the most similar obj in cosine distance with obj1 is',spec_name[obj1_index])
print('the most similar obj in cosine distance with obj2 is',spec_name[obj2_index])

