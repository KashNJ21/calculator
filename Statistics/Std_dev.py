from Statistics.Population_Variance import variance

def std_dev(a, b, c):
    try:
       a = int(a)
       b = int(b)
       c = int(c)
       array = [a,b,c]
       result = variance(a,b,c) ** (1 / 2)
       return result
    except ZeroDivisionError:
        print("Error: Invalid input")
    except ValueError:
        print ("Error: Please enter a number")