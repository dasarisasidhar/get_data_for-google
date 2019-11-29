import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.google.com/search?q=azure+devops')
soup = BeautifulSoup(page.content, 'html5lib') 
#print(soup.prettify())
#value = soup.find_all(class_=True)
#soup.findAll('div', attrs = {"class":"kno-rdesc"})
classes = []
print("hi")
for element in soup.find_all(class_=True):
    classes.extend(element["class"])
    #print(element["class"])
    if element["class"] == ['BNeawe', 's3v9rd', 'AP7Wnd']:
        print(element)

#classes = [value 
#           for element in soup.find_all(class_=True) 
#           for value in element["class"]]
#print(classes)