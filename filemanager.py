"""
file management module
version 0.1
designed for a purpose

date created: 25/2/2022
"""

"""designed to reduce the chance of getting an error
i have made the with-open process and module and made it
an importable piece of code"""

class Sesame:

    def __init__(self, directory_OR_name_of_file):
        self.dir = directory_OR_name_of_file

    """making the files"""

    def newTxt(self, text):  # check
        self.text = text

        with open(self.dir, 'w') as file:
            file.write(self.text)
            return True

    def updateTxt(self, text):  # check
        self.text = text

        with open(self.dir, 'a') as file:
            file.write(self.text)
            print('transaction complete')

    """seeing the files"""

    def readTxt(self, ):  # check

        with open(self.dir, 'r') as file:
            self.read_txt = file.read()
            print(self.read_txt)

    def readTxtLine(self):  # check

        with open(self.dir, 'r') as file:
            self.line = file.readline()
            return self.line

    """out of order"""
    # # currently having an issue with the opener
    # # i know there is a way to open it without imoprting anthing
    # # infact i know there is away to open anyfile without
    # # importing anything, im searching for it, for now i will
    # # disable it
    # def seeImg(self ):
    #
    #     with open(self.dir, 'rb') as file:
    #         self.read_img = file
    #         return self.read_img
    ### the above claim was a confused one. i confused
    ### command line with python. i will put the nessecary outside modules

    """copying the files"""

    def copyNonTxt(self, directory_original=None, directory_the_new=None):
        # self.dirOrg = directory_original
        self.dirCopy = directory_the_new
        # if self.dirOrg == None:
        #     self.dirOrg = self.dir
        if self.dirCopy == None:
            self.dirCopy = f"-copy{self.dirOrg}"

        with open(self.dir, 'rb') as file:
            copier = file.read()
            with open(self.dirCopy, 'wb') as theCopy:
                theCopy = theCopy.write(copier)
                return True

    def copyTxt(self, directory_original=None, directory_the_new=None):
        # self.dirOrg = directory_original
        self.dirCopy = directory_the_new
        # if self.dirOrg is None:
        #     self.dirOrg = self.dir
        if self.dirCopy is None:
            self.dirCopy = f"{self.dirOrg}-copy.txt"

        with open(self.dir, 'r') as file:
            copier = file.read()
            with open(self.dirCopy, 'w') as theCopy:
                theCopy = theCopy.write(copier)
                return True

    def copy_x(self, directory_original=None, directory_the_new=None):
        self.dirOrg = directory_original
        self.dirCopy = directory_the_new
        if self.dirOrg is None:
            self.dirOrg = self.dir
        if self.dirCopy is None:
            self.dirCopy = f"{self.dirOrg}-copy.txt"

        with open(self.dir, 'rb') as file:
            copier = file.read()
            with open(self.dirCopy, 'wb') as theCopy:
                theCopy = theCopy.write(copier)
                return True

    def showcommands(self):
        print(
            "newTxt - for making new text files"
            "updateTxt - appending to a text file"
            "readTxt - reads a text file"
            "copyNonTxt - copies non text files"
            "copyTxt - copies text files"
            "copy_x - copies any form of file"
            ""
        )