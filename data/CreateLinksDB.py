import pymongo

def links_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    return mydb['Links']
