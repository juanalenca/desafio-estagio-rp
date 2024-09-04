#1) Sequência de Fibonacci

def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    if n in fib_seq:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = 21  # você pode mudar o número aqui
print(fibonacci_sequence(numero))
