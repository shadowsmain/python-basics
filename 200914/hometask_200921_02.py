row_record = '217.168.17.5 - - [ 17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
split = row_record.split()
adress = split [0]
datetime = split [4]
request_method = split [6]
directory = split [7]
print(adress, datetime, request_method, directory)