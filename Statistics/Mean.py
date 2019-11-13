def mean(a, b, length):
    try:
       a = int(a)
       b = int(b)
       length = int(length)
       result = (a + b) / length
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")
