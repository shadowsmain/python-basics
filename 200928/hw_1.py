import students_stat

students_log = students_stat.parse_marks('students_log.txt')
# students_stat.show_marks(students_log, raw=True)
# students_stat.show_marks(students_log, raw=False)
# students_stat.show_marks(students_log, raw=False, sep=' | ')
students_stat.save_marks('students_log.csv', students_log)