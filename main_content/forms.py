from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Contact Number',
            'message': 'How can we help?',
            'services': 'Select Services',
        }
        widgets = {
            "services": forms.CheckboxSelectMultiple(),
        }
        error_messages = {
            'name': {
                'required': 'Please enter your full name.',
                'max_length': 'Your name cannot exceed 100 characters.',
            },
            'email': {
                'required': 'Please enter your email address.',
                'invalid': 'Please enter a valid email address.',
            },
            'phone': {
                'required': 'Please enter your contact number.',
                'max_length': 'Your contact number cannot exceed 15 digits.',
            },
            'message': {
                'required': 'Please tell us how we can help you.',
            },
            'services': {
                'required': 'Please select at least one service.',
            },
        }
        
        

# dashboard form
# forms.py
from .models import Pages, SubSection

class MyForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Pages.objects.all(), empty_label="Select Category")
    subcategory = forms.ModelChoiceField(queryset=SubSection.objects.none(), empty_label="Select SubCategory")
    
    # Add more form fields as needed
