# Thayer Yang
# 30 SEP 2024
# Simple If Statements Practice

# Task 1

superheroes = {'Ironman', 'Spiderman', "Captain America", "Wolverine", "Deadpool","Hawkeye"}

fav_superhero = 'Spiderman'

if fav_superhero in superheroes:
    print('Your favorite superhero '+fav_superhero+' is in the list.')
else:
    print('Your favorite superhero '+fav_superhero+' is not in the list.')


# Task 2

quiz_score = 92

if quiz_score >=85:
    print('You\'ve earn a B')
else:
    print('You got lower than a B')

# Task 3

quote = 'May the force be with you.'

if quote.startswith('M'):
    print("Quote starts with \"M\".")
else:
    print("Quote does not start with \"M\".")

# Task 4
    
filename = "thisisanimage.png"

if filename.endswith('.png'):
    print('Filename does end in ".png".')
else:
    print('Filename does not end in ".png".')

# Task 5
    
is_registered = False

if is_registered == False:
    print('You are not registered for classes at NMC.')
else:
    print('You are registered for classes at NMC.')


