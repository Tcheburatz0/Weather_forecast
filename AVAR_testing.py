import requests
# s_city = "Petersburg,RU"
appid = "ee5d55c03e00461d6c01b4e1b991bc40"
# city_id for SPb
city_id = 498817


# Прогноз
def request_forecast(city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        sum = 0
        count = 0
        a = []
        morns_six = []
        morns_nine = []
        for i in data['list']:
            if i['dt_txt'].find('06:00:00') != -1:
                morns_six.append(i['main']['temp'])
            if i['dt_txt'].find('09:00:00') != -1:
                morns_nine.append(i['main']['temp'])
            sum += i['main']['temp']
            count += 1
    except Exception as e:
        print("Exception (forecast):", e)
        pass

    print("Средняя температура = ", format(round(sum/count, 2)))
    print('Максимальная прогнозная утренняя (6-и утра) температура = ', max(morns_six))
    print('Максимальная прогнозная утренняя (9-и утра) температура = ', max(morns_nine))


request_forecast(city_id)
