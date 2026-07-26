
from deduplication.deduplicator import Deduplicator


def test_duplicate_text():

    deduplicator = Deduplicator()

    dataset = [
        {"text": "Hello"},
        {"text": "Hello"},
        {"text": "World"}
    ]

    result = deduplicator.process(dataset)

    assert len(result) == 2


def test_duplicate_instruction():

    deduplicator = Deduplicator()

    dataset = [
        {
            "instruction": "Say Hi",
            "input": "",
            "output": "Hi"
        },
        {
            "instruction": "Say Hi",
            "input": "",
            "output": "Hi"
        }
    ]

    result = deduplicator.process(dataset)

    assert len(result) == 1


def test_case_insensitive():

    deduplicator = Deduplicator()

    dataset = [
        {"text": "HELLO"},
        {"text": "hello"}
    ]

    result = deduplicator.process(dataset)

    assert len(result) == 1
