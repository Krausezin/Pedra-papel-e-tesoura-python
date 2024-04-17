import random
from time import sleep
jog1 = ""
random1 = ""


class Ppt:
    def __init__(self, pedra, papel, tesoura):
        self.pedra = pedra
        self.papel = papel
        self.tesoura = tesoura

    def acao1(self):
        if self.pedra is True:
            jogador2.pedra1()
        if self.tesoura is True:
            jogador2.tesoura1()
        if self.papel is True:
            jogador2.papel1()

    def pedra1(self):
        if self.pedra is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Pedra!\033[1;97m Empatou!\033[m")
            contagem[2] = contagem[2] + 1
            print("\033[1;97m-=\033[m"*22)
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.papel is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Papel!\033[1;31m Você Perdeu!\033[m")
            contagem[1] = contagem[1] + 1
            print("\033[1;97m-=\033[m"*22)
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.tesoura is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Tesoura!\033[1;32m Você Venceu!\033[m")
            print("\033[1;97m-=\033[m"*22)
            contagem[0] = contagem[0] + 1
            placar()
            print("\033[1;97m-=\033[m"*22)
        return

    def tesoura1(self):
        if self.pedra is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Pedra!\033[1;31m Você Perdeu!\033[m")
            print("\033[1;97m-=\033[m"*22)
            contagem[1] = contagem[1] + 1
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.papel is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Papel!\033[1;32m Você Venceu!\033[m")
            contagem[0] = contagem[0] + 1
            print("\033[1;97m-=\033[m"*22)
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.tesoura is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Tesoura!\033[1;97m Empatou!\033[m")
            contagem[2] = contagem[2] + 1
            print("\033[1;97m-=\033[m" * 22)
            placar()
            print("\033[1;97m-=\033[m" * 22)
        return

    def papel1(self):
        if self.pedra is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Pedra!\033[1;32m Você Venceu!\033[m")
            contagem[0] = contagem[0] + 1
            print("\033[1;97m-=\033[m"*22)
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.papel is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Papel!\033[1;97m Empatou!\033[m")
            print("\033[1;97m-=\033[m" * 22)
            contagem[2] = contagem[2] + 1
            placar()
            print("\033[1;97m-=\033[m"*22)
        if self.tesoura is True:
            jokenpo()
            print("\033[1;97m-=\033[m"*22)
            print("O Computador escolheu Tesoura!\033[1;31m Você Perdeu!\033[m")
            print("\033[1;97m-=\033[m"*22)
            contagem[1] = contagem[1] + 1
            placar()
            print("\033[1;97m-=\033[m"*22)
        return

    def jogada(self):
        global jog1
        jog1 = input("\n\033[1;97mEscolha: pedra, papel ou tesoura! > \033[m")
        if jog1.upper() == "PEDRA":
            self.pedra = True
        elif jog1.upper() == "PAPEL":
            self.papel = True
        elif jog1.upper() == "TESOURA":
            self.tesoura = True
        else:
            print("Comando Inválido!")
            main()

    def reset(self):
        self.pedra = False
        self.tesoura = False
        self.papel = False

    def random(self):
        global random1
        random1 = random.choice(ppt2)
        if random1 == "pedra":
            self.pedra = True
        if random1 == "papel":
            self.papel = True
        if random1 == "tesoura":
            self.tesoura = True


def jokenpo():
    print("\033[1;97m-=\033[m"*22)
    print("\033[1;97mJó\033[m")
    sleep(0.7)
    print("\033[1;97mken\033[m")
    sleep(0.7)
    print("\033[1;97mpô\033[m")
    sleep(0.7)


def placar():
    print("\033[1;33m→\033[m\033[1;97mPLACAR\033[m\033[1;33m←\033[m")
    print(f"\033[1;97m|\033[m\033[1;32m{contagem[0]}\033[m\033[1;97m|\033[m\033[1;31m{contagem[1]}"
          f"\033[m\033[1;97m|\033[m\033[1;97m{contagem[2]}\033[m\033[1;97m|\033[m")


ppt2 = ["pedra", "papel", "tesoura"]
contagem = [0, 0, 0]


def main():
    while True:
        jogador1.jogada()
        jogador2.random()
        jogador1.acao1()
        jogador1.reset()
        jogador2.reset()


jogador1 = Ppt(False, False, False)
jogador2 = Ppt(False, False, False)
main()
