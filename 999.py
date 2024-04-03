# s = 'prive+++**********t'
# plus = '+'
# umn = '*'
# count = 0
# count_=0
# for i in range(len(s)):
#    if s[i] in plus:
#        count +=1
#    if s[i] in umn:
#        count_ +=1
#
# print(f'Символ + встречается {count} раз')
# # if s[i] in umn:
# #    count +=1
# print(f'Символ * встречается {count_} раз')

# s = 'aaabbbbcddd' #7
# count = 0
# las = ''
#
# for i in range(len(s)-1):
#    if s[i] == s[i+1]:
#        count +=1
# print(count)


# put your python code here
# s = 'Вдохновение-это умение приводить себя в рабочее состояние'
# count_glas = 0
# count_soglas = 0
#
#
# glas = ('ауоыиэяюёеАУОЫИЭЯЮЁЕ')
# soglas = ('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
#
# for i in range(len(s)):
#     if s[i] in glas:
#         count_glas += 1
#     if s[i] in soglas:
#         count_soglas += 1
#
# print(f"Количество гласных букв равно {count_glas}")
# print(f"Количество согласных букв равно {count_soglas}")

# i = 375
#
# while i !=0:
#     n = i%2
# print(n)

fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))