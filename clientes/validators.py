def cpf_valido(cpf):
    return len(cpf) == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def telefone_valido(telefone):
    return len(telefone) == 11