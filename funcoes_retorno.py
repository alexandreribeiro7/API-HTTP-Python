def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=0):
    if taxa_servico == 0 and desconto_fidelidade == 0:
        return consumo
    
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor

print(calcular_conta(consumo=100))