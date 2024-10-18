import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

API_URL = "http://127.0.0.1:5000"

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Manager")

        tk.Button(root, text="Створити базу даних", command=self.create_database).pack(pady=10)
        tk.Button(root, text="Вибрати базу даних", command=self.use_database).pack(pady=10)
        tk.Button(root, text="Створити таблицю", command=self.create_table).pack(pady=10)
        tk.Button(root, text="Додати дані в таблицю", command=self.add_data).pack(pady=10)
        tk.Button(root, text="Переглянути таблицю", command=self.view_table).pack(pady=10)
        tk.Button(root, text="Пошук рядка", command=self.search_row).pack(pady=10)  # Додано нову кнопку
        tk.Button(root, text="Вихід", command=root.quit).pack(pady=10)

    def create_database(self):
        db_name = simpledialog.askstring("Введіть назву бази даних", "Назва:")
        if db_name:
            response = requests.post(f"{API_URL}/databases", json={"db_name": db_name})
            self.show_message(response)

    def use_database(self):
        db_name = simpledialog.askstring("Введіть назву бази даних", "Назва:")
        if db_name:
            response = requests.post(f"{API_URL}/databases/use", json={"db_name": db_name})
            self.show_message(response)

    def create_table(self):
        table_name = simpledialog.askstring("Введіть назву таблиці", "Назва:")
        if table_name:
            response = requests.post(f"{API_URL}/tables", json={"table_name": table_name})
            self.show_message(response)

    def add_data(self):
        table_name = simpledialog.askstring("Введіть назву таблиці", "Назва таблиці:")
        if table_name:
            row_data = simpledialog.askstring("Введіть дані", "Дані (JSON формат):")
            if row_data:
                try:
                    json_data = eval(row_data)  # Преобразування рядка в JSON
                    response = requests.post(f"{API_URL}/tables/{table_name}/add_data", json=json_data)
                    self.show_message(response)
                except Exception as e:
                    messagebox.showerror("Помилка", f"Неправильний формат даних: {e}")

    def view_table(self):
        table_name = simpledialog.askstring("Введіть назву таблиці", "Назва таблиці:")
        if table_name:
            response = requests.get(f"{API_URL}/tables/{table_name}")
            if response.status_code == 200:
                table_data = response.json()
                messagebox.showinfo("Дані таблиці", str(table_data))
            else:
                self.show_message(response)

    def search_row(self):
        table_name = simpledialog.askstring("Введіть назву таблиці", "Назва таблиці:")
        if table_name:
            field_name = simpledialog.askstring("Введіть назву поля", "Назва поля для пошуку:")
            field_value = simpledialog.askstring("Введіть значення", "Значення для пошуку:")
            if field_name and field_value:
                response = requests.get(f"{API_URL}/tables/{table_name}/search", params={"field_name": field_name, "field_value": field_value})
                if response.status_code == 200:
                    result_row = response.json()
                    messagebox.showinfo("Результат пошуку", str(result_row))
                else:
                    self.show_message(response)

    def show_message(self, response):
        if response.status_code == 200 or response.status_code == 201:
            messagebox.showinfo("Успіх", response.json().get("message", "Успішно!"))
        else:
            messagebox.showerror("Помилка", response.json().get("error", "Щось пішло не так."))


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
