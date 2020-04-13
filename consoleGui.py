from abc import ABC, abstractmethod

#   method that will create a choice dialog
def openQuestionChecked(question, checks=None, negativeResponse=None):

    output = ""

    #   base output if no checks or negative response are needed
    if checks is None and negativeResponse is None:
        #   just return answer
        print("\n" + question)
        output = input()
        return output

    #   interpret question when checks are given
    else:
        #   Keep asking the same question until checks are met or user exits
        print("\n" + question)
        print("type exit if you don't know")
        while True:
            output = input()

            #   escape if satisfactory answer is unknown
            if output == "exit":
                return "ERROR"

            #   loop through the checks
            satisfactory = True
            for check in checks:
                if check not in output:
                    satisfactory = False

            # act based on the outcome of these checks
            if satisfactory:
                return output
            elif negativeResponse is not None:
                print("\n" + negativeResponse)
                print("Try again or type exit if you don't know")
            else:
                print("\nThat's not right, try again or type exit if you don't know")

#   shorthand way of coding above question
def openQuestion(question):
    return openQuestionChecked(question, None, None)

# method that returns an int corresponding to a given answer
def multipleChoice(question, *inp_options):

    # failsafe for elementByMultiplechoice
    options = list()
    if type(inp_options[0]) is list:
        for e in inp_options[0]:
            options.append(e)
    else:
        options = inp_options

    print("\n" + question)
    while True:
        # ask question and prepare for answers
        possibleAnswers = []
        for i, option in enumerate(options):

            # count how many numeral chars are in this possible answer to account for inputs beginning with numbers
            lengthOfExpectedUserInput = 1
            for j in range(len(option)):
                if not option[j].isdigit():
                    break
                elif j+1 > lengthOfExpectedUserInput:
                    lengthOfExpectedUserInput = j+1


            # distill info
            newAns = option[0:lengthOfExpectedUserInput].upper()
            firstChar = option[lengthOfExpectedUserInput:lengthOfExpectedUserInput+1].upper()
            listOption = "[" + newAns + "]" + " " + firstChar + option[lengthOfExpectedUserInput+1:len(option)]

            # list options and save answer
            possibleAnswers.append(newAns)
            print(listOption)

        # add exit for escape
        print("[X] Exit\n")

        # get answer
        ans = input().upper()

        # check answer
        if ans == "X":
            return -1
        else:
            for i in range(len(possibleAnswers)):
                if ans == possibleAnswers[i]:
                    return i
        print("that's not an option, type \"X\" if you don't know")

# method that returns an int based on a question
def getInt(question):
    print(question)
    while True:
        ans = input()
        output = 0
        if ans == "exit":
            return -1
        try:
            return int(ans)
        except:
            print("that is not a valid answer, try again or type exit to exit")

# checks if there are no errors in answers #TODO write method
def noErrorsInValues(self):
    pass

class Element(ABC):

    def list(self):
        pass

    def getMPQlisting(self):
        pass

def getElementByMultipleChoice(question, input):
    # print(type(input))
    if type(input) is list:
        answers = list()
        for i in range(len(input)):
            answers.append(str(i) + str(input[i].getMPQlisting()))
        multipleChoice(question, answers)
    elif type(input) is dict:
        return getElementByMultipleChoice(question, list(input.values()))
    else:
        print("ERROR: not a valid iterable for multiplechoice")




