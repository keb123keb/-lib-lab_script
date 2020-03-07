#!/usr/bin/python

import sys
import os




def clean_cir(target_file):
    con_list=[]
    excluded_list = ['.TEMP','.OPTION\n','+','.END\n','.INCLUDE','.PARAM']
    contain=""
    with open(target_file,'r') as f:
        flag=False
        for line in f.readlines():
            words=line.split(" ")
            #print(words[0])
            if (words[0]==".ends") and (flag==True):
                #con_list = con_list[:-1]
                con_list[-1] = '*****  '+con_list[-1]
                con_list.append("*****  "+line)
            #elif (words[0]=='.TEMP') or   (words[0]=='.OPTION\n') or(words[0]=='+') or(words[0]=='.END\n') or (words[0]=='.INCLUDE'):
            elif (words[0] in excluded_list):
                #a=1
                con_list.append("*****  "+line)
            else:
                con_list.append(line)

            if words[0] == ".subckt":
                flag=True
            else:
                flag=False

    with open(target_file,'w') as f:
        f.write(''.join(con_list))

## confirm which files need to be cleand
target_files=[]
if len(sys.argv) > 1:
    for i in range(len(sys.argv)-1):
        if sys.argv[i+1].split(".")[-1] == "cir":
            target_files.append(sys.argv[i+1])
else:
    for filename in os.listdir("./"):
        if filename.endswith(".cir"):
            target_files.append(filename)

## clean those files
if len(target_files) == 0:
    print("\nNo file is changed.")
else:
    for name in target_files:
        clean_cir(name)
    print("\n\nTotal change files Number: {}".format(len(target_files)))
    print("\nChanged files:")
    for i,name in zip(range(len(target_files)),target_files):
        print("{}. {}".format(i+1,name))
print("\nCompletes !!")

