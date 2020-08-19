# LeetCode Aug challenge 18

def sameConsecutiveDiffsNum(N, K):
    result = {}

    def dfs(digits, num):
        if len(digits) == N:
            result[digits] = 1
            return

        if num-K >= 0:
            dfs(digits+str(num-K), num-K)

        if num+K < 10:
            dfs(digits+str(num+K), num-K)      

    for i in range(10):
        if i==0 and N != 1:
            continue
        dfs(str(i), i)

    return [int(x) for x in result.keys()]

print(sameConsecutiveDiffsNum(3, 7))