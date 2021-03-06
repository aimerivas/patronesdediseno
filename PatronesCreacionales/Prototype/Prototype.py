#Ruiz Lea German                       8/09/17
#Patrones De Diseño                    Instituto Tecnologico de Tijuana
#Patrones Creacionales                 MAE Rene Solis Reyes

class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, name, obj):
        
        self._objs[name] = obj

    def unregisterObject(self, name):
        del self._objs[name]

    def clone(self, name, **attr):
        obj = deepcopy(self._objs[name])
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    class A:
        pass 

    a = A()
    prototype = Prototype()
    prototype.registerObject("a", a)
    b = prototype.clone("a", a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)