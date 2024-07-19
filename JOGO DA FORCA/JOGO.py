import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_adivinhadas):
    return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

def jogo_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_erradas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas_erradas < max_tentativas:
        print("\nPalavra: ", mostrar_palavra(palavra, letras_adivinhadas))
        letra = input("Adivinhe uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente novamente.")
            continue
        
        letras_adivinhadas.add(letra)
        
        if letra in palavra:
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            tentativas_erradas += 1
            print(f"A letra '{letra}' não está na palavra. Tentativas restantes: {max_tentativas - tentativas_erradas}")

        if set(palavra).issubset(letras_adivinhadas):
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_forca()
