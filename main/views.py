import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        # 'name': 'Nazkya Raahiil Ramandha', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    product = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    product = Item.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increase_amount(request, id):
    product = Item.objects.get(pk = id)
    product.amount += 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))


def decrease_amount(request, id):
    product = Item.objects.get(pk = id)
    product.amount -= 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def clear_item(request):
    Item.objects.all().delete()
    return HttpResponseRedirect(reverse('main:show_main')) 

def get_product_json(request):
    product_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        date_added = request.POST.get("date_added")

        new_product = Item(name=name, amount=amount, price=price, description=description, category=category, date_added=date_added)
        new_product.user = request.user
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


# gabisa
@csrf_exempt
def edit_item_ajax(request, product_id):
    if request.method == 'PUT':
        try:
            product = Item.objects.get(id=product_id)
        except Item.DoesNotExist:
            return HttpResponseNotFound()

        product.name = request.POST.get("name")
        product.amount = request.POST.get("amount")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.date_added = request.POST.get("date_added")

        product.save()

        return HttpResponse("OK", status=200)

    return HttpResponseNotFound()


# @csrf_exempt
# def delete_item_ajax(request, id):
#     if request.method == 'POST':
#         try:
#             product = Item.objects.get(pk=id)
#             product.delete()
#             return JsonResponse({'message': 'Item deleted successfully'})
#         except Item.DoesNotExist:
#             return JsonResponse({'error': 'Item does not exist'}, status=404)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


def delete_item_ajax(request, id):
    if request.method == "DELETE":
        try:
            # Replace this with your item deletion logic
            # For example, if you have a Product model:
            # product = Product.objects.get(pk=product_id)
            # product.delete()
            product = Item.objects.get(pk = id)
            product.delete()
            # Simulate a successful deletion for demonstration
            return JsonResponse({'message': 'Item deleted successfully'})
        except Exception as e:
            # Handle errors and exceptions
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"],
            category = data["category"],
            date_added = data["date_added"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


