



def reverseWords(s):
    ln = len(s)
    res, temp = "", ""

    for i in range(ln-1, -1, -1):
        temp += s[i]
        if (i == 0):
            res = temp + " " + res
        elif (s[i] == " "):
            res = temp + res
            temp = ""

    los = len(res)
    print("'" + res + "'")
    res = res[:los-1]
    res = "'" + res + "'"
    return res

print(reverseWords("c"))