# Импортирую json
import json


def five_recent_operations():
    """Создаю функцию, которая берет список json, преобразовывает его в обычный словарь. Затем создаю новый словарь с
    последними успешными операциями и возвращаю 5 последних успешных операций"""
    with open('../src1/operations.json', "rt", encoding='utf-8') as dictionary_json:
        # Создаю словарь
        dictionary_python = json.load(dictionary_json)
        # Создаю пустой словарь в который добавлю 5 последних операций
        dictionary_executed = []
        for transfer_status in dictionary_python:
            # проверяю есть ли ключ "state"
            if "state" in transfer_status:
                # Если ключ равен успешной операции, то добавляю его в новый список
                if transfer_status["state"] == "EXECUTED":
                    dictionary_executed.append(transfer_status)
        return dictionary_executed[-5:]


def print_date_and_description_transfer_type(number):
    """Вывожу дату и описание типа перевода"""
    return f"{number["date"][8:10]}.{number["date"][5:7]}.{number["date"][0:4]} {number["description"]}"


def print_where_from_and_where_operation_was_performed(number):
    """Вывожу откуда и куда была совершена операция"""
    # Проверяю есть ли информация откуда совершена операция, если нет, то выводим только куда ушли деньги
    if "from" in number:
        # Если переводят со счёта
        if number["from"][0] == "С":
            # Если переводят со счёта на счёт(счета маскирую)
            if number["to"][0] == "С":
                return f"{number["from"][0:4]} **{number["from"][-4:]} -> {number["to"][0:4]} **{number["to"][-4:]}"
            # Если переводят со счёта на карту(счёт и карту маскирую)
            else:
                return f"{number["from"][0:4]} **{number["from"][-4:]} -> {number["to"][0:-12]} {number["to"][-12:-10]}** **** {number["to"][-4:]}"
        # Если переводят с карты
        else:
            # Если переводят с карты на счёт(карту и счёт маскирую)
            if number["to"][0] == "С":
                return f"{number["from"][0:-12]} {number["from"][-12:-10]}** **** {number["from"][-4:]} -> {number["to"][0:4]} **{number["to"][-4:]}"
            # Если переводят с карты на карту(карты маскирую)
            else:
                return f"{number["from"][0:-12]} {number["from"][-12:-10]}** **** {number["from"][-4:]} -> {number["to"][0:-12]} {number["to"][-12:-10]}** **** {number["to"][-4:]}"
    else:
        # Деньги поступили на счёт
        if number["to"][0] == "С":
            return f"{number["to"][0:4]} **{number["to"][-4:]}"
        # Деньги поступили на карту
        else:
            return f"{number["to"][0:-12]} {number["to"][-12:-10]}** **** {number["to"][-4:]}"


def print_transaction_amount_and_currency(number):
    """Вывожу сумму операции и валюту"""
    # это с кавычками и запятой
    a = number["operationAmount"]["amount"], number["operationAmount"]["currency"]["name"]
    # Это с запятой
    b = ", ".join(a)
    # Вывод информации как нужно
    return b.replace(", ", " ")
