#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def game_start(comments_id):
    # 遊戲開始貼文底下的回覆
    start_id=jd["data"][-1]["id"]  #遊戲開始貼文id
    start_res = requests.get("https://graph.facebook.com/v13.0/"+"116833604352865_116842771018615"+"/comments?access_token="+token)
    start_jd=json.loads(start_res.text)
    time.sleep(2)
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
            
     

