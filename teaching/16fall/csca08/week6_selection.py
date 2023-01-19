def test_ph(ph):
    if(ph < 7.0):
        if(ph > 5.0):
            return "Your water is acidic, but you're probably okay"
        else:
            if(ph < 2):
                return "RUN!"
            else:
                return "That's pretty acidic, I wouldn't drink it"
    else:
        if(ph > 7.0):
            if(ph > 11):
                return "RUN!"
            else:
                return "That's pretty basic stuff"
        else:
            return "Your water is neutral"


def test_ph_better(ph):
    # first deal with unrealistic ph levels
    if((ph > 11) or (ph < 2)):
        result = "RUN!"
    # deal with anything over 7
    elif(ph > 7):
        result = "That's pretty basic stuff"
    # deal with the case of it being exactly 7
    elif(ph == 7):
        result = "Your water is neutral"
    # deal with anything over five
    # (and since we're using an elif, we know that it's below 7 at this point)
    elif(ph > 5):
        result = "Your water is acidic, but you're probably okay"
    # deal with anything below five
    # (if we reached this point, we know that the ph is 5 or lower)
    else:
        result = "That's pretty acidic, I wouldn't drink it"
    return result
