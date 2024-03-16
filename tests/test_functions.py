from src1.functions import five_recent_operations, print_date_and_description_transfer_type, \
    print_where_from_and_where_operation_was_performed, print_transaction_amount_and_currency

test_1 = five_recent_operations()
test_1_sorted = sorted(test_1, key=lambda x: x["date"])


def test_five_recent_operations():
    assert five_recent_operations() == test_1


def test_print_date_and_description_transfer_type():
    assert print_date_and_description_transfer_type(test_1_sorted[0]) == "09.03.2018 Перевод организации"


def test_print_where_from_and_where_operation_was_performed():
    assert print_where_from_and_where_operation_was_performed(test_1_sorted[1]) == "Счет **8409 -> Счет **8266"
    assert print_where_from_and_where_operation_was_performed(
        test_1_sorted[2]) == "МИР 5211 27** **** 8469 -> Счет **2662"
    assert print_where_from_and_where_operation_was_performed(test_1_sorted[4]) == "Счет **2265"


def test_print_transaction_amount_and_currency():
    assert print_transaction_amount_and_currency(test_1_sorted[2]) == "6381.58 USD"
from src1.functions import five_recent_operations, print_date_and_description_transfer_type, \
    print_where_from_and_where_operation_was_performed, print_transaction_amount_and_currency

test_1 = five_recent_operations()
test_1_sorted = sorted(test_1, key=lambda x: x["date"])


def test_five_recent_operations():
    assert five_recent_operations() == test_1


def test_print_date_and_description_transfer_type():
    assert print_date_and_description_transfer_type(test_1_sorted[0]) == "09.03.2018 Перевод организации"


def test_print_where_from_and_where_operation_was_performed():
    assert print_where_from_and_where_operation_was_performed(test_1_sorted[1]) == "Счет **8409 -> Счет **8266"
    assert print_where_from_and_where_operation_was_performed(
        test_1_sorted[2]) == "МИР 5211 27** **** 8469 -> Счет **2662"
    assert print_where_from_and_where_operation_was_performed(test_1_sorted[4]) == "Счет **2265"


def test_print_transaction_amount_and_currency():
    assert print_transaction_amount_and_currency(test_1_sorted[2]) == "6381.58 USD"
