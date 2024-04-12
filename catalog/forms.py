from django import forms

from catalog.models import Product, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):

    stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data in self.stop_words:
            raise forms.ValidationError('В названии содержатся запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if cleaned_data in self.stop_words:
            raise forms.ValidationError('В описании содержатся запрещенные слова')

        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
