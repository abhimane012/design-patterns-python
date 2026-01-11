# Logging Factory

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, msg):
        pass


class DataBaseLogger(Logger):
    def log(self, msg):
        print(f"[DataBaseLogger]", msg)


class ConsoleLogger(Logger):
    def log(self, msg):
        print(f"[ConsoleLogger]", msg)


class FileLogger(Logger):
    def log(self, msg):
        print(f"[FileLogger]", msg)


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self):
        pass


class DataBaseLoggerFactory(LoggerFactory):
    def create_logger(self):
        return DataBaseLogger()


class FileLoggerFactory(LoggerFactory):
    def create_logger(self):
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()


def process_logger(factory: LoggerFactory, msg: str):
    logger = factory.create_logger()
    logger.log(msg)


if __name__ == "__main__":
    console_logger = ConsoleLoggerFactory()
    process_logger(console_logger, "This is console logger")

    db_logger = DataBaseLoggerFactory()
    process_logger(db_logger, "This is database logger")

    file_logger = FileLoggerFactory()
    process_logger(file_logger, "This is file logger")
