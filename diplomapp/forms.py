from django import forms


class FormUserAdd(forms.Form):
    name = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={
            'class': 'form-control new-fm', 
            'placeholder': 'Ваше имя'}))
    email = forms.EmailField(max_length=50,
            widget=forms.EmailInput(attrs={
            'class': 'form-control new-fm', 
            'placeholder': 'Введите email'}))
    phone_number = forms.CharField(max_length=11,
            widget=forms.TextInput(attrs={
            'class': 'form-control new-fm', 
            'placeholder': 'Номер телефона'}))

    def clean_phone_number(self):
        phone_number : str = self.cleaned_data['phone_number']
        if not (phone_number.startswith('8') or phone_number.isdigit()):
            raise forms.ValidationError('Введите номер телефона в формате 79009009999')
        return phone_number
