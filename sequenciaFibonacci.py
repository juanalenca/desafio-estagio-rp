#1) Sequência de Fibonacci

def pertence_fibonacci(n):
    if n < 0:
        return f"O número {n} não pertence à sequência de Fibonacci."
    
    fib_a, fib_b = 0, 1  # Inicializando os dois primeiros números da sequência
    while fib_a < n:
        fib_a, fib_b = fib_b, fib_a + fib_b
    
    if fib_a == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = 21  # você pode mudar o número aqui
print(pertence_fibonacci(numero))
