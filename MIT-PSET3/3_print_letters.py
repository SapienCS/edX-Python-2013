def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = [x for x in string.ascii_lowercase if x not in lettersGuessed]
    return ''.join(available)