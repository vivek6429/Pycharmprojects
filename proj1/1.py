# user_input=int(input("enter the value :"))
# sum=0
# for i in range(1,user_input+1):
#     sum=sum+i**2
# print("The sum is :",sum)

class Student():
    name = ""
    yearofstudy = 0
    number_of_subjects = 0
    mark_list = []
    total = 0
    passval=60 # marks input is in 100s  average value must be greater than this

    def __init__(self, name, cls, subjectno):
        self.name = name
        self.yearofstudy = cls
        self.number_of_subjects
        self.number_of_subjects=subjectno

    def readMarks(self):
        for i in range(1, self.number_of_subjects + 1):
            inp = int(input("enter the mark of subject " + str(i) + "in 100 :") or "0")
            self.mark_list.append(inp)

    def calculateMarks(self):
        for i in self.mark_list:
            self.total += i
        self.avg = self.total / len(self.mark_list)

    def printMarks(self):
        print("Total=", self.total)
        print("Average=", self.avg)
        if self.avg > self.passval:
            print(" Student passed")
        else:
            print("Student failed")
