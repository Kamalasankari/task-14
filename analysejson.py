# JSON
# Working with JSON
import requests


class AnalysingJsonObject:

    def __init__(self, web_url):
        self.url = web_url

    # fetch data from the API server
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def count_json_data(self):
        count = 0
        for data in self.fetch_data():
            count = count + 1
        return count

    def fetch_name(self):
        list3=[]
        for data in self.fetch_data():
            print(data['name']['official'])
            for k, v in data['currencies'].items():
                print(v['name'])
                print(v['symbol'])
        #         list3.append(v['name'])
        #         list3.append(v['symbol'])
        # return list3


    def fetch_dollar_name(self):
        list1 = []
        print("country which have dollar as its currency")
        for data1 in self.fetch_data():
            currency_keys = list(data1.get('currencies', {}).keys())
            if currency_keys == ["USD"]:
                # print(name)
                # print(currency_keys)
                list1.append(data1['name']['common'])
        return list1

    def fetch_euro_name(self):
        list2 = []
        print("country which have euro as its currency")
        for data2 in self.fetch_data():
            name = data2["name"]["common"]
            currency_keys = list(data2.get('currencies', {}).keys())
            if currency_keys == ["EUR"]:
                # print(name)
                # print(currency_keys)
                list2.append(data2["name"]["common"])
        return list2


url = "https://restcountries.com/v3.1/all"

s = AnalysingJsonObject(url)
print(s.count_json_data())
print(s.fetch_data())

dollar_list = s.fetch_dollar_name()
print(dollar_list)
euro_list = s.fetch_euro_name()
print(euro_list)
s.fetch_name()


