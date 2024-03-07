class Time:
    def __init__(self, h, m):
        self.hour = h
        self.min = m

    def __add__(self,other):
        if isinstance(other,type(self)):
            return Time(self.hour+other.hour,self.min+other.min)
        elif isinstance(other,type(3)):
            return Time(self.hour+other,self.min)
        else:
            return None
    
    def __le__(self, other):
        return self.min <= other.min if self.hour == other.hour else self.hour < other.hour
    
    def __str__(self):
        return f"Time: {self.hour}:{self.min}"
    

t1 = Time(10,30)
t2 = Time(5,20)
t3 = Time(5,10)
# print(t2<=t1)
# print(t2<=t3)
# print(t1+5)
# print(t1+t2)


