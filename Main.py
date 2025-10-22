def binary(arr, low, high, key):
    mid = (low+high)//2
    if low <= high:
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binary(arr, mid+1, high, key)
        elif arr[mid]>key:
            return binary(arr, low, mid-1, key)
    else:
      return -1
key = int(input("Enter number you are searching for:"))
high = 4
low = 0
arr=[1, 2, 3, 4, 5]
print(binary(arr, low, high, key))
