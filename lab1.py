sport = 'boxing'
print(sport)

is_student = False
is_teacher = True

if is_student:
    print("Студент")
elif is_teacher:
    print("Вчитель")

is_hot = False
is_cold = True

Hot_Cold = is_hot or is_cold
print(Hot_Cold)

import math

x = 15.241
y = 7.118

math_task_1 = 3 * math.sqrt(x + pow(y,3)) / math.pow(y, 1/3)
math_task_2 = 3 / (4 * x) * math.cos(y)

result = math_task_1 + math_task_2

print(result)