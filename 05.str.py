say = 'ВСЕМ ПРИВЕТ!'
print(say)
print(dir(say))

# say_2 = say

say_2 = say.upper()
print(say_2)

say_3 = say_2.capitalize()
print(say_3)


if say.endswith('!'):
    print('EMOTIONS')
