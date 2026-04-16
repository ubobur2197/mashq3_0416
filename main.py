# 1
bolinadimi = lambda a, b: a % b == 0
print(bolinadimi(20, 4))


# 2
doira_yuza = lambda r: 3.14 * r * r
print(doira_yuza(7))


# 3
kvadrat_ayirma = lambda a, b: (a - b) ** 2
print(kvadrat_ayirma(8, 3))


# 4
kabisa = lambda yil: (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
print(kabisa(2024))


# 5
uchburchak = lambda a, b, c: "teng tomonli" if a == b == c else ("teng yonli" if a == b or b == c or a == c else "oddiy")
print(uchburchak(3, 3, 5))
