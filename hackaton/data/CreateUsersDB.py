import pymongo
import pprint
def db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    mycol1 = mydb['Inventory']
    mycol2 = mydb['Users']
    # 1- Secreatery, 2- Teacher, 3-Student

    data = {
        'name': 'Rafael Azriaiev',
        'id': '309044071',
        'password': '1234',
        'Usertype': 3
    }
    user = mycol2.find_one({'id': data['id']})
    if user == None:
        mycol2.insert_one(data)
    elif not user['id'] == data['id']:
        mycol2.insert_one(data)

    data = {
        'name': 'Tal Shaked',
        'id': '312208523',
        'password': '12345',
        'Usertype': 2
    }
    user = mycol2.find_one({'id': data['id']})
    if user == None:
        mycol2.insert_one(data)
    elif not user['id'] == data['id']:
        mycol2.insert_one(data)

    data = {
        'name': 'Yovel Aloni',
        'id': '319122842',
        'password': '123456',
        'Usertype': 1
    }
    user = mycol2.find_one({'id': data['id']})
    if user == None:
        mycol2.insert_one(data)
    elif not user['id'] == data['id']:
        mycol2.insert_one(data)

