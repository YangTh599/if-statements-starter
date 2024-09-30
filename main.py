# Thayer Yang
# 30 SEP 2024
# Simple If Statements Practice

# Task 1

superheroes = {'Ironman', 'Spiderman', "Captain America", "Wolverine", "Deadpool","Hawkeye"}

fav_superhero = input('What is your favorite superhero?:\n')

if fav_superhero.title() in superheroes:
    print('Your favorite superhero '+fav_superhero.title()+' is in the list.')
else:
    print('Your favorite superhero '+fav_superhero.title()+' is not in the list.')

print()

# Task 2

quiz_score = int(input('Enter your integer quiz score:\n'))

if quiz_score >=85:
    print('You\'ve earn a B')
else:
    print('You got lower than a B')
print()

# Task 3

quote = input('Enter a quote:\n')

if quote.startswith('M'):
    print("Quote starts with \"M\".")
else:
    print("Quote does not start with \"M\".")

print()

# Task 4
    
filename = "thisisanimage.png"

if filename.endswith('.png'):
    print(f'Filename {filename} does end in ".png".')
else:
    print(f'Filename {filename} does not end in ".png".')

print()

# Task 5
    
is_registered = False

if not is_registered:
    print('You are not registered for classes at NMC.')
else:
    print('You are registered for classes at NMC.')


