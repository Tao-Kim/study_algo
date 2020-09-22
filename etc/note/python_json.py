import json

dic = {
    "1.FirstName": "Gildong",
    "2.LastName": "Hong",
    "3.Age": 20,
    "4.University": "Yonsei University",
    "5.Courses": [
        {
            "Major": "Statistics",
            "Classes": ["Probability",
                        "Generalized Linear Model",
                        "Categorical Data Analysis"]
        },
        {
            "Minor": "ComputerScience",
            "Classes": ["Data Structure",
                        "Programming",
                        "Algorithms"]
        }
    ]
}
dic_json_1 = json.dumps(dic)
print(dic_json_1) # {"1.FirstName": "Gildo .....
print(type(json.loads(dic_json_1)), json.loads(dic_json_1)) # dict


dic_json_2 = json.dumps(dic, indent=4)
print(dic_json_2)
print(json.loads(dic_json_2))
# {
#    "1.FirstName": "Gildong",
#    "2.LastName": "Hong",

# 파일로 처리 dumps -> dump, loads -> load