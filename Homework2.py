number_of_homework_completed = 12
number_of_hours_spent = 1.5
courseName = 'Python'
timeForOneTask = number_of_hours_spent / number_of_homework_completed
print(type(number_of_homework_completed))
print(type(number_of_hours_spent))
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
print('Курс: ' + courseName + ', ' + 'всего задач:  ',number_of_homework_completed,',', ' затрачено часов:',number_of_hours_spent,',', ' среднее время выполенения ',timeForOneTask,' часа.', sep="")
print(f'Курс: {courseName}, всего задач: {number_of_homework_completed}, затрачено часов: {number_of_hours_spent}, среднее время выполенения {timeForOneTask} часа.')
print(f'Курс: {courseName}, \nвсего задач: {number_of_homework_completed}, \nзатрачено часов: {number_of_hours_spent}, \nсреднее время выполенения {timeForOneTask} часа.')

