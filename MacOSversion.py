import tkinter as tk
from tkinter import messagebox
import time
import threading


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Таймер 1:40")
        self.root.geometry("300x150")
        
        # Настройка интерфейса (нативно и просто)
        self.label = tk.Label(root, text="Нажмите кнопку для старта\nУведомления каждые 2 мин (на 1:40)", pady=20)
        self.label.pack()

        self.btn_start = tk.Button(root, text="НАЧАТЬ", command=self.start_timer, 
                                   width=15, height=2, bg="#e1e1e1")
        self.btn_start.pack()


    def show_notification(self):
        # Создает всплывающее окно поверх всех окон
        top = tk.Toplevel()
        top.title("Внимание!")
        top.geometry("250x100+10+10") # Позиция (почти в углу)
        top.attributes("-topmost", True) # Всегда сверху
        
        tk.Label(top, text="Прошло 1:40, 3:40...\nПора действовать!", pady=10).pack()
        tk.Button(top, text="OK", command=top.destroy).pack()
        

    def run_logic(self):
        start_time = time.time()
        while True:
            time.sleep(1)
            elapsed = int(time.time() - start_time)
            
            # Проверка условий: 100 сек (1:40), 220 сек (3:40) и т.д.
            # Формула: (время + 20) делится на 120 без остатка
            if elapsed > 0 and (elapsed + 20) % 120 == 0:
                # Запуск уведомления в основном потоке интерфейса
                self.root.after(0, self.show_notification)
                time.sleep(2) # Чтобы не спамило в ту же секунду

    def start_timer(self):
        self.btn_start.config(state="disabled", text="РАБОТАЕТ")
        # Запускаем фоновый поток, чтобы программа не зависла
        thread = threading.Thread(target=self.run_logic, daemon=True)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
