arr = [2, 4, 6, 8, 10, 12, 14]
target = 14
length=len(arr)-1
half=len(arr)//2

while half>=0 and half<=length:
    print("length of half",half)
    if arr[half]==target:
        print(f"{target} found at index {half}")
        break
    if arr[half]>target :
        print("target is going to find left",arr[half])
        while half>=0 :
            if arr[half]==target:
                print(f"{target} found at index {half}")
                break
            half=half-1
        else:
            print("target not in the list")
            break
    if arr[half]<target :
        print("target is going to find right",arr[half])
        while half<=length :
            if arr[half]==target:
                print(f"{target} found at index {half}")
                break
            half=half+1
        else: 
            print("target not in the list")
            break