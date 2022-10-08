class MedianFinder(object):

    def __init__(self):
        self.lst = []
        
    def add_num(self, number: int):
        self.lst.append(number)
        self.lst.sort()

    def find_median(self) -> float:
        med = len(self.lst)//2
        if(len(self.lst) % 2 == 0):
            a = round((self.lst[med-1] + self.lst[med]) / 2, 5)
        else:
            a = round(self.lst[med],5)
        return a
            
             



x = MedianFinder()
x.add_num(1)
print(x.find_median())
x.add_num(10)
x.add_num(6.333)
print(x.find_median())
x.add_num(3)
print(x.find_median())