
from django.http import JsonResponse
from django.shortcuts import render,redirect
from orders.models import OrderModel
from .models import CartModel
from products.models import ProductModel
from accounts.forms import LoginForm,GuestForm
from billing.models import BillingProfileModel
from accounts.models import GuestEmail
from address.forms import AddressForm
from address .models import AddressModel
# Create your views here.

def cart_detail_api_view(request):
    cart_obj,new_obj=CartModel.objects.new_or_get(request)
    products=[{
            "id":x.id,
            "url":x.get_absolute_url(),
            "name":x.name,
            "price":x.price
            } 
              for x in cart_obj.products.all()]

    cart_data={"products":products,"subtotal":cart_obj.subtotal,"total":cart_obj.total}
    return JsonResponse(cart_data)


def cart_home(request):
    cart_obj,new_obj=CartModel.objects.new_or_get(request)
    return render(request,"carts/home.html",{"cart":cart_obj})

def cart_update(request):
    product_id=request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj=ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:cart_home")
        cart_obj,new_obj=CartModel.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added=False
        else:
            cart_obj.products.add(product_obj)
            added=True
        request.session['cart_items']=cart_obj.products.count()
    # return redirect(product_obj.get_absolute_url())
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            print("Ajax Request")
            json_data = {
                "added":added,
                "removed":not added,
                "cartItemCount":cart_obj.products.count()
            }
            return JsonResponse(json_data,status=200)
            # return JsonResponse({"message":"Error 400"},status=400)
    return redirect("cart:cart_home")

def checkout_home(request):
    cart_obj,cart_created=CartModel.objects.new_or_get(request)
    order_obj=None
    if cart_created or cart_obj.products.count()==0:
        return redirect("cart:cart_home")
    login_form=LoginForm()
    guest_form=GuestForm()
    address_form=AddressForm()


    billing_address_id=request.session.get("billing_address_id",None)
    shipping_address_id=request.session.get("shipping_address_id",None)


    billing_profile, billing_profile_created = BillingProfileModel.objects.new_or_get(request)
    address_qs=None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs=AddressModel.objects.filter(billing_profile=billing_profile)

            order_obj, order_obj_created = OrderModel.objects.new_or_get(billing_profile, cart_obj)
            if shipping_address_id:
                order_obj.shipping_address=AddressModel.objects.get(id=shipping_address_id)
                del request.session["shipping_address_id"]
            if billing_address_id:
                order_obj.billing_address=AddressModel.objects.get(id=billing_address_id)
                del request.session["billing_address_id"]
            if billing_address_id or shipping_address_id:
                order_obj.save()
    #To finalize the  checkout
    #we need to (update the order_obj to done i.e paid) and del request.session['cart_id'] then redirect to success page
    
    if request.method=="POST":
        "Check that the order is done"
        is_done=order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items']=0
            del request.session['cart_id']
            return redirect("cart:success")
    
    context={
            "object":order_obj,
            "billing_profile":billing_profile,
            "login_form":login_form,
            "guest_form":guest_form,
            "address_form":address_form,
            "address_qs":address_qs,
        }
    return render(request,"carts/checkout.html",context)

def checkout_done_view(request):
    return render(request,"carts/checkout-done.html",{})