for n in range(2, 1001):
    # Vérifie si n est premier
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end= " ")
