# write a class of fractions and functions: addition, subtraction, multiplication and division
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __cmp__(self, arg):
        if self > arg:
            return -1
        elif self == arg:
            return 0
        else:
            return 1

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def Add(self, other):
      new_num_a = self.num * other.den + \
                self.den * other.num
      new_den_a = self.den * other.den
      common_a = gcd(new_num_a, new_den_a)
      return Fraction(new_num_a//common_a, new_den_a//common_a)

    def Sub(self, other):
      new_num_s = self.num * other.den - \
                self.den * other.num
      new_den_s = self.den * other.den
      common_s = gcd(new_num_s, new_den_s)
      return Fraction(new_num_s//common_s, new_den_s//common_s)
    
    def Mul(self, other):
      new_num_m = self.num * other.num 
      new_den_m = self.den * other.den
      common_m = gcd(new_num_m, new_den_m)
      return Fraction(new_num_m//common_m, new_den_m//common_m)
     

    def Div(self, other):
      new_num_d = other.den * self.num 
      new_den_d = self.den * other.num
      common_d = gcd(new_num_d, new_den_d)
      return Fraction(new_num_d//common_d, new_den_d//common_d)

myf_1 = Fraction(4, 5)
myf_2 = Fraction(3, 7)
f3 = Fraction.Add(myf_1, myf_2)
f4 = Fraction.Sub(myf_1, myf_2)
f5 = Fraction.Mul(myf_1, myf_2)
f6 = Fraction.Div(myf_1, myf_2)

print('First fraction: ')
myf_1.show()
print('Second fraction: ')
myf_2.show()
print(myf_1, '+', myf_2, '=', f3)
print(myf_1, '-', myf_2, '=', f4)
print(myf_1, '*', myf_2, '=', f5)
print(myf_1, ':', myf_2, '=', f6)
