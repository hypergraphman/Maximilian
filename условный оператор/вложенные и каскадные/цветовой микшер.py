RED = 'Красный'
BLUE = 'Синий'
YELLOW = 'Жёлтый'
VIOLET = 'Фиолетовый'
ORANGE = 'Оранжевый'
GREEN = 'Зелёный'
ERROR = 'ошибка'

color_1 = input()
color_2 = input()
if (color_1 == RED and color_2 == BLUE or
   color_2 == RED and color_1 == BLUE):
    print(VIOLET)
elif (color_1 == RED and color_2 == YELLOW or
     color_2 == RED and color_1 == YELLOW):
    print(ORANGE)
elif (color_1 == BLUE and color_2 == YELLOW or
     color_2 == BLUE and color_1 == YELLOW):
    print(GREEN)
elif color_1 == RED and color_2 == RED:
    print(RED)
else:
    print(ERROR)
