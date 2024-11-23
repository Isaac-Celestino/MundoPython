#abre e reproduza um arquivo de audio mp3

import pygame

# Inicializando o mixer e o pygame
pygame.mixer.init()
pygame.init()

# Corrigindo o caminho do arquivo de música
caminho = r"C:\Users\isaac\Music\musicas python\OutKast - Hey Ya! (Lyrics).mp3"

# Carregando e tocando a música
pygame.mixer.music.load(caminho)
pygame.mixer.music.play()

# Mantendo o programa rodando enquanto a música toca
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Parando a música e finalizando o pygame
pygame.mixer.music.stop()
pygame.quit()
