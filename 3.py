#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def level_1():
     #第一關:(正解:5個)
    level1_id = jd["data"][-3]["id"]
    level1_res = requests.get("https://graph.facebook.com/v13.0/"+level1_id+"/comments?access_token="+token)
    level1_jd=json.loads(level1_res.text)
    time.sleep(2)
    
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
    time.sleep(2)
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


     

