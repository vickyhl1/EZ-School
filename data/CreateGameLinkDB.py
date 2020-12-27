import pymongo

def game_links_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    return mydb['Game_Links']
