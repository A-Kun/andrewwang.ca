def student_data(name, age, stu_id, is_enrol):
    '''(str, int, str, bool) -> str
    Given a student's name, age, student number, and enrolment status, function will return a string representation of their data, in the order of student number, name, age and enrolment status.
    REQ: age >= 0
    
    >>> student_data('Brian', 45, '666666', True)
    '<666666,Brian,45,True>'
    >>> student_data('Marzieh', 45, '000000', True)
    '<000000,Marzieh,45,True>'
    >>> student_data('Louis', 40, '010101', False)
    '<010101,Louis,40,False>'
    '''
    # create a string to return, starting with <
    data = '<'
    # add the first component to the data, student number
    data += stu_id + ','
    # add the name to the data
    data += name + ','
    # data = data + name + ','
    # cast age to str then add the age to the data
    data += str(age) + ','
    # cast enrolment to str then add enrolment status to the data
    data += str(is_enrol) + '>'
    # return the data
    return data


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
