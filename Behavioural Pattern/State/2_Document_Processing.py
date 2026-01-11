from abc import ABC, abstractmethod

# state  draft -> Review -> Finalize ->Published


class DocumentState(ABC):
    @abstractmethod
    def process_document(self, context):
        pass


class DraftState(DocumentState):
    def process_document(self, context):
        print(f"Processing document in the {self.__class__.__name__}.")
        context.document_state = ReviewState()


class ReviewState(DocumentState):
    def process_document(self, context):
        print(f"Processing document in the {self.__class__.__name__}.")
        context.document_state = FinalizeState()


class FinalizeState(DocumentState):
    def process_document(self, context):
        print(f"Processing document in the {self.__class__.__name__}.")
        context.document_state = PublishedState()


class PublishedState(DocumentState):
    def process_document(self, context):
        print(
            f"Document cant be processed further as it is in {self.__class__.__name__}."
        )


class Document:
    def __init__(self):
        self.document_state = DraftState()

    def process_document(self):
        self.document_state.process_document(self)


if __name__ == "__main__":
    document = Document()
    document.process_document()
    document.process_document()
    document.process_document()
    document.process_document()
    document.process_document()
