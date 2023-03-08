'''
    Lê uma palavra do teclado e inverte a posição de seus caracteres.
'''
def inverted_string():

    word = input("\nEscreva uma palavra: ")
    lenght = len(word)
    inverted_word = ''

    while lenght > 0:
        inverted_word += word[lenght-1]
        lenght -= 1
    
    print(f"A palavra '{word}' invertida é '{inverted_word}'.\n")

inverted_string()