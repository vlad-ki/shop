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
            # тут может быть не insert, а update с параметром, который создает новую запить если не находит существующую.
            # можно сделать проверку на наличие _id.(+) Если _id то вызываем update
            # хочу что бы для обносления обьекта в монге я менял атрибуты обьекта класса и вызовал .save()
            # хочу что бы monufacturer и model не хранидись в products, а хранились только их _id и названия подтяшивались по _id
            # что бы при смене названия менять его в таблице названий а не в каждм продукте по отдельности. 
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
            # здесь в список пусть добавляются обекты класса.
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

    def __str__(self):
        return

# нужен метод который вернут словарь с данными о продукте.
    def dict():
        pass
