import random
import time


def eval(sorted_list, reference_list):
    if sorted_list == reference_list:
        return "두 리스트는 동일합니다."
    else:
        return "두 리스트는 동일하지 않습니다."

def read_data(path):
    with open(path, 'r') as file:
        datas = file.readlines()
        return [int(i) for i in datas]
    
# Pivot을 선택하는 함수
def choose_pivot(arr, left, right, pivot_type):
    if pivot_type == "random":
        return random.randint(left, right)
    elif pivot_type == "mid":
        return (left + right) // 2
    
# Pivot을 기준으로 리스트를 나누고 Pivot의 최종 위치를 반환하는 함수
def partition_mid(arr, left, right):
    pivot_index = choose_pivot(arr, left, right, "mid")
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    pivot = arr[left]
    low = left + 1
    high = right
    
    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    
    arr[left], arr[high] = arr[high], arr[left]
    return high

def partition(arr, left, right):
    pivot_index = choose_pivot(arr, left, right, "random")
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    pivot = arr[left]
    low = left + 1
    high = right
    
    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    
    arr[left], arr[high] = arr[high], arr[left]
    return high

# Quick Sort 알고리즘을 사용하여 리스트를 정렬
def Quick_sort_mid(arr, left, right):
    if left < right:
        pivot_index = partition_mid(arr, left, right)
        Quick_sort_mid(arr, left, pivot_index - 1)
        Quick_sort_mid(arr, pivot_index + 1, right)
    

def Quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        Quick_sort(arr, left, pivot_index - 1)
        Quick_sort(arr, pivot_index + 1, right)

if __name__ == "__main__":
  ## input file ##
    path = "C:/Users/82109/algorithm/al/inupt_quick_sort.txt"
    input = read_data(path)
    t_input = input.copy()
    f_input = input.copy()
    print("orig", input)
    t_input.sort()
    Quick_sort_mid(input, 0, len(input) - 1)
    Quick_sort(f_input, 0, len(f_input) - 1)
    

    print(f"Quick sort, 내장 sort 함수 사용 후 비교: {eval(t_input, input)}")
    print(f"Quick mids, 내장 sort 함수 사용 후 비교: {eval(t_input, f_input)}")

    print("mide", input)
    print("sort", t_input)
    print("rand", f_input)

    print('------' * 20)

    # -----시간 측정 -----------
    start = time.time_ns()
    for _ in range(1000):
        f_input = read_data(path)
        f_input.sort()
    end = time.time_ns()
    print(f"내장 Sort: {end - start} ns")

    print('------' * 20)

    start = time.time_ns()
    for _ in range(1000):
        s_input = read_data(path)
        Quick_sort_mid(s_input, 0, len(s_input) - 1)
    end = time.time_ns()
    print(f"Quick_sort_mid- 중앙값: {end - start} ns")

    print('------' * 20)

    start = time.time_ns()
    for _ in range(1000):
        t_input = read_data(path)
        Quick_sort(t_input, 0, len(t_input) - 1)
    end = time.time_ns()
    print(f"Quick Sort-random: {end - start} ns")

    print('------' * 20)
