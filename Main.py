# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Comparsions import Comparsion
from Peoples import People
from Peoples import Match_Condition

if __name__ == "__main__":
    
    # P1 = People()
    # P2 = People()

    # P1.Aquire_Infor()
    # P2.Aquire_Infor()

    # Test bench
    P1=People('Fat',28,Match_Condition.Grow_Loc[1],Match_Condition.Work_Loc[1],
            Match_Condition.Degree[1],Match_Condition.Apparance[1],
            Match_Condition.Salary_Rate[1])


    P2=People("Zach",27,Match_Condition.Grow_Loc[1],Match_Condition.Work_Loc[2],
            Match_Condition.Degree[2],Match_Condition.Apparance[2],
            Match_Condition.Salary_Rate[2])

    Compare = Comparsion()
    Compare.Simple_Compare(P1,P2)
    Compare.print_score()