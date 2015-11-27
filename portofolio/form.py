from django import forms

class KontakForm(forms.Form):
	 Name=forms.CharField(required=True,widget=forms.TextInput({'class':'input-box'}))
	 Email=forms.EmailField(required=True,widget=forms.TextInput({'class':'input-box'}))
	 Subject=forms.CharField(required=True,widget=forms.TextInput({'class':'input-box'}))
	 Message= forms.CharField(required=True,widget=forms.Textarea({'class':'materialize-textarea'}))

    
