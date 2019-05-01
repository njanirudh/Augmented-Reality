import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    pygame.display.set_mode((600,600), DOUBLEBUF|OPENGL)
main()

img = pygame.image.load('/home/anirudh/NJ/Github/Augmented-Reality/assets/stones.jpg')
textureData = pygame.image.tostring(img, "RGB", 1)
width = img.get_width()
height = img.get_height()

im = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, im)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
glEnable(GL_TEXTURE_2D)

def wall():
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-4,-4,-16)
    glTexCoord2f(0,1)
    glVertex3f(-4,4,-16)
    glTexCoord2f(1,1)
    glVertex3f(4,4,-8)
    glTexCoord2f(1,0)
    glVertex3f(4,-4,-8)
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    glLoadIdentity()
    gluPerspective(45, 1, 0.05, 100)
    glTranslatef(0,0,-5)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    wall()

    pygame.display.flip()
    pygame.time.wait(50)