"""

input collection module
version 0.1
designed for a purpose

date created: 25/2/2022

"""


class Input:  # made to avoid the tiresome input collection process
    def __init__(self, text_tp_print='', caps=0):
        self.text = text_tp_print
        self.doo = input(f"{self.text}")
        self.caps = caps

    def out(self):
        if self.caps == 1:
            return self.doo.lower()
        elif self.caps == 2:
            return self.doo.upper()
        else:
            return self.doo
# all is tested and finalized, just import and use when ever you need it,
# thanking not needed
