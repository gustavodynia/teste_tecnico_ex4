sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

soma = sp + rj + mg + es + outros

def porcentagem(local):
    resultado = local / soma
    return resultado * 100
    

print(f'São Paulo representou: {porcentagem(sp):.2f}% do total faturado.')
print(f'Rio de Janeiro representou: {porcentagem(rj):.2f}% do total faturado.')
print(f'Minas Gerais representou: {porcentagem(mg):.2f}% do total faturado.')
print(f'Espirito Santo representou: {porcentagem(es):.2f}% do total faturado.')
print(f'Outros representaram: {porcentagem(outros):.2f}% do total faturado.')