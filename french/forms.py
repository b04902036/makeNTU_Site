from django import forms

class FrenchMenuForm(forms.Form):
	time = forms.CharField(max_length = 100, required = False)
	title_for_link = forms.CharField(max_length = 100, required = False)
	href = forms.CharField(max_length = 100, required = False)
class FrenchNoteForm(forms.Form):
	title = forms.CharField(max_length = 100, required = False)
	content = forms.CharField(max_length = 10000, widget = forms.Textarea())
