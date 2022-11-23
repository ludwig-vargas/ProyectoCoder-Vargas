from django import forms
from ckeditor.widgets import CKEditorWidget
from service.models import Service

CATEGORY = (('Tecnologia','Tecnologia'),('Ropa','Ropa'),('Electrodomesticos','Electrodomesticos'))

class ServiceForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del Producto:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre del servicio',
                'required':'True',
            }
        ),
    )
    
    code_service = forms.CharField(
        label='Codigo del Servicio:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Codigo del servicio',
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
        label='Precio del Servicio:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Precio del servicio',
                'required':'True',
            }
        ),
    )
    
    numberphone = forms.IntegerField(
        label='Numero de Telefono:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Numero de Telefono',
                'required':'True',
            }
        ),
    )
    
    email = forms.EmailField(
        label='Correo Electronico',
        required=False,
        widget=forms.TextInput(
          attrs={
                'class':'form-control',
                'placeholder':'Correo electronico',
                'required':'True',
          }  
        ),
    )
    
    description = forms.CharField(
        label='Descripcion:',
        required=False,
        widget=CKEditorWidget(),
    )
    
    image = forms.ImageField(
        label='Imagen del Servicio:',
        required=False,
    )
    
    class Meta:
        model = Service
        fields = ['name','code_service','category','price','numberphone','email','description', 'image']
    
class CommentServiceForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-2",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,     
                "rows": 3,
                "style":"height: 100px",
            }
        ),
    )