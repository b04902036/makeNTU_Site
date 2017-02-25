from django import forms

class BikeForm(forms.Form):
	myName = forms.CharField(max_length=500)
	myId = forms.CharField(max_length=100)