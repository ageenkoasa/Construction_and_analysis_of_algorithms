"""
Есть K сотрудников и K задач. Для каждого сотрудника определены задачи, которые он умеет выполнять. 
Назначить задачи сотрудникам так, чтобы каждый работал только над одной задачей, и все задачи были выполнены. 
В случае невозможности такого назначения указать, какого сотрудника необходимо обучить какой задаче для возможности назначения.
"""

# Aлгоритм поиска максимального паросочетания в двудольном графе 
# Каждая доля графа будет представлять собой сотрудников и задачи, а ребра будут соответствовать возможным назначениям задач сотрудникам

# Основная цель - найти наибольшее количество непересекающихся рёбер (пар) между двумя долями графа
# Алгоритм Хопкрофта–Карпа - O(E * sqrt(V))
class AssignmentProblem:
    def __init__(self, num_employees, skills):
        self.num_employees = num_employees
        self.skills = skills
        self.graph = [[] for _ in range(num_employees)]
        self.matching = [-1] * num_employees

    def add_edge(self, employee, task):
        self.graph[employee].append(task)

    def find_matching(self):
        for employee in range(self.num_employees):
            visited = [False] * self.num_employees
            self.try_augment(employee, visited)

    def try_augment(self, employee, visited):
        for task in self.graph[employee]:
            if not visited[task]:
                visited[task] = True
                if self.matching[task] == -1 or self.try_augment(self.matching[task], visited):
                    self.matching[task] = employee
                    return True
        return False

    def find_assignment(self):
        self.find_matching()
        assignment = [(self.matching[task], task) for task in range(len(self.matching)) if self.matching[task] != -1]
        return assignment

if __name__ == "__main__":
    num_employees = 10
    skills = {
        0: [0, 1, 2],
        1: [1, 2, 3],
        2: [0, 2, 4],
        3: [3, 4, 5],
        4: [3, 5, 6],
        5: [4, 6, 7],
        6: [5, 7, 8],
        7: [6, 8, 9],
        8: [7, 9],
        9: [8, 9],
    }

    assignment_problem = AssignmentProblem(num_employees, skills)

    for employee in skills:
        for task in skills[employee]:
            assignment_problem.add_edge(employee, task)

    assignment_problem.find_assignment()

    assignment = assignment_problem.find_assignment()
    if len(assignment) == num_employees:
        print("Задачи успешно назначены:")
        for employee, task in assignment:
            print(f"Сотрудник {employee} выполняет задачу {task}")
    else:
        print("Невозможно назначить все задачи. Необходимо обучить сотрудников.")