def person_profile(**abc):
    return f"Имя: {abc['name']}, Фамилия: {abc['surname']}, Город рождения: {abc['city']}, Возраст: {abc['age']}, Почта: {abc['email']}, Телефон: {abc['number']}"

print(person_profile(name="Philipp", surname="Grivskiy", city="Saint-Petersburg", age="31", email="fgrivskiy@gmail.com", number="89502240542"))