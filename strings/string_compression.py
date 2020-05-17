def compress_string(s):
    out = ""
    sum = 1

    for i in range(len(s)) - 1:
        if s[i] == s[i + 1]:
            sum += 1
        else:
            out += s[i] + str(sum)
            sum = 1
    if out[-1] ==s[-1]:
        out+=s[-1]
    else:
        out+=s[-1]+str(1)

    return out
