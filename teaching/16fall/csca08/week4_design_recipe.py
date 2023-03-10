def student_data(name, age, student_num, in_a08):
    """
    (str, int, str, bool) -> str
    Given a student's name, age, student number, and enrolment status,
    function will return a string representation of their data, in the order
    of student number, name, age and enrolment status.
    REQ: age >= 0
    >>> student_data("Brian",35,"1234567",False)
    '<1234567,Brian,35,False>'
    >>> student_data("Nick",97,"0000001",True)
    '<0000001,Nick,97,True>'
    >>> student_data("Jana", 18, "1234567", False)
    '<1234567,Jana,18,False>'
    """
    ## internal comments and code
    ## remember: comment first, code after
    # create a string to return
    data = "<"
    # add the compenents of the data in the order of number, name , age, status
    # add the first component to the data, student number
    data += student_num + ","
    # add the name to the data
    data += name + ","
    # typecast the age and add it to the data
    age = str(age)
    data += age + ","
    ## notice how the two lines above are "covered" by the comment above
    # typecast the enrolment status and add it to the data
    ## notice below, we did the same thing in one line (it's all the same)
    data += str(in_a08) + ">"
    # return the data
    return data

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
