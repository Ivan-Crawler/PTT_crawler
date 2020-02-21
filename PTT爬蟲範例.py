# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:55:36 2019

@author: Ivan
"""
from Ivan_ptt import crawl_ptt_page

## 必要設定的欄位
# 1. Board_Name修改ptt板位
# 2. page_num想要爬幾頁
Gossiping = crawl_ptt_page(Board_Name ='Gossiping',page_num= 5)
Elephants = crawl_ptt_page(Board_Name ='Elephants' ,
                            start =4921 ,page_num= 5)

for i in ['Gossiping','BabyMother','basketball','e-shopping','fatworld','FITNESS','MuscleBeach','Road_Running','sex','WomenTalk']:
    crawl_ptt_page(Board_Name =i,page_num= 1)