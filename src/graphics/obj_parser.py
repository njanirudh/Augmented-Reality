import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import cv2
from threaded_webcam import WebcamVideoStream
import Image

webcam = WebcamVideoStream().start()

def wall(image):
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

def main():
    pygame.init()
    pygame.display.set_mode((600,600), DOUBLEBUF|OPENGL)

    img = pygame.image.load('/home/anirudh/NJ/Github/Augmented-Reality/assets/stones.jpg')
    textureData = pygame.image.tostring(img, "RGB", 1)
    width = img.get_width()
    height = img.get_height()

    im = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, im)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    glEnable(GL_TEXTURE_2D)

    GLMainLoop(img)

def GLMainLoop(im):


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # convert image to OpenGL texture format
        #tx_image = cv2.flip(webcam.read(), 0)
        tx_image = webcam.read()

        tx_image = Image.fromarray(tx_image)
        ix = tx_image.size[0]
        iy = tx_image.size[1]
        tx_image = tx_image.tobytes('raw', 'BGRX', 0, -1)

        # create texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, tx_image)

        glLoadIdentity()
        gluPerspective(45, 1, 0.05, 100)
        glTranslatef(0, 0, -5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        wall(im)

        pygame.display.flip()
        pygame.time.wait(50)

main()

