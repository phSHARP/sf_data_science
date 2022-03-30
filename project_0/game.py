import numpy as np

number = np.random.randint(1, 101)  # Guessing the number
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100:'))
    
    if predict_number > number:
        print('It must be lesser than that!')
    
    elif predict_number < number:
        print('It must be greater than that!')
    
    else:
        print(f'You did it! The number is {number}, guessed for {count} tries.')
        break  # End of the game
