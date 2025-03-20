class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self.vida = 100  # Todos começam com 100 de vida
        self.forca = forca  # A força define o dano do ataque

    def atacar(self, outro_personagem):
        if outro_personagem.vida > 0:
            outro_personagem.vida -= self.forca
            if outro_personagem.vida < 0:
                outro_personagem.vida = 0  # Garante que a vida não fique negativa
            print(f"{self.nome} atacou {outro_personagem.nome} causando {self.forca} de dano!")
        else:
            print(f"{outro_personagem.nome} já foi derrotado!")

    def status(self):
        print(f"{self.nome} tem {self.vida} de vida restante.")

# Criando dois personagens
heroi = Personagem("Herói", 15)
vilao = Personagem("Vilão", 10)

# Exibindo status antes da luta
heroi.status()
vilao.status()

# Herói ataca o Vilão
heroi.atacar(vilao)

# Exibindo status após o ataque
heroi.status()
vilao.status()
