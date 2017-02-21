from bottle import (
    route, post,
    debug, run,
    request, response,
    redirect, template
)

from product import Product, ProductSaveException

debug(True)


@route('/')
def glavnaia():
    list_of_products = Product().list()
    return template('templates/home.tpl', list_of_products=list_of_products)


@route('/add_product')
def add():
    return template('templates/add_product.tpl', ProductSave=None)


@post('/add_product')
def post_add():
    try:
        Product(
            monufacturer=request.forms.get('monufacturer'),
            model=request.forms.get('model'),
            amount=request.forms.get('amount'),
            price=request.forms.get('price'),
            bprice=request.forms.get('bprice'),
            description=request.forms.get('description'),
            image=request.forms.get('image'),
        ).save(new_monufacturer=bool(request.forms.get('new_monufacturer')) or False)
        return template('templates/add_product.tpl', ProductSave=True)
    except ProductSaveException:
        return template('templates/add_product', ProductSave=False)


@route('/edit_product')
def route_impl():
    _id = request.query._id
    product = Product().find(**{'_id': _id})
    return template('templates/edit_product.tpl', product=product)


@post('/edit_product')
def post_impl():
    try:
        Product(
            monufacturer=request.forms.get('monufacturer'),
            model=request.forms.get('model'),
            amount=request.forms.get('amount'),
            price=request.forms.get('price'),
            bprice=request.forms.get('bprice'),
            description=request.forms.get('description'),
            image=request.forms.get('image'),
        ).save(new_monufacturer=bool(request.forms.get('new_monufacturer')) or False)
        return template('templates/edit_product.tpl', ProductSave=True)
    except ProductSaveException:
        return template('templates/edit_product.tpl', ProductSave=False)


run(host='localhost', port=8080, reloader=True)
