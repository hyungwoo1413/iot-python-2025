# 함수, Function, Method, Procedure...
# 인자, 파라미터, 매개변수, Parameter, Argument...
# def 함수명(인자1, 파라미터2, 매개변수3):
#   함수안으로 진입

def say_hi():
    print('안녕~ ')

def say_hello(name):
    print(f'{name}, 안녕!!')

def get_age(birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '바이바이~'


print('인사하기:', end=' ')
say_hi() # 함수 호출

name = input('이름입력> ')
print('이름으로 인사하기:', end=' ')
say_hello(name)

year = int(input('생일년도> '))
real_age = get_age(year)
print(f'나이는: {real_age}세')

print('작별인사: ', closing())