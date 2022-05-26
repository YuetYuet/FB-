#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def level_3():
    #第三關(正解:ans_count==3)
    level3_id = jd["data"][-5]["id"] #第三關id
    level3_res = requests.get("https://graph.facebook.com/v13.0/"+level3_id+"/comments?access_token="+token)
    level3_jd=json.loads(level3_res.text)
    time.sleep(2)
    if level3_jd["data"]==[]: #確認有無留言
        return level_3() #沒有的話繼續執行確認
    
    else:
        for num in range(0,len(level3_jd["data"])):
            level3_comments=level3_jd["data"][num]["message"] #第一個留言內容
            level3_comments_id = level3_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level3_comments_id)
            score3=0
            #正確答案
            correct=["pandas","numpy","datetime","time","BeautifulSoup","selenium","pymongo",
                    "pymysql","cv2","tkinter","random","requests","bs4"]
            
            if name in level3_comments:
                level3_comments=level3_comments.split("+")  #回答留言是字串，先用"+"切割後判斷是否正確
                comments_id.append(level3_comments[0])
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

     

