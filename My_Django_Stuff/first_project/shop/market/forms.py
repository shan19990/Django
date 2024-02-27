from django import forms
from market.models import marketItems

class addItemForm(forms.ModelForm):
    class Meta:
        model = marketItems
        fields = ["itemName","itemDescription","itemPrice","itemPic",]