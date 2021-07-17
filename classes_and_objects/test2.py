class worker:
    company_name = "xalqbank"
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = f"{self.name}.{self.surname}@{self.company_name}.az"

w1 = worker("murad", "samadov", 100)
w2 = worker("fuad", "semedov", 200)

print(w1.email)