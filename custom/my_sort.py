"""各种排序算法实现"""


def findSmallest(arr):
    """
    返回数组最小值的所在的index
    :param arr:
    :return:
    """
    smallest = arr[0]
    smallest_index = 0
    for key, value in enumerate(arr):
        if value < smallest:
            smallest = value
            smallest_index = key
    return smallest_index


def select_sort(arr):
    """
    非原地排序，新增了一个数组，排序完成后原数组为空了
    :param arr:
    :return:
    """
    newArr = []
    for _ in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))  # 这里pop操作是原地修改的
    return newArr


def quick_sort(arr):
    """
    快排，原地排序
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def bubble_sort(arr):
    """
    冒泡排序 原地排序
    :param arr:
    :return:
    """
    count = len(arr)
    if count < 1:
        return arr

    for i in range(0, count):
        for j in range(i + 1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insert_sort(arr):
    """
    未完待续
    :param arr:
    :return:
    """
    # 插入排序
    count = len(arr)
    if count <= 1:
        return arr

    for i in range(1, count):
        key = arr[i]
        for j in range(i - 1, 0, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j] = key
    return arr


if __name__ == '__main__':
    # arr = [5, 3, 6, 2, 10]
    # print(select_sort(arr))
    # arr1 = [5, 3, 6, 2, 10]
    # print(quick_sort(arr1))
    # arr2 = [5, 3, 6, 2, 10]
    arr3 = [5, 3, 6, 2, 10]
    print(insert_sort(arr3))
