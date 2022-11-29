"""

input collection module
version 0.1
designed for a purpose

date created: 25/2/2022

"""


class Input:  # made to avoid the tiresome input collection process
    def __init__(self, text_to_print='', caps=0):
        self.text = text_to_print
        self.doo = input(f"{self.text}")
        self.caps = caps

    def out(self):
        if self.caps == 1:
            return self.doo.lower()
        elif self.caps == 2:
            return self.doo.upper()
        else:
            return self.doo


"""

the interrogation module
Version 0.1.1 
designed for a purpose

date created: 25/2/2022

"""


class Ask:
    yeses = ['yes', 'y']
    nos = ['no', 'n']

    def __init__(self, question, option="y/n", loopingFinal='Please', loop=None):  # question input
        self.q = question
        self.loop = loop
        self.looper = loopingFinal
        self.option = option

    def askIT(self):
        self.ans = input(f'{self.q}  {self.option}  ')  # not only yes or no, the user can specify shit, V - 0.1.1
        self.ans.lower()
        if self.ans in self.yeses:  # yes check
            return True
        elif self.ans in self.nos:  # no check
            return False
        else:  # loops if the input is neither
            if self.loop is None:
                print(f"{self.option} {self.looper}")
                return self.askIT()
