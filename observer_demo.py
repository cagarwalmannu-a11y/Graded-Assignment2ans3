class MarksUpdateNotifier:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, student_id, new_marks):
        for observer in self.observers:
            observer.update(student_id, new_marks)

class EmailNotifier:
    def update(self, student_id, new_marks):
        print(f"Sending email to student {student_id} with new marks {new_marks}")

class AuditLogNotifier:
    def update(self, student_id, new_marks):
        print(f"Logging update for student {student_id} with new marks {new_marks}")

def test_observer():
    notifier = MarksUpdateNotifier()
    email_notifier = EmailNotifier()
    audit_log_notifier = AuditLogNotifier()
    notifier.register_observer(email_notifier)
    notifier.register_observer(audit_log_notifier)
    notifier.notify_observers(1, 90)

if __name__ == "__main__":
    test_observer()
