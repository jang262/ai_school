# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

with open('./swit_chat.json', 'r', encoding='UTF8') as jsonfile:
    swit_chat_data = json.load(jsonfile)
    # print(swit_chat_data)
    temp_dict = {}
    for i in swit_chat_data['data']:
        if i['content'] != None:
            if i['user_name'] not in temp_dict.keys():
                temp_dict[i['user_name']] = 1
            else:
                temp_dict[i['user_name']] += 1
    # print("temp_dict : ", temp_dict)
    # print("temp_dict.items() : ", temp_dict.items())
    max_num = max(temp_dict.values())
    print("max_num: ", max_num)
    max_list = []
    for i in temp_dict.keys():
        # print(i, temp_dict[i])
        if max_num == temp_dict[i]:
            a = [i, temp_dict[i]]
            max_list.append(a)
    print(max_list)
# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기
