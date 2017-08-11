# welcome to cindy game: THis is a game designed in a way to please a girl whose name is Wang Lao Ji @Copyright 08/09/2017
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

Scores_Dis={"Age":10,"Grow_Loc":10,"Work_Loc":30,"Degree":10,"Apparance":20,"Salary_Rate":20}

class Match_Condition:
    Grow_Loc=["杭州","温州","其他"]
    Work_Loc=["杭州","温州","硅谷","洛杉矶","温哥华"]
    Degree=["高中","大学","研究生","博士"]
    Apparance=["Bad","Average","Good"]
    Salary_Rate=["Low","Middle","High"]


def Aquire_Infor():
    infor=[]
    print "你的名字？: "
    infor.append(raw_input())
    print "你的年龄？: "
    infor.append(raw_input())
    print "请选择出生地？: "
    for n in range (0,len(Match_Condition.Grow_Loc)):
        print n,Match_Condition.Grow_Loc[n],
    infor.append(int(raw_input()))
    print "请选择工作地？: "
    for n in range (0,len(Match_Condition.Work_Loc)):
        print n,Match_Condition.Work_Loc[n],
    infor.append(int(raw_input()))
    print "请选择学历？: "
    for n in range (0,len(Match_Condition.Degree)):
        print n,Match_Condition.Degree[n],
    infor.append(int(raw_input()))
    print "给自己的外表打几分？: "
    for n in range (0,len(Match_Condition.Apparance)):
        print n,Match_Condition.Apparance[n],
    infor.append(int(raw_input()))
    print "收入水平？: "
    for n in range (0,len(Match_Condition.Salary_Rate)):
        print n,Match_Condition.Salary_Rate[n],
    infor.append(int(raw_input()))
    return infor

infor=Aquire_Infor()


class People:
    def __init__(self,name,age,Grow_Loc,Work_Loc,Degree,Apparance,Salary_Rate):
        self.name=name
        self.age=age
        self.Grow_Loc=Grow_Loc
        self.Work_Loc=Work_Loc
        self.Degree=Degree
        self.Apparance=Apparance
        self.Salary_Rate=Salary_Rate

P1=People(infor[0],infor[1],Match_Condition.Grow_Loc[infor[2]],Match_Condition.Work_Loc[infor[3]],
          Match_Condition.Degree[infor[4]],Match_Condition.Apparance[infor[5]],
          Match_Condition.Salary_Rate[infor[6]])


P2=People("Zach",27,Match_Condition.Grow_Loc[1],Match_Condition.Work_Loc[2],
          Match_Condition.Degree[2],Match_Condition.Apparance[2],
          Match_Condition.Salary_Rate[2])


def Comparation():
    score=0
    if abs(int(P1.age)-int(P2.age))<3:
        score=Scores_Dis["Age"]*1+score
    else:
        score=Scores_Dis["Age"]*0.5+score
    print score

    if P1.Grow_Loc==P2.Grow_Loc:
        score=Scores_Dis["Grow_Loc"]*1+score
    else:
        score=Scores_Dis["Grow_Loc"]*0.5+score
    print score

    if P1.Work_Loc==P2.Work_Loc:
        score=Scores_Dis["Work_Loc"]*1+score
    else:
        score=Scores_Dis["Work_Loc"]*0.5+score
    print score

    if P1.Degree==P2.Degree:
        score=Scores_Dis["Degree"]*1+score
    else:
        score=Scores_Dis["Degree"]*0.5+score
    print score

    if P1.Apparance==P2.Apparance:
        score=Scores_Dis["Apparance"]*1+score
    else:
        score=Scores_Dis["Apparance"]*0.5+score
    print score

    if P1.Salary_Rate==P2.Salary_Rate:
        score=Scores_Dis["Salary_Rate"]*1+score
    else:
        score=Scores_Dis["Salary_Rate"]*0.5+score
    return score


print "It Seems like "+P1.name+" and "+P2.name+" has "+str(Comparation())+"% probability to match"


