import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# Ma trận ảnh gốc
image = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1]
])

# Kernel Sobel dọc
kernel = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])

# Tính feature map bằng tích chập 2D
feature_map = convolve2d(image, kernel, mode='valid')

# Vẽ ảnh
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Hiển thị ảnh gốc
sns.heatmap(image, cmap="Greys", cbar=True, annot=True, ax=axs[0])
axs[0].set_title("Ảnh gốc")

# Hiển thị Feature map (sau khi áp kernel)
sns.heatmap(feature_map, cmap="RdBu_r", center=0, cbar=True, annot=True, ax=axs[1])
axs[1].set_title("Feature Map (Sobel dọc)")

plt.tight_layout()
plt.show()
