class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price} грн. - {self.quantity} шт."
class Cart:
    def __init__(self):
        self.items = []
        self.total = 0
    def add_item(self, item):
        self.items.append(item)
        self.total += item.price
    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item.price
    def show_items(self):
        print("Товари у вашому кошику:")
        for item in self.items:
            print(item)
    def clear_items(self):
        self.items = []
        self.total = 0
class CashRegister:
    def __init__(self):
        self.products = []
        self.cart = Cart()
        self.user = None
        self.admin = "Admin"
        self.password = "Admin"
    def load_products(self):
        try:
            with open("products.txt", "r") as file:
                for line in file:
                    name, price, quantity = line.split(",")
                    product = Product(name, float(price), int(quantity))
                    self.products.append(product)
        except FileNotFoundError:
            print("Файл products.txt не знайдено")
    def save_products(self):
        with open("products.txt", "w") as file:
            for product in self.products:
                file.write(f"{product.name},{product.price},{product.quantity}\n")
    def show_products(self):
        print("Доступні товари:")
        for i, product in enumerate(self.products):
            print(f"{i + 1}. {product}")
    def register_user(self):
        name = input("Введіть ваше ім'я: ")
        self.user = name
        print(f"Вітаємо, {name}! Ви успішно зареєструвалися в системі.")
    def add_product(self):
        try:
            name = input("Введіть назву товару: ")
            price = float(input("Введіть ціну товару: "))
            quantity = int(input("Введіть кількість товару: "))
        except ValueError:
            print("Некоректне введення. Будь ласка, введіть числові значення.")
            return
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Ви додали новий товар: {product}")
    def remove_product(self):
        self.show_products()
        try:
            index = int(input("Введіть номер товару, який хочете видалити: "))
            product = self.products.pop(index - 1)
        except (ValueError, IndexError):
            print("Некоректний номер товару. Будь ласка, введіть дійсне число.")
            return
        print(f"Ви видалили товар: {product}")
    def edit_product(self):
        self.show_products()
        try:
            index = int(input("Введіть номер товару, який хочете змінити: "))
            product = self.products[index - 1]
        except (ValueError, IndexError):
            print("Некоректний номер товару. Будь ласка, введіть дійсне число.")
            return
        print(f"Ви обрали товар: {product}")
        name = input("Введіть нову назву товару або натисніть Enter, щоб залишити стару: ")
        price = input("Введіть нову ціну товару або натисніть Enter, щоб залишити стару: ")
        quantity = input("Введіть нову кількість товару або натисніть Enter, щоб залишити стару: ")
        if name:
            product.name = name
        if price:
            try:
                product.price = float(price)
            except ValueError:
                print("Некоректне введення. Будь ласка, введіть числове значення.")
        if quantity:
            try:
                product.quantity = int(quantity)
            except ValueError:
                print("Некоректне введення. Будь ласка, введіть ціле число.")
        print(f"Ви змінили товар: {product}")
    def buy_product(self):
        self.show_products()
        try:
            index = int(input("Введіть номер товару, який хочете купити: "))
            product = self.products[index - 1]
        except (ValueError, IndexError):
            print("Некоректний номер товару. Будь ласка, введіть дійсне число.")
            return
        print(f"Ви обрали товар: {product}")
        if product.quantity <= 0:
            print(f"На жаль, товар {product.name} закінчився")
            return
        self.cart.add_item(product)
        product.quantity -= 1
        print(f"Ви додали товар {product.name} у ваш кошик")
    def pay(self):
        self.cart.show_items()
        print(f"Загальна сума до оплати: {self.cart.total} грн.")
        try:
            cash = float(input("Введіть суму готівкою: "))
        except ValueError:
            print("Некоректне введення. Будь ласка, введіть числове значення.")
            return
        if cash >= self.cart.total:
            change = cash - self.cart.total
            print(f"Ваша решта: {change} грн.")
            self.cart.clear_items()
            print("Дякуємо за покупку!")
        else:
            print("Ви ввели недостатню суму")
    def run(self):
        self.load_products()
        print("Вітаємо вас у додатку \"Касовий апарат\"")
        while True:
            print("Меню:")
            print("1. Зареєструватись в системі")
            print("2. Переглянути доступні товари")
            print("3. Купити товар")
            print("4. Оплатити товари з кошика")
            print("5. Увійти як адміністратор")
            print("6. Вийти з системи")
            choice = input("Введіть ваш вибір: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.show_products()
            elif choice == "3":
                self.buy_product()
            elif choice == "4":
                self.pay()
            elif choice == "5":
                login = input("Введіть логін адміністратора: ")
                password = input("Введіть пароль адміністратора: ")
                if login == self.admin and password == self.password:
                    self.admin_menu()
                else:
                    print("Невірний логін або пароль")
            elif choice == "6":
                print("До побачення!")
                break
            else:
                print("Неправильний вибір, спробуйте ще раз")
    def admin_menu(self):
        print("Меню адміністратора:")
        print("1. Додати новий товар")
        print("2. Видалити існуючий товар")
        print("3. Змінити інформацію про товар")
        print("4. Повернутись до головного меню")
        choice = input("Введіть ваш вибір: ")
        if choice == "1":
            self.add_product()
        elif choice == "2":
            self.remove_product()
        elif choice == "3":
            self.edit_product()
        elif choice == "4":
            return
        else:
            print("Неправильний вибір, спробуйте ще раз")
if __name__ == "__main__":
    cash_register = CashRegister()
    cash_register.run()