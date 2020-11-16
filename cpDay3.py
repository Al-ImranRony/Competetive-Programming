# Day 3 of 100daysCodingChallenge
# Day 1 of daily coding challenge


def k_pair(arr, k):
    for i in range(len(arr)):
        if (k - arr[i]) in arr:
            return True
    return False


if __name__ == "__main__":
    arr = list(map(int, input("Enter an array: ").split()))
    k = int(input("Enter k: "))
    ans = k_pair(arr, k)
    print(ans)