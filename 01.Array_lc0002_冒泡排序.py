

class bubble_sort:
    def __init__(self, arr:list):
        self.arr_1 = arr
    def sort():
        length = len(self.arr_1)
        return self.arr_1


def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swappedFlag = False
        for j in range(0, n-i-1):  # 0 到 n-i 还需要 -1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swappedFlag = True
        if not swappedFlag:
            break
    return arr

if __name__ == "__main__":
    arr = [3, 2, 4, 6, 1, 3]
    print(bubble_sort(arr))

