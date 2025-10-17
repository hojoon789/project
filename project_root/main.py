# main.py : 프로그램 시작

from models import Student, GradeBook

def main():
    # 학생 객체 생성
    alice = Student("Alice", [90, 85, 92])
    bob = Student("Bob", [70, 75, 68])

    # 성적표 객체 및 학생 추가
    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    # 전체 반 평균 출력
    print(f"전체 학생 반 평균 점수: {round(gb.class_average(), 2)}")

    # 각 학생의 점수와 학점 출력
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()