class Date:
    def __init__(self, date):
        self.date = date

    def extract_data(self):
        try:
            date, month, year = self.date.split()
            return date, month, year
        except Exception as e:
            print(f"Не удалось выделить дату из строки! {e}")

    @staticmethod
    def validate_data(date_input):
        try:
            date, month, year = date_input
            if int(date) not in range(1, 32):
                raise ValueError('День указан некорректно!')
            elif int(month) not in range(1, 13):
                raise ValueError('Месяц указан некорректно!')
            elif int(year) not in range(0, 2100):
                raise ValueError('Год указан некорректно!')
        except ValueError as e:
            print(e)
        else:
            print("Дата провалидирована успешно!")



my_date_cls = Date("13-06 2021")
my_date = my_date_cls.extract_data()
print(my_date)
if my_date:
    my_date_cls.validate_data(my_date)