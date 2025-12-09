# Définition de la fonction
def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Vérification pour éviter une division par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : division par zéro"
    else:
        return "Opérateur non valide"

# Appels de la fonction avec différents opérateurs
print(calcule(10, '+', 5))   # ➜ 15
print(calcule(10, '-', 5))   # ➜ 5
print(calcule(10, '*', 5))   # ➜ 50
print(calcule(10, '/', 2))   # ➜ 5.0
print(calcule(10, '%', 3))   # ➜ 1
print(calcule(10, '/', 0))   # ➜ Erreur : division par zéro
print(calcule(10, 'x', 2))   # ➜ Opérateur non valide

