__author__ = 'pallavipriya'

class userDefinedException(Exception):

    def __init__(self,balance,amount):

        self.balance = balance
        self.amount = amount


    def leftAmount(self):
        return self.amount-self.balance



try:
    raise userDefinedException(100,50)
except userDefinedException as e:
    print("I am sorry, your balance is less by{}".format(e.leftAmount()))


