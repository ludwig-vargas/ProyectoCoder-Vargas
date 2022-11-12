from django import forms
from ckeditor.widgets import CKEditorWidget
from product.models import Product

CATEGORY = (('Tecnologia','Tecnologia'),('Ropa','Ropa'),('Electrodomesticos','Electrodomesticos'))

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del Producto:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre del producto',
                'required':'True',
            }
        ),
    )
    
    code_product = forms.IntegerField(
        label='Codigo de Producto:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Codigo del producto',
                'required':'True',
            }
        ),
    )
    
    category = forms.ChoiceField(
        choices=CATEGORY,
        label='Categoria',
        required=False,
        widget=forms.Select(
            attrs={
                'class':'form-control',
                'required':'True',
            }
        ),     
    )
    
    
    price = forms.IntegerField(
        label='Precio de Producto:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Precio del producto',
                'required':'True',
            }
        ),
    )
    
    amount = forms.IntegerField(
        label='En existencia:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Cantidad del producto',
                'required':'True',
            }
        ),
    )
    
    description = forms.CharField(
        label='Descripcion:',
        required=False,
        widget=CKEditorWidget(
            attrs={
                'required':'True',
            }
        ),
    )
    
    class Meta:
        model = Product
        fields = ['name','code_product','category','price','amount','description']
    
    