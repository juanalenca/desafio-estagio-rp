#2) Verificação de existência da letra 'a'

def verificar_letra_a(string):
    contador = string.lower().count('a')
    
    if contador > 0:
        return f"A letra 'a' ocorre {contador} vezes na string."
    else:
        return "A letra 'a' não ocorre na string."

# Exemplo de uso:
texto = "Aprendizado de máquina"  # você pode mudar a string aqui
print(verificar_letra_a(texto))
