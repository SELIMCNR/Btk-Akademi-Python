#Question soru klası 

class Question:
    def __init__(self,text,choices,answer):
        self.text = text 
        self.choices=choices
        self.answer = answer 

    def checkAnswer(self,answer): #soru cevabı doğrumu
        return self.answer == answer
    


# Quiz klası 
class Quiz:
    def __init__(self,questions):
        self.quesitons = questions
        self.score=0
        self.quesitonsIndex = 0 
        
    def getQuestion(self):
        return self.quesitons[self.quesitonsIndex]
        
    def displayQuestion(self):
        question = self.getQuestion()    
        print(f"Soru {self.quesitonsIndex + 1 }: {question.text} ")
        
        for q in question.choices:
            print('-'+q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
           self.score +=1      
        
        self.quesitonsIndex +=1
        
    def loadQuestion(self):
        if len(self.quesitons) == self.quesitonsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    
    def showScore(self):
        print("score: ",self.score)
          
    def displayProgress(self):
        totalQuestion = len(self.quesitons)
        questionNumber = self.quesitonsIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionNumber} of {totalQuestion} '.center(100,'*')) 
                
    
        
q1 = Question('En iyi programlama dili hangisidir ?',['C#','Javascript','Java'],'Python')
q2 = Question('En popüler programlama dili hangisidir ?',['C#','Javascript','Java'],'Python')
q3 = Question('En çok kazandıran programlama dili hangisidir ?',['C#','Javascript','Java'],'Python')
q4 = Question('En kolay programlama dili hangisidir ?',['C#','Javascript','Java'],'Python')
q5 = Question('En  sevilen programlama dili hangisidir ?',['C#','Javascript','Java'],'Python')
Questions = [q1,q2,q3,q4,q5]

quiz = Quiz(Questions)

quiz.loadQuestion()
        
        