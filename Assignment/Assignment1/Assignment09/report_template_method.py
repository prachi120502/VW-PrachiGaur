from abc import ABC, abstractmethod



class ReportGenerator(ABC):

    def generate_report(self):
        """
        Template Method - Defines the fixed sequence
        """
        self.parse()
        self.validate()

        if self.requires_revalidation():
            self.revalidate()

        self.save()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def revalidate(self):
        """
        Optional step - only for special reports
        """
        print("Revalidating report...")

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def requires_revalidation(self):
        pass





class StandardReport(ReportGenerator):

    def parse(self):
        print("Parsing standard report...")

    def validate(self):
        print("Validating standard report...")

    def save(self):
        print("Saving standard report...")

    def requires_revalidation(self):
        return False





class SpecialReport(ReportGenerator):

    def parse(self):
        print("Parsing special report...")

    def validate(self):
        print("Validating special report...")

    def save(self):
        print("Saving special report...")

    def requires_revalidation(self):
        return True




def main():
    print("Choose Report Type:")
    print("1. Standard Report (PDF, DOCX, TXT)")
    print("2. Special Report (CSV, JSON)")

    choice = input("Enter choice: ")

    if choice == "1":
        report = StandardReport()
    elif choice == "2":
        report = SpecialReport()
    else:
        print("Invalid choice")
        return

    print("\nGenerating Report...\n")
    report.generate_report()


if __name__ == "__main__":
    main()