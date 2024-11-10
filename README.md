# Fibonacci em Vetor (Beecrowd - Problema 1176)

## Descrição
Neste problema, você deve **calcular o N-ésimo termo da série de Fibonacci** para diferentes valores fornecidos como entrada. 

A sequência de Fibonacci é definida da seguinte forma:
- `Fib(0) = 0`
- `Fib(1) = 1`
- `Fib(n) = Fib(n-1) + Fib(n-2)` para `n >= 2`

A série começa com `0, 1, 1, 2, 3, 5, 8, ...`, onde cada número é a soma dos dois anteriores.

Todos os valores de Fibonacci calculados neste problema devem caber em um **inteiro de 64 bits sem sinal**, portanto não há problemas de overflow com os valores permitidos.

## Entrada
- A primeira linha da entrada contém um **inteiro T** (1 ≤ T ≤ 20), indicando o número de casos de teste.
- Cada uma das próximas **T linhas** contém um único inteiro **N** (0 ≤ N ≤ 60), que representa o N-ésimo termo da série de Fibonacci a ser calculado.

## Saída
- Para cada caso de teste, imprima a mensagem `"Fib(N) = X"`, onde **X** é o valor do N-ésimo termo da série de Fibonacci.

### Exemplo de Entrada
```
3
0
4
2
```

### Exemplo de Saída
```
Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
```

## Lógica Utilizada
A ideia principal é **pré-calcular** todos os valores da série de Fibonacci de `0` a `60` e armazená-los em um vetor. Dessa forma, para cada entrada, podemos simplesmente acessar o valor pré-calculado em **O(1)** (tempo constante).

Essa abordagem é extremamente eficiente, pois evita o custo de recalcular os valores de Fibonacci repetidamente para cada caso de teste.

## Implementação em Python

```python
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
```

## Explicação do Código
1. **Pré-calculação**:
   - Utilizamos uma lista chamada `fib` para armazenar os primeiros 61 termos da sequência de Fibonacci (de `Fib(0)` até `Fib(60)`).
   - A lista é inicializada com os dois primeiros termos conhecidos (`0` e `1`) e o restante preenchido com zeros.
   - Usamos um loop para preencher os demais valores com base na fórmula `Fib(n) = Fib(n-1) + Fib(n-2)`.

2. **Leitura e processamento dos casos de teste**:
   - Lemos o número de casos de teste `T`.
   - Para cada caso, lemos o valor `N` e simplesmente acessamos o valor pré-calculado `fibonacci[N]` para exibir o resultado.

## Complexidade
- A pré-calculação dos termos de Fibonacci até `Fib(60)` tem uma complexidade de **O(60)**.
- Para cada caso de teste, o acesso ao valor pré-calculado é **O(1)**.
- Portanto, a solução é altamente eficiente para os limites do problema.

## Como Executar
Para testar o código em um ambiente local:
1. Salve o código em um arquivo, por exemplo, `fibonacci.py`.
2. Abra um terminal e execute:
   ```bash
   python3 fibonacci.py
   ```
3. Insira os valores de entrada conforme o exemplo fornecido.

## Notas Finais
Este problema é uma excelente introdução ao uso de **técnicas de pré-calculação** para melhorar a eficiência de algoritmos que precisam ser executados várias vezes com entradas semelhantes.
