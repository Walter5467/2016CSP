def days():
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets "interactive on": figures redrawn when updated

def picks():
    a = [] # Makes an empty list
    
    a += [random.choice([1, 3, 10])]
    
    for choices in range(5):
        a += [random.choice([1, 3, 10])]
        
    plt.hist(a)
    plt.show()
    
def dice():
    import random
    value = [1,2,3,4,5,6]
    dice = [1,2,3,4,5,6]
    number = random.choice(dice)
    print 'Dice:',number 
    if number is 1:
        final = random.choice(value)
    if number is 2:
        final = random.choice(value) + random.choice(value)
    if number is 3:
        final = random.choice(value) + random.choice(value) + random.choice(value)
    if number is 4:
        final = random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value)
    if number is 5:
        final = random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value) 
    if number is 6:
        final = random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value) + random.choice(value)
    print 'Total:',final
    
def matches(ticket, winners):
    Total = 0
    if len(ticket) != 5:
        print 'You must have 5 guesses.'
    if len(winners) != 5:
        print 'You must have 5 winning numbers'
    if ticket[0] == winners[0]:
        Total = Total + 1
    if ticket[0] == winners[1]:
        Total = Total + 1
    if ticket[0] == winners[2]:
        Total = Total + 1
    if ticket[0] == winners[3]:
        Total = Total + 1
    if ticket[0] == winners[4]:
        Total = Total + 1
    if ticket[1] == winners[0]:
        Total = Total + 1 
    if ticket[1] == winners[1]:
        Total = Total + 1
    if ticket[1] == winners[2]:
        Total = Total + 1
    if ticket[1] == winners[3]:
        Total = Total + 1
    if ticket[1] == winners[4]:
        Total = Total + 1
    if ticket[2] == winners[0]:
        Total = Total + 1
    if ticket[2] == winners[1]:
        Total = Total + 1
    if ticket[2] == winners[2]:
        Total = Total + 1
    if ticket[2] == winners[3]:
        Total = Total + 1
    if ticket[2] == winners[4]:
        Total = Total + 1
    if ticket[3] == winners[0]:
        Total = Total + 1
    if ticket[3] == winners[1]:
        Total = Total + 1
    if ticket[3] == winners[2]:
        Total = Total + 1
    if ticket[3] == winners[3]:
        Total = Total + 1
    if ticket[3] == winners[4]:
        Total = Total + 1
    if ticket[4] == winners[0]:
        Total = Total + 1
    if ticket[4] == winners[1]:
        Total = Total + 1
    if ticket[4] == winners[2]:
        Total = Total + 1
    if ticket[4] == winners[3]:
        Total = Total + 1
    if ticket[4] == winners[4]:
        Total = Total + 1
    return Total
    
def lottery(tickets, winner):
    Total = 0
    for item in tickets:
        if item == item in winner:
            Total = Total + 1
    return Total
            
    