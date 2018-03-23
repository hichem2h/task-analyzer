from task_analyzer import TaskAnalyzer
from task01_tests import check_remainder, check_negative


task_analyzer = TaskAnalyzer([check_remainder, check_negative])
task_analyzer.analyze()
print(task_analyzer.failures)