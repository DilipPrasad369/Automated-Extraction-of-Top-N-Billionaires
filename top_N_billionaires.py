# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:08:39 2022

@author: HOME
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

n=10

driver=webdriver.Chrome('C:\\chromedriver')

driver.get('https://www.forbes.com/real-time-billionaires/#5d10077a3d78')

table=driver.find_element(By.CLASS_NAME,'ng-table')

rows=table.find_elements(By.TAG_NAME,'tr')


head=rows.pop(0)
header=head.find_elements(By.TAG_NAME,'th')
headers=[]
for i in header:
    headers.append(i.text)


for i in range(len(rows)):
    if i>n:
        break
    else:
        columns=[]
        cols=rows[i].find_elements(By.TAG_NAME,'td')
        
        for j in range(1,len(cols)):
            print(headers[j],':',cols[j].text)
            
        print('')


driver.close()