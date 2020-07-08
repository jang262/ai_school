# 1. 어제 안되신 분들은 json -> students 로 만들어보고 읽기 / 쓰기
#     - 이름, 나이, 직업, 아이디, 비밀번호
# 2. 관련 데이터 별로 출력해보기! (각각을 하나의 함수로!)
#     - 학생 이름 전부 출력해보기
#     - 20살 미만 학생 open의 쓰기모드를 활용하여 넣어보기
#     - 성인이 아닌 학생 출력하기 (20세 미만..)
#     - 조건문으로 아이디를 안넣으면 쓰기 안되게 막아보기
#     - 모든 로직은 open 을 최대한 활용하기 !

import json
from collections import OrderedDict
import os

def students_name_print(x):
    print("\n 학생 이름 전부 출력해보기")
    with open(x, "r", encoding="utf=8") as file:
        json_data = json.load(file)
    for i in json_data.keys():
        for j in json_data[i].keys():
            print(f"이름 : {json_data[i][j]['name']}, 나이 : {str(json_data[i][j]['age'])} 살")

def youth_save(create_file_name, file_data):
    print("\n 20살 미만 학생 open의 쓰기모드를 활용하여 넣어보기")
    dump_data = {}
    with open(file_data, "r", encoding="utf=8") as file:
        json_data = json.load(file)
    for i in json_data.keys():
        for j in json_data[i].keys():
            if json_data[i][j]['age'] < 20:
                dump_data[j] = json_data[i][j]
    if os.path.isfile(create_file_name):
        print("같은 파일명이 존재하여 파일을 생성할 수 없습니다.")
    else:
        with open(create_file_name, "w", encoding="utf=8") as make_file:
            json.dump(dump_data, make_file, ensure_ascii=False, indent="\t")
            print(f"{create_file_name}파일이 생성되었습니다.")
        with open(create_file_name, "r", encoding="utf=8") as file:
            json_data = json.load(file)
            print(json_data)

def youth_print(x):
    print("\n 성인이 아닌 학생 출력하기 (20세 미만..)")
    with open(x, "r", encoding="utf=8") as file:
        json_data = json.load(file)
    for i in json_data.keys():
        for j in json_data[i].keys():
            if json_data[i][j]['age'] < 20:
                print(f"이름 : {json_data[i][j]['name']}, 나이 : {str(json_data[i][j]['age'])} 살")

def id_validation(): # 그런데 처음부터 데이터 구조를 id를 키값으로 만들어서 키가 없으면 들어가지지 않을꺼 같습니다.
    print("조건문으로 아이디를 안넣으면 쓰기 안되게 막아보기")
    result = 1
    for i in file_data.keys():
        for j in file_data[i].keys():
            if len == 0:
                result = 0
                print("id가 존재하지 않습니다.")
    return result


file_data = OrderedDict()

# 기본 회원정보 딕셔너리
Students_id = {'j262':
            {"pw" : 'j26!@',
             "name" : '장이욱',
             "dream" : '무사히 수료하자',
             "interesting" : 'bigdata',
             "age" : 38,
             "jab" : "전직 군인",
             "number" : 1
             },
            'jjj':
            {"pw" : 'j26!@',
             "name" : '장이욱1',
             "dream" : '무사히 수료하자',
             "interesting" : 'bigdata',
             "age" : 18,
             "jab" : "전직 군인",
             "number" : 2
             },
            'csy':
            {"pw" : '3326',
            "name" : '장이욱2',
            "dream" : '화이팅화이팅',
            "interesting" : '오늘 아침 메뉴',
            "age" : 30,
            "jab" : "전직 군인",
            "number" : 3
            }
          }
file_data["Students_id"] = Students_id

if os.path.isfile("students_id.json"):
    print("같은 파일명이 존재하여 파일을 생성할 수 없습니다.")
else:
    with open("students_id.json", "w", encoding="utf=8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

file_name = "students_id.json"
students_name_print(file_name)
youth_print(file_name)
youth_save("youth_students_id.json", file_name)
