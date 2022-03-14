# -*- coding: utf-8 -*-
"""
a.data fetching script
@author: Reham Mohamed
To : AIM 
"""

import requests
import pandas as pd

#read dialect_dataset csv file for IDs
path = "C:\\Users\\Reham\\Desktop\\AIM\\" # the path to the file change it according to your location
max_batch = 1000 # max_batch is defined by 1000 as a requirement

# reading the csv file using pandas
df = pd.read_csv(path+'dialect_dataset.csv') 

#iterate to extract max_batch ids from csv
start=0
for j in range (start,df.shape[0],max_batch):
    # modify max_batch at the last iteration as the last batch is less than 1000
    if df.shape[0] - j < max_batch:
        max_batch = df.shape[0] % max_batch
    print(j)
    ids=[]
    for i in range (max_batch):
        idd = df['id'][j+i]
        idd = str(idd)
        ids.append(idd)   
        
    # post json request requires the URL and the ids (not exceeding 1000)
    r = requests.post('https://recruitment.aimtechnologies.co/ai-tasks',
                      json=ids
                     )
    response = r.json()
    
    # adding this step to cancel the sort executed on the response 
    data=[]
    for i in range (max_batch):
        data.append(response[ids[i]])
        
    #extract the corresponding dialects   
    dialect=list(df['dialect'][j:j+max_batch])
    # create csv file for the fetched data
    fetched_data = pd.DataFrame({'dialect': dialect,'data': data })
    if j==start:
        final_data = fetched_data 
    else:
        #final_data.update(fetched_data)
        frames = [final_data, fetched_data]
        final_data = pd.concat(frames)
        print("updated....")

final_data.to_csv(path+"fetched_data.csv",index=False)