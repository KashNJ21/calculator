def median(a, b, c):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       input_data = [a,b,c]
       array_sorted = sorted(input_data)
       if len(input_data) % 2 == 1:
           result = array_sorted[int(((len(input_data) + 1) / 2) - 1)]
       else:
           result = (array_sorted[int(((len(input_data) + 1) / 2) - 1)] + array_sorted[int(((len(input_data) + 1) / 2))]) / 2.0
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")