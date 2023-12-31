from django.shortcuts import render, get_object_or_404
from .cart import Cart 
from shop.models import Product
from django.http import JsonResponse

def cart_summary(request): 
    return render(request, "cart_summary.html", {})


def cart_add(request): 
    #get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post': 
        #get stuff
        product_id = int(request.POST.get('product_id'))
      
        #lookup prod in database
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product)
        #Crt quantity
        cart_quantity = cart.__len__()
        
        #Return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({ 'qty': cart_quantity})
        return response


def cart_delete(request): 
    pass


def cart_update(request):
    pass