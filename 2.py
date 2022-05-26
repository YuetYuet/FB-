#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def level_char():  #選擇角色
    level_char_id = jd["data"][-2]["id"]
    char_res = requests.get("https://graph.facebook.com/v13.0/"+level_char_id+"/comments?access_token="+token)
    char_jd=json.loads(char_res.text)
    time.sleep(2)
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



     

