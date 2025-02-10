# 메인에서 제일 처음 실행되는 함수
import os
from Movie import Movie

VERSION = 0.5

def clearScrean(): # os에 특화된 팁
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    
    os.system(command)

def run():
    # movie = Movie('어벤저스: 인피니티 워',2018,'디즈니',8.6)
    # print(movie)
    # set_movie()
    clearScrean()
    lst_movie = [] # 영화리스트를 담는 변수 list타입
    load_movie(lst_movie)

    while True:
        sel_menu = set_menu()
        if sel_menu == 1:
            print('')
            # print('영화 입력')
            try: 
                movie = set_movie()
                lst_movie.append(movie)
                print('영화 입력 성공')
            except Exception as e:
                print(f'영화 입력 실패 {e}')
        elif sel_menu == 2:
            print('')
            print('영화 출력\n')
            get_movie(lst_movie)
            print('')
        elif sel_menu == 3:
            print('영화 검색\n')
            title = input('검색할 영화명 입력 > ')
            search_movie(lst_movie, title)
        elif sel_menu == 4:
            print('영화 삭제\n')
            title = input('삭제할 영화명 입력 > ')
            del_movie(lst_movie, title)
        elif sel_menu == 5:
            # print('앱 종료')
            # 종료직전 DB생성하고 완료
            save_movie(lst_movie)
            break
        else:
            pass # 아무것도 하지 않음

        input() # 입력대기: 엔터치면 넘어감
        clearScrean() # 메뉴 기능이 완료되면 화면 클리어

# 영화검색 함수
def search_movie(items: list, title: str):
    count = 0
    for item in items: # item이 Movie 클래스인지 알 수 없음
        if item.isNameContain(title):
            count += 1
            print(item)
            print('------------------------------')
    print(f'검색 데이터 수: {count}개')




def del_movie(items: list, title: str):
    for i, item in enumerate(items):
        if item.isNameExist(title):
            del items[i] # 인덱스로 리스트에 요소하나를 삭제

# 폴더에 파일로 영화리스트 저장
def save_movie(items: list):
    f = open('movie_db.txt', mode='w', encoding='utf-8') # 파일쓰기로 오픈
    for item in items:
        f.write(f'{item.getTitle()}|')
        f.write(f'{item.getYear()}|')
        f.write(f'{item.getCompany()}|')
        f.write(f'{item.getRate()}\n')

    f.close()

def load_movie(items: list):
    f = open('movie_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline().replace('\n','')
        if not line: break # 무한루프 빠져나가는 조건

        lines = line.split('|') # 구분자로 잘라서 4개 요소의 리스트 생성
        title = lines[0]
        year = int(lines[1])
        company = lines[2]
        rate = float(lines[3])

        movie = Movie(title, year, company, rate)
        items.append(movie)

    f.close()

def set_movie():
    title, year, company, rate = input('영화입력[제목|개봉년|제작사|평점 순] > ').split('|') # 입력 중 발생하는 예외
    year = int(year) # 년도는 정수로
    rate = float(rate) # 평점은 실수로
    # print(title, year, company, rate)
    movie = Movie(title=title,year=year,company=company,rate=rate) # 데이터형 예외
    return movie

# lst변수는 list타입이라고 지정
def get_movie(items: list):
    for item in items:
        print(item) # Movie 객체
        print('------------------------------')
    print(f'총 데이터 수: {len(items)}개')

def set_menu():
    str_menu = (f'내 영화 앱 v{VERSION}\n\n'
                '1. 영화 입력\n'
                '2. 영화 출력\n'
                '3. 영화 검색\n'
                '4. 영화 삭제\n'
                '5. 앱 종료\n')
    print(str_menu)
    try:
        sel_menu = int(input('메뉴 번호입력: ')) # 예외있음
    except Exception as e:
        sel_menu = 0
    return sel_menu

if __name__ == '__main__':
    # print('내 영화 앱 시작')
    run()

print('프로그램 종료')

