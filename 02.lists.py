


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

#i = 0
avg_mark = 0
for item in student_marks:
    avg_mark += item

#while i < len(student_marks):
   # print(type(avg_mark), type(student_marks[i]))
    #avg_mark += int(student_marks[i])
    #i += 1
for mark in enumerate(student_marks):
    print('оценка', mark)

user_full_name = ['Ivan, Ivanov']
first_name, second_name = user_full_name

print(first_name, second_name)
a, b, c, d, e = [15, 45, 87, 96, 4]
print (a, b, c, d, e)