from django import forms
from .models import Category, News

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'created_at', 'image', 'categories']
    
    created_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )