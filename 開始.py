#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
import time

token="EAAKP6m7lRsYBAOgHpjyevQjR4q2HEWsNk2ljaqR73c6ws6Oxox7DRnTTLocbzRFLK1HqEnXpp5cmZA7hXfelSZBIYqaZAAkpWmaIH8wg5Y04ou6uSlZB3TVeu0pBUaazV88BwEHmNeLZBiNfDH3HZBl8DSs5lvhGfp2rjixvTBtUZApvZA5fYpbV7SxL6wwML5xFXx5ewFWzHyyjzjqa2zmF"
blueberry_id="116833604352865"

# 粉專的連結-讀取
res = requests.get("https://graph.facebook.com/v13.0/"+blueberry_id+"/posts?access_token="+token)
jd=json.loads(res.text)


##GAME ON!!!!!
active = True     #是否開始玩遊戲及啟動關卡 
ans_total={} #存放角色的答案&得分，例:{"level1":["A",2]}
char_name=["派森","百科","伊瑟爾"]

while active:
    user_id=[]
    comments_id=[]
    ans_comments=[]
    player_name=[]
    
    player_num=game_start(comments_id)  #玩遊戲的人數=int
    print(player_num)
    player_name=level_char()  #玩家選擇角色名=[]
    
    for name in player_name:
        ans_total[name]={}
        
    for name in player_name: #第一關
        level_1()
        ans_total[name]["level1"]=level_1()
        
    for name in player_name: #第二關
        level_2()
        ans_total[name]["level2"]=level_2()
        
    print(ans_total)


    if ans_total[player_name[0]]["level2"] ==0 or ans_total[player_name[0]]["level2"] == 0 or ans_total[player_name[0]]["level2"] == 0 :      
        for name in player_name: 
            level_3()
            ans_total[name]["level3"]=level_3()
        print(ans_total)
        
        for name in player_name: 
            level_4()
            ans_total[name]["level4"]=level_4()
        print(ans_total)
    
    elif  ans_total[player_name[0]]["level2"] == 2 or ans_total[player_name[0]]["level2"] == 2 or ans_total[player_name[0]]["level2"] == 2:
        for name in player_name: 
            level_4()
            ans_total[name]["level4"]=level_4()
        print(ans_total)
        
    for name in player_name: 
        level_5()
        ans_total[name]["level5"]=level_5()
    print(ans_total)

    for name in player_name: 
        level_6()
        ans_total[name]["level6"]=level_6()
    print(ans_total)

    for name in player_name: 
        level_7(ans_total)
        active=level7()
    print(ans_total)


     

