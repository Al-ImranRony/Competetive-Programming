# Codechef easy practice

for i in range(int(input())):
    n = int(input())
    carSpeeds = list(map(int, input().split()))
    speedestCars = 1
    maxFront = carSpeeds[0] 
    for i in range(1, n):
        if (carSpeeds[i] < maxFront):
            speedestCars += 1
            maxFront = min(carSpeeds[i], maxFront)
    
    print(speedestCars)


