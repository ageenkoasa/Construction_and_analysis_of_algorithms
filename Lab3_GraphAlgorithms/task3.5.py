"""
В компании есть N сотрудников и M задач для исполнения. У каждого сотрудника есть список задач, в работе над которыми он заинтересован и умеет выполнять (в порядке убывания интереса). 
Для каждой задачи же известен список эффективности сотрудников, умеющих выполнять эту задачу (в порядке убывания эффективности). 
Над каждой задачей может работать не более одного сотрудника, и каждый сотрудник может работать не более чем над одной задачей.

Провести 2 разных распределения максимального числа задач по сотрудникам в компании в соответствии с принципами:

(а) Сотрудник мог быть назначен выполнять задачу, только если все более интересные для него задачи были назначены для выполнения другим, более эффективным сотрудником.

(б) Задача назначена сотруднику, только если все более эффективные для выполнения данной задачи сотрудники были назначены на более интересные для них задачи.
"""

# Aлгоритмы жадного назначения задач сотрудникам

def distribute_tasks_principle_a(employees, tasks):
    task_assignments = {}
    employee_task_counts = {employee: 0 for employee in employees}
    
    for task in tasks:
        min_task_count = min(employee_task_counts.values())
        eligible_employees = [employee for employee, count in employee_task_counts.items() if count == min_task_count]
        employee = eligible_employees[0]
        
        task_assignments[task] = employee
        employee_task_counts[employee] += 1
    
    return task_assignments


def distribute_tasks_principle_b(employees, tasks):
    task_assignments = {}
    employee_assignments = {}
    
    for task in tasks:
        for employee in employees:
            if employee not in employee_assignments or \
                    (task in employees[employee] and \
                    all(task in employees[other_employee] and employees[other_employee].index(task) > employees[employee].index(task) 
                        for other_employee in employee_assignments if other_employee != employee)):
                task_assignments[task] = employee
                employee_assignments[employee] = task
                break
    
    return task_assignments

employees = {
    1: [1, 2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
}

tasks = [1, 2, 3, 4, 5, 6, 7, 8]

print("Принцип (а):")
task_assignments_1 = distribute_tasks_principle_a(employees, tasks)
for task, employee in task_assignments_1.items():
    print(f"Задача {task} назначена сотруднику {employee}")

print("\nПринцип (б):")
task_assignments_2 = distribute_tasks_principle_b(employees, tasks)
for task, employee in task_assignments_2.items():
    print(f"Задача {task} назначена сотруднику {employee}")
