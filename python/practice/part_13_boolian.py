if []:
    print("[] is True.")
if [1,2,3]:
    print("[1,2,3] is True.")
if {}:
    print("{} is True.")
if {'abc' : 1}:
    print("{'abc' : 1} is True.")
if 0:
    print("0 is True.")
if 1:
    print("1 is True.")

"""
            False            True
number        0              0을 제외한 모든 수
문자열      빈문자열          빈문자열을 제외한 모든 문자열
리스트      빈리스트          빈리스트를 제외한 모든 리스트
딕셔너리    빈딕셔너리        빈딕셔너리를 제외한 모든 빈딕셔너리
기타        none 오브젝트

"""
#
a = 1 or 10
b = 0 or 10

print("a:{}, b:{}".format(a,b))
# or 연산 결과는 앞의 값이 true이면 앞의값, 앞의 값이 false이면 뒤의값을 따름
