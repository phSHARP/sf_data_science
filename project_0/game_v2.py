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
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # Estimated number
        if number == predict_number:
            break  # End cycle if guessed succesfully
    return(count)

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
    random_array = np.random.randint(1, 101, size=(1000))  # List of guessed numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))  # Average number of attempts
    
    print(f'Your algorithm guesses a number in {score} attempts on average.')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)