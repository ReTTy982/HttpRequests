import requests
import json
import datetime
from datetime import timedelta

local = "http://127.0.0.1:8000/wypozyczalnia/"
server = "http://70.34.244.229:8081/wypozyczalnia/"
url_global = server

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
    url= url_global + "my_login"
    #url = "http://127.0.0.1:8000/wypozyczalnia/test"
    session = requests.Session()
    password = "orMHO4gp8dq"
    username = "jelgee0"
    session.auth = (username, password)
    auth = session.post("http://127.0.0.1:8000/wypozyczalnia/my_login")
    response = session.get("http://127.0.0.1:8000/wypozyczalnia/my_login")
    #response = requests.post(url=url, auth=(username, password))
    #x = response.content.decode("utf-8")
    return auth

def search_my_books(x):
    

    
    url = "http://127.0.0.1:8000/wypozyczalnia/search_my_books"
    r = x.post(url)
    print(r.json()["book_title"])

def serial_test():
    url = "http://70.34.244.229:8081/wypozyczalnia/author"
    url = "http://127.0.0.1:8000/wypozyczalnia/book_copies"
    data = {'author_name': 'Emmi Guilleton','copy_status': 'na stanie'}
    request = requests.get(url=url,data=data)
    parsed = json.loads(request.content)
    print(json.dumps(parsed,indent=4))

def serial_add():
    url = url = "http://127.0.0.1:8000/wypozyczalnia/book_copies"
    data = {'book_id':5,'branch_id':8}
    request = requests.post(url=url,data=data)
    if request.status_code != 400:
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.status_code)
        print(request.content)

def book_copy_get():
    url = url_global + "book_copies"
    data = {'id': 1}
    #data = {'book_id': 1}
    #data = {}
    #data =None
    request = requests.get(url=url,params=data)
    print(request.url)
    if request.status_code != 400:
        print(request.status_code)
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.status_code)
        print(request.content)

    print(request.url)
def book_copy_add():
    url = url_global + "book_copies"
    data = {'id' : 25, 'delete':1}
    request = requests.post(url, data=data)
    parsed = json.loads(request.content)
    print(json.dumps(parsed,indent=4))


def book_add():
    url = url_global +"books"
    data = {'author':6,'publisher_name':'Mohr Group', 'category' : 'Drama','book_title':'testowniś'}
    request = requests.post(url=url,data=data)
    parsed = json.loads(request.content)
    print(json.dumps(parsed,indent=4))

def book_get():
    url = url_global +"books"

def get_authors():
    url = url_global + "authors"
    data = {'author_name' : "Gloria Burdass"}
    request = requests.get(url=url,params=data)
    if request.status_code != 400:
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.status_code)

def add_authors():
    url = url = "http://127.0.0.1:8000/wypozyczalnia/authors"
    data = {'author_name' : "Gloria Burdass"}
    data = {'author_name' : '1'}
    request = requests.post(url=url,data=data)
    if request.status_code != 400:
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.content)
    

def add_issue():
    url = url = "http://127.0.0.1:8000/wypozyczalnia/issue_book"
    date_issue = datetime.datetime.now()
    print(date_issue)
    print(type(date_issue))
    date_due = datetime.datetime.now() + datetime.timedelta(20)
    data = {'copy': 10,'library_user':1,'date_issue' :date_issue, 'date_due' :date_due,'operation':'oddaj'}
    data = {'operation': 'oddaj', 'id': 5005}
    data = {'copy': 10,'library_user':1,'date_issue' :date_issue, 'date_due' :date_due,'operation':'wypozycz'}
    request = requests.post(url=url,data=data)

def get_issue():
    url ="http://127.0.0.1:8000/wypozyczalnia/issue_book"
    data = {'user_id' : 1}
    request = requests.get(url=url,params=data)
    if request.status_code != 400:
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.status_code)

def get_user():
    url ="http://70.34.244.229:8081/wypozyczalnia/library_user"
    data = {'first_name' : 'Gregoire'}
    request = requests.get(url, data=data)
    if request.status_code != 400:
        parsed = json.loads(request.content)
        print(json.dumps(parsed,indent=4))
    else:
        print(request.status_code)

def add_user():
    url ="http://127.0.0.1:8000/wypozyczalnia/library_user"
    data = {'first_name' : 'Polek','last_name' : 'Paczynski','login' : "poleczek",'password': 'krewetka1998$','address' : "Nie wiem"}
    request = requests.post(url, data=data)
def logout(session):
    url = local + "logout"
    requests.get(url=url)
    
if __name__ == "__main__":
    book_copy_get()
    #book_copy_add()
    #book_copy_get()
    #book_add()
    # get_authors()
     #add_authors()
    # add_issue()
    # get_issue()
    # get_user()
    # add_user()
    
