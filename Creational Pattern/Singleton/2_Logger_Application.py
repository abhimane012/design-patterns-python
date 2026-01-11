# Logger Application example

from datetime import datetime


class Logger:
    __instance = None

    @staticmethod
    def get_instance(file_name: str):
        if not Logger.__instance:
            return Logger(file_name)
        else:
            return Logger.__instance

    def __init__(self, file_name: str):
        if not Logger.__instance:
            print(f"Initializing log file")
            self.__file_name = file_name
            Logger.__instance = self

    def __store_log(self, msg):
        with open(self.__file_name, "a") as file:
            file.write(f"[{datetime.today()}] - {msg}\n")

    def info(self, msg):
        self.__store_log(f"[INFO] - {msg}")

    def error(self, msg):
        self.__store_log(f"[ERROR] - {msg}")

    def critical(self, msg):
        self.__store_log(f"[CRITICAL] - {msg}")

    def exception(self, msg):
        self.__store_log(f"[EXCEPTION] - {msg}")


if __name__ == "__main__":
    log = Logger.get_instance("log1.log")
    log.info("This is info log")
    log.error("This is info log")
    log.critical("This is info log")
    log.exception("This is info log")

    log = Logger.get_instance("log2.log")
    log.info("This is info log2")
    log.error("This is info log2")
    log.critical("This is info log2")
    log.exception("This is info log2")
