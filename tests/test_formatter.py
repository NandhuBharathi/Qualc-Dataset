
from formatters.formatter import Formatter


def test_text():

    formatter = Formatter()

    row = {
        "type": "text",
        "text": "Hello World"
    }

    result = formatter.format(row)

    assert result["text"] == "Hello World"


def test_instruction():

    formatter = Formatter()

    row = {
        "type": "instruction",
        "instruction": "Say hello",
        "input": "",
        "output": "Hello"
    }

    result = formatter.format(row)

    assert result["instruction"] == "Say hello"
    assert result["output"] == "Hello"


def test_gsm8k():

    formatter = Formatter()

    row = {
        "type": "gsm8k",
        "question": "2 + 2 = ?",
        "answer": "4"
    }

    result = formatter.format(row)

    assert result["output"] == "4"
