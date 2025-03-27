import requests
import bs4

url = "https://filmnet.ir/"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text , 'html.parser')
title = soup.find_all("div",attrs={"class":"carousel css-1b47hri e1eum8tf0"})

for i in title :
    print(i.text)

# print(title)
# print(soup.prettify())
# print(response)
# print(response.text)