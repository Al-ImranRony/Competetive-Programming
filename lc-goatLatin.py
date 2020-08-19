# LeetCode Aug challenge 19

def toGoatLatin(S: str) -> str:
    count = 0
    res = []
    for word in S.split():
        count+=1
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            res.append(word+"ma"+'a'*count)
        else:
            res.append(word[1:]+word[0]+"ma"+'a'*count)
    return " ".join(res)

print(toGoatLatin("I speak Goat Latin"))