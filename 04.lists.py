mock_lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.19',
    '19.05.21'
]
student_marks = [5, 4, 3, 2, 5]

i = 0
while i < len(student_marks) :
    print(mock_lesson_dates[i],'mark', student_marks[i])
    i += 1
