from django import forms

class Predict(forms.Form):

    CHOICES = [
        ('bachelor', "Bachelor's Degree"),
        ('masters', "Master's Degree"),
        ('phd', "Phd"),
    ]

    age = forms.IntegerField()
    yoe = forms.IntegerField()
    education = forms.ChoiceField(choices=CHOICES)