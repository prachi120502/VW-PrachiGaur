from abc import ABC, abstractmethod
import time




def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def validate_before_save(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_valid:
            raise Exception("Report validation failed. Cannot save.")
        print("[VALIDATION] Report validated before saving.")
        return func(self, *args, **kwargs)
    return wrapper




class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("[RESOURCE] Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[RESOURCE] Closing file...")
        if self.file:
            self.file.close()




class BaseReport(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.is_valid = False

    @abstractmethod
    def generate_data(self):
        """
        Generator method - yields report data lazily
        """
        pass

    def validate(self):
        print("Validating report...")
        self.is_valid = True

    @log_operation
    @time_execution
    @validate_before_save
    def save(self):
        """
        Save report using context manager
        """
        with FileManager(self.filename, "w") as file:
            for chunk in self.generate_data():  # Generator used here
                file.write(chunk + "\n")
        print("Report saved successfully.")




class TextReport(BaseReport):

    def generate_data(self):
        print("Generating text report data...")
        for i in range(1, 6):
            yield f"Line {i}: This is a text report entry."




class StructuredReport(BaseReport):

    def generate_data(self):
        print("Generating structured report data...")
        yield "ID,Name,Score"
        for i in range(1, 6):
            yield f"{i},User{i},{i*10}"





def main():
    print("Select Report Type:")
    print("1. Text Report")
    print("2. Structured Report")

    choice = input("Enter choice: ")

    if choice == "1":
        report = TextReport("text_report.txt")
    elif choice == "2":
        report = StructuredReport("structured_report.csv")
    else:
        print("Invalid choice.")
        return

    report.validate()
    report.save()


if __name__ == "__main__":
    main()