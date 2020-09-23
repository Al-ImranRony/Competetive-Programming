# LeetCode Sept challenge 23


def canCompleteCircuit(gas, cost) -> int:
        if sum(gas) < sum(cost): return -1
        
        startIdx = tankGas = 0
        for i in range(len(gas)):
            tankGas += gas[i] - cost[i]
            if tankGas < 0:
                startIdx, tankGas = i+1, 0
        return startIdx

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(canCompleteCircuit([2,3,4], [3,4,3])) 