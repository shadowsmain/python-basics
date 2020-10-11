concrete_request = 'https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text=patronymic'


def parse_get_data(request):
trash, raw_get_data = concrete_request.split('?', maxsplit=1)
get_data = raw_get_data.split('&')

parsed_get_data = []
parsed_get_data_as_dict = {}
for pair in get_data:
    tmp = pair.split('=')
    parsed_get_data.append(tmp)
    parsed_get_data_as_dict[tmp[0]] = tmp[1]
return(parsed_get_data_as_dict)

request_1 = parse_get_data('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text=patronymic')