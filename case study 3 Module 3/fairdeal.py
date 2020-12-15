# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:32:04 2020

@author: Hp
"""
import re
import  pandas
list1=[]
pd=pandas.read_csv("fairDealcustomerdata.csv")
print(pd)

df = Dataframe(pd.name)

split_names = (df['Fullname']
    .str.strip()
    .str.split(' ', n=1, expand=True)
    .rename(columns={0:'Title', 1:'First_name'})
)