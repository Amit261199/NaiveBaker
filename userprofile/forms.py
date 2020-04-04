from django import forms

class ProductForm(forms.ModelForm):
	title		= forms.CharField(
						widget = forms.TextInput(
								attrs = {
								"placeholder" : "my title"
								}
							)
					)
	email		= forms.EmailField() 