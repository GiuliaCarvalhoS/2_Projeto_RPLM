import time
from pygame import mixer
from PIL import Image



def menu(*arguments):
    i = 1
    print("----- Menu de Opções -----")
    for arg in arguments:
        print(f"[{i}] {arg}\n")
        i += 1






# Função que recebe opções e monta um menu


mixer.init()
# Introdução
print("Olá, esse é o nosso jogo de detetive feito para a disciplina do curso de Resolução de Problemas com Lógica Matematica")
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

#Primeiras preposições 


#Menu de resposta
