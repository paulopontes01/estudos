import timeit
import random

# Criando uma lista grande de números aleatórios (entre 1 e 100.000)
random_numbers = [random.randint(1, 100000) for _ in range(1_000_000)]

# Abordagem 2: Usando set() para eliminar duplicatas rapidamente
def sum_unique_fast(numbers):
    return sum(set(numbers))

# Medindo o tempo de execução da abordagem rápida
fast_time = timeit.timeit(lambda: sum_unique_fast(random_numbers), number=1)

# Exibindo os resultados
print(f"Tempo de execução - Abordagem rápida (set): {fast_time:.4f} segundos")

