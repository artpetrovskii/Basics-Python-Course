dana_data = '01.01.2020'
data_list = dana_data.split('.')
dict_months = {
    "1": "января",
    "2": 'феврал',
    "3": 'марта',
    "4": 'апреля',
    "5": 'мая',
    "6": 'июня',
    "7": 'июля',
    "8": 'августа',
    "9": 'сентября',
    "01": "января",
    "02": 'феврал',
    "03": 'марта',
    "04": 'апреля',
    "05": 'мая',
    "06": 'июня',
    "07": 'июля',
    "08": 'августа',
    "09": 'сентября',
    "10": 'октября',
    "11": 'ноября',
    "12": 'декабря',
}
dict_days = {
    '1': 'первое', '2': 'второе', '3': 'третье', '4': 'четвёртое',
    '5': 'пятое', '6': 'шестое', '7': 'седьмое', '8': 'восьмое',
    '9': 'девятое', '01': 'первое', '02': 'второе', '03': 'третье',
    '04': 'четвёртое', '05': 'пятое', '06': 'шестое', '07': 'седьмое',
    '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое',
    '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
    '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
    '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
    '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье',
    '24': 'двадцать четвёртое', '25': 'двадцать пятое',
    '26': 'двадцать шестое', '27': 'двадцать седьмое',
    '29': 'двадцать девятое', '28': 'двадцать восьмое', '30': 'тридцатое',
    '31': 'тридцать первое',
}
for key in dict_days:
    if data_list[0] == key:
        data_list[0] = dict_days[key]

for key in dict_months:
    if data_list[1] == key:
        data_list[1] = dict_months[key]

answer_data = data_list[0] + ' ' + data_list[1] + ' ' + data_list[2] + " года"
print(answer_data)
