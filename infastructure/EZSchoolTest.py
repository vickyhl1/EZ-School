import unittest
import sys
import pymongo
import tkinter
sys.path.append('..')
from data import db_operations
from data import user_db_init, inventory_db_init,game_links_db_init,Schedule_db_init,ScheduleTeacher_db_init,seker_db_init
user_db_init()
inventory_db_init()
game_links_db_init()
Schedule_db_init()
ScheduleTeacher_db_init()
import ScheForOneClassSecretary
client = pymongo.MongoClient()
mydb = client['EZSchooldb']


class MyTestCase(unittest.TestCase):
    def test_isinUsers(self):
        """
        checks if the user is in the DB by id
        """
        global mydb
        # 123456789 is in DB
        userobj = mydb['Users'].find_one({'id':'123456789'})
        self.assertIsNotNone(userobj,"sould not be NONE")

        # 000000000 is not in DB
        userobj = mydb['Users'].find_one({'id':'000000000'})
        self.assertIsNone(userobj,"sould be NONE")

    def test_checkUpdateUser(self):
        """
        checks if filed update is working
        """
        #find one user
        global mydb
        userobj = mydb['Users'].find_one({'id':'123456789'})

        #current password:1234
        self.assertEqual("1234",userobj['password'],"should be equal")

        #update new password:123456
        newpass ="123456"
        mydb['Users'].update_one({'id':userobj['id']}, {'$set': {'password':newpass}})
        userobj = mydb['Users'].find_one({'id':'123456789'})
        self.assertEqual(newpass,userobj['password'],"should be equal")

        #update old password: 1234
        mydb['Users'].update_one({'id':userobj['id']}, {'$set': {'password':"1234"}})

    def test_getUser(self):
        """
        checks if the function returns the correct user
                """
        f = open("Current_user.txt", "w")
        txt="319122842\nYovel Aloni"
        f.write(txt)
        f.close()

        global mydb
        userobj = mydb['Users'].find_one({'id':'319122842'})
        userobj1=db_operations.getUser()
        self.assertEqual(userobj1['id'],userobj['id'],"should be equal")

    def test_getSuject_and_setSuject(self):
        """
        checks if the function setSuject updatess the subject and the function getSubject return the correct subject
        """
        subject = "Math"
        db_operations.setSubject(subject)
        self.assertEqual(db_operations.getSubject(),subject,"should be equal")

    def test_ScheduleClassesDB(self):
        """
        the function checks if the DB updates and return correct values
        """
        global mydb
        userobj = mydb['ScheduleClasses'].find_one({'name':'class1'})
        mycol = mydb['ScheduleClasses']
        nameDay="sunday1"

        #the schedule is not arr
        arr=["בדיקה","בדיקה","בדיקה","בדיקה","בדיקה"]
        self.assertNotEqual(userobj[nameDay],arr,"should not be equal")

        #input arr in to schedule
        myquery = {nameDay: userobj[nameDay]}
        newval = {"$set": {nameDay: arr}}
        mycol.update_one(myquery, newval)
        userobj = mydb['ScheduleClasses'].find_one({'name':'class1'})
        self.assertEqual(userobj[nameDay],arr,"should be equal")

        myquery = {nameDay: userobj[nameDay]}
        newarr=["תנך","חשבון","חשבון","היסטוריה","היסטוריה"]
        newval = {"$set": {nameDay: newarr}}
        mycol.update_one(myquery, newval)
        userobj = mydb['ScheduleClasses'].find_one({'name':'class1'})

        self.assertNotEqual(userobj[nameDay],arr,"should not be equal")
        self.assertEqual(userobj[nameDay],newarr,"should be equal")

    def test_ScheduleTeacherDB(self):
        global mydb
        userobj = mydb['ScheduleTeacher'].find_one({'id': '312208523'})
        mycol = mydb['ScheduleClasses']
        nameDay = "sunday1"

        # the schedule is not arr
        arr = ["בדיקה", "בדיקה", "בדיקה", "בדיקה", "בדיקה"]
        self.assertNotEqual(userobj[nameDay], arr, "should not be equal")

        # input arr in to schedule
        myquery = {nameDay: userobj[nameDay]}
        mycol = mydb['ScheduleTeacher']
        newval = {"$set": {nameDay: arr}}
        mycol.update_one(myquery, newval)
        userobj = mydb['ScheduleTeacher'].find_one({'id': '312208523'})
        self.assertEqual(userobj[nameDay], arr, "should be equal")

        myquery = {nameDay: userobj[nameDay]}
        newarr = ["תנך כיתה ד", "חשבון כיתה ב", "חשבון כיתה ב", "היסטוריה כיתה א", "היסטוריה כיתה א"]
        newval = {"$set": {nameDay: newarr}}
        mycol.update_one(myquery, newval)
        userobj = mydb['ScheduleTeacher'].find_one({'id': '312208523'})

        self.assertNotEqual(userobj[nameDay], arr, "should not be equal")
        self.assertEqual(userobj[nameDay], newarr, "should be equal")

    def test_inventoryDB(self):
        global mydb
        mycol= mydb['Inventory']
        object=mycol.find_one({'item_name': 'עיפרון HB2'})
        self.assertEqual(object['id'],'001',"should be equal")
        self.assertEqual(object['price'],2,"should be equal")
        self.assertEqual(object['qty'],50,"should be equal")

if __name__ == '__main__':
    unittest.main()
