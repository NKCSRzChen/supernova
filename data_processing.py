# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:52:42 2019

@author: ChR-PC
"""

import os
import shutil
import csv
import pandas as pd

rootdir = '/home/chenrui/FutureCup/training'
destdir = '/home/chenrui/chenrui_git/Data/supernova/Images'
outputfile = '/home/chenrui/chenrui_git/Data/supernova/Names/train.txt'
def merge_files(srcdir, destdir):
    file_list = []
    list_all = os.listdir(srcdir)
    for ifile in list_all:
        file_list.extend(os.listdir(os.path.join(srcdir, ifile)))
        for i in range(0, len(file_list)):
            shutil.copy(os.path.join(os.path.join(srcdir, ifile), file_list[i]), destdir)
        file_list = []



def generate_names(srcdir, outputfile):
    #list_all = os.listdir(srcdir)
    list1 = []
    list1 = os.listdir(srcdir)
    # for file in list_all:
    #    list1 = os.listdir(os.path.join(rootdir, file))
    list2 = []
    for item in list1:
        list2.append(item.split(".")[0])
    f = open(outputfile,'w')
    f.write('\n'.join(list2))
    f.close()
    
    
#merge_files(rootdir,destdir)
generate_names(destdir,outputfile)