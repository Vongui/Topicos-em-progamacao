def busca_binaria(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return busca_binaria(arr, x, mid + 1, high)
    else:
        return busca_binaria(arr, x, low, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
print(busca_binaria(arr, x, 0, len(arr) - 1))