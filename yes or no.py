"""

the interrogation module
Version 0.1
designed for a purpose

date created: 22/2/2022
"""

class Ask:
    yeses = ['yes', 'y']
    nos = ['no', 'n']

    def __init__(self, question, loop=None):  # question input
        self.q = question

    def askIT(self):
        self.ans = input(f'{self.q}  (y/n)  ')
        self.ans.lower()
        if self.ans in self.yeses:  # yes check
            return True
        elif self.ans in self.nos:  # no check
            return False
        else:  # loops if the input is neither
            if loop is None:
                print("y/n please")
                return self.askIT()


'''no need for this kind of crap, you can use the class itself
and its methods to complete such actions like the second one, below'''
# # val = Ask("are you a tomato?")
# # if val.askIT() == True:
# #     print(1)
# # elif val.askIT() == False:
# #     print(2)
#
# if Ask('are you a potato?').askIT() == True:
#     print(1)



"""

the interrogation module
Version 0.1.1 
designed for a purpose

date created: 25/2/2022

"""

class Ask:
    yeses = ['yes', 'y']
    nos = ['no', 'n']

    def __init__(self, question, option="y/n",loopingFinal='Please' ,loop=None):  # question input
        self.q = question
        self.looper = loopingFinal
    def askIT(self):
        self.ans = input(f'{self.q}  {self.option}  ') # not only yes or no, the user can specify shit
        self.ans.lower()
        if self.ans in self.yeses:  # yes check
            return True
        elif self.ans in self.nos:  # no check
            return False
        else:  # loops if the input is neither
            if loop is None:
                print(f"{self.option} {self.looper}")
                return self.askIT()