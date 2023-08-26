from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, nome_valido, rg_valido, telefone_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve conter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Permitido apenas letras."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve conter 9 dígitos"})
        if not telefone_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O Telefone deve seguir o seguinte modelo: 11 12345-1234"})

        return data







    """def validate_cpf(self, cpf):
        if len(cpf) !=11:
            raise serializers.ValidationError('O CPF deve conter 11 dígitos.')
        return cpf
    
    def validate_nome (self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError('Permitido apenas letras.')
        return nome
    
    def validate_rg(self, rg):
        if len(rg) !=9:
            raise serializers.ValidationError('O RG deve conter 09 dígitos.')   
        return rg
    
    def validate_celular(self, celular):
        if len(celular) !=11:
            raise serializers.ValidationError('O Celular deve conter 11 dígitos.')
        return celular"""

    