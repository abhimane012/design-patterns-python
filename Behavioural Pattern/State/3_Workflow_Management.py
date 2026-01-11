from abc import ABC, abstractmethod


class WorkflowState(ABC):
    @abstractmethod
    def handle_workflow(self, workflow):
        pass


class PendingState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Handling workflow in the Pending state.")
        workflow.state = InProgressState()


class InProgressState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Handling workflow in the In-Progress state.")
        workflow.state = CompletedState()


class CompletedState(WorkflowState):
    def handle_workflow(self, workflow):
        print("Handling workflow in the Completed state.")
        workflow.state = None


class Workflow:
    def __init__(self):
        self.state = PendingState()

    def handle(self):
        self.state.handle_workflow(self)


if __name__ == "__main__":
    workflow = Workflow()
    while True:
        if workflow.state:
            workflow.handle()
        else:
            break
