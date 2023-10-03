import requests


class Brew:

    def __init__(self, web_url, state):
        self.url = web_url
        self.stat = state

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()



    def details_of_brewaries(self,state):
        counts = {}
        count1 = 0
        self.stat = state
        for data in self.fetch_data():
            # print(data['name'])
            # print(data['state_province'])
            if str(data['state']) == self.stat:
                print(data['name'])
                count1 = count1 + 1
        print("Number of Breweries ", count1)

    def type_brew(self,state):
        self.stat = state
        list1 = []
        res1 = {}
        for data in self.fetch_data():
            list1.append(data['brewery_type'])
            for i in list1:
                res1[i] = list1.count(i)
        print(res1)

    def count_web_brew(self,state):
        self.stat= state
        count2 = 0
        for data in self.fetch_data():
            if data['website_url']:
                print(data['state'])
                print(data['website_url'])
                count2 = count2 + 1
        print("number of breweries having websites in the state", self.stat, "is", count2)




url1 = "https://api.openbrewerydb.org/v1/breweries?by_state=Alaska"
print("Alaska")
s = Brew(url1, "Alaska")
s.details_of_brewaries("Alaska")
s.type_brew("Alaska")
s.count_web_brew("Alaska")
url2 = "https://api.openbrewerydb.org/v1/breweries?by_state=Maine"
print("Maine")
b = Brew(url2,"Maine")
b.details_of_brewaries("Maine")
b.type_brew("Maine")
b.count_web_brew("Maine")
url3 = "https://api.openbrewerydb.org/v1/breweries?by_state=New%20York"
print("New York")
a = Brew(url1, "New York")
a.details_of_brewaries("New York")
a.type_brew("New York")
a.count_web_brew("New York")


