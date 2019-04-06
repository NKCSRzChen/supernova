# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:04:17 2019

@author: ChR-PC
"""
filename = '/home/chenrui/chenrui_git/Data/supernova/Names/all.txt'

trainname = '/home/chenrui/chenrui_git/Data/supernova/Names/train.txt'
testname = '/home/chenrui/chenrui_git/Data/supernova/Names/test.txt'
validname = '/home/chenrui/chenrui_git/Data/supernova/Names/valid.txt'

flag = 0

data_list = []
with open(filename, 'r') as f:
    for line in f:
        flag+=1
        data_list.append(line)
        if flag == 14679:
            with open(trainname,'w') as trainf:
                for data in data_list:
                    trainf.write(data)
            data_list = []
        elif flag == 16776:
            with open(testname,'w') as testf:
                for data in data_list:
                    testf.write(data)
            data_list = []
        elif flag == 18873:
            with open(validname,'w') as validf:
                for data in data_list:
                    validf.write(data)
        else:
            continue

        