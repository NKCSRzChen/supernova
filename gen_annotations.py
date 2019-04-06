# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:23:11 2019

@author: ChR-PC
"""

import csv
import numpy as np
import pandas as pd
csv_data = pd.read_csv('list.csv')
# print(csv_data.shape)
namelist = []
list1 = []
list2 = []
list3 = []
list4 = []
judge = []
labels_dic = {}



for i in range(csv_data.shape[0]):
    namelist.append(csv_data.loc[i]['id'])
    list1.append(csv_data.loc[i]['x']-7)
    list2.append(csv_data.loc[i]['y']-7)
    list3.append(csv_data.loc[i]['x']+7)
    list4.append(csv_data.loc[i]['y']+7)
    judge.append(csv_data.loc[i]['judge'])
    
judge = list(set(judge))

for i in range(len(judge)):
    
    
    labels_dic[str(judge[i])] = i+1
    
# for i in range(csv_data.shape[0]):
#     print(csv_data.loc[i]['id']+str('_a'))
for i in range(csv_data.shape[0]):
#for i in range(1):
    csv_data.loc[i]['id']
    label = csv_data.loc[i]['judge'] 
    #print(label)
    left =list1[i]
    upper = list2[i]
    right = list3[i]
    lower = list4[i]
    tag = labels_dic[label]
    gt_bbox = [int(left), int(upper), int(right), int(lower), int(tag)]

    gt_bbox = np.array(gt_bbox).reshape(1,5)
    #print(np.array(gt_bbox).shape)
    #gt_bbox = np.int32(np.array(gt_bbox).flatten()).tostring()
    np.savetxt(str(csv_data.loc[i]['id'] + str('_a')) + '.txt', np.array(gt_bbox), fmt='%i')
    np.savetxt(str(csv_data.loc[i]['id'] + str('_b')) + '.txt', np.array(gt_bbox), fmt='%i')
    np.savetxt(str(csv_data.loc[i]['id'] + str('_c')) + '.txt', np.array(gt_bbox), fmt='%i')
    '''
    f = open(str(csv_data.loc[i]['id']+str('_a')) +'.txt','w')
    
    f.writelines([str(list1[i])+' ',str(list2[i])+' ',str(list3[i])+' ',str(list4[i])+' ',str(labels_dic[label])])
    f.close()
    f = open(str(csv_data.loc[i]['id']+str('_b')) +'.txt','w')
    #f.writelines([str(list1[i])+' ',str(list2[i])+' ',str(list3[i])+' ',str(list4[i])+' ',csv_data.loc[i]['judge']])
    f.writelines([str(list1[i])+' ',str(list2[i])+' ',str(list3[i])+' ',str(list4[i])+' ',str(labels_dic[label])])
    f.close()
    f = open(str(csv_data.loc[i]['id']+str('_c')) +'.txt','w')
    #f.writelines([str(list1[i])+' ',str(list2[i])+' ',str(list3[i])+' ',str(list4[i])+' ',csv_data.loc[i]['judge']])
    f.writelines([str(list1[i])+' ',str(list2[i])+' ',str(list3[i])+' ',str(list4[i])+' ',str(labels_dic[label])])
    f.close()
    '''