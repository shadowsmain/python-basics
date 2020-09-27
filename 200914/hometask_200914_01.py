student_marks = []
while True:
    mark = input('Введите оценку студента:\n')
    if mark:
        student_marks.append(int(mark))
        if int(mark) > 5:
            print('неверно введена оценка')
            student_marks.remove(int(mark))
        elif int(mark) <= 1:
            print('неверно введена оценка')
            student_marks.remove(int(mark))
    else:
        break
        print('ввод завершен')

avg_mark = 0
for marks in student_marks:
    avg_mark += marks
avg_mark /= len(student_marks)
if not student_marks:
    print('')
else:
    print('marks:', student_marks)
    print('Средний балл:', avg_mark)