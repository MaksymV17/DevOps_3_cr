import sys

def main():
    # Перевіряємо, чи є аргумент --help
    if len(sys.argv) > 1 and "--help" in sys.argv:
        print("Використання: python sys_tool.py [опції]")
        print("Опції:")
        print("\t--help\tпоказати цю підказку")
        return  # Виходимо з функції, щоб далі нічого не друкувати

    # Це виконається тільки якщо не було --help
    print("командна строка")

if __name__ == "__main__":
    main()