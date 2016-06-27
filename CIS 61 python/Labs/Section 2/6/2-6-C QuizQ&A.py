from pprint import pprint

class Questions:
    def __init__(self, question):
        self.Question = question
    def print(self):
        print("Answer", self.Question)
        
class Answers:
    def __init__(self, answer):
        self.Answer = answer
    def print(self):
        print("Answer", self.Answer)
        
class Quiz:
    def __init__(self, quizNumber, questions, answers):
        self.QuizNumber = quizNumber
        self.Questions = questions
        self.Answers = answers
    def print(self):
        print("Quiz Number", self.QuizNumber)
    def print(self):
        print("Questions", self.Questions.Question)
    def print(self):
        print("Answers", self.Answers.Answer)

class Quizzes:
    def __init__(self):
        self.QuizList = []
    def AddQuiz(self, quiz):
        self.QuizList.append(quiz)
        print(quiz.QuizNumber)
        print(quiz.Questions.Question)
        print(quiz.Answers.Answer)
    def printQuizzes(self, quiz):

        i = 0
        while i < 2:
            print("\n", self.QuizList[i])
            i += 1

            

Qs1 = Questions("?, ?, ?")
As1 = Answers("True,False,True")
Q1 = Quiz("1", Qs1, As1)
Qs = Quizzes()
Qs.AddQuiz(Q1)

Qs2 = Questions("?, ?, ?")
As2 = Answers("True,True,True")
Q2 = Quiz("2", Qs2, As2)
Qs.AddQuiz(Q2)

Qs.printQuizzes(Q1)

