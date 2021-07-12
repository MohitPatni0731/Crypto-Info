import requests
from bs4 import BeautifulSoup as bs
import random

question = input("Enter the Number of Cryptocurrency from below you want to know about :- \n 1. Bitcoin \n 2. Ethereum \n 3. Dogecoin \n 4. Tether \n 5. Cardano \n Enter Here :- ")

if question == "1":
    url='https://www.coindesk.com/price/bitcoin'
    r=requests.get(url)

    soup=bs(r.content,'html.parser')
    price=soup.find('div',{'class':'price-large'})
    print("Bitcoin:",price.text)
    percent=soup.find('span',{'class':'percent-value-text'})
    percentage=float(percent.text)
    if percentage>0:
        print('Bitcoin increased today')
    else:
        print('Bitcoin decreased today')

elif question == "2":
    url='https://www.coindesk.com/price/ethereum'
    r=requests.get(url)

    soup=bs(r.content,'html.parser')
    price=soup.find('div',{'class':'price-large'})
    print("Ethereum:",price.text)
    percent=soup.find('span',{'class':'percent-value-text'})
    percentage=float(percent.text)
    if percentage>0:
        print('Ethereum increased today')
    else:
        print('Ethereum decreased today')

elif question == "3":
    url='https://www.coindesk.com/price/dogecoin'
    r=requests.get(url)

    soup=bs(r.content,'html.parser')
    price=soup.find('div',{'class':'price-large'})
    print("Dogecoin:",price.text)
    percent=soup.find('span',{'class':'percent-value-text'})
    percentage=float(percent.text)
    if percentage>0:
        print('Dogecoin increased today')
    else:
        print('Dogecoin decreased today')

elif question == "4":
    url='https://www.coindesk.com/price/Tether'
    r=requests.get(url)

    soup=bs(r.content,'html.parser')
    price=soup.find('div',{'class':'price-large'})
    print("Tether:",price.text)
    percent=soup.find('span',{'class':'percent-value-text'})
    percentage=float(percent.text)
    if percentage>0:
        print('Tether increased today')
    else:
        print('Tether decreased today')

elif question == "5":
    url='https://www.coindesk.com/price/cardano'
    r=requests.get(url)

    soup=bs(r.content,'html.parser')
    price=soup.find('div',{'class':'price-large'})
    print("Cardano:",price.text)
    percent=soup.find('span',{'class':'percent-value-text'})
    percentage=float(percent.text)
    if percentage>0:
        print('Cardano increased today')
    else:
        print('Cardano decreased today')

else:
    print("Enter the number correctly")
