import pygame


FONT_FAMILY= "impact"
FONT_COLOR_BLACK= (0, 0, 0)

def get_score_element(points):
    font= pygame.font.SysFont(FONT_FAMILY, 50)
 
    text= font.render("SCORE: " + str(points), True, FONT_COLOR_BLACK)
    text_rect= text.get_rect()
    text_rect.center= (950,50)
    return text, text_rect

def get_text_element(text_to_display, width, height):
    font= pygame.font.SysFont(FONT_FAMILY, 50)

    text= font.render(text_to_display,True, FONT_COLOR_BLACK)
    text_rect= text.get_rect()
    text_rect.center= (width,height)
    return text, text_rect
