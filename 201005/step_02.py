concrete_request ='https://translate.google.com/?hl=ru#view=home&op=translate&sl=auto&tl=ru&text=patronymic'
# parse GET data -> dict
correct_answer = {
    'view': 'home',
    'op': 'translate',
    'sl': 'en',
    'tl': 'ru',
    'text': 'patronymic',
}
#print(concrete_request)
answer = None
trash, raw_get_data = concrete_request.split('?', maxsplit=1)
print(concrete_request.split('?'))
#print(trash)
print(raw_get_data)
get_data = raw_get_data.split('&')
print(get_data):
parsed_get_data = []
    for pair in get_data
    print(pair)


assert answer == correct_answer, 'bad parser!'




