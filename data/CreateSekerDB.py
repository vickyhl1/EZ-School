import pymongo

def seker_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    return mydb['Seker']
