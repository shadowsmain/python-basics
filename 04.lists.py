lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.19',
    '19.05.21',
]
student_marks = [
    5,
    4,
    3,
    2,
]
lesson_dates_2 = [
    '19.05.15',
    '19.05.17',
    '19.05.19',
    '19.05.21',
]

student_marks_2 = [
    5,
    4,
    3,
    2,
]


# lesson_dates_and_marks = [
#     ['19.05.15', 5],
#     ['19.05.17', 4],
#     ['19.05.19', 3],
#     ['19.05.21', 2],
# ]

for lesson_dates, mark, mark_2 in zip(lesson_dates, student_marks, student_marks_2):
    print(lesson_dates, 'оценка', 'студента 1', mark, 'студента 2', mark_2)

# i = 0
# while i < len(student_marks) :
#     print(mock_lesson_dates[i],'mark', student_marks[i])
#     i += 1
# for item in student_marks:
#     print('оценка', item)
#
# for item in enumerate(student_marks):
#     print('оценка', item)
#
#
#
# for lesson_date, mark in lesson_dates_and_marks:
#     #print(mock_lesson_dates[i],'оценка', mark)
#     #lesson_dates, mark = record
#     print (lesson_dates, 'оценка', mark)