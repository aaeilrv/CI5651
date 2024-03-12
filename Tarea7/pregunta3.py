def computeLPS(pattern):
    lps = [0] * len(pattern)
    i = 1
    j = 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
    
    return pattern[:lps[-1]]

print(computeLPS("abracadabra"))
print(computeLPS("aaaaa"))