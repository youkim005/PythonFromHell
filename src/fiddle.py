from pymoulinette.grader import Grader
from pymoulinette.submits import Answers, Submits


def fiddle_submits():
    submit = Submits("src/pymoulinette/day00")
    answer = Answers("day00")
    print(submit)
    print(answer)


def fiddle_grade():
    grader = Grader("src/pymoulinette/day00")
    print(grader)
    grader.grade()


def fiddle_submit_list():
    submit = Submits("src/pymoulinette/day00")
    answer = Answers("day00")
    for exlst in zip(submit, answer):
        print(exlst)


if __name__ == "__main__":
    fiddle_submit_list()
    # fiddle_grade()