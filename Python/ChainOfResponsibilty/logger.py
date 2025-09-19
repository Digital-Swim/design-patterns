from abc import ABC, abstractmethod

# --- Handler Interface ---
class Logger(ABC):
    def __init__(self, next_logger=None):
        self.next_logger = next_logger

    @abstractmethod
    def log(self, level: str, message: str):
        pass

    def set_next(self, next_logger):
        self.next_logger = next_logger
        return next_logger  # allows chaining


# --- Concrete Loggers ---
class InfoLogger(Logger):
    def log(self, level: str, message: str):
        if level == "INFO":
            print(f"[INFO]: {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)


class DebugLogger(Logger):
    def log(self, level: str, message: str):
        if level == "DEBUG":
            print(f"[DEBUG]: {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)


class ErrorLogger(Logger):
    def log(self, level: str, message: str):
        if level == "ERROR":
            print(f"[ERROR]: {message}")
        elif self.next_logger:
            self.next_logger.log(level, message)


# --- Client Code ---
if __name__ == "__main__":
    # Setup chain: Info -> Debug -> Error
    error_logger = ErrorLogger()
    debug_logger = DebugLogger(error_logger)
    info_logger = InfoLogger(debug_logger)

    # Send messages
    info_logger.log("INFO", "This is an info message")
    info_logger.log("DEBUG", "This is a debug message")
    info_logger.log("ERROR", "This is an error message")
    info_logger.log("WARNING", "This level is not handled")
