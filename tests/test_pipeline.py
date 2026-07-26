
from preprocess.cleaner import Cleaner
from deduplication.deduplicator import Deduplicator
from preprocess.validator import Validator
from formatters.formatter import Formatter
from merge.merger import Merger


def test_pipeline():

    dataset = [
        {"text": "Hello World"},
        {"text": "Hello World"},
        {"instruction": "Say Hi", "response": "Hi"}
    ]

    cleaner = Cleaner()
    deduplicator = Deduplicator()
    validator = Validator()
    formatter = Formatter()
    merger = Merger()

    cleaned = cleaner.process(dataset)
    deduplicated = deduplicator.process(cleaned)
    validated = validator.process(deduplicated)
    formatted = formatter.process(validated)
    merged = merger.process([formatted])

    assert len(merged) > 0
