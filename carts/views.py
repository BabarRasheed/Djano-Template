from django.shortcuts import render, redirect,HttpResponse
from e_store.models import ProductModel
from .models import CartItemModel, CheckoutInformation, ShippingPolicy
from.forms import CheckoutForm
from decimal import Decimal
import stripe
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from django.contrib.auth.decorators import login_required

stripe.api_key = "sk_test_51PL1k8P2sy5my1JqpwW1Aqp7KsmS2VXXWWmJFaVD40oacCF1lem0rMkR812PHqSHuHyg7aVJ86u4LHldmqO7RbYQ00rSLf3DdI"
def view_cart(request):
    cart_items = CartItemModel.objects.filter(user=request.user)
    total_price = 0
    tax = 0
    grand_total = 0
    for item in cart_items:
        price = item.product.discounted_price()
        total_price += price*item.quantity
    tax += (2*total_price)/100
    grand_total += total_price + tax
    # total_price = sum(item.product.price * item.quantity for item in cart_items)
    # tax_rate = Decimal(0.15)
    # tax_amonunt = total_price * tax_rate
    # Grandtotal = tax_amonunt + total_price
    context = {'cart_items': cart_items, 'total_price': total_price,"grand_total":grand_total,'tax':tax}
    return render(request, 'checkout_cart.html',context)
 
def add_to_cart(request, product_id):
    product = ProductModel.objects.get(id=product_id)
    cart_item, created = CartItemModel.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("viewcart") # view_cart that we creaet in urls 'name' use in it
 
def remove_from_cart(request, item_id):
    cart_item = CartItemModel.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def check_out(request):
    return render (request,'checkout_info.html')

def save_info(request):
    if request.method == "POST":
        print('hello 1')
        form = CheckoutForm(request.POST)
        print(form)
        if form.is_valid():
            print('hello 2')

            checkout_info = form.save(commit=False)
            print('hello 3')

            if request.user.is_authenticated:
                print('hello 4')

                checkout_info.user = request.user
            print('hello 5')
            checkout_info.save()
            return redirect('home') 
        else:
            print('hello 6')
            return render(request, 'checkout_payment.html', {'form': form})
    else:
        print('hello 7')
        form = CheckoutForm()
        return render(request, 'checkout_payment.html', {'form': form})
    
def checkout_info(request):
    return render(request, 'checkout_info.html')

def payment(request):
    return render(request, 'checkout_payment.html')


class Payment_cart(LoginRequiredMixin, View):            # Payment Methods
    template_name = 'checkout_payment.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            payment_method_id = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": str(request.POST.get('cardnumber')),
                    "exp_month": request.POST.get('mm'),
                    "exp_year": request.POST.get('yy'),
                    "cvc": str(request.POST.get('number')),
                },
            )
            customer = stripe.Customer.create(
                email=request.user.email,
                name=str(request.POST.get('cardholder')),
            )
            stripe.PaymentMethod.attach(
                payment_method_id.id,
                customer=customer.id,
            )

            product = CartItemModel.objects.filter(user=request.user).aggregate(Sum('product__price'))
            amount = product.get('product_price_sum')

            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency="usd",
                payment_method_types=["card"],
                customer=customer.id,
                payment_method=payment_method_id.id
            )
            confirm_payment = stripe.PaymentIntent.confirm(payment_intent.id, payment_method="pm_card_visa")
            shipping = 150
            sub_total = 0
            total = 0
            product_show = CartItemModel.objects.all()
            for item in product_show:
                if item.product:
                    item.pro_total = item.quantity * item.product.price
                    sub_total += item.pro_total
                    total = (sub_total + shipping)
                    item.save()
            context = {
                'product_show': product_show,
                'sub_total': sub_total,
                'total': total,

            }
            
        return render(request, template_name="checkout_complete.html", context={"intent": confirm_payment,"cart_image": product,"total": total})
    

@login_required(login_url="login")
def cart_complete(request):
    if request.method == 'POST':
        return render(request, 'checkout_complete.html')
