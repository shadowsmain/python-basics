


# student_marks = []
# while True:
#        mark = input('введите оценку студента:\n')
#        if mark:                           # '' == False, () == False, [] == False
#            student_marks.append(int(mark))
#        else:
#          break
#
# print('ввод завершен')
# print(student_marks)



#mock_student_marks = ['5', '4', '3', '2']
mock_student_marks = [5, 4, 3, 2]
student_marks = mock_student_marks

i = 0
avg_mark = 0
while i < len(student_marks):
   # print(type(avg_mark), type(student_marks[i]))
    avg_mark += int(student_marks[i])
    i += 1
avg_mark /= len(student_marks)
print('средний балл', avg_mark)