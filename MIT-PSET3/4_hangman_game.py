def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %d letters long.' % len(secretWord)
    guess_count = 8
    lettersGuessed = []
    while guess_count > 0:
        print '-----------'
        if isWordGuessed(secretWord, lettersGuessed):
            print 'Congratulations, you won!'
            return
        print 'You have %d guesses left' % guess_count
        print 'Available Letters:', getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print 'Good guess: ', getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
            guess_count -= 1
    print '-----------'
    print 'Sorry, you ran out of guesses. The word was', secretWord + '.'

