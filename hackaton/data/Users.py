import mongoengine

class Users:
    Id = mongoengine.StringField(required=True)
    Passwords = mongoengine.StringField(required=True)
    Usertype = mongoengine.IntField(required=True, min_value=1, max_value=3)


meta = {
    'db_alias': 'core',
    'collection': 'Users'
}