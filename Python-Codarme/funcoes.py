# def dar_boas_vindas(nome, sobrenome, nome_do_curso):
#     print("Olá", nome, sobrenome)
#     print("Bem vindo ao curso de:", nome_do_curso)

# # dar_boas_vindas("Gabriel", "Saldanha", 'JavaScript')
# dar_boas_vindas("Gabriel", "Saldanha", nome_do_curso='JavaScript')

def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor

valor = calcular_conta(consumo=200, taxa_servico=0.1, desconto_fidelidade=0.05)
print("O valor é:", valor)


# consumo = 100
# servico = consumo * taxa_servico # 10
# desconto = consumo * desconto_fidelidade # 5

# valor = consumo + servico# 100 + 10 = 110
# valor = valor - desconto # 110 - 5

# => 105
