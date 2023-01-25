import requests
import json

def register():
    url = 'http://70.34.244.229:8081/wypozyczalnia/my_register'

    params = {'username':'Testownik1','password':'haslomaslo'}
    r = requests.post(url=url,data=params)
    print(r.text)

def get_data():
    url = "http://70.34.244.229:8081/wypozyczalnia/test"
    
    r= requests.post(url=url)
    print(r.content)


def search_book():
    url  = "http://127.0.0.1:8000/wypozyczalnia/search_book"
    params = {"branch": 6}
    r= requests.post(url=url,data=params)
    print(r.content)

def login():
    url="http://127.0.0.1:8000/wypozyczalnia/my_login"
    #url = "http://127.0.0.1:8000/wypozyczalnia/test"
    session = requests.Session()
    password = "zdutton0"
    username = "uKnMDFnLyMkt"
    session.auth = (username, password)
    auth = session.post("http://127.0.0.1:8000/wypozyczalnia/my_login")
    response = session.get("http://127.0.0.1:8000/wypozyczalnia/my_login")
    #response = requests.post(url=url, auth=(username, password))
    #x = response.content.decode("utf-8")
    return session

def search_my_books(x):
    

    
    url = "http://127.0.0.1:8000/wypozyczalnia/search_my_books"
    r = x.post(url)
    print(r.json()["book_title"])

    
if __name__ == "__main__":
    x = login()
    
    search_my_books(x)