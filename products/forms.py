from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for product management to add products"""

    class Meta:
        model = Product
        fields = '__all__'

    image1 = forms.ImageField(
        label='Image1', required=False, widget=CustomClearableFileInput)

    image2 = forms.ImageField(
        label='Image2', required=False, widget=CustomClearableFileInput)

    image3 = forms.ImageField(
        label='Image3', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
