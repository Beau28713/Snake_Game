import pygame

def window(width, height, window_text):
    size = width, height

    main_window = pygame.display.set_mode(size)
    pygame.display.set_caption(window_text)


    return main_window