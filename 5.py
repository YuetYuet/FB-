#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def level_4():
    #第四關(正解:A)
    level4_id = jd["data"][-6]["id"] #第四關id
    level4_res = requests.get("https://graph.facebook.com/v13.0/"+level4_id+"/comments?access_token="+token)
    level4_jd=json.loads(level4_res.text)
    time.sleep(3)
    if level4_jd["data"]==[]:
        return level_4()
    else:
        for num in range(player_num):
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
    time.sleep(2)
    if level5_jd["data"]==[]:
        return level_5()

    else:
        for num in range(player_num):
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
    time.sleep(2)
    
    if level6_jd["data"]==[]:
        return level_6()

    else:
         for num in range(player_num):
            level6_comments=level6_jd["data"][num]["message"] #第一個留言內容
            level6_comments_id = level6_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level6_comments_id)
            level6_comments=level6_comments.split("+")            
            comments_id.append(level6_comments[0])
            
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

