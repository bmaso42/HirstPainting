###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import colorgram
import turtle as t
import random

# color_list = colorgram.extract('image.jpg', 100)
# colors_rbg = []
#
# for i in color_list:
#     new_rbg = i.rgb
#     r = new_rbg[0]
#     b = new_rbg[1]
#     g = new_rbg[2]
#     rbg_tuple = (r, b, g)
#     colors_rbg.append(rbg_tuple)
#
# print(colors_rbg)

#CREATED COLOR LIST FROM EXTRACT, COMMENTED OUT NO LONGER NEEDED COLORGRAM CODE
color_list = ((202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                  (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                  (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                  (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                  (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
                  (254, 194, 0))
t.colormode(255)
tim = t.Turtle()
tim.penup()
# tim.setpos(-200, -200)
# tim.color(random.choice(color_list))
# tim.dot(20)
# tim.setpos(-150, -200)
# tim.dot(20)
# print(tim.pos())
origin = -250
i = 0
j = 0
for i in range(10):
    for j in range(10):
        tim.setpos(origin + j*50, origin + i*50)
        tim.color(random.choice(color_list))
        tim.dot(20)




sc = t.Screen()
sc.setup(1000, 1000,0, 0)
sc.exitonclick()