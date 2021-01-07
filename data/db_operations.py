import pymongo

def connect_to_db(db_name):
    client = pymongo.MongoClient()
    mydb = client[db_name]
    return mydb

def connect_to_collection(db,collec_name):
    mycoll = db[collec_name]
    return mycoll

def connect_to_db_and_collection(db_name,collec_name):
    db = connect_to_db(db_name)
    collection = connect_to_collection(db,collec_name)
    return collection


def getUser():
    f = open("Current_user.txt", "r")
    userid = f.readline().rstrip()
    f.close()
    mycol = connect_to_db_and_collection('EZSchooldb', 'Users')
    userobj = mycol.find_one({'id': userid})
    return userobj

def getSubject():
    f = open("Current_Subject.txt", "r")
    subject = f.readline().rstrip()
    f.close()
    return subject

def setSubject(subject):
    f = open("Current_Subject.txt", "w")
    f.seek(0)
    f.truncate()
    f.write(subject)
    f.close()

def findUser(userId):
    mycol = connect_to_db_and_collection('EZSchooldb', 'Users')
    userobj = mycol.find_one({'id': userId})
    return userobj