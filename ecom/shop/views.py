from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact,Orders,OrderUpdate
from math import ceil
import json

# METHODS***************************************************************************************************************

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds}
    return render(request, 'shop/index.html',params)

def about(request):

    return render(request, 'shop/about.html')

def contact(request):
    thank=False
    if request.method=="POST":
        print(request)
        name =request.POST.get('name','')
        print(name)
        email1 = request.POST.get('email1', '')
        print(email1)
        contact = request.POST.get('contact', '')
        print(contact)
        query = request.POST.get('query', '')
        print(query)
        contact=Contact(name=name,email=email1,phone=contact,query=query)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html',{thank:'thank'})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodview(request,myid):
    # on clicking quick view button
    product= Product.objects.filter(id=myid)
    #0 isliye likha hai kyokii data ya array list ke form me ja raha hai!!!

    return render(request, 'shop/prodview.html', {'product': product[0]})

def checkout(request):
    if request.method=="POST":
        print(request)
        items_json = request.POST.get('itemsJson', '')
        print(items_json)
        name = request.POST.get('name', '')
        print(name)
        email = request.POST.get('email', '')
        print(email)
        address=request.POST.get('add1', '')+" "+ request.POST.get('add2', '')
        print(address)
        add1 = request.POST.get('add1', '')
        print(add1)
        add2 = request.POST.get('add2', '')
        print(add2)
        city = request.POST.get('city', '')
        print(city)
        state = request.POST.get('state', '')
        print(state)
        zip1 = request.POST.get('zip1', '')
        print(zip1)
        phone = request.POST.get('phone', '')
        print(phone)
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip1, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')