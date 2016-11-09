def add_tip(total, tip_percent):
    '''Return the total amount including tip
    '''
    tip = tip_percent*total
    return total + tip


def hyp(leg1, leg2):
    hyp = ((leg1**2)+(leg2**2)**0.5)
    return hyp
    print hyp
    
def mean(a, b, c):
    mean = ((a + b + c) / 3)
    return mean
    print mean
    
def perimeter(base, height):
    perimeter = (base*2) + (height*2)
    return perimeter
    print perimeter
    
def quad(a, b, c):
    quad = -(b) + ((b**2) - (4*(a*c)**2)**0.5)/(2*a)
    return quad
    print quad



    


    
