# Импортирую функцию для создания списка из 5 последних успешных операций и вывода этих самых операций
from functions import five_recent_operations, print_date_and_description_transfer_type, print_where_from_and_where_operation_was_performed, print_transaction_amount_and_currency

dictionary = five_recent_operations()
# Сортирую список по ключу "date"
dictionary_sorted = sorted(dictionary, key=lambda x: x["date"])

# Вывожу дату и описание типа перевода последней операции
print(print_date_and_description_transfer_type(dictionary_sorted[0]))
# Вывожу откуда и куда была совершена последняя операция
print(print_where_from_and_where_operation_was_performed(dictionary_sorted[0]))
# Вывожу сумму операции и валюту последней операции
print(print_transaction_amount_and_currency(dictionary_sorted[0]))
# Пустая строка
print()

# 4 с конца операция
print(print_date_and_description_transfer_type(dictionary_sorted[1]))
print(print_where_from_and_where_operation_was_performed(dictionary_sorted[1]))
print(print_transaction_amount_and_currency(dictionary_sorted[1]))
print()

# 3 операция
print(print_date_and_description_transfer_type(dictionary_sorted[2]))
print(print_where_from_and_where_operation_was_performed(dictionary_sorted[2]))
print(print_transaction_amount_and_currency(dictionary_sorted[2]))
print()

# 3 операция
print(print_date_and_description_transfer_type(dictionary_sorted[3]))
print(print_where_from_and_where_operation_was_performed(dictionary_sorted[3]))
print(print_transaction_amount_and_currency(dictionary_sorted[3]))
print()

# 1 операция
print(print_date_and_description_transfer_type(dictionary_sorted[4]))
print(print_where_from_and_where_operation_was_performed(dictionary_sorted[4]))
print(print_transaction_amount_and_currency(dictionary_sorted[4]))
print()
