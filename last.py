#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def level_7(ans_total):
    #第七關(交給命運: 結業Y/N)
    level7_id = jd["data"][-9]["id"] #第七關id(結果)
    level7_res = requests.get("https://graph.facebook.com/v13.0/"+level7_id+"/comments?access_token="+token)
    level7_jd=json.loads(level7_res.text)
    time.sleep(3)
    
    if level7_jd["data"]==[]:
        return level_7(ans_total)

    else:
         for num in range(player_num):
            level7_comments=level7_jd["data"][num]["message"] #第一個留言內容
            level7_comments_id = level7_jd["data"][num]["id"] #第一個留言id
            comments_id.append(level7_comments_id)        
            comments_id.append(level7_comments)

            if level7_comments!="百科" and level7_comments!="派森" and level7_comments!="伊瑟爾":
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
                    content = "你的總分:"+str(total)+"，闖關失敗"
                    if level7_comments=="百科":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/Ph04ym0/bike-lose.jpg&access_token="+token)
                    elif level7_comments=="派森":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/CzqFsLW/python-lose.jpg&access_token="+token)
                    elif level7_comments=="伊瑟爾":
                        lose_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&attachment_url=https://i.ibb.co/zNw1DyF/excel-lose.jpg&access_token="+token)

                    content2 = "是否要再玩一次?"
                    ask_again = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&access_token="+token)
                    time.sleep(15)
                    if restart_comments=="要" or restart_comments=="好" or restart_comments=="yes" or restart_comments=="Yes":
                        content = "重新開始，點我"
                        content_link = "%23Blueberry學堂_結業式"
                        restart_comments= requests.post("https://graph.facebook.com/v13.0/"+level6_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)


                elif total >= 10:
                    #回覆貼文網址:WIN
                    content = "你的總分:"+str(total)+"，恭喜你可以畢業了🏆"
                    win_link = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?"+content+"&attachment_url=https://i.ibb.co/86j3wvD/win.jpg&access_token="+token)
                    content2 = "是否要再玩一次?"
                    ask_again = requests.post("https://graph.facebook.com/v13.0/"+level7_comments_id+"/comments?message="+content+"&access_token="+token)
                    time.sleep(15)
                    
                    restart_comments = level7_jd["data"][num]["message"] #是否要再玩一次_回復
                    restart_comments_id = level7_jd["data"][num]["id"] #是否要再玩一次_回復_id
                    comments_id.append(restart_comments_id)
                    if restart_comments=="要" or restart_comments=="好" or restart_comments=="yes" or restart_comments=="Yes":
                        content = "重新開始，點我"
                        content_link = "%23Blueberry學堂_結業式"
                        restart_comments= requests.post("https://graph.facebook.com/v13.0/"+level6_comments_id+"/comments?message="+content+"%0A"+" "+content_link+"&access_token="+token)

            if len(restart_jd["data"][3]["message"])>4:
                active=delete_comments()
                
    return active
            
def delete_comments():

    for comments in comments_id:
        requests.delete("https://graph.facebook.com/v13.0/"+comments+"?access_token="+token)
    active = False

    return active  

