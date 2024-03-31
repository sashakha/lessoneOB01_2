class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} по цене {price} добавлен в магазин {self.name}.")

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}"


# Создаем список магазинов для удобства выбора
stores = [
    Store("Замуж от Борисыча", "Невский проспект, 45"),
    Store("Счастливая стопа", "Воронцовский бульвар, 72"),
    Store("Книжный червь", "Пулковское шоссе, 12 корпус 2")
]


def list_stores():
    print("Список магазинов:")
    for index, store in enumerate(stores, start=1):
        print(f"{index}. {store}")


def choose_store():
    list_stores()
    choice = int(input("Выберите магазин по номеру: "))
    return stores[choice - 1]


def add_item_to_store(store):
    item_name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    store.add_item(item_name, price)


if __name__ == "__main__":
    while True:
        print("\n1. Добавить товар в магазин\n2. Выход")
        user_choice = input("Выберите действие: ")

        if user_choice == "1":
            chosen_store = choose_store()
            add_item_to_store(chosen_store)
        elif user_choice == "2":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

