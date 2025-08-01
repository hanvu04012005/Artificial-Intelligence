Ôn Tập AI - Lab Cuối Kỳ
Họ tên: Nguyễn Hạn Vũ
MSSV: 2374802010571
Môn học: Nhập môn Trí tuệ nhân tạo
Giảng viên: Nguyễn Thái Anh

CÂU 1: TÌM DFS TRÊN ĐỒ THỊ
Yêu cầu: Duyệt đồ thị theo chiều sâu (DFS) từ một đỉnh xuất phát.

Đồ thị:


Hướng dẫn:

Biểu diễn đồ thị dưới dạng danh sách kề.

Viết hàm DFS đệ quy để in thứ tự các đỉnh được thăm.

Bỏ qua trọng số cạnh vì DFS không phụ thuộc vào trọng số.

Ví dụ Python:

python
Sao chép
Chỉnh sửa
graph = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 5, 7, 9],
    4: [1, 5, 6],
    5: [2, 3, 4, 6],
    6: [4, 5, 7],
    7: [3, 6, 8, 9],
    8: [7, 9],
    9: [3, 7, 8]
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(1)  # Hoặc đổi đỉnh xuất phát tùy đề bài
CÂU 2: Tối Ưu Hóa Hàm Một Biến
Bài toán:
Tìm giá trị lớn nhất của hàm:

𝑓
(
𝑥
)
=
−
𝑥
2
+
10
𝑥
+
50
,
𝑥
∈
[
0
,
10
]
f(x)=−x 
2
 +10x+50,x∈[0,10]
Ý tưởng:

Áp dụng thuật toán di truyền (Genetic Algorithm - GA)

Mã hóa x dưới dạng chuỗi nhị phân

Fitness là giá trị của hàm f(x)

Thực hiện chọn lọc, lai ghép và đột biến qua nhiều thế hệ

Kết quả mong đợi:
x gần 5, vì tại đó f(x) đạt cực đại.

CÂU 3: Phân Loại Chó và Mèo bằng CNN
Dữ liệu:
Từ Kaggle: Dogs vs Cats Dataset

Yêu cầu:

Xây dựng mô hình học sâu CNN để phân loại hình ảnh chó/mèo

Các bước:

Tiền xử lý dữ liệu (resize, augment)

Xây dựng mô hình CNN (Keras/TensorFlow)

Huấn luyện và đánh giá mô hình

Kiểm thử trên ảnh mới

Gợi ý cấu trúc CNN đơn giản:

python
Sao chép
Chỉnh sửa
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])
CÂU 4: Dự Đoán Chơi hay Không bằng Naive Bayes
Tập dữ liệu:

Day	Outlook	Temperature	Humidity	Wind	Play
...	...	...	...	...	...

Yêu cầu:

Dự đoán cột Play (Yes/No) bằng mô hình Naive Bayes

Sử dụng dữ liệu phân loại (Categorical)

Áp dụng Laplace smoothing (nếu cần)

Các bước:

Mã hóa đặc trưng thành dạng số (Label Encoding)

Áp dụng Naive Bayes phân loại rời rạc (sklearn.naive_bayes.CategoricalNB)

Dự đoán mẫu mới

Ví dụ Python (dùng sklearn):

python
Sao chép
Chỉnh sửa
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Giả sử bạn đã nhập DataFrame `df` từ bảng
for col in ['Outlook', 'Temperature', 'Humidity', 'Wind', 'Play']:
    df[col] = LabelEncoder().fit_transform(df[col])

X = df[['Outlook', 'Temperature', 'Humidity', 'Wind']]
y = df['Play']

model = CategoricalNB()
model.fit(X, y)

# Dự đoán
sample = [[1, 2, 0, 1]]  # Tùy mẫu mới
print("Dự đoán:", model.predict(sample))
Kết luận
Trong 4 câu hỏi ôn tập, em đã áp dụng các kỹ thuật cốt lõi của trí tuệ nhân tạo:

Cấu trúc dữ liệu & thuật toán (DFS)

Tối ưu hoá với thuật toán di truyền

Học sâu với CNN

Học máy với Naive Bayes
