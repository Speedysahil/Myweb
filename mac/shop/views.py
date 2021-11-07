from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contact , Orders , OrderUpdate
from math import ceil
from datetime import datetime
import json
# Create your views here.
def index(request):
    product = Product.product.all()
    allProds = []

    catprods = Product.product.values('category',"id",'price')
    cats = {item['category']for item in catprods}
    for cat in cats:
        prod = Product.product.filter(category=cat)

        n = len(product)
        nSlides =  n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    print(params)
    return render(request, "shop/index.html", params)

def about(request):
    contact = Contact(name='name',desc='desc',phone='phone',msg_id='id', email='email')

    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":

        name =request.POST.get('name','')

        email = request.POST.get('email', '') #aman
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        contact = Contact(name=name, phone=phone, email=email, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method == "POST":
        email = request.POST.get('email','')
        orderId = request.POST.get('orderId', '')
        try:
            order = Orders.product.filter(order_id=orderId,email=email)
            if len(order) > 0:
                update = OrderUpdate.product.filter(order_id=orderId)
                updates = []
                myDate = datetime.now()
                formatedDate = myDate.strftime("%d-%B-%Y  %H:%M:%S")
                for item in update:

                    updates.append({'text':item.update_desc,'time':formatedDate})
                    response = json.dumps(updates,default=str)
                    return HttpResponse(response)

            else:
                pass
        except Exception as e:
            pass
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.product.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html", {'product': product})

def checkout(request):
    if request.method == "POST":

        name =request.POST.get('name','')
        amount = request.POST.get('amount', '')

        email = request.POST.get('email', '')
        items_json = request.POST.get('itemsJson', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        order = Orders(name=name, phone=phone, email=email,
                       items_json= items_json,address=address, city=city, state=state, zip_code=zip_code,amount=amount)
        order.save()
        update = OrderUpdate(order_id = order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id':id})
    return render(request, 'shop/checkout.html')
