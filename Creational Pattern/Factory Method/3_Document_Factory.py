# Document factory example

from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def open(self):
        pass


class HTMLDocument(Document):
    def open(self):
        print(f"opening HTML Document.....")


class XMLDocument(Document):
    def open(self):
        print(f"opening XML Document.....")


class PDFDocument(Document):
    def open(self):
        print(f"opening PDF Document.....")


class XLSXDocument(Document):
    def open(self):
        print(f"opening XLSX Document.....")


class DOCXDocument(Document):
    def open(self):
        print(f"opening DOCX Document.....")


class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self):
        pass


class HTMLDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return HTMLDocument()


class XMLDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return XMLDocument()


class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()


class XLSXDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return XLSXDocument()


class DOCXDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return DOCXDocument()


# client code
def process_document(document_factory: DocumentFactory):
    document = document_factory.create_document()
    document.open()


if __name__ == "__main__":
    html_factory = HTMLDocumentFactory()
    process_document(html_factory)

    xml_factory = XMLDocumentFactory()
    process_document(xml_factory)

    pdf_factory = PDFDocumentFactory()
    process_document(pdf_factory)

    xlsx_factory = XLSXDocumentFactory()
    process_document(xlsx_factory)

    docx_factory = DOCXDocumentFactory()
    process_document(docx_factory)
