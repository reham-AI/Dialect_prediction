# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:20:08 2022

@author: Reham
"""

import pandas as pd
import re
import string

# the path to the file change it according to your location
path = "C:\\Users\\Reham\\Desktop\\AIM\\"
df = pd.read_csv(path+'fetched_data.csv') 

# ckeck nan values and duplicates
#df.isna().sum()

# cleaning data removing the user name, all english characters, numbers, emojis, punctuation, spaces..etc

def clean_data(line):
    arabic="".join([i for i in line if i not in string.punctuation]) #remove punctuation
    arabic = re.sub(r'[a-zA-Z0-9?]', '', arabic).strip()             #remove englis letters and numbers
    arabic = re.sub(r'[^\w]', ' ', arabic).strip()                   #remove emojis
    arabic = " ".join(arabic.split())                                #remove duplicate spaces
    return arabic

df['data']= df['data'].apply(lambda x: clean_data(x))

# convert dialect labels from (categorical) into (numerical)

df['dialect'] = df['dialect'].astype('category')
df['dialect'] = df['dialect'].cat.codes

