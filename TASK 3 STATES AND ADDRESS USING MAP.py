#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os
os.getcwd()


# In[3]:


driverPath = r"C:\Users\Merit.MSSPLACA002\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)


driver.maximize_window()
driver.get("https://ai.fmcsa.dot.gov/hhg/Search.asp?ads=a")
l=[]
c=[]
p=[]
w=[]
z=[]
xn=[]

s=driver.find_elements_by_xpath("//tbody/tr[2]/td[1]/map[1]//following::area['alt']")
for nnm in s:
    xn.append(nnm.text)
for i in range(1,len(s)+1):
    try:
            name=driver.find_element_by_xpath("//tbody/tr[2]/td[1]/map[1]/area[{}]".format(i)).click()
            a=driver.find_elements_by_xpath("//body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[8]/td[1]/table[1]/tbody[1]/tr[2]/td[1]//following::a")
            for j in range(2,len(a)-10):
                d=driver.find_elements_by_xpath("//body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[8]/td[1]/table[1]/tbody[1]/tr[{}]/td[1]".format(j))
                b=driver.find_elements_by_xpath("//body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[8]/td[1]/table[1]/tbody[1]/tr[{}]/td[2]".format(j))
                t=driver.find_elements_by_xpath("//body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[8]/td[1]/table[1]/tbody[1]/tr[{}]/td[3]".format(j))
                u=driver.find_elements_by_xpath("//tbody/tr[{}]/td[4]".format(j))
                for n in d:
                    p.append(n.text)
                for m in b:
                    c.append(m.text)
                for x in t:
                    w.append(x.text)
                for v in u:
                    z.append(v.text)
            time.sleep(2)
            driver.back()
            driver.refresh()
            df=pd.DataFrame(list(zip(p,c,w,z)), columns =["Company Name","Headquarters Location","Company Type","Fleet Size"])
            df.to_excel(r"C:\\Users\\Merit.MSSPLACA002"+"\\"+"State{}.xlsx".format(i), index = False)
            p.clear()
            c.clear()
            w.clear()
            z.clear()
            del df
    except:
        pass


# In[ ]:





# In[ ]:




