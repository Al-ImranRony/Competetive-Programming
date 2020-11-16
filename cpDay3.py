# Day 3 of 100daysCodingChallenge
# Day 1 of daily coding challenge

arr, k = [10, 15, 3, 7], 17
for i in range(len(arr)):
    if (k - arr[i]) in arr:
        print("True")
        break
print("False")