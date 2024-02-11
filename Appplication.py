class TacticalOrganizer:
    def __init__(self):
        self.checklist = {}

    def display_menu(self):
        print("=== Тактичний Органайзер ===")
        print("1. Переглянути чек-лист")
        print("2. Додати елемент до чек-листа")
        print("3. Модифікувати елемент чек-листа")
        print("4. Видалити елемент з чек-листа")
        print("5. Пошук спорядження")
        print("6. Замовити спорядження")
        print("7. Позначити елемент як знайдений")
        print("8. Позначити елемент як не знайдений")
        print("9. Переглянути детальну інформацію про елемент")
        print("10. Вийти")

    def view_checklist(self):
        print("=== Чек-лист ===")
        for item, details in self.checklist.items():
            status = "✓" if details["found"] else "✗"
            print(f"{status} {item}")

    def view_item_details(self, item):
        if item in self.checklist:
            details = self.checklist[item]
            status = "✓" if details["found"] else "✗"
            print(f"{status} {item}: {details['description']}")
            if details["found"]:
                if "link" in details:
                    print(f"   Посилання: {details['link']}")
                else:
                    print("   Посилання: Немає посилання")
        else:
            print(f"Елемент {item} не знайдено в чек-листі.")

    def add_to_checklist(self, item, details, found=False, link=None):
        self.checklist[item] = {"description": details, "found": found, "link": link}
        print(f"{item} додано до чек-листа.")

    def search_equipment(self, keyword):
        pass

    def place_order(self):
        # Логіка замовлення спорядження
        pass

    def modify_item(self, item):
        if item in self.checklist:
            print(f"Модифікуємо елемент: {item}")
            new_details = input("Введіть нові деталі: ")
            new_link = input("Введіть нове посилання (залиште порожнім, якщо не хочете змінювати): ")
            self.checklist[item]["description"] = new_details
            if new_link:
                self.checklist[item]["link"] = new_link
            print("Елемент модифіковано.")
        else:
            print(f"Елемент {item} не знайдено в чек-листі.")

    def remove_item(self, item):
        if item in self.checklist:
            del self.checklist[item]
            print(f"Елемент {item} видалено з чек-листа.")
        else:
            print(f"Елемент {item} не знайдено в чек-листі.")

    def mark_as_found(self, item, link=None):
        if item in self.checklist:
            self.checklist[item]["found"] = True
            if link:
                self.checklist[item]["link"] = link
            print(f"Елемент {item} позначено як знайдений.")
        else:
            print(f"Елемент {item} не знайдено в чек-листі.")

    def mark_as_not_found(self, item):
        if item in self.checklist:
            self.checklist[item]["found"] = False
            self.checklist[item].pop("link", None)
            print(f"Елемент {item} позначено як не знайдений.")
        else:
            print(f"Елемент {item} не знайдено в чек-листі.")
    
    def create_base_checklist(self):
        response = input("Чи бажаєте отримати базовий чек-лист? (Так/Ні): ").lower()
        if response == "так":
            base_checklist = {
                "Рюкзак": {"description": "Модель MIL-TEC А-TACS FG 36 Л", "found": False,
                            "link": "https://militarka.com.ua/ua/rjukzak-shturmovoj-bol-shoj-mil-tec-a-tacs-fg-36-l.html"},
                "Рейвенкавер": {"description": "Трекмейтс накидка для рюкзака", "found": False,
                                "link": "https://highlander.com.ua/nakidka-trekmates-backpack-raincover-45l-sirij"},
                # Додайте інші предмети за необхідністю
            }

            self.checklist.update(base_checklist)
            print("Створено базовий чек-лист.")

def main():
    organizer = TacticalOrganizer()
    organizer.create_base_checklist()

    while True:
        organizer.display_menu()

        choice = input("Введіть номер опції: ")

        if choice == '1':
            organizer.view_checklist()
        elif choice == '2':
            item = input("Введіть назву елементу: ")
            details = input("Введіть деталі елементу: ")
            link = input("Введіть HTTP посилання на елемент (за бажанням): ")
            organizer.add_to_checklist(item, details, link=link)
        elif choice == '3':
            item_to_modify = input("Введіть назву елементу для модифікації: ")
            organizer.modify_item(item_to_modify)
        elif choice == '4':
            item_to_remove = input("Введіть назву елементу для видалення: ")
            organizer.remove_item(item_to_remove)
        elif choice == '5':
            keyword = input("Введіть ключове слово для пошуку: ")
            organizer.search_equipment(keyword)
        elif choice == '6':
            organizer.place_order()
        elif choice == '7':
            item_to_mark_found = input("Введіть назву елементу, який ви знайшли: ")
            link_found_item = input("Введіть HTTP посилання на знайдений елемент (за бажанням): ")
            organizer.mark_as_found(item_to_mark_found, link_found_item)
        elif choice == '8':
            item_to_mark_not_found = input("Введіть назву елементу, який ви не знайшли: ")
            organizer.mark_as_not_found(item_to_mark_not_found)
        elif choice == '9':
            item_to_view_details = input("Введіть назву елементу для перегляду деталей: ")
            organizer.view_item_details(item_to_view_details)
        elif choice == '10':
            print("Дякуємо за використання Тактичного Органайзера. До побачення!")
            break
        else:
            print("Будь ласка, введіть правильний номер опції.")

if __name__ == "__main__":
    main()
