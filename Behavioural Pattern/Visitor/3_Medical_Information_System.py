from abc import ABC, abstractmethod


class MedicalInformationSystem:
    def __init__(self):
        self.medical_data = []

    def add_medical_data(self, data):
        self.medical_data.append(data)

    def process_data(self, visitor):
        for data in self.medical_data:
            data.accept(visitor)
        print("*" * 30)


class MedicalData(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Symptoms(MedicalData):
    def accept(self, visitor):
        visitor.visit_symptoms(self)


class TestResults(MedicalData):
    def accept(self, visitor):
        visitor.visit_test_results(self)


class MedicalHistory(MedicalData):
    def accept(self, visitor):
        visitor.visit_medical_history(self)


class MedicalVisitor(ABC):
    @abstractmethod
    def visit_medical_history(self, medical_history):
        pass

    @abstractmethod
    def visit_test_results(self, test_results):
        pass

    @abstractmethod
    def visit_symptoms(self, symptoms):
        pass


class DataAnalyzer(MedicalVisitor):
    def visit_medical_history(self, medical_history):
        print(f"Analyze Medical History Data")

    def visit_symptoms(self, symptoms):
        print(f"Analyze Symptoms Data")

    def visit_test_results(self, test_results):
        print(f"Analyze Test Results Data")


class Diagnoser(MedicalVisitor):
    def visit_medical_history(self, medical_history):
        print(f"Dianosing Medical History Data")

    def visit_symptoms(self, symptoms):
        print(f"Diagnosing Symptoms Data")

    def visit_test_results(self, test_results):
        print(f"Diagnosing Test Results Data")


class RecordProcessor(MedicalVisitor):
    def visit_medical_history(self, medical_history):
        print(f"Processing Medical History Record")

    def visit_symptoms(self, symptoms):
        print(f"Processing Symptoms Record")

    def visit_test_results(self, test_results):
        print(f"Processing Test Results Record")


if __name__ == "__main__":
    medical_information_system = MedicalInformationSystem()

    symptoms = Symptoms()
    test_results = TestResults()
    medical_history = MedicalHistory()

    medical_information_system.add_medical_data(symptoms)
    medical_information_system.add_medical_data(test_results)
    medical_information_system.add_medical_data(medical_history)

    analyzer = DataAnalyzer()
    medical_information_system.process_data(analyzer)

    diagnoser = Diagnoser()
    medical_information_system.process_data(diagnoser)

    record_processor = RecordProcessor()
    medical_information_system.process_data(record_processor)
