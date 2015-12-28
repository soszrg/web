#encoding=utf8
from django import forms


class ContractForm(forms.Form):
    title = forms.CharField(max_length=10, label=r'主题')
    email = forms.EmailField(required=False, label=r'邮箱')
    message = forms.CharField(widget=forms.Textarea, label=r'内容')
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 4:
            raise forms.ValidationError('Not enough words')
        
        return None
    
    
class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=20, label="First Name")
    last_name = forms.CharField(max_length=20, label="Last Name")
    email = forms.EmailField(label='Email')
    
class PubForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    address = forms.CharField(max_length=30, label='Address')
    city = forms.CharField(max_length=30, label='City')
    state_province = forms.CharField(max_length=30, label='State Province')
    country = forms.CharField(max_length=30, label='Country')
    website = forms.URLField(max_length=30, label='Website')
    
class BookForm(forms.Form):
    title = forms.CharField(max_length=30, label='Title')
    authors = forms.CharField(label='Authors')
    publisher= forms.CharField(max_length=30, label='Publisher')
    pub_date = forms.DateField(label='Publish Date')