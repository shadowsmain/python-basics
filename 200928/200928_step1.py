# row = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
# # [<remote_IP_address>, <request_datetime>, <request_method>, <requested_resource>]
# # _row_splitted = row.split(maxsplit=1)
# # remote_IP_address = _row_splitted[0]
# # row_tail = _row_splitted[1]
# #
# # print(remote_IP_address)
# # print(row_tail)
#
# # [first_name, last_name, age] = ['Иван', 'Петров', 19]
# # (first_name, last_name, age) = ('Иван', 'Петров', 19)
# # first_name, last_name, age = 'Иван', 'Петров', 19
# # print(first_name, last_name, age)
#
# remote_IP_address, row_tail = row.split(maxsplit=1)  # [left_part, right_part]
# _, _request_datetime = row_tail.split('[', maxsplit=1)
# request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)
#
# _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
# request_method, requested_resource, _ = _request_method.split(maxsplit=2)
#
# parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
# print(parsed_row)
# parsed_row = list(map(str.strip, parsed_row))
# print(parsed_row)

# remote_IP_address = remote_IP_address.strip()
# request_datetime = request_datetime.strip()
# request_method = request_method.strip()
# requested_resource = requested_resource.strip()
#
# print(remote_IP_address)
# print(request_datetime)
# print(request_method)
# print(requested_resource)

# print(row_tail)

# '217.168.17.5' -> remote_IP_address
# '- - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"' -> row_tail
# '- - ' -> _
# '17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"' -> _request_datetime
# '17/May/2015:08:05:12 +0000' -> request_datetime
# ' "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"' -> row_tail
# ' ' -> _
# 'GET /downloads/product_2 HTTP/1.1' -> _request_method
# ' 200 3316 "-" "-"' -> row_tail
# 'GET' -> request_method
# '/downloads/product_2' -> requested_resource
# 'HTTP/1.1' -> _

src_data = '''93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
217.168.17.5 - - [17/May/2015:08:05:34 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
217.168.17.5 - - [17/May/2015:08:05:09 +0000] "GET /downloads/product_2 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
93.180.71.3 - - [17/May/2015:08:05:57 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
217.168.17.5 - - [17/May/2015:08:05:02 +0000] "GET /downloads/product_2 HTTP/1.1" 404 337 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
217.168.17.5 - - [17/May/2015:08:05:42 +0000] "GET /downloads/product_1 HTTP/1.1" 404 332 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"
80.91.33.133 - - [17/May/2015:08:05:01 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
93.180.71.3 - - [17/May/2015:08:05:27 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"
188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'''


for row in src_data.split('\n'):
    # print(row)
    remote_IP_address, row_tail = row.split(maxsplit=1)
    _, _request_datetime = row_tail.split('[', maxsplit=1)
    request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)

    _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
    request_method, requested_resource, _ = _request_method.split(maxsplit=2)

    parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
    parsed_row = list(map(str.strip, parsed_row))
    print(parsed_row)