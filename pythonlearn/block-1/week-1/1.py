# Day 1: Installation and first code

# Написание первой программы "Hello, World!"
# - **Практические задачи:**
#   1. Написать скрипт, который выводит ваше имя и возраст.
#   2. Запросить у пользователя данные и вывести их.
#   3. Простая программа для расчета стоимости покупки с учетом скидки.
#   4. Написать калькулятор площади круга.

#   5. Создать программу, выводящую ASCII-арт на экран.

# print('Hello, world!')

# ===========================================================================

# #   1. Написать скрипт, который выводит ваше имя и возраст.
# import datetime  # Импортируем модуль работы со временем

# current_datetime = datetime.datetime.now() # Получаем текущие дату и время
# current_year = current_datetime.year

# your_name = input("Назовите ваше имя: ")
# year_birth = input("Введите год вашего рождения: ") # Запрашиваем год рождения

# age = current_year - int(year_birth)
# print(f"Мое имя - {your_name}")
# print(f"Мой возраст - {age} лет")


# from datetime import date

# def get_difference(startdate, enddate):
#     diff = enddate - startdate
#     return diff.days

# # Инициализируем даты
# startdate = date(1965, 11, 8)
# enddate = date(2025, 3, 27)

# # Вызываем функцию и сохраняем результат
# days = get_difference(startdate, enddate)

# # Выводим результат
# print(f'Я прожил уже {days} дней')

# ===========================================================================

# 3. Простая программа для расчета стоимости покупки с учетом скидки.

# Для расчета стоимости покупки с учетом скидки используется следующий алгоритм:
# Определите сумму скидки в денежном выражении, используя формулу:
# Сумма скидки = Базовая цена × (Процент скидки / 100%)
# Вычислите конечную стоимость товара со скидкой:
# Цена со скидкой = Базовая цена - Сумма скидки


# БАЗОВОЕ РЕШЕНИЕ

# basePrice = float(input("Введите стоимость товара: "))
# print(f"Стоимость товара: {basePrice} рублей")

# discount = float(input("Введите процент скидки: "))
# print(f"Процент скидки: {discount} %")

# discountAmount = basePrice * (discount / 100)
# finalPrice = basePrice - discountAmount

# print(f"Сумма скидки: {discountAmount} рублей")
# print(f"Итоговая цена со скидкой: {finalPrice} рублей")


# ===================== УЛУЧШЕННАЯ МОДИФИКАЦИЯ ===========================

# def calculate_discount(base_price, discount_percent):
    
#     if discount_percent < 0:
#         discount_percent = 0
#     elif discount_percent > 100:
#         discount_percent = 100
        
#     discount_amount = base_price * (discount_percent / 100)
#     final_price = base_price - discount_amount
    
#     return discount_amount, final_price

# def main():
#     try:
#         base_price = float(input("Введите стоимость товара: "))
#         if base_price < 0:
#             print("Ошибка: стоимость товара не может быть отрицательной.")
#             return
            
#         print(f"Стоимость товара: {base_price:.2f} рублей")

#         discount = float(input("Введите процент скидки: "))
#         print(f"Процент скидки: {discount:.1f} %")

#         discount_amount, final_price = calculate_discount(base_price, discount)
        
#         print(f"Сумма скидки: {discount_amount:.2f} рублей")
#         print(f"Итоговая цена со скидкой: {final_price:.2f} рублей")
        
#     except ValueError:
#         print("Ошибка: введите корректное числовое значение.")


# if __name__ == "__main__":
  
#     main()
    
# ===========================================================================

#   4. Написать калькулятор площади круга.

# Алгоритм вычисления площади круга:
# Определите радиус круга (r).
# Используйте формулу площади круга: S = πr²

import math 

pi = math.pi 

rad = float(input("Введите радиус круга в см: "))
print(f"Радиус круга: {rad:.2f} см")  

square = pi*rad**2
print(f"Площадь круга: {square:.2f} см квадратных")  # Ограничиваем значение 2 знаками после запятой

# =======================+===== End Day One ==================================

