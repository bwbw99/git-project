import complete
import csv

class feat:
    def __init__(self):
        self.result = 0

    def run(self):
        #과목코드: dictionary로 저장
        lectures = {
            '101':'논리회로','102':'선형대수학','103':'소프트웨어공학','104':'수치해석','105':'신호및시스템',
            '106':'알고리즘','107':'오픈소스SW','108':'운영체제','109':'이산수학','110':'자료구조',
            '111':'정보보호이론','112':'창의적설계','113':'컴파일러','114':'컴퓨터구조','115':'확률및통계',
            '901':'수학의세계','902':'인간행동과심리','903':'창의와소통','904':'한국사','905':'ACT'}

        #학생 a를 생성
        a = complete.gradeCalculator()

        #grade: 학점, int형으로 저장
        grade = 0

        #score: 평점, float형으로 저장
        total_score = 0.0

        while(True):
            print("작업을 선택하세요")
            print("1. 입력")
            print("2. 출력")
            print("3. 조회")
            print("4. 계산")
            print("5. 파일 저장")
            print("6. 파일 불러오기")
            print("7. 종료")
            # 선택할 작업의 번호
            match input():
                case '1':
                    print("과목명을 입력하세요:")
                    name = input()
                    key = 'undefined'
                    for i in lectures.keys():
                        if lectures[i] == name:
                            key = i
                            before_score = [0.0,'None']
                    if key == 'undefined':
                        print("잘못된 과목명입니다.")
                    else:
                        print("학점을 입력하세요:")
                        try:
                            grade = int(input())
                            for i in range(len(a.key)):
                                if a.key[i] == key: #재수강
                                    match a.score_str[i]:
                                        case 'A+':
                                            before_score = [4.5, 'A+']
                                        case 'A':
                                            before_score = [4.0, 'A']
                                        case 'B+':
                                            before_score = [3.5, 'B+']
                                        case 'B':
                                            before_score = [3.0, 'B']
                                        case 'C+':
                                            before_score = [2.5, 'C+']
                                        case 'C':
                                            before_score = [2.0, 'C']
                                        case 'D+':
                                            before_score = [1.5, 'D+']
                                        case 'D':
                                            before_score = [1.0, 'D']
                                        case 'F':
                                            before_score = [0, 'F']
                                    a.delete(i)
                                    break
                            print("평점을 입력하세요:")
                            match input():
                                case 'A+':
                                    score = [4.5, 'A+']
                                case 'A':
                                    score = [4.0, 'A']
                                case 'B+':
                                    score = [3.5, 'B+']
                                case 'B':
                                    score = [3.0, 'B']
                                case 'C+':
                                    score = [2.5, 'C+']
                                case 'C':
                                    score = [2.0, 'C']
                                case 'D+':
                                    score = [1.5, 'D+']
                                case 'D':
                                    score = [1.0, 'D']
                                case 'F':
                                    score = [0.0, 'F']
                            if int(2*before_score[0]) < int(2*score[0]):
                                total_score -= before_score[0]*grade
                                total_score += score[0]*grade
                                a.set(key,grade,score[0],score[1])
                            else:
                                a.set(key,grade,score[0],score[1])
                        except:
                            print("잘못된 입력입니다.")
                case '2':
                    for i in range(len(a.key)):
                        print("["+ lectures[a.key[i]] + "] " + str(a.grade[i]) + "학점: " + a.score_str[i])
                case '3':
                    print("과목명을 입력하세요:")
                    name = input()
                    key = 'undefined'
                    for i in lectures.keys():
                        if lectures[i] == name:
                            key = i
                    if key == 'undefined':
                        print("잘못된 과목명입니다.")
                    else:
                        for i in range(len(a.key)):
                            if a.key[i] == key: 
                                print("[" + name + "] " + str(a.grade[i]) + "학점: " + a.score_str[i])
                            elif i == len(a.key)-1:
                                print("과목을 수강하지 않아 정보가 없습니다.")
                case '4':
                    submit_grade = 0
                    open_grade = 0
                    for i in range(len(a.grade)):
                        open_grade += a.grade[i]
                        if a.score_str[i] != 'F':
                            submit_grade += a.grade[i]
                    if open_grade == 0: #예외처리1
                        print("수강한 과목이 없어서 계산이 불가합니다")
                    elif submit_grade == 0: #예외처리2
                        print("F학점만 존재하기 때문에 계산이 불가합니다")
                    else:
                        print("제출용: " + str(submit_grade) + "학점 (GPA: " + str(total_score/submit_grade) + ")")
                        print("열람용: " + str(open_grade) + "학점 (GPA: " + str(total_score/open_grade) + ")")
                case '5':
                    f = open('data.csv', 'w', encoding = 'utf-8', newline = '')
                    wr = csv.writer(f)
                    wr.writerow(a.key)
                    wr.writerow(a.grade)
                    wr.writerow(a.score_float)
                    wr.writerow(a.score_str)
                    print('저장되었습니다.')
                case '6':
                    f = open('data.csv', 'r')
                    rdr = csv.reader(f)
                    lines = []
                    for line in rdr:
                        lines.append(line)
                    a.key = lines[0]
                    a.grade = lines[1]
                    a.score_float = lines[2]
                    a.score_str = lines[3]
                    print('파일을 불러왔습니다.')
                case '7':
                    print("프로그램을 종료합니다.")
                    break
                case _:
                    print("잘못된 입력입니다. 1, 2, 3, 4, 5, 6, 7 중에 선택하세요.")