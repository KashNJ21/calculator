from Statistics.Mean import mean
from Statistics.Std_dev import std_dev
def corr_coef(a, b, c, d, e, f):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        scorex = []
        scorey = []
        x = [a,b,c]
        y = [d,e,f]
        for i in x:
            scorex.append((i - mean(a,b,c,3)) / std_dev(a,b,c))

        for j in y:
            scorey.append((j - mean(d,e,f,3)) / std_dev(d,e,f))
        result =(sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)
        return result
    except ZeroDivisionError:
        print("Error: Wrong number, not valid!!")
    except ValueError:
        print ("Error: Only Numeric Values are valid!!")