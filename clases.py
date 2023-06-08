class circle (object):
    def __init__(self,radio,color):
        self.radio = radio;
        self.color = color;
    def addradius(self,r):
        self.radio=self.radio+r

class rectangulo (object):
    def __init__(self,radio,color):
        self.radio = radio;
        self.color = color;

objeto = circle(5,"red")

print(objeto.radio)
objeto.addradius(5)
print(objeto.radio)