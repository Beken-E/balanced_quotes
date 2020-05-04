def harmony(s):
    count = -1
    obychniy = 0
    kvadrat = 0
    figutniy = 0
    for i in s:
        count += 1
        if i in [")"] and s[count - 1] in ["[", "{"]:
            obychniy += 100
        elif i in ["]"] and s[count - 1] in ["(", "{"]:
            kvadrat += 100
        elif i in ["}"] and s[count - 1] in ["(", "["]:
            figutniy += 100
        elif i == "(":
            obychniy += 1
        elif i == ")":
            obychniy -= 1
        elif i == "[":
            kvadrat += 1
        elif i == "]":
            kvadrat -= 1
        elif i == "{":
            figutniy += 1
        else:
            figutniy -= 1

    if obychniy + kvadrat + figutniy == 0:
        return "YES"
    else:
        return "NO"    

print(harmony("[][]{}{}{}(((([]))))[[{}]][]()"))