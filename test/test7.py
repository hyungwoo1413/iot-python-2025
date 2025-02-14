myList = [5,4,3,2,1]

def my_selectSort(lst = list):
    # 여기에 구현
    # 주어진 배열 중에서 최솟값을 찾는다.
    # 그 값을 맨 앞에 위치한 값과 교체한다(패스(pass)).
    # 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.
    # 하나의 원소만 남을 때까지 위의 1~3 과정을 반복한다.

    a = 0
    
    for i in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                a = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = a
            i += 1
    return lst


print(my_selectSort(myList))

# result = [1,2,3,4,5]