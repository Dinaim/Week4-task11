# 3) Попросить пользователя ввести слова через пробел. Отсортировать слова по
# количеству символов и вывести на экран результат.


text = input('Please write your text: ')
l = text.split()
q=""
for i in sorted(l,key=lambda x: len(x)):
    q = q + " " + i
print(q)



