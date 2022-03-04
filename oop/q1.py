class cylinder:
    def __init__(self,height,base,readius):
        self.height = height
        self.base = base
        self.radius = radius
    def getvolume(self):
        volume = 3.14*self.radius*self.radius*self.height
        return volume
    def getsurfacearea(self):
        surfacearea = 3.14*2*self.radius*(self.radius+self.height)
        return surfacearea
    def getbasearea(self):
        basearea = 3.14*self.radius*self.base*self.height
        return basearea
    def getlateralsurfaceraea(self):
        lateral = 2*3.14*self.radius*self.base *self.height
        return lateral

height = int(input("enter height"))
base = int(input("enter base"))
radius = int(input("enter radius"))
c1 = cylinder(height,base,radius)
print("Volume of cylinder is",c1.getvolume())
print("Surface area of cylinder is",c1.getsurfacearea())
print("base area of cylinder is",c1.getbasearea())
print("lateral surfacea of cylinder is",c1.getlateralsurfaceraea())