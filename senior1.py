import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# 创建一个 2x2 的子图布局
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 行 2 列

# 绘制子图
axs[0, 0].plot(x, y1, color='b')
axs[0, 0].set_title("Subplot A")
axs[0, 0].set_ylabel("Amplitude")
axs[0, 0].set_xlabel("Time")

axs[0, 1].plot(x, y2, color='g')
axs[0, 1].set_title("Subplot B")
axs[0, 1].set_ylabel("Amplitude")
axs[0, 1].set_xlabel("Time")

axs[1, 0].plot(x, y3, color='r')
axs[1, 0].set_title("Subplot C")
axs[1, 0].set_ylabel("Amplitude")
axs[1, 0].set_xlabel("Time")
axs[1, 0].set_ylim(-10, 10)  # 限制 tan 图形的 y 轴范围

axs[1, 1].plot(x, y4, color='orange')
axs[1, 1].set_title("Subplot D")
axs[1, 1].set_ylabel("Amplitude")
axs[1, 1].set_xlabel("Time")

# 添加子图标签
for i, ax in enumerate(axs.flat):
    ax.text(-0.1, 1.1, f"({chr(97 + i)})", transform=ax.transAxes, 
            fontsize=14, fontweight='bold', va='top', ha='right')

# 调整布局
plt.tight_layout()
plt.show()
