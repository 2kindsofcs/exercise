class WithExample:
    def __init__(self):
        print("I am born")

    def __enter__(self):
        print("with someone")
        return self

    def __exit__(self, type, value, traceback):
        print("ok, goodbye...")

a = WithExample()

print("")

with WithExample() as value:
    print(value)
    print("hmm...")

print("who's there?")
