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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        try:
            alt_name = str(self.__getitem__('name')).split('"')[5]
        except:
            alt_name = 'product image'

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            field.widget.attrs['alt'] = alt_name
