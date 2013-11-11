def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = len(secretWord)
    #print count
    while count > 0:
        if secretWord[count-1] not in lettersGuessed:
            return False
        count -= 1
    return True