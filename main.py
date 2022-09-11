import requests
import fake_useragent
from bs4 import BeautifulSoup as BS

session = requests.session()

link = 'https://login.kundalik.com/login'

user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    'login': 'erdauletov',
    'password': 'Darxan2005'
}

response = session.post(link, data=data, headers=header).text

link = 'https://schools.kundalik.com/class.aspx?class=1984360143203428201&view=members'
r = session.get(link)
html = BS(r.content, 'html.parser')

cookies_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

t = html.select('.page-wrapper > #content > .col34 > .people')
for el in t:
    title = el.find_all('td', 'tdName')
    for p in title:
        print(' '.join(p.text.strip().split(maxsplit=2)[:2]))
