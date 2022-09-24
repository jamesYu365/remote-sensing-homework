# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:40:48 2022
E-mail: 3181780875@qq.com
@author: Dell

"""

import os
import matplotlib.pyplot as plt
import numpy as np

def read_database(database_path):
    database_list=os.walk(database_path)
    database_list=list(map(list,iter(database_list)))
    database_list=database_list[0][-1]
    return database_list


def plot_result(obj1_refle,obj2_refle,obj1_index,obj2_index,spec_ary,spec_name,distance):
    fig,axs=plt.subplots(1,2,figsize=(10,5),dpi=200)
    axs[0].plot(obj1_refle,'r*',label='object1')
    axs[0].plot(spec_ary[:,obj1_index],'b',label=spec_name[obj1_index])
    axs[1].plot(obj2_refle,'r*',label='object2')
    axs[1].plot(spec_ary[:,obj2_index],'b',label=spec_name[obj2_index])
    axs[0].legend()
    axs[0].set_xlabel('wave length')
    axs[0].set_ylabel('reflectance')
    axs[1].legend()
    axs[1].set_xlabel('wave length')
    axs[1].set_ylabel('reflectance')
    plt.savefig(f'matched_object_spectral_{distance}.png',dpi=200)
    
    
def cal_euclidean(obj1_refle,obj2_refle,spec_ary):
    obj1_error=((spec_ary-obj1_refle)**2).sum(axis=0)
    obj2_error=((spec_ary-obj2_refle)**2).sum(axis=0)
    
    obj1_index=np.argmin(obj1_error)
    obj2_index=np.argmin(obj2_error)
    
    return obj1_index,obj2_index


def cal_mahalanobis(obj1_refle,obj2_refle,spec_ary):
    obj1_error=((obj1_refle-spec_ary).T@np.linalg.inv(np.cov(spec_ary))@(obj1_refle-spec_ary)).diagonal()
    obj2_error=((obj2_refle-spec_ary).T@np.linalg.inv(np.cov(spec_ary))@(obj2_refle-spec_ary)).diagonal()
    
    obj1_index=np.argmin(obj1_error)
    obj2_index=np.argmin(obj2_error)
    
    return obj1_index,obj2_index


def cal_cosine(obj1_refle,obj2_refle,spec_ary):
    obj1_error=(obj1_refle*spec_ary).sum(axis=0)/np.sqrt((obj1_refle**2).sum(axis=0))/np.sqrt((spec_ary**2).sum(axis=0))
    obj2_error=(obj2_refle*spec_ary).sum(axis=0)/np.sqrt((obj2_refle**2).sum(axis=0))/np.sqrt((spec_ary**2).sum(axis=0))
    
    obj1_index=np.argmax(obj1_error)
    obj2_index=np.argmax(obj2_error)
    
    return obj1_index,obj2_index









