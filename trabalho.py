import sys
import time
from pygame import mixer
from PIL import Image



def menu(*arguments):
    i = 1
    print("----- Menu de Opções -----")
    for arg in arguments:
        print(f"[{i}] {arg}\n")
        i += 1


mixer.init()
# Introdução
print("-" * 180)
print("Olá, esse é o nosso jogo de detetive feito para a disciplina Resolução de Problemas com Lógica Matematica do curso de Engenharia de Software")
print("-" * 180)

# Primeiro parágrafo
print("")
print(
    "Você foi contratado para dirigir um novo filme de terror, porém, há uma grande dúvida: quem será a estrela do seu filme de terror? ")
print(
    "Giulia, Fernando, Lucas e eu (André), como somos muitos generosos,lhe indicamos cinco possíveis estrelas ( Chucky, Jigsaw, Annabelle, "
    "Samara Morgan, A Pennywise e Zé do caixão)\ne convidamos você junto a nossos indicados para uma PoolParty.\nQuem sabe assim você os conhece "
    "melhor, e poderá tomar sua decisão.")

print("-" * 180)
# time.sleep(15)

# Segundo parágrafo
print("")
print(
    "Em um dado momento você, Chuky, Jigsaw e Zé do caixão, estão na cozinha batendo um papo. Chuky está contando sobre sua filha Glenda, e o"
    " fato dela ser gênero fluido")
print(
    "Jigsaw está tendo dificuldade em alcançar o armário da cozinha para pegar um copo, parece que sua bicicletinha não é alta o suficiente.\n"
    "Zé do caixão, por alguma razão sai da cozinha (que coisa não é mesmo… quem será que vai morrer?)...")
print("-" * 180)
# time.sleep(5)
# Mostra o som do grito
mixer.music.load("./sound/y2meta.com - Grito de terror (320 kbps).mp3")
# mixer.music.play()
# time.sleep(2.5)
mixer.music.stop()

# Terceiro parágrafo
print("")
print("Parágrafo 3")
print("Vocês saem da cozinha em direção ao grito, que parece vir da sala de estar. Ao chegar lá, você se depara com o corpo estendido do zé do caixão no chão.\n\033[31mHá um corte no corpo do Zé, indo da sua garganta até um pouco abaixo do umbigo… \033[0m")

img = Image.open('AREA9 (1).png')  # cria o objeto

# img.show() #apresenta a imagem na tela

print("Descubra quem é o assassino antes que todos morram")
# Primeiras preposições
print("-" * 180)

print("Escolha 2 pistas (preposições):")

preposicoes = ["Pista1", "Pista2", "Pista3", "Pista4"]
preposicoesT = ['Se você, Jigsaw e Chucky estavam na cozinha, então o assassino não estava na cozinha',
                'Samara estava fumando na varanda e a varanda é perto da sala',
                'Se a faca de PennyWise era de churrasco, então ele estava cortando as pernas das crianças para o churras',
                'Se Anabelle está mexendo no anel sobre a luva, então ela é a assassina'
                ]

menu(preposicoes)

print("-" * 180)

primeiraEscolha = -1

while primeiraEscolha < 0 or primeiraEscolha > len(preposicoes):
    try:
        primeiraEscolha = int(input("Sua primera escolha é: "))
        if 0 < primeiraEscolha <= len(preposicoes):
            preposicoes.pop(primeiraEscolha - 1)
            print([preposicoesT[primeiraEscolha]])
            preposicoesT.pop(primeiraEscolha)
    except ValueError:
        pass

menu(preposicoes)

segundaEscolha = -1

while segundaEscolha < 0 or segundaEscolha > len(preposicoes):
    try:
        segundaEscolha = int(input("Sua segunda escolha é: "))
        if 0 < segundaEscolha <= len(preposicoes):
            preposicoes.pop(segundaEscolha - 1)
            print([preposicoesT[segundaEscolha]])
            preposicoesT.pop(segundaEscolha)

    except ValueError:
        pass

escolhassassino = ''

while escolhassassino != "S" or escolhassassino != "N" or escolhassassino == '':
    print("-" * 180)
    escolhassassino = input("Deseja dizer quem é o assassino? [S/N]").upper().strip()
    if escolhassassino == "S" or escolhassassino == "N":
        break

if escolhassassino == "S":
    print("-" * 180)
    nomeassassino = input("Digite o nome do assassino: ").upper().strip()
    if nomeassassino != "ANNABELLE":
        # Mostra o som do grito
        mixer.music.load("./sound/y2meta.com - Grito de terror (320 kbps).mp3")
        mixer.music.play()
        time.sleep(2.5)
        mixer.music.stop()
        print("-" * 180)
        print("\033[31mVOCÊ MORREU\033[0m")
        print("-" * 180)
        sys.exit()
    else:
        print("SOM VITÓRIA")
        print("VOCÊ GANHOU")
