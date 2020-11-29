import mongoengine

class inventory:
    amount = mongoengine.IntField(default=0)
    name = mongoengine.StringField(required=True)


    
meta = {
    'db_alias': 'core',
    'collection': 'Users'
}


