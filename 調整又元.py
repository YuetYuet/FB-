#!/usr/bin/env python
# coding: utf-8

# In[104]:


import requests
import json
import pandas as pd
import time

token="EAAKP6m7lRsYBAF2MnQ5H5gZAAkTqV9dBMzq0vrpUS16o2IkykYyIacK4vVMLJzeZAGF5F5SVHZA7s6CfeqzsTiKedoOWcnQ12gSf3jo9ugPbNyGq8sASw0EdOzlID0ezQhmV7ZCEws1bESiHJMWlTSztcTQEcZARqOP8uY1zzjhmnEz63iL1fAFRyfmNmwJyHaeH4r5XnRM5fVdC0U6qO"
blueberry_id="116833604352865"

# 粉專的連結-讀取
res = requests.get("https://graph.facebook.com/v13.0/"+blueberry_id+"/posts?access_token="+token)
jd=json.loads(res.text)

def game_start(comments_id):
    # 遊戲開始貼文底下的回覆
    start_id=jd["data"][-1]["id"]  #遊戲開始貼文id
    start_res = requests.get("https://graph.facebook.com/v13.0/"+"116833604352865_116842771018615"+"/comments?access_token="+token)
    start_jd=json.loads(start_res.text)
    
    if start_jd["data"]==[]:
        return game_start(comments_id)
    
    else:
        # 是否開始玩遊戲:判斷comments的內容關鍵字
        for num in range(len(start_jd["data"])):
            
            level_start_comments = start_jd["data"][num]["message"]   #遊戲留言
            level_start_comments = level_start_comments.split("+")

            if "start" in level_start_comments or "Start" in level_start_comments:  #如果留言:start
                start_comments_id = start_jd["data"][num]["id"] #留言id
                comments_id.append(start_comments_id)
                #回覆貼文網址:選擇角色
                content = "進入選擇角色，點我↓"
                content_link = "%23Blueberry學堂_選擇角色"
                level_char_link = requests.post("https://graph.facebook.com/v13.0/"+start_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                player_num = int(level_start_comments[1])

                
            else: 
                start_comments_id = start_jd["data"][num]["id"] #留言id
                comments_id.append(start_comments_id)
                content = "通關密語錯誤，請按F5再重新輸入"
                level_char_link = requests.post("https://graph.facebook.com/v13.0/"+start_comments_id+"/comments?message="+content+"&access_token="+token)
                time.sleep(3)
                #刪除留言:要留所有留言的id
                requests.delete("https://graph.facebook.com/v13.0/"+start_comments_id+"?access_token="+token)
                comments_id.pop(num)
                
                return game_start(comments_id)
            
    return player_num
            
def level_char():  #選擇角色
    level_char_id = jd["data"][-2]["id"]
    char_res = requests.get("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?access_token="+token)
    char_jd=json.loads(char_res.text)
    player_name=[]  #儲存玩家選擇角色

    if char_jd["data"] == []:  #判斷有無留言
        return level_char()
    
    #判斷留言數，不等於人數就繼續迴圈
    elif len(char_jd["data"])!= player_num:
        return level_char()
    
    else:     #判斷留言:選擇角色 #每個留言都判斷角色名稱
        for num in range(player_num):
            level_char_name = char_jd["data"][num]["message"]
            
            if  "一號角色" in level_char_name or "派森" in level_char_name:
                level_char_id = char_jd["data"][num]["id"]
                comments_id.append(level_char_id)
                comments_id.append("派森")
                #回覆貼文網址:選擇角色
                content = "進入第一關，點我↓"
                content_link = "%23Blueberry學堂_第一關"
                level1_link = requests.post("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                player_name.append("派森")  #儲存玩家選擇角色
                
            elif "二號角色" in level_char_name or "百科" in level_char_name:
                level_char_id = char_jd["data"][num]["id"]
                comments_id.append(level_char_id)
                comments_id.append("百科")
                
                content = "進入第一關，點我↓"
                content_link = "%23Blueberry學堂_第一關"
                level1_link = requests.post("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                player_name.append("百科")
                
            elif "三號角色" in level_char_name or "伊瑟爾" in level_char_name:
                level_char_id = char_jd["data"][num]["id"]
                comments_id.append(level_char_id)
                comments_id.append("伊瑟爾")
                content = "進入第一關，點我↓"
                content_link = "%23Blueberry學堂_第一關"
                level1_link = requests.post("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                player_name.append("伊瑟爾")
            
            else:
                content = "輸入錯誤，請按F5再重新輸入"
                level1_link = requests.post("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?message="+content+"&access_token="+token)
                time.sleep(3)
                #刪除留言:要留所有留言的id
                requests.delete("https://graph.facebook.com/v13.0/"+level_char_id+"?access_token="+token)
                return level_char(player_num)
            
    print(comments_id)       
    return player_name
            

def level_1():
     #第一關:(正解:5個)
    level1_id = jd["data"][-3]["id"]
    level1_res = requests.get("https://graph.facebook.com/v13.0/"+level1_id+"/comments?access_token="+token)
    level1_jd=json.loads(level1_res.text)
    
    if level1_jd["data"] == []:  #確認有無留言
        return level_1()  #沒有的話繼續執行確認
    
    elif len(level1_jd["data"]) != player_num:  #判斷留言數，不等於人數就繼續迴圈
        return level_1()
    
    else:
        for num in range(player_num):
            level1_comments=level1_jd["data"][num]["message"] #留言內容
            level1_comments_id = level1_jd["data"][num]["id"]
            comments_id.append(level1_comments_id)
            level1_comments=level1_comments.split("+")
            comments_id.append(level1_comments[0])
            if name in level1_comments:           
                if "5個" in level1_comments or "5" in level1_comments or "五" in level1_comments:
                    score1=5
                    content = "進入第二關，點我↓"
                    content_link = "%23Blueberry學堂_第二關"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                  
                elif "4個" in level1_comments or "4" in level1_comments or "四" in level1_comments:
                    score1=4
                    content = "進入第二關，點我↓"
                    content_link = "%23Blueberry學堂_第二關"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                  
                elif "3個" in level1_comments or "3" in level1_comments or "三" in level1_comments:
                    score1=3
                    content = "進入第二關，點我↓"
                    content_link = "%23Blueberry學堂_第二關"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                  
                elif "2個" in level1_comments or "2" in level1_comments or "二" in level1_comments:
                    score1=2
                    content = "進入第二關，點我↓"
                    content_link = "%23Blueberry學堂_第二關"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                  
                elif "1個" in level1_comments or "1" in level1_comments or "一" in level1_comments:
                    score1=1
                    content = "進入第二關，點我↓"
                    content_link = "%23Blueberry學堂_第二關"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                  
                else:
                    content = "輸入錯誤，請按F5再重新輸入"
                    level1_link = requests.post("https://graph.facebook.com/v13.0/"+level1_comments_id+"/comments?message="+content+"&access_token="+token)
                    time.sleep(3)
                    #刪除留言:要留所有留言的id
                    requests.delete("https://graph.facebook.com/v13.0/"+level1_comments_id+"?access_token="+token)
                    return level_1()
    return score1

def level_2():
    #第二關(正解:A)
    level2_id = jd["data"][-4]["id"] #第二關id
    level2_res = requests.get("https://graph.facebook.com/v13.0/"+level2_id+"/comments?access_token="+token)
    level2_jd=json.loads(level2_res.text)
    if level2_jd["data"] == []:  #確認有無留言
        return level_2()        #沒有的話繼續執行確認  
    elif len(level2_jd["data"]) != player_num:  #判斷留言數，不等於人數就繼續迴圈
        return level_2()    
    
    else:
        for num in range(len(level2_jd["data"])):
            level2_comments=level2_jd["data"][num]["message"] #第一個留言內容
            level2_comments_id = level2_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level2_comments_id)
            level2_comments=level2_comments.split("+")            
            comments_id.append(level2_comments[0])
            
            if name in level2_comments:
                if "A" in level2_comments or "a" in level2_comments:  #正解:A
                    score2=2   #答對+2分，回覆貼文網址:level4
                    content = "進入第三關，點我↓"
                    content_link = "%23Blueberry學堂_第三關"
                    level4_link = requests.post("https://graph.facebook.com/v13.0/"+level2_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                elif "B" in level2_comments or "C" in level2_comments or "b" in level2_comments or "c" in level2_comments:
                    score2=0   #答錯0分，回覆貼文網址:level3
                    content = "進入加分題，點我↓"
                    content_link = "%23Blueberry學堂_請把握機會"
                    level3_link = requests.post("https://graph.facebook.com/v13.0/"+level2_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                else:
                    content = "輸入錯誤，不給你分數XD，直接下一關"
                    content_link = "%23Blueberry學堂_請把握機會"
                    level3_link = requests.post("https://graph.facebook.com/v13.0/"+level2_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                
    return score2

def level_3():
    #第三關(正解:ans_count==3)
    level3_id = jd["data"][-5]["id"] #第三關id
    level3_res = requests.get("https://graph.facebook.com/v13.0/"+level3_id+"/comments?access_token="+token)
    level3_jd=json.loads(level3_res.text)
    if level3_jd["data"]==[]: #確認有無留言
        return level_3() #沒有的話繼續執行確認
    
    else:
        for num in range(0,len(level3_jd["data"])):
            level3_comments=level3_jd["data"][num]["message"] #第一個留言內容
            level3_comments_id = level3_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level3_comments_id)

            #正確答案
            correct=["pandas","numpy","datetime","time","BeautifulSoup","selenium","pymongo",
                    "pymysql","cv2","tkinter","random","requests","bs4"]
            if name in level3_comments:
                level3_comments=level3_comments.split("+")  #回答留言是字串，先用"+"切割後判斷是否正確
                comments_id.append(level3_comments[0])
                name=level3_comments[0]
                ans_count=0  #計算回答正確的答案有幾個

                for ans in level3_comments[1:]:
                    if ans in correct:
                        ans_count+=1

                if ans_count==3:  #如果正確答案數==3:正解
                    #回覆貼文網址:level4
                    score3=2
                    content = "全對! 可以加2分，進入下一關，點我↓"
                    content_link = "%23Blueberry學堂_第四關"
                    level4_link = requests.post("https://graph.facebook.com/v13.0/"+level3_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                else:
                    #回覆貼文網址:level4
                    score3=0
                    content = "有錯! 真可惜，直接進入下一關，點我↓"
                    content_link = "%23Blueberry學堂_第四關"
                    level4_link = requests.post("https://graph.facebook.com/v13.0/"+level3_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
    
    return score3

def level_4():
    #第四關(正解:A)
    level4_id = jd["data"][-6]["id"] #第四關id
    level4_res = requests.get("https://graph.facebook.com/v13.0/"+level4_id+"/comments?access_token="+token)
    level4_jd=json.loads(level4_res.text)
    if level4_jd["data"]==[]:
        return level_4()
    else:
        for num in range(0,len(level4_jd["data"])):
            level4_comments=level4_jd["data"][num]["message"] #第一個留言內容
            level4_comments_id = level4_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level4_comments_id)
            
            if name in level4_comments:
                if "A" in level4_comments or "a" in level4_comments:
                    score4=2
                    content = "答對囉，進入第五關，點我↓"
                    content_link = "%23Blueberry學堂_第五關"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level4_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                elif "B" in level4_comments or "b" in level4_comments or "C" in level4_comments or "c" in level4_comments:
                    score4=0
                    content = "真可惜，進入第五關，點我↓"
                    content_link = "%23Blueberry學堂_第五關"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level4_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

                else: #回答非選項
                    score4=0
                    content = "亂打，不給你分數，直接進入第五關，點我↓"
                    content_link = "%23Blueberry學堂_第五關"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level4_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

    return score4

def level_5():
    #第五關(正解:B)
    level5_id = jd["data"][-7]["id"] #第五關id
    level5_res = requests.get("https://graph.facebook.com/v13.0/"+level5_id+"/comments?access_token="+token)
    level5_jd=json.loads(level5_res.text)
    if level5_jd["data"]==[]:
        return level_5()

    else:
        for num in range(0,len(level5_jd["data"])):
            level5_comments=level5_jd["data"][num]["message"] #第一個留言內容
            level5_comments_id = level5_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level5_comments_id)
            level5_comments=level5_comments.split("+")            
            comments_id.append(level5_comments[0])
            name=level5_comments[0]
            
            if name in level5_comments:

                if "B" in level5_comments or "b" in level5_comments:  #正解!
                    score5=2
                    #回覆貼文網址:level6
                    content = "原來你有關心小孫喔~，進入最終關，點我↓"
                    content_link = "%23Blueberry學堂_Final"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level5_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                elif "A" in level5_comments or "C" in level5_comments or "a" in level5_comments or "c" in level5_comments:
                    score5=0
                    #回覆貼文網址:level6
                    content = "原來你不關心小孫 XD，進入最終關，點我↓"
                    content_link = "%23Blueberry學堂_Final"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level5_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

                else: #回答非選項
                    score5=0
                    content = "再亂打，忍你很久了，小心被當掉，進入最終關，點我↓"
                    content_link = "%23Blueberry學堂_Final"
                    level5_link = requests.post("https://graph.facebook.com/v13.0/"+level4_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

    return score5

def level_6():
    #第六關(正解:C)
    level6_id = jd["data"][-8]["id"] #第六關id
    level6_res = requests.get("https://graph.facebook.com/v13.0/"+level6_id+"/comments?access_token="+token)
    level6_jd=json.loads(level6_res.text)
    if level6_jd["data"]==[]:
        return level_6()

    else:
         for num in range(0,len(level6_jd["data"])):
            level6_comments=level6_jd["data"][num]["message"] #第一個留言內容
            level6_comments_id = level6_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level6_comments_id)
            level6_comments=level6_comments.split("+")            
            comments_id.append(level6_comments[0])
            name=level6_comments[0]
            
            if name in level6_comments:
                if "C" in level6_comments or "c" in level6_comments:
                    score6=2
                    #回覆貼文網址:level7
                    content = "上課有認真喔! 進入成績計算，點我↓"
                    content_link = "%23Blueberry學堂_是輪迴嗎"
                    level7_link = requests.post("https://graph.facebook.com/v13.0/"+level6_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                elif "A" in level6_comments or "B" in level6_comments or "a" in level6_comments or "b" in level6_comments:
                    score6=0
                    #回覆貼文網址:level7
                    content = "答錯了! 進入成績計算，點我↓"
                    content_link = "%23Blueberry學堂_是輪迴嗎"
                    level7_link = requests.post("https://graph.facebook.com/v13.0/"+level6_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)
                else:
                    score6=-1
                    content = "亂寫，給你扣1分，進入成績計算，點我↓"
                    content_link = "%23Blueberry學堂_是輪迴嗎"
                    level7_link = requests.post("https://graph.facebook.com/v13.0/"+level6_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

    return score6

def level_7(ans_total):
    #第七關(交給命運: 結業Y/N)
    level7_id = jd["data"][-9]["id"] #第七關id(結果)
    level7_res = requests.get("https://graph.facebook.com/v13.0/"+level7_id+"/comments?access_token="+token)
    level7_jd=json.loads(level7_res.text)
    
    if level7_jd["data"]==[]:
        return level_7(ans_total)

    else:
         for num in range(0,len(level7_jd["data"])):
            level7_comments=level7_jd["data"][num]["message"] #第一個留言內容
            level7_comments_id = level7_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level7_comments_id)
            level7_comments_name=level7_comments.split("+")            
            comments_id.append(level7_comments_name[0])

            if level7_comments!="百科" or level7_comments!="派森" or level7_comments!="伊瑟爾":
                #如果沒寫對角色名稱
                content = "很誇張，忘記自己的名子，請按F5再重新輸入"
                level7_char_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&access_token="+token)
                time.sleep(3)
                #刪除留言:要留所有留言的id
                requests.delete("https://graph.facebook.com/v13.0/"+level7_comments_id+"?access_token="+token)
                return level_7(ans_total)

            elif level7_comments=="百科" or level7_comments=="派森" or level7_comments=="伊瑟爾":
                score_record=pd.DataFrame(ans_total)
                total=0
                for each_score in score_record[level7_comments]:
                    total+=each_score   
                print(total)

                if total < 10:
                    #回覆貼文網址:lose
                    content = "你的總分:"+str(total)+"闖關失敗"
                    if level7_comments=="百科":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/Ph04ym0/bike-lose.jpg&access_token="+token)
                    elif level7_comments=="派森":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/CzqFsLW/python-lose.jpg&access_token="+token)
                    elif level7_comments=="伊瑟爾":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/zNw1DyF/excel-lose.jpg&access_token="+token)

                    content2 = "是否要再玩一次?"
                    ask_again = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&access_token="+token)
                    time.sleep(5)
                    restart_comments = restart_jd["data"][3]["message"] #是否要再玩一次_回復
                    restart_comments_id = restart_jd["data"][3]["id"] #是否要再玩一次_回復
                    comments_id.append(restart_comments_id)

                    if len(restart_jd["data"][3]["message"])>4:
                        active=delete_comments()

                elif total >= 10:
                    #回覆貼文網址:WIN
                    content = "你的總分:"+str(total)+"恭喜你可以畢業了🏆"
                    win_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?"+content+"&attachment_url=https://i.ibb.co/86j3wvD/win.jpg&access_token="+token)
                    content2 = "是否要再玩一次?"
                    ask_again = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&access_token="+token)
                    time.sleep(5)
                    restart_comments = restart_jd["data"][3]["message"] #是否要再玩一次_回復
                    restart_comments_id = restart_jd["data"][3]["id"] #是否要再玩一次_回復_id
                    comments_id.append(restart_comments_id)

                    if len(restart_jd["data"][3]["message"])>4:
                        active=delete_comments()
    return active
            
def delete_comments():

    if level7_comments=="百科":
        for comments in comments_id:
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[0]+"?access_token="+token)
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[-1]+"?access_token="+token)
            if comments=="百科":
                state=comments_id.index("百科")-1
                requests.delete("https://graph.facebook.com/v13.0/"+comments_id[state:state+2]+"?access_token="+token)
        active = False

    elif level7_comments=="派森":
        for comments in comments_id:
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[0]+"?access_token="+token)
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[-1]+"?access_token="+token)
            if comments=="派森":
                state=comments_id.index("派森")-1
                requests.delete("https://graph.facebook.com/v13.0/"+comments_id[state:state+2]+"?access_token="+token)
        active = False

    elif level7_comments=="伊瑟爾":
        for comments in comments_id:
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[0]+"?access_token="+token)
            requests.delete("https://graph.facebook.com/v13.0/"+comments_id[-1]+"?access_token="+token)
            if comments=="伊瑟爾":
                state=comments_id.index("伊瑟爾")-1
                requests.delete("https://graph.facebook.com/v13.0/"+comments_id[state:state+2]+"?access_token="+token)
        active = False
    return active  


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


     


# In[ ]:





# In[ ]:




