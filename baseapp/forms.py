from django.contrib.auth.forms import UserCreationForm
from .models import User, Book, Category
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField
from django.forms.widgets import DateInput
from django import forms
from django.utils.text import slugify
class SignUpForm(UserCreationForm):
    # phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(), required=True)
    class Meta:
        
        model = User
        # class Meta:
        #     widgets = {
        #     'phone':PhoneNumberPrefixWidget()
        #     }
        labels = {'dob':('D.O.B')}
        widgets = {'dob':DateInput(attrs = {'type':'date'}),}
        fields = ('email', 'name', 'phone', 'gender', 'dob')

# form to place a book on sale
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'category', 'name', 'author', 'edition', 'pages', 'image', 'description','condition', 'price', 'available', 
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        
        if not slug:
            name = self.cleaned_data.get('name', '')
            slug = slugify(name)
        return slug