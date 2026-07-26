
from merge.merger import Merger


def test_merge_two_datasets():

    merger = Merger()

    datasets = [
        [
            {"text": "Hello"},
            {"text": "World"}
        ],
        [
            {"instruction": "Say Hi", "input": "", "output": "Hi"}
        ]
    ]

    result = merger.process(datasets)

    assert len(result) == 3


def test_skip_empty_dataset():

    merger = Merger()

    datasets = [
        [],
        [{"text": "Hello"}],
        None
    ]

    result = merger.process(datasets)

    assert len(result) == 1


def test_empty_input():

    merger = Merger()

    result = merger.process([])

    assert result == []