else:
    print("")
    print("-" * 180)
    print("Pennywise adentra a sala com uma faca de churrasco em sua mão esquerda..\n"
          "-Jorginho me empresta a doze, diz Jigsaw ao ver Pennywise com a faca em mãos\n"
          "-Ora Ora Ora... O palhaço ficou com toda a diversão - murmura Chucky\n"
          "- Eu estava picando as pernas como me pediram. Além do mais, não teria problemas em matar um de vocês! Vocifera Penywise\n"
          "Bom...nisso Penywise tem toda a razão, todos assassinos e com certeza não teriam problemas em matarem uns aos outros,\n"
          "inclusive você! Mas, na situação em que se encontra o país, nenhuma proposta de trabalho pode ser negada… Bom, vamos voltar a história.\n"
          "Chucky atira o coração do Zé na direção de Penny, que o pega com uma bocada\n")
    print("-" * 180)
    print("-Bom garoto, bom garoto... - caçoa Chucky\n"
          "-Só gostaria de lembrar, que escolher um de nós para seu filmezinho novo, vai impactar diretamente na sua carreira e toda sua vida\n"
          "Jigsaw fala isso diretamente pra você\n"
          "E Jigsaw tem razão! Bom, veja bem, nós não queremos que você escolha um vilão que não fará sucesso nos cinemas...depositamos dinheiro\n"
          "em cima de você, escolha aquele que nos trará mais fama e dinheiro. Caso contrário, essa casa cheia de assassinos e monstros será o menor\n"
          "dos seus problemas")
    print("-" * 180)
    print("Você, Chucky e Jigsaw, o trio inseparável, estão em um quarto conversando\n"
          "- Olha, é mais do que claro que não foi um de nós que matou aquele cara! Eu sugiro que a gente arranque as tripas dos outros que não "
          "estavam na sala - diz Chucky\n"
          "- Vamos jogar um jogo…\n"
          "-Ah cala a boca !!! - Você e Chucky falam ao mesmo tempo\n"
          "- Deixem aquela boneca comigo! diz Chucky\n"
          "- Você parece muito interessado na Anabelle Chucky, questiona Jigsaw\n"
          "- Ela tem que respeitar meus 32 anos de carreira. Ela tá começando a vida dela.\nEu não comecei ontem, tenho toda uma história de vida,"
          " tenho toda uma história de trabalho. Eu fui pioneiro do movimento, hoje eu sou um ícone, vocifera Chucky\n"
          "- Então vamos ficar de olho em cada um? Pergunta Jigsaw\n"
          "Você sugere que Chucky fique de olho em Anabelle, Jigsaw em Penywise e você ficará de olho em Samara")


    #SEGUNDA MORTE

    # Mostra o som do grito
    mixer.music.load("./sound/y2meta.com - Grito de terror (320 kbps).mp3")
    mixer.music.play()
    time.sleep(2.5)
    mixer.music.stop()
    print("-" * 180)
    print("Todos escutam um grito, dessa vez vindo da garagem")
    print("Vocês correm direto para o som do grito\n"
          "\033[31mLá encontram Samara\033[0m….uuuuu… que interessante, agora restam dois suspeitos...ou será que não ?!\n"
          "Vamos falar então da morte da Samara?!\n"
          "Ela foi encontrada no carro, com os cabelos em pé"
          "- A garota tentou fazer uma ligação direta no carro e foi ligada com Deus hahah - Chucky caçoa\n"
          "- Não seja idiota! Mexa nela… viu, assassinada! - Comenta Jigsaw, de sua bicicletinha. Como a bicicleta de Jigsaw é"
          "muito baixa para\n"
          "conseguir ver pela janela, abriram a porta do carro para Jigsaw ver melhor"
          "Samara estava parecida com Nick-quase-sem-cabeça (se você não entendeu a referência, sinto muito\n"
          "-Hum, a mesma arma talvez, o corte está limpo...provavelmente fora o mesmo que matou aquele cara lá, pontua chucky")

    #Adicionando novas preposições
    preposicoesT.append()

    preposicoes = ["Pista1", "Pista2", "Pista3", "Pista4"]
    menu(preposicoes)

    print("-" * 180)

    primeiraEscolha = -1

    while primeiraEscolha < 0 or primeiraEscolha > len(preposicoes):
        try:
            primeiraEscolha = int(input("Sua primera escolha é: "))
            if 0 < primeiraEscolha <= len(preposicoes):
                preposicoes.pop(primeiraEscolha - 1)
                print([preposicoesT[primeiraEscolha]])
                preposicoesT.pop(primeiraEscolha)
        except ValueError:
            pass

    menu(preposicoes)

    segundaEscolha = -1

    while segundaEscolha < 0 or segundaEscolha > len(preposicoes):
        try:
            segundaEscolha = int(input("Sua segunda escolha é: "))
            if 0 < segundaEscolha <= len(preposicoes):
                preposicoes.pop(segundaEscolha - 1)
                print([preposicoesT[segundaEscolha]])
                preposicoesT.pop(segundaEscolha)

        except ValueError:
            pass

    escolhassassino = ''

    while escolhassassino != "S" or escolhassassino != "N" or escolhassassino == '':
        print("-" * 180)
        escolhassassino = input("Deseja dizer quem é o assassino? [S/N]").upper().strip()
        if escolhassassino == "S" or escolhassassino == "N":
            break

    if escolhassassino == "S":
        print("-" * 180)
        nomeassassino = input("Digite o nome do assassino: ").upper().strip()
        if nomeassassino != "ANNABELLE":
            # Mostra o som do grito
            mixer.music.load("./sound/y2meta.com - Grito de terror (320 kbps).mp3")
            mixer.music.play()
            time.sleep(2.5)
            mixer.music.stop()
            print("-" * 180)
            print("\033[31mVOCÊ MORREU\033[0m")
            print("-" * 180)
            sys.exit()
        else:
            print("SOM VITÓRIA")
            print("VOCÊ GANHOU")
    else:
        print("Continua história")