import pymongo

def connect_to_collection(collection_name):
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']
    mycol = mydb[collection_name]
    return mycol

def inventory_db_init():


    mycol = connect_to_collection('Inventory')

    inventory = [
        {
            'id': '001',
            'item_name': 'עיפרון HB2',
            'price': 2,
            'qty': 50
        },
        {
            'id': '002',
            'item_name': 'עט שחור 0.5',
            'price': 15,
            'qty': 30},
        {
            'id': '003',
            'item_name': 'דפי משבצות A4 (חבילה 72)',
            'price': 25,
            'qty': 100},
        {
            'id': '004',
            'item_name': 'מרקרים',
            'price': 10,
            'qty': 70},
        {
            'id': '005',
            'item_name': 'דפי שורות A4 (חבילה 72)',
            'price': 25,
            'qty': 100},
        {
            'id': '006',
            'item_name': 'קלסר שחור',
            'price': 30,
            'qty': 65}
    ]

    for item in inventory:
        exisiting_item = mycol.find_one({'id': item['id']})
        if exisiting_item == None:
            mycol.insert_one(item)
        elif not exisiting_item['id'] == exisiting_item['id']:
            mycol.insert_one(item)
