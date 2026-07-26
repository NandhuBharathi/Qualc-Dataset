from configs.schema import SCHEMA


class Cleaner:

    def process(self, dataset):

        cleaned = []

        for row in dataset:

            record = self.normalize(row)

            if record:
                cleaned.append(record)

        return cleaned


    def normalize(self, row):

        # Plain Text
        if "text" in row:
            text = str(row["text"]).strip()

            if text:
                return {
                    "type": "text",
                    "text": text
                }


        # QA (SQuAD)
        if "context" in row and "question" in row and "answers" in row:

            return {
                "type": "qa",
                "context": str(row["context"]).strip(),
                "question": str(row["question"]).strip(),
                "answers": row["answers"]
            }


        # BoolQ
        if "passage" in row and "question" in row and "answer" in row:

            return {
                "type": "boolq",
                "passage": str(row["passage"]).strip(),
                "question": str(row["question"]).strip(),
                "answer": str(row["answer"])
            }


        # Dolly
        if "instruction" in row and "response" in row:

            return {
                "type": "instruction",
                "instruction": str(row["instruction"]).strip(),
                "input": str(row.get("context", "")).strip(),
                "output": str(row["response"]).strip()
            }


        # GSM8K
        if "question" in row and "answer" in row:

            return {
                "type": "gsm8k",
                "question": str(row["question"]).strip(),
                "answer": str(row["answer"]).strip()
            }


        # Generic Instruction
        if all(field in row for field in SCHEMA["instruction"]):

            return {
                "type": "instruction",
                "instruction": str(row["instruction"]).strip(),
                "input": str(row["input"]).strip(),
                "output": str(row["output"]).strip()
            }


        # Chat
        if all(field in row for field in SCHEMA["chat"]):

            return {
                "type": "chat",
                "prompt": str(row["prompt"]).strip(),
                "response": str(row["response"]).strip()
            }


        # Code
        if all(field in row for field in SCHEMA["code"]):

            return {
                "type": "code",
                "code": row["code"],
                "language": row["language"]
            }

        return None
