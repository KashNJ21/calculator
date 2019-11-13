from Statistics.Mean import mean

def variance(a, b, c):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       array = [a,b,c]
       sum = 0
       for i in range(len(array)):
           sum += (array[i] - mean(a,b,c,3)) ** 2
       result = sum / len(array)
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")