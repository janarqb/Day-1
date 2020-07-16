def bigger_guy(num1, num2):
    if num1 > num2:
     return num1
    else:
     return num2 
def biggest_guy (num1, num2, num3):
    return bigger_guy(bigger_guy(num1, num2), num3)
 

def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('num1', 'num1', 'num2') == 'num2' # 'num2' is greater than 'num1'
  except (AssertionError) as e:
    print(e)
print("Wrong!!")
print("Correct buddy!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()


