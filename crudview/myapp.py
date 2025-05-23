import json
import requests

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    headers={ 'content-Type':'application/json'}
    r=requests.get(url=URL, data=json_data, headers=headers)
    data=r.json()
    print(data)
get_data()

def post_data():
    data={
        'name':'isha',
        'roll':68,
        'city':'porbandar'
    }
    headers={ 'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data, headers=headers)
    data=r.json()
    print(data) 
# post_data()
def update_data():
    data={
        'id':6,
        'name':'Rohit',
        'city':'Mumbai'
    }
    headers={ 'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data,headers=headers)
    data=r.json()
    print(data)
# update_data()
def delete_data():
    data={"id":6}
    headers={ 'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)
# delete_data()