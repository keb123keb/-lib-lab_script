#!/usr/bin/python

import sys
import os
import re

def to_m(target_file):
    con_list=[]
    content = ""
    with open(target_file,'r') as f:
        for line in f.readlines():
            content = content + line.split("\n")[0].split("\r")[0]
    #print( content )
    #print( re.search(r'TIME.*\$&%#',content).group() )
    text = re.search(r'TIME.*\$&%#',content).group()
    #print( re.sub(r'([a-zA-Z_0-9]+)\(([a-zA-Z_0-9]+)',r'\1__\2__',text))
    text2 = re.sub(r'([a-zA-Z_0-9]+)\(([a-zA-Z_0-9]+)',r'\1__\2__',text)
    #print( re.findall(r'[a-zA-Z_0-9]+',text2) );
    tags = re.findall(r'[a-zA-Z_0-9]+',text2);
    #tags = ['_{0}_'.format(tag) for tag in tags]
    
    #print( content[content.find("$&%#"):-1] )
    values = content[content.find("$&%#"):-1]
    #values = re.search(r'$&%#.*([0-9E\+-].*)0\.1000000E\+31',content).group()
    values2 = re.findall(r'[0-9\.]+E(?:\+|-)(?:[0-9]{2})',values)
    #print( values2 );
    #print( len(values2) )
    len_tag = len(tags)
    len_val = len(values2)
    result = []
    for i in range(len_tag):
        result.append([])
    for i in range(len_val):
        result[i%len_tag].append(values2[i])
    #print(result)
    len_3 = len_val/len_tag ;
    #print(str(len_val)+";"+str(len_tag)+";"+str(len_3));

    with open(re.sub(r'.tr([0-9])$',r'_\1.m',target_file),'w') as f:
        for i in range(len_tag):
            f.write(tags[i]+" = [ ")
            for j in range(len_3):
                f.write(" "+str(float(result[i][j]))+" ")
            f.write("];\n")
        #f.write(''.join(con_list))

## confirm which files need to be cleand
target_files=[]
if len(sys.argv) > 1:
    for i in range(len(sys.argv)-1):
        if re.search(r'^tr[0-9]$',sys.argv[i+1].split(".")[-1]):
            #target_files.append(re.sub(r'.tr[0-9]$','',sys.argv[i+1]))
            target_files.append(sys.argv[i+1])
else:
    for filename in os.listdir("./"):
        if re.search(r'^tr[0-9]$',filename.split(".")[-1]):
            #target_files.append(re.sub(r'.tr[0-9]$','',filename))
            target_files.append(filename)

## clean those files
if len(target_files) == 0:
    print("\nNo file is changed.")
else:
    for name in target_files:
        to_m(name)
    print("\n\nTotal generated files Number: {}".format(len(target_files)))
    print("\ngenerated files:")
    target_files = [re.sub(r'.tr([0-9])$',r'_\1.m',target_file) for target_file in target_files]
    #print(target_files);
    for i,name in zip(range(len(target_files)),target_files):
        print("{}. {}".format(i+1,name))
print("\nCompletes !!")

