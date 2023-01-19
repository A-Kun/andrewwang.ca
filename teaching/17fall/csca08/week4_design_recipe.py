def student_data(name, age, student_num, in_a08):
    '''(str, int, str, bool) -> str
    Given a student's name, age, student number, and enrolment status,
    function will return a string representation of their data, in the order
    of student number, name, age and enrolment status.
    REQ: age >= 0

    >>> student_data('Brian', 55, '9118765', False)
    '<9118765,Brian,55,False>'
    >>> student_data('Andrew', 35, '555555', True)
    '<555555,Andrew,35,True>'
    >>> student_data('Natalie', 95, '314159', False)
    '<314159,Natalie,95,False>'
    '''
    # create a string to return
    data = "<"
    # add the student number to the data
    data = data + student_num + ','
    # add the name to the data
    data += name + ','
    # typecast the age and add it to the data
    data += str(age) + ','
    # typecast the enrolment status and add it to the data
    data += str(in_a08) + '>'
    # return the data
    return data


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
