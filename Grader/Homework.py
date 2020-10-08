
class Homework:


    def __init__(self):
        pass

    def parseAnswers(self, answerFile):
        tempArray = []
        for ans in answerFile:
            tempArray.append(ans)
        return tempArray

    def parseHints(self, hintFile):
        #return a dictionaryor list or something
        pass

    def submit(self, guess, qNum, studentID):
        pass

    def getHint(self, hintNum):
        #lessen hintNum to highest possible hint value
        pass

