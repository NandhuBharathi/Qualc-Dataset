
class Validator:

    def process(self, dataset):

        validated = []

        for row in dataset:

            if self.is_valid(row):
                validated.append(row)

        return validated


    def is_valid(self, row):

        record_type = row.get("type")


        # Text
        if record_type == "text":

            return (
                isinstance(row.get("text"), str)
                and row["text"].strip() != ""
            )


        # QA
        if record_type == "qa":

            return (
                isinstance(row.get("context"), str)
                and row["context"].strip() != ""
                and isinstance(row.get("question"), str)
                and row["question"].strip() != ""
                and row.get("answers") is not None
            )


        # Instruction
        if record_type == "instruction":

            return (
                isinstance(row.get("instruction"), str)
                and isinstance(row.get("output"), str)
                and row["instruction"].strip() != ""
                and row["output"].strip() != ""
            )


        # Chat
        if record_type == "chat":

            return (
                isinstance(row.get("prompt"), str)
                and isinstance(row.get("response"), str)
                and row["prompt"].strip() != ""
                and row["response"].strip() != ""
            )


        # Code
        if record_type == "code":

            return (
                isinstance(row.get("code"), str)
                and row["code"].strip() != ""
                and isinstance(row.get("language"), str)
                and row["language"].strip() != ""
            )

        return False
