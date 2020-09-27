# LeetCode Sept challenge 26


def findPoisonedDuration(timeSeries, duration: int) -> int:
    prev, totalTime = timeSeries[0], duration

    for i in range(1, len(timeSeries)):
        if (prev + duration) >= timeSeries[i]:
            totalTime += timeSeries[i]-prev
        else: 
            totalTime += duration
        prev = timeSeries[i]

    return totalTime


print(findPoisonedDuration([1,3,6], 4))
print(findPoisonedDuration([1,2], 2))
print(findPoisonedDuration([1,4], 2))