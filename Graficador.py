# El que funciona como graficador
from IA import Renderer, V2

width = 820
height = 880

rend = Renderer(width, height)


# ________________________________________________
#  Comienzan las poligonos


primero = [(165, 380),(185, 360),(180, 330),(207, 345),(233, 330),(230, 360),(250, 380),(220, 385),(205, 410),(193, 383)]
rend.glDraw(primero)

# 1.     
rend.glLine(V2(165, 380), V2(185, 360))
rend.glLine(V2(180, 330), V2(207, 345))
rend.glLine(V2(233, 330), V2(230, 360))
rend.glLine(V2(250, 380), V2(220, 385))
rend.glLine(V2(205, 410), V2(193, 383))


# 2.     
rend.glLine(V2(321, 335), V2(288, 286))
rend.glLine(V2(339, 251), V2(374, 302))



# 3.           
rend.glLine(V2(377, 249), V2(411, 197))


# 4.      
rend.glLine(V2(413, 177), V2(448, 159))
rend.glLine(V2(502, 88), V2(553, 53))
rend.glLine(V2(535, 36), V2(676, 37))
rend.glLine(V2(659, 214), V2(615, 214))
rend.glLine(V2(632, 230), V2(580, 230))
rend.glLine(V2(597, 215), V2 (552, 214))
rend.glLine(V2(517, 144), V2(466, 180))


# 5.           
rend.glLine(V2(682, 175), V2(708, 120))
rend.glLine(V2(735, 148), V2 (739, 170))



rend.glFinished("Lab01.bmp")