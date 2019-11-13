def mean(a, b, c, length):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       length = int(length)
       result = (a + b + c) / length
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")
