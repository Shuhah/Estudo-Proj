#calculador de divida que vou deixar pros meus netos

def invest(preju, juros, anos, aportn) :
    
    valor = preju * (1 + juros / jurosn) ** (preju * anos)
    return valor

preju = float(input("divida original: R$ "))
juros = float(input("taxa de juros: (%)")) / 100
anos = int(input("Quantos anos? "))
jurosn = int(input("digite 1 para juros ao ano, 12 para ao mês."))

valor = invest(preju, juros, anos, jurosn)

print(f"Seus netos devem R$ {valor} depois de {anos} ano(s)")