import pymongo

def Schedule_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    mycol = mydb['ScheduleClasses']

    return mycol

