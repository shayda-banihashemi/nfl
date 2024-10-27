import pywebio
import builtins


class Terminal:
    @staticmethod
    def cprint(message):
        builtins.print(message)

    @staticmethod
    def cinput(message):
        return builtins.input(message)


class Web(Terminal):
    @staticmethod
    def cprint(message):
        pywebio.output.put_markdown(message)

    @staticmethod
    def cinput(message):
        return pywebio.input.input(message)


def main():
    io = Web()
    print = io.cprint
    input = io.cinput

    print("Personal details")
    name = input("Name")
    age = input("Age")
    favorite_color = input("Favorite color")
    print(f"{name} is {age} years' old and likes {favorite_color} best.")


if __name__ == "__main__":
    main()
