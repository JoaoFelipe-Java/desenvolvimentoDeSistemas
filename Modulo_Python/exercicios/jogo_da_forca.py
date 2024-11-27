def jogo_da_forca():
    # PYTHON - Palavra secreta
    # _ _ _ _ _ _ - 6 tentativas
    # Qual letra vai tentar
    tentativas = 6
    palavra_secreta = 'PYTHON'
    letras_secretas = set(palavra_secreta)
    letra_tentadas = set()

    while tentativas > 0 and letras_secretas:
        palavra_exibida = []
        for letras in palavra_secreta:
            if letras in letra_tentadas:
                palavra_exibida.append(letras)
            else:
                palavra_exibida.append('_')
        print("Palavra: ",''.join(palavra_exibida))

        letras = input("Digite uma letra").upper()
        letra_tentadas.add(letras)

        if letras in letras_secretas:
            print(f'Boa a letra {letras} esta certa')
        else:
            print(f'Ho nao {letras} errada')
            tentativas -= 1
            print(f'Vidas restante {tentativas}')
        if letras == '0':
            break   

def encontrar_alunos():
    print()


def estoque_loja():
    print()