import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cpu_percent = psutil.cpu_percent()
print(f"Uso da CPU: {cpu_percent}%")

memory = psutil.virtual_memory()
print(f"Uso de memória: {memory.percent}%")

disk_usage = psutil.disk_usage("/")
print(f"Uso de disco: {disk_usage.percent}%")


