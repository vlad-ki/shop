from os.path import dirname, join
from pymongo import MongoClient
from bson.objectid import ObjectId


FILE = join(dirname(__file__), 'datebase.json')


class ProductSaveException(ValueError):
    pass


class Product(object):
    def __init__(
        self, id=None, monufacturer=None, model=None, amount=None, price=None, bprice=None,
            description=None, image=None
    ):  
        self.id = id
        self.monufacturer = monufacturer
        self.model = model
        self.amount = int(amount) if amount else None
        self.price = int(price) if price else None
        self.bprice = int(bprice) if bprice else None
        self.description = description
        self.image = image

    def save(self, new_monufacturer=False):
        db = MongoClient().shop

        if self.monufacturer:
            monufacturer_id = db.monufacturers.find(
                {'name': self.monufacturer},
                {'_id': 1}
            )

        if monufacturer_id.count() != 0:
            monufacturer_id = monufacturer_id[0]['_id']
        elif monufacturer_id.count() == 0 and new_monufacturer is True:
            monufacturer_id = db.monufacturers.insert_one(
                {'name': self.monufacturer}
            ).inserted_id
        else:
            raise ProductSaveException

        db.products.insert(
            {
                'monufacturer_id': monufacturer_id,
                'monufacturer': self.monufacturer,
                'model': self.model,
                'amount': self.amount,
                'price': self.price,
                'description': self.description,
                'image': self.image,
                'bprice': self.bprice
            })

    def list(self):
        list_of_products = []
        db = MongoClient().shop
        for product in db.products.find():
            list_of_products.append(product)
        return list_of_products

    def find(self, **kwargs):
        db = MongoClient().shop
        kwargs['_id'] = ObjectId(kwargs['_id'])
        return db.products.find_one(kwargs)

    def update(self):
        db = MongoClient().shop
        ident = {'_id': self.id}
        value = {
            'monufacturer': self.monufacturer,
            'model': self.model,
            'amount': self.amount,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'bprice': self.bprice
        }
        res = db.products.update_one(ident, value)
        return res.matched_count
