from django.shortcuts import render
from market.models import marketItems
from market.forms import addItemForm


def marketplace(request):
    items = marketItems.objects.all()
    return render(request,"market/market.html",{"items":items})

def marketplaceAdd(request):
    if request.method == "POST":
        form = addItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = addItemForm()
    return render(request,"market/market_add.html",{"form":form})