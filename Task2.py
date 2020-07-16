def square_number (number): 
    return number ** 2

def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")
#test your code by un-commneting the line(s) below
test_square_number()