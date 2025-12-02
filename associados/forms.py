from django import forms


class AssociadoForms(forms.Form):
    
    GENERO_CHOICE=(
        ('M','Masculino'),
        ('F','Feminino'),
        ('O','Outros'),
        ('PN','Prefiro não responder')
    )
    
    nome_completo = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100
    )
    
    nome_social = forms.CharField(
        label='Nome Social',
        required=True,
        max_length=100
    )
    
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Digite seu e-mail'})
    )
    
    rg = forms.CharField(
        label="RG",
        required=True,
        max_length=7,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu RG'})
    )
    
    
    genero= forms.ChoiceField(
        label='Por favor informe o seu gênero',
        choices=GENERO_CHOICE,
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'Identifique sua identidade'}),
        required=True  # Permitir que a pessoa não declare, embora haja 'Prefiro Não Declarar'
    )
    
    genero_outro = forms.CharField(
        label='Selecione "Outro" acima e especifique',
        max_length=100,
        required=True,
        help_text='Use apenas se a opção "Outro" tiver sido selecionada.'
    )
     
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                'placeholder': 'Digite sua senha'}
        ),
    )
    senha_2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',   }
        )
    )
    




class LoginForm(forms.Form):

    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
    widget = forms.PasswordInput()
    )