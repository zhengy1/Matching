class Comparsion:

    def __init__(self):
        self.Scores_Dis={"Age":10,"Grow_Loc":10,"Work_Loc":30,"Degree":10,"Apparance":20,"Salary_Rate":20}

    def Simple_Compare(self,P1,P2):
        
        self.P1 = P1
        self.P2 = P2
        score=0
        if abs(int(P1.age)-int(P2.age))<3:
            score=self.Scores_Dis["Age"]*1+score
        else:
            score=self.Scores_Dis["Age"]*0.5+score
        # print score

        if P1.Grow_Loc==P2.Grow_Loc:
            score=self.Scores_Dis["Grow_Loc"]*1+score
        else:
            score=self.Scores_Dis["Grow_Loc"]*0.5+score
        # print score

        if P1.Work_Loc==P2.Work_Loc:
            score=self.Scores_Dis["Work_Loc"]*1+score
        else:
            score=self.Scores_Dis["Work_Loc"]*0.5+score
        # print score

        if P1.Degree==P2.Degree:
            score=self.Scores_Dis["Degree"]*1+score
        else:
            score=self.Scores_Dis["Degree"]*0.5+score
        # print score

        if P1.Apparance==P2.Apparance:
            score=self.Scores_Dis["Apparance"]*1+score
        else:
            score=self.Scores_Dis["Apparance"]*0.5+score
        # print score

        if P1.Salary_Rate==P2.Salary_Rate:
            score=self.Scores_Dis["Salary_Rate"]*1+score
        else:
            score=self.Scores_Dis["Salary_Rate"]*0.5+score        
        self.score = score

    def print_score(self):
        # print self.score
        print "It Seems like "+self.P1.name+" and "+self.P2.name+" has "+str(self.score)+"% probability to match"