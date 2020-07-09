# TODO_0 : csv 모듈 불러오기
import csv
import json
from collections import OrderedDict
import os

csv_save_file = 'students_csv.csv'
json_save_file = "students_json.json"
# students_data = [["id", "pw", "name", "dream", "interesting", "age", "jab", "number"],
#                  ["j1", "j26!@", "장이욱", "무사히 수료하자", "bigdata", 38, "전직 군인", 1],
#                  ["j2", "j26!@", "장이욱", "무사히 수료하자", "bigdata", 38, "전직 군인", 2],
#                  ["j3", "j26!@", "장이욱", "무사히 수료하자", "bigdata", 38, "전직 군인", 3]]
# with open (csv_save_file, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     for i in students_data[:]:
#         writer.writerow(i)

def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기
# csv파일인 경우 로그인
# def signin(id, pw):
#     result = 0
#     with open (csv_save_file, 'r', newline='', encoding='utf-8') as csvfile:
#         rdr = csv.reader(csvfile)
#         next(rdr)
#         for line in rdr:
#             print(line)
#             if id == line[0]:
#                 if pw == line[1]:
#                     print("로그인 성공")
#                     result = 1
#                     return result
#                 else:
#                     print("비밀번호가 틀렸습니다.")
#                     break
#             else:
#                 print("signin 없는 id")
#     return result

# json 파일인 경우 로그인
def signin(id, pw):
    result = 0
    with open (json_save_file, 'r', newline='', encoding='utf-8') as csvfile:
        json_data = json.load(csvfile)
        print(json_data)
        for data in json_data:
            print(data)
            if id == data['id']:
                print("id 존재")
                print(id, data)
                if pw == data['pw']:
                    print("로그인 성공")
                    result = 1
                    return result
                else:
                    print("비밀번호가 틀렸습니다.")
                    break
            else:
                print("없는 id")
    return result

# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기
def id_Validation(id):
    result = False
    with open (csv_save_file, 'r', newline='', encoding='utf-8') as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)
        for line in rdr:
            if id == line[0]:
                result = id
                # print("id 존재")
    return result

# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# def signup(id, pw):
#     students_csv_data = []
#     students_csv_data.append(id)
#     students_csv_data.append(pw)
#     with open(csv_save_file, 'a', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(students_csv_data)

# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)
def signup(dict_user):
    file_name = "students_json.json"
    if os.path.isfile(file_name):
        # file exists
        with open (file_name, 'a+') as outfile:
            outfile.seek(outfile.tell() - 1, os.SEEK_SET)
            # outfile.seek(-1, os.SEEK_END)
            outfile.truncate()
            outfile.write(',')
            json.dump(dict_user, outfile)
            outfile.write(']')
    else:
        # create file
        with open(file_name, 'w') as outfile:
            array = []
            array.append(dict_user)
            json.dump(array,outfile)

def userlist():
    print("현재 존재하는 유저 :")
    # TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
    # json파일인 경우
    with open(json_save_file, "r", encoding="utf=8") as file:
        json_data = json.load(file)
        print(json_data)

    # csv파일인 경우
    # with open (csv_save_file, 'r', newline='', encoding='utf-8') as csvfile:
    #     rdr = csv.reader(csvfile)
    #     next(rdr)
    #     for line in rdr:
    #         print(line)
    #         print(f"id : {line[0]}, pw : {line[1]}")

def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()

def start():
    log_on = 0
    print('csv 로 데이터 다루기 로그인 예제')
    signup_or_login = input('1 - 로그인 / 2 - 회원가입 : \n')

    if signup_or_login == "1":
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        log_on = signin(id, pw)
    elif signup_or_login == "2":
        # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
        id, pw = user_input()
        # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
        if id_Validation(id) == True:
            print("사용할 수 없는 id입니다.")
            exitcheck()
        else:
            # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현
            dict_user = {
                "id": id,
                "pw": pw
            }
            # signup(id, pw)
            signup(dict_user)
            userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()

start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
