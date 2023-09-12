from pygame import*
from random import randint


class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_y = size_y
        self.size_x = size_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y




class muro(sprite.Sprite):
    def __init__(self, width, height,pared_x, pared_y, color1= 0, color2=0, color3= 0):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image = ((self.color1, self.color2, self.color3))
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = pared_x
        self.rect.y = pared_y

    def dib_wall(self):
        draw.rect(window, (self.color1, self.color2, self.color3), (self.rect.x, self.rect.y, self.width, self.height))

class Balon(sprite.Sprite):
    def __init__(self, pelota_x, pelota_y, pelota_image, sizep_y, sizep_x):
        super().__init__()
        self.image = transform.scale(image.load(pelota_image), (sizep_x, sizep_y))
        self.size_y = sizep_y
        self.size_x = sizep_x
        self.rect = self.image.get_rect()
        self.rect.x = pelota_x
        self.rect.y = pelota_y


    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))




def gol():
    pass

def afuera():
    pass


a = 700
b = 350


window = display.set_mode((a,b))
stadium = transform.scale(image.load("ist.jpg"),(a,b))
muro1 = muro(75, 150, 25, 25, 10, 104, 39)
balon = Balon(20, 20, 100, 0,("ball.png"))


clock =time.Clock()
fps = 60
game = True
font.init()






L = 0 
P = 0



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    keys = key.get_pressed()


    if keys[K_SPACE]:
        P += 1
    L +=1
    if L == 1000:
        L == 0
    
        if P > 90:
            gol()
        else:
            afuera()




    
    font1 = font.SysFont("Arial", 40)
    Puntos = font1.render("Vas por<<< "+ str (P)+" >>>tienen que ser 40'!", True,(255,255,255))    
    Tiempo = font1.render("Te quedan<<< "+ str (L)+" >>>Segundos, Apurate!", True,(255,255,255))


    window.blit(stadium,(0,0))
    window.blit(Puntos,(100, 0))
    window.blit(Tiempo,(100, 310))
    dib_wall(muro1)
    Balon.reset()

    
    
    
    
    
    
    
    display.update()
    clock.tick(fps)