class car:
    color=""
    model = 0
    def __init__ (self , color , model):

        self.color = color
        self.model = model

   # def setColor(self , color):
       # self.color = color
       # print(self.color)


car1 = car("black" , 1998)
car2 = car("white" , 2019)

print(car1.color)