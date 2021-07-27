from django import forms

class NameForm(forms.Form):
    method_name = forms.CharField(label='Имя метода', max_length=100)
    method_params = forms.CharField(label='Параметры метода (формат ввода: парам1:знач1 парам2:знач2)', max_length=255, required=False)
