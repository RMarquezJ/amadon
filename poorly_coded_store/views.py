from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout(request):

  quantity_from_form = int(request.POST["quantity"])
  id_from_form = float(request.POST["productid"])
  price_from_id = Product.objects.get(id=id_from_form)
  total_charge = quantity_from_form * price_from_id.price
  print("Charging credit card...")

  Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
  
  return redirect('/redir')


def redir(request):

  orders=Order.objects.all()
  lastelement=Order.objects.last()
    
  totalorder=0
  for order in orders:
    totalorder += int(order.total_price)

  totalquantity=0
  for quantity in orders:
    totalquantity += int(order.quantity_ordered)

  context={
    'order' : Order.objects.all(),
    'totalorder' : totalorder,
    'totalquantity': totalquantity,
    'newbuy' : int(lastelement.total_price)
  }

  return render(request, "store/checkout.html", context)
