import tkinter as tk
import get_values
import time

fenster = tk.Tk()

core_temeratue = get_values.core_temperature()
RAM_toal, RAM_used, RAM_free = get_values.RAM()
RAM_percent_used = round(int(RAM_used)*100/int(RAM_toal),1)

tk.Label(text = "Core temerature: %s°C"%core_temeratue).pack()
tk.Label(text = "Total RAM: %skb"%RAM_toal).pack()
tk.Label(text = "Used RAM: %skb"%RAM_used).pack()
tk.Label(text = "Free RAM: %skb"%RAM_free).pack()
tk.Label(text = "Used RAM: %s%%"%RAM_percent_used).pack()
time.sleep(1)
fenster.mainloop()