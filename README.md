# b4.12

users.py

run py users.py

Программа запрашивает:
Имя - текст
Фамилия - текст
Пол - текст (подсказка предлагает написать Male или Female)
Email - текст
Год рождения - текст (подсказка предлагает написать в формате 1990)
Месяц рождения - текст (подсказка предлагает написать в формате 04)
День рождения - текст (подсказка предлагает написать в формате 01 - конкретный день месяца)
Рост - float (подсказка предлагает ввести значение в метрах - 1.82)

По окончании ввода запрощенных данных программа 
1. Собирает дату рождения из введенных года, месяца и дня
2. Выводит дату рождения в консоль
3. Сохраняет польхователя в таблицу user

------------------------------------------------------------

find_athlete.py

run py find_athlete.py

Программа запрашивает:
1. ID пользователя (должен быть целым числом, валидация на формат не реализована)

По окончании ввода:
1. Если пользователь с таким ID существует в таблице user, то программа выводит:
1.1. Список ID атлетов с ближайшими днями рождения и их дни рождения
1.2. Список ID атлетов с ближайшим ростом и их рост
2. Если такого пользователя не существует, то программа выводит в консоль сообщение No such user
