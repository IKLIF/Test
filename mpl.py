import matplotlib.pyplot as plt
import numpy as np

# Создаем данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем график
plt.plot(x, y)

# Добавляем заголовок и подписи к осям
plt.title("Пример графика с использованием Matplotlib")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображаем график
plt.show()
