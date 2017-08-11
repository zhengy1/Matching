# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Match_Condition:
    Grow_Loc=["杭州","温州","其他"]
    Work_Loc=["杭州","温州","硅谷","洛杉矶","温哥华"]
    Degree=["高中","大学","研究生","博士"]
    Apparance=["Bad","Average","Good"]
    Salary_Rate=["Low","Middle","High"]

class People:
    def __init__(self,name = None, age = None, Grow_Loc = None,Work_Loc=None,Degree=None,Apparance=None,Salary_Rate=None):
        self.name=name
        self.age=age
        self.Grow_Loc=Grow_Loc
        self.Work_Loc=Work_Loc
        self.Degree=Degree
        self.Apparance=Apparance
        self.Salary_Rate=Salary_Rate

    def Aquire_Infor(self):
        infor=[]
        print "你的名字？: "
        self.name = raw_input()

        print "你的年龄？: "
        self.age = int(raw_input())

        print "请选择出生地？: "
        for n in range (0,len(Match_Condition.Grow_Loc)):
            print n,Match_Condition.Grow_Loc[n],
        self.Grow_Loc = int(raw_input())

        print "请选择工作地？: "
        for n in range (0,len(Match_Condition.Work_Loc)):
            print n,Match_Condition.Work_Loc[n],
        self.Work_Loc = int(raw_input())

        print "请选择学历？: "
        for n in range (0,len(Match_Condition.Degree)):
            print n,Match_Condition.Degree[n],
        self.Degree = int(raw_input())

        print "给自己的外表打几分？: "
        for n in range (0,len(Match_Condition.Apparance)):
            print n,Match_Condition.Apparance[n],
        self.Apparance = int(raw_input())

        print "收入水平？: "
        for n in range (0,len(Match_Condition.Salary_Rate)):
            print n,Match_Condition.Salary_Rate[n],
        self.Salary_Rate = int(raw_input())