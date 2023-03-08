''' 
    Calcula a sequência de Fibonacci de forma recursiva. 

    Parâmetro: Número de termos da sequência.
'''
def fibonacci_generator(num_terms):
    
    if num_terms in {0, 1}:  
        return num_terms
    
    return fibonacci_generator(num_terms - 1) + fibonacci_generator(num_terms - 2)  

'''
    Lê um número do teclado e verifica se este faz parte da Sequência de Fibonacci.
'''
def number_is_present():

    # Número máximo de termos da sequência de Fibonacci usado para testes.
    MAX_TERMS = 30  

    number = int(input("\n - Escreva um número: "))
    sequence = [fibonacci_generator(term) for term in range(MAX_TERMS)]
    
    print (f"\n{sequence}")
    print(f"\nO número {number} {'pertence' if number in sequence else 'não pertence'} à sequência.\n")

number_is_present()