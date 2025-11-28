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
    
    genero= forms.ChoiceField(
        label='Por favor informe o seu gênero',
        choices=GENERO_CHOICE,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True  # Permitir que a pessoa não declare, embora haja 'Prefiro Não Declarar'
    )
    
    genero_outro = forms.CharField(
        label='Selecione "Outro" acima e especifique',
        max_length=100,
        required=True,
        help_text='Use apenas se a opção "Outro" tiver sido selecionada.'
    )
     
    senha= forms.CharField(
        label='senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    ) 
    
    
    
    