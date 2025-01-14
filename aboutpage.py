from pygame import mixer
import pygame
from pygame.locals import *
import sys
import pygame.freetype



pygame.init()

#title and icon

pygame.display.set_caption("Woods and Stones")
icon = pygame.image.load('gameico.ico')
pygame.display.set_icon(icon)

#background music
mixer.music.load('bgsound.mp3')
mixer.music.play(-1) #enabeling looping




def aboutPage():
    (w, h) = (800, 800)



    pygame.freetype.init()

    # font for header
    #font_header = pygame.freetype.Font('/Users/sawamurahinako/Library/Fonts/meiryob.ttc', 80)
    font_header = pygame.freetype.Font('C:\Windows\Fonts\FORTE.TTF', 80)

    # font for text
    font1 = pygame.font.SysFont("comicsansms", 30)

    pygame.display.set_mode((w, h), 0, 32)

    screen = pygame.display.get_surface()

    text2 = font1.render("Play occurs on a 3 by 3 grid of 9 empty squares. ", True, (255, 255, 255))

    text3 = font1.render("Two players alternate placing their items alternately. ", True, (255, 255, 255))

    text4 = font1.render("Stone has to be placed first every time. ", True, (255, 255, 255))

    text5 = font1.render("One player place stone, the other wood. ", True, (255, 255, 255))

    text6 = font1.render("Repeat this three times.If one player places ", True, (255, 255, 255))

    text7 = font1.render("three of the same items in a line , that player wins.", True, (255, 255, 255))

    text8 = font1.render("If there is no winner, players can move their", True, (255, 255, 255))

    text9 = font1.render("stones or woods to the adjacent empty squares", True, (255, 255, 255))

    text10 = font1.render("alternately until the winner is decided.", True, (255, 255, 255))

    # button
    text_back_button = font1.render("Back", True, (255, 255, 255))
    back_button = pygame.Rect(10, 10, 100, 50)

    # background image
    bg = pygame.image.load("bgpic.png").convert_alpha()
    rect_bg = bg.get_rect()

    while (1):
        pygame.display.update()
        pygame.time.wait(100)
        screen.fill((0, 0, 0, 0))
        screen.blit(bg, rect_bg)

        pygame.draw.rect(screen, (191, 138, 23), Rect(0, 0, 800, 80))

        pygame.draw.rect(screen, (0, 80, 0), Rect(15, 100, 770, 150))

        pygame.draw.rect(screen, (0, 80, 0), Rect(15, 270, 770, 150))

        pygame.draw.rect(screen, (0, 80, 0), Rect(15, 440, 770, 150))

        # button
        pygame.draw.rect(screen, (0, 150, 0), back_button)
        screen.blit(text_back_button, (25, 15))

        # Header "About"
        font_header.render_to(screen, (250, 10), 'About', (255, 255, 255, 250))

        screen.blit(text2, (30, 110))

        screen.blit(text3, (30, 150))

        screen.blit(text4, (30, 190))

        screen.blit(text5, (30, 280))

        screen.blit(text6, (30, 320))

        screen.blit(text7, (30, 360))

        screen.blit(text８, (30, 450))

        screen.blit(text９, (30, 490))

        screen.blit(text10, (30, 530))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    print("Back button was pressed")
                    import frontpage
                    frontpage.main_menu()



if __name__ == "__main__":
    aboutPage()

