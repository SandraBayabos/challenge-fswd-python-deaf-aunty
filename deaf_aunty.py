speak = input('Speak to aunty: ')


def talk_to_aunty(speak):
    if(speak == 'I love you aunty, I have to go now'):
        return(print('ok. Goodbye'))
    if(speak == speak.upper()):
        return(print('YOU ARE VERY RUDE!'))
    elif(speak == speak.lower()):
        return(print('WHAT? SPEAK UP!'))
    else:  # (both upper and lower)
        return(print('SHOW SOME RESPECT!'))


talk_to_aunty(speak)
