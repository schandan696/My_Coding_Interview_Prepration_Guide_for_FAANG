def fractionToDecimal(numr, denr):
    mp = {}
    neg = False
    if numr * denr < 0:
        neg = True
    numr = abs(numr)
    denr = abs(denr)
    rem = numr%denr
    res = str(numr//denr)+"."
    while rem != 0 and rem not in mp:
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // denr
        res += str(res_part)
        rem = rem % denr
    # print(res)
    if (rem != 0):
        repeted = res[mp[rem]:]
        res = res.replace(repeted, "")
        res +=  "(" + repeted + ")"
        return res
    if res[-1] == ".":
        return res.replace(".", "")
    if neg:
        return "-"+res
    return res

numr, denr = -1, -2147483648
res = fractionToDecimal(numr, denr)
print(res)