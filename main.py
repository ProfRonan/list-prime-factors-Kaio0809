"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    lfp = []
    if is_prime(number):
        lfp.append(number)
    else:
        j = 2
        while number > 1:
            if is_prime(j) and number % j == 0:
                lfp.append(j)
                number = number / j
            else:
                j += 1

    return lfp
