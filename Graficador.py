# El que funciona como graficador
from IA import Renderer, V2

width = 820
height = 880

rend = Renderer(width, height)


# ________________________________________________
#  Comienzan las poligonos


primero = [(165, 380),(185, 360),(180, 330),(207, 345),(233, 330),(230, 360),(250, 380),(220, 385),(205, 410),(193, 383)]
rend.glColor(0,0,1)
rend.glFill(primero)



segundo = [(321, 335),(288, 286),(339, 251),(374, 302)]
rend.glColor(1,0,1)
rend.glFill(segundo)



tercero = [(377, 249),(411, 197),(436, 249)]
rend.glColor(1,1,1)
rend.glFill(tercero)




cuarto = [(413, 177),(448, 159),(502, 88),(553, 53),(535, 36),(676, 37),(660, 52),
(750, 145),(761, 179),(672, 192),(659, 214),(615, 214),(632, 230),(580, 230),
(597, 215),(552, 214),(517, 144),(466, 180)]
rend.glColor(0,1,1)
rend.glFill(cuarto)




quinto = [(321, 335),(288, 286),(339, 251),(374, 302)]
rend.glColor(1,0,0)
rend.glFill(quinto)


rend.glFinished("Lab01.bmp")