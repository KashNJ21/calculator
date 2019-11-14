from Statistics.Mean import mean
from Statistics.Std_dev import std_dev
def standardized_score(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        value = [a,b,c]
        result = (a-mean(a,b,c,3) ) / std_dev(a,b,c)
        return result
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")