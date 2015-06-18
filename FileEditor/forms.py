from django import forms

class EditorForm(forms.Form):
	data = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))