import pymongo
import pprint



def user_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    mycol = mydb['Users']
    # 1- Secreatery, 2- Teacher, 3-Student

    data = [
    {
        'name': 'Rafael Azriaiev',
        'id': '309044071',
        'password': '1234',
        'Usertype': 3},
    {
        'name': 'Tal Shaked',
        'id': '312208523',
        'password': '12345',
        'Usertype': 2},
    {
        'name': 'Yovel Aloni',
        'id': '319122842',
        'password': '123456',
        'Usertype': 1}
    ]
    for user in data:
        existing_user = mycol.find_one({'id': user['id']})
        if existing_user == None:
            mycol.insert_one(user)
        elif not existing_user['id'] == user['id']:
            mycol.insert_one(user)

