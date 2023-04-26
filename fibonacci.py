def fibonacci(n):
    """
    Funkcia vráti Fibonacciho postupnosť pre zadané číslo n.
    """
    if n <= 0:
        return "Zadajte platné číslo väčšie ako 0."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        return fibonacci_list


# Príklad použitia:
cislo = int(input("Zadajte číslo pre Fibonacciho postupnosť: "))
vysledok = fibonacci(cislo)
print(vysledok)
