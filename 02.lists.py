


student_marks = []
while True:
        mark = input ('введите оценку студента:')
        if mark:                           # '' == False, () == False, [] == False
            student_marks.append(mark)
        else:
            break

print('ввод завершен')
print(student_marks)