
import traceback


class SafeRun:

    @staticmethod
    def execute(name, function, *args, **kwargs):

        try:

            return function(*args, **kwargs)

        except Exception as e:

            print("=" * 60)
            print(f"FAILED : {name}")
            print("=" * 60)

            print(e)
            traceback.print_exc()

            return None
