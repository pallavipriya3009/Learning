__author__ = 'pallavipriya'

def func(anum):

    try:
        100/anum
    except ZeroDivisionError as e:
        print (e)
    except Exception as e:
        print(e)
    else:
        print ("the value is {}".format(100/anum))
    finally:
        print("this is done")

func(0)
#func(5)






