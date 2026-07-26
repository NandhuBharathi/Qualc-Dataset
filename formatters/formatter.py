class Formatter:

    def process(self, dataset):

        formatted = []

        for row in dataset:

            record = self.format(row)

            if record:
                formatted.append(record)

        return formatted


    def format(self, row):

        # Plain Text
        if row["type"] == "text":

            return {
                "text": row["text"]
            }


        # QA (SQuAD)
        if row["type"] == "qa":

            answer = ""

            if isinstance(row["answers"], dict):
                answer = row["answers"].get("text", [""])[0]

            return {
                "instruction": "Answer the question using the context.",
                "input": f"Context:\n{row['context']}\n\nQuestion:\n{row['question']}",
                "output": answer
            }


        # BoolQ
        if row["type"] == "boolq":

            return {
                "instruction": "Answer the question with True or False.",
                "input": f"Passage:\n{row['passage']}\n\nQuestion:\n{row['question']}",
                "output": str(row["answer"])
            }


        # Dolly
        if row["type"] == "instruction":

            return {
                "instruction": row["instruction"],
                "input": row["input"],
                "output": row["output"]
            }


        # GSM8K
        if row["type"] == "gsm8k":

            return {
                "instruction": "Solve the math problem.",
                "input": row["question"],
                "output": row["answer"]
            }


        # Chat
        if row["type"] == "chat":

            return {
                "instruction": row["prompt"],
                "input": "",
                "output": row["response"]
            }


        # Code
        if row["type"] == "code":

            return {
                "instruction": f"Write {row['language']} code.",
                "input": "",
                "output": row["code"]
            }

        return None
