class consoleGui:

    #   method that will create a choice dialog
    @staticmethod
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
    @staticmethod
    def openQuestion(question):
        return consoleGui.openQuestionChecked(question, None, None)

    # method that returns an int corresponding to a given answer
    @staticmethod
    def multipleChoice(question, *options):
        print("\n" + question)
        while True:
            # ask question and prepare for answers
            possibleAnswers = []
            for i, option in enumerate(options):

                # distill info
                newAns = option[0:1].upper()
                firstChar = option[1:2].upper()
                listOption = "[" + newAns + "]" + " " + firstChar + option[2:0]

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
    @staticmethod
    def getInt(self):
        pass

    # checks if there are no errors in answers
    @staticmethod
    def noErrorsInValues(self):
        pass


print(consoleGui.multipleChoice("here are some options!", "ab", "bc", "ca"))
