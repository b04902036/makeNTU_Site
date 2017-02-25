from django import forms
class CommentForm(forms.Form):
	post_by = forms.CharField(max_length = 50, required = False)
	email = forms.EmailField(max_length = 50)
	comment = forms.CharField(max_length = 1000, widget=forms.Textarea())