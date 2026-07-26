
from verify.verify import Verifier


def test_verifier_runs():

    verifier = Verifier()

    dataset = [
        {"text": "Hello"},
        {
            "instruction": "Say Hi",
            "input": "",
            "output": "Hi"
        },
        {
            "code": "print('Hello')",
            "language": "python"
        }
    ]

    verifier.show(dataset)


def test_empty_dataset():

    verifier = Verifier()

    verifier.show([])
