class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grades(self, index):
        score = self.get_by_index(index)
        if score < 50:
            return "F"
        elif 50 <= score < 60:
            return "E"
        elif 60 <= score < 70:
            return "D"
        elif 70 <= score < 80:
            return "C"
        elif 80 <= score < 90:
            return "B"
        else:
            return "A"

    def find(self, score):
        positions = []
        idx = 0
        searched_data = self.scores
        while idx < len(searched_data):
            if searched_data[idx] == score:
                positions.append(idx)
            idx += 1
        return positions
if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
