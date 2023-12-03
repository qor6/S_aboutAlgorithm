def read_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return [int(i) for i in lines]

def create_heap_array(path):
    A = [None]
    A.extend(read_data(path))
    return A

def down_heap(arr, heap_size, i):
    # 왼쪽 자식 노드와 오른쪽 자식 노드 계산
    left_child = 2 * i
    right_child = 2 * i + 1
    bigger = i

    # 왼쪽 자식이 힙 크기 내에 있고 현재 값보다 큰 경우
    if left_child <= heap_size and arr[left_child] > arr[i]:
        bigger = left_child

    # 오른쪽 자식이 힙 크기 내에 있고 현재 값보다 큰 경우
    if right_child <= heap_size and arr[right_child] > arr[bigger]:
        bigger = right_child

    # 더 큰 자식이 존재하는 경우 교환하고 재귀적으로 호출
    if bigger != i:
        arr[i], arr[bigger] = arr[bigger], arr[i]
        down_heap(arr, heap_size, bigger)
        # print(f"Step {heap_size}: {arr[1:]}")


def build_heap(arr):
    heap_size = len(arr) - 1
    for i in range(heap_size // 2, 0, -1):
        down_heap(arr, heap_size, i)

def heap_sort(arr):
    build_heap(arr)
    heap_size = len(arr) - 1

    for i in range(heap_size, 0, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heap_size -= 1
        down_heap(arr, heap_size, 1)
        # print(f"Step {heap_size}: {arr[1:]}")

if __name__ == "__main__":
    path = "C:/Users/82109/graphics/al/input.txt"
    A = create_heap_array(path)
    B = A.copy()

    print(f"origt: ", A[1:])
    heap_sort(A)
    
    print(f"heap_sort: ", A[1:])
    sorted_array = A[1:]
    output_path = "C:/Users/82109/graphics/al/output.txt"
    with open(output_path, 'w') as output_file:
        output_file.write("\n".join(map(str, sorted_array)))