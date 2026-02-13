import os


class ShoppingList:

    def __init__(self, filename="shopping_list.txt"):
        self.filename = filename
        self.items = {} 
        self.load_items()

    
    
   

    def start_menu(self):
        print("\n====== Shopping List Manager ======")
        print("Type item name to add (example: Milk x2)")
        print("Commands:")
        print("SHOW   - Display list")
        print("REMOVE - Remove an item")
        print("SEARCH - Search by name")
        print("CLEAR  - Clear entire list")
        print("HELP   - Show menu")
        print("DONE   - Save and exit")
        print("===================================")

    def add_to_list(self, item):
        name, qty = self._parse_item(item)

        if name in self.items:
            self.items[name] += qty
            print(f"Updated {name} quantity to {self.items[name]}.")
        else:
            self.items[name] = qty
            print(f"{name} added with quantity {qty}.")

        print(f"Total unique items: {len(self.items)}")

    def remove_item(self, item):
        name = self._normalize(item)

        if name in self.items:
            del self.items[name]
            print(f"{name} removed from list.")
        else:
            print(f"{name} not found.")

    def show_shopping_list(self):
        if not self.items:
            print("Shopping list is empty.")
            return

        print("\nMy Shopping List:")
        for name in sorted(self.items.keys()):
            qty = self.items[name]
            print(f"- {name} (x{qty})")

    def save_items(self):
        try:
            with open(self.filename, "w") as file:
                for name, qty in self.items.items():
                    file.write(f"{name},{qty}\n")
            print("Shopping list saved.")
        except Exception:
            print("Error saving file.")

    def load_items(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        name, qty = line.split(",")
                        self.items[name] = int(qty)
        except Exception:
            print("Error loading file. Starting fresh.")
            self.items = {}

    
    # Extra Features
   

    def clear_list(self):
        confirm = input("Are you sure you want to clear the list? (yes/no): ")
        if confirm.lower() == "yes":
            self.items.clear()
            print("Shopping list cleared.")
        else:
            print("Clear cancelled.")

    def search_item(self, keyword):
        keyword = keyword.lower()
        found = False

        for name in self.items:
            if keyword in name.lower():
                print(f"Found: {name} (x{self.items[name]})")
                found = True

        if not found:
            print("No matching items found.")

    
    
    def _normalize(self, text):
        return text.strip().capitalize()

    def _parse_item(self, text):
        text = text.strip()

        if "x" in text.lower():
            parts = text.lower().split("x")
            name = self._normalize(parts[0])
            try:
                qty = int(parts[1])
                if qty <= 0:
                    qty = 1
            except:
                qty = 1
        else:
            name = self._normalize(text)
            qty = 1

        return name, qty



# Main Program


def main():
    app = ShoppingList()
    app.start_menu()

    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            command = user_input.lower()

            if command == "done":
                print("Exiting... Goodbye!")
                app.save_items()
                app.show_shopping_list()
                break

            elif command == "help":
                app.start_menu()

            elif command == "show":
                app.show_shopping_list()

            elif command == "remove":
                item = input("Item to remove: ")
                app.remove_item(item)

            elif command == "clear":
                app.clear_list()

            elif command == "search":
                keyword = input("Enter keyword to search: ")
                app.search_item(keyword)

            else:
                app.add_to_list(user_input)

        except EOFError:
            print("\nEOF detected. Saving before exit...")
            app.save_items()
            break


if __name__ == "__main__":
    main()