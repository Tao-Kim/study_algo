# https://wikidocs.net/13
# https://rfriend.tistory.com/tag/title%28%29
# 전체적으로 정리가 잘되있어서 링크를 첨부함
# 위 사이트에 없는 조작법 추가 작성중

"""
문자열 문자 단위로 바꾸기

반환 : string
문법 : 문자열.translate(str.maketrans(바꿀문자들, 새문자둘)
"""
translator = str.maketrans("abc", "123")
s = "Apple and Banana"
s = s.translate(translator)
print(s) # "Apple 1nd B1n1n1" = 대소문자 구별



"""
문자열 양쪽의 특정 문자 제거

반환 : string
문법 : strip(문자들), lstrip(문자들), rstrip(문자들) 
"""
s = ".,apple."

s1 = s.strip('.')
print(s1) # ,apple

s2 = s.lstrip('.')
print(s2) # ,apple.

s3 = s.rstrip('.')
print(s3) # .,apple

s4 = s.strip('.,')
print(s4) # apple