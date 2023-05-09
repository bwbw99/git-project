#수강목록 클래스
class gradeCalculator:
    key = []
    grade = []
    score_float = []
    score_str = []
    
    def __init__(self):
        self.result = 0

    def set(self,k,g,sf,ss):
        self.key.append(k)
        self.grade.append(g)
        self.score_float.append(sf)
        self.score_str.append(ss)

    def delete(self,i):
        del self.key[i]
        del self.grade[i]
        del self.score_float[i]
        del self.score_str[i]

#클래스 호출 방법 : a = gradeCalculator() 의 형태
#클래스 사용하는 이유 : 다른 학생의 학점도 계산할 수 있음 (ex b = gradeCalculator())