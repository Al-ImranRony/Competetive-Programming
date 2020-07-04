import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
for i in range(n):    
    for j in range(n-1):
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
    if numSwaps == 0:
        break

print("Array is sorted in", numSwaps, "swaps.")
print("First Element: ", a[0])
print("Last Element: ", a[-1])


