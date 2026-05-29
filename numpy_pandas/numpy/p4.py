import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

def my_function():
    # stmts
    try:
        print(array3[1][3]) # IndexError
        print(array5[4]) # NameError
        print(array1[0][0]) # SyntaxError array1 is not 2D array
        print(array2[2][0]) # IndexError
        print(array2[1][0]) # IndexError
    except IndexError:
        print(f'You tried to access an element from 4th row. But there are only 3 rows available in te array')
    except:
        print('Some error occured. Sorry for the inconvinience')
    finally:
        pass
    try:
        print('After the except block')
    except:
        pass
# try  except  raise/throw  throws  finally 