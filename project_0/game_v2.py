import numpy as np

def random_predict(number:int=1) -> int:
    '''
    Randomly guessing a number
    
    Args:
        number (int, optional): guessed number. Defaults to 1
    
    Returns:
        int: number of attempts
    '''
    
    count = 0
    left_border, right_border = 1, 101
    
    while True:
        count += 1
        predict_number = np.random.randint(left_border, right_border)  # Estimated number
        if predict_number < number:
            left_border = predict_number + 1  # Exclude predicted number
        elif predict_number > number:
            right_border = predict_number     # Exclude predicted number (by not adding 1)
        else:
            break  # End cycle if guessed succesfully
    return count

def score_game(random_predict:int) -> int:
    '''
    How many attempts in average does our algorithm need to predict 1000 numbers
    
    Args:
        random_predict (int): guess function
    
    Returns:
        int: average number of attempts
    '''
    
    count_ls = []  # List for saving the number of attempts
    np.random.seed(1)  # Fixing the seed for the result consistency
    random_array = np.random.randint(1, 101, size=1000)  # List of guessed numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    np.random.seed()  # Unfixing the seed in order to avoid side effects
    score = int(np.mean(count_ls))  # Average number of attempts
    
    print(f'Your algorithm guesses a number in {score} attempts on average.')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
