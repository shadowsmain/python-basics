import statistics
with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        l = len(row)
        shadow = []
        i = 0
        while i < l:
            s_int = ''
            a = row[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = row[i]
                else:
                    break
            i += 1
            if s_int != '':
                shadow.append(int(s_int))

        print(row.split()[0], row.split()[1], row.split()[2].replace(",", ":"), shadow)


        avg = statistics.mean(shadow)
        print(avg)
