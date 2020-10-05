# __enter__
# context manager (f closed)
# __exit__ -> f.close()
with open('nginx_los_head.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        print(row)

print(f.closed)
#f = open('nginx_los_head.txt', 'r', encoding='utf-8')