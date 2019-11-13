def mode(a, b, c, d):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       d = int(d)
       array = [a,b,c,d]
       most = max(list(map(array.count, array)))
       result = list(set(filter(lambda x: array.count(x) == most, array)))
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")