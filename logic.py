import csv
from datetime import datetime

class QualityCriterion:
    """
    A single quality audit question.
    """
    def __init__(self, q_id: int, text: str, opt_yes: str, opt_no: str, opt_na: str):
        self.id = q_id
        self.question_text = text
        # Creates a list of options, ignoring N/A where not needed.
        self.options = [opt for opt in [opt_yes, opt_no, opt_na]]
    
    def calculate_score(self, user_input: str) -> dict:
        """
        A pure function, determining the score values based on the selected answer.
        Always returns the exact same dictionary output for the same input string.
        """
        if user_input == "Yes":
            return {"score": 1, "possible": 1}
        elif user_input == "No":
            return {"score": 0, "possible": 1}
        else:
            return {"score": 0, "possible": 0}
    
class QualityController:
    """
    Manages the audit process, loading criteria and saving results.
    """
    def __init__(self):
        self.quality_criteria = []
        self.total_score = 0
    
    def load_criteria_from_csv(self,filepath: str) -> None:
        """
        Reads the audit questions from a CSV and creates QualityCriterion objects.
        """
        self.quality_criteria = []
        try:
            with open(filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    criterion = QualityCriterion(
                        q_id=int(row['id']),
                        text=row['question_text'],
                        opt_yes=row['option_yes'],
                        opt_no=row['option_no'],
                        opt_na=row['option_na']
                    )
                    self.quality_criteria.append(criterion)
        except FileNotFoundError:
            pass

    def save_audit_to_csv(self, filepath: str, advisor_name: str, auditor_name: str, final_score: float) -> None:
        """
        Appends the completed audit results to a permanent CSV log.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, auditor_name, advisor_name, f"{final_score:.2f}%"])