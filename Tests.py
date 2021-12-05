import main
import pytest


class Tests_Pytests:

    def setUp(cls):
        print('method setUp')

    @pytest.mark.parametrize('string_, expected_result',[
        ('(((([{}]))))', 'Сбалансировано'),
        ('[([])((([[[]]])))]{()}', 'Сбалансировано'),
        ('{{[()]}}', 'Сбалансировано'),
        ('}{}', 'Несбалансировано'),
        ('{{[(])]}}', 'Несбалансировано'),
        ('[[{())}]', 'Несбалансировано')
    ])
    def test_check_balance(self, string_, expected_result):
        assert main.check_balance(string_) == expected_result