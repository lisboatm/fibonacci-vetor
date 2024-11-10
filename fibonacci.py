def pre_calcular_fibonacci():
    # Pré-calcular os valores de Fibonacci de 0 a 60
    fib = [0, 1] + [0] * 59
    for i in range(2, 61):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def main():
    # Pré-calculando a sequência de Fibonacci
    fibonacci = pre_calcular_fibonacci()
    
    # Lendo o número de casos de teste
    T = int(input())
    
    # Processando cada caso de teste
    for _ in range(T):
        N = int(input())
        print(f"Fib({N}) = {fibonacci[N]}")

if __name__ == "__main__":
    main()
