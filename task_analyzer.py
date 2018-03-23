class AnalyzerInterface:

    def analyze(self):
        raise NotImplementedError()

    def report(self):
        raise NotImplementedError()

    def scan_mission(self):
        raise NotImplementedError()

    def scan_best_practices(self):
        raise NotImplementedError()


import traceback


class TaskAnalyzer(AnalyzerInterface):
    def __init__(self, tests):
        self.tests = tests
        self.failures = []

    def analyze(self):
        for test in self.tests:
            try:
                test()
            except AssertionError as error:
                a = traceback.extract_tb(error.__traceback__)
                self.failures.append(a.format())