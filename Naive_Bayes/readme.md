# EDUCATION
Xây dựng một mô hình đơn giản giúp cphân nội dung(tích cực hoặc tiêu cực) sử dụng thuật toán **Bernoulli Naive Bayes**. Kết quả được hiển thị rõ ràng bằng:
- Kết luận cảm xúc (`positive` hoặc `negative`)
- Mức độ tin cậy dự đoán
- Biểu đồ ROC tổng hợp
- Biểu đồ xác suất dự đoán cho từng lớp
Giao diện người dùng được xây dựng bằng thư viện Gradio
---
##  Các bước xử lý chính trong mã

### 1. Nạp dữ liệu (`load_data`)
```python
def load_data():
    return pd.read_csv('Naive_Bayes/Education.csv')
```
- Đọc file CSV chứa văn bản và nhãn (Label: positive/negative).
---
### 2. Chia dữ liệu train/test (`split_train_test`)
```python
def split_train_test(data, ratio_test=0.2):
```
- Trộn ngẫu nhiên dữ liệu và chia thành 80% để huấn luyện, 20% để kiểm tra.
---
### 3. **Huấn luyện mô hình** (`train_model`)
```python
model = BernoulliNB()
model.fit(X_train_vect, y_train_bin)
```
- Vector hóa văn bản bằng `CountVectorizer` (biến văn bản thành ma trận nhị phân).
- Huấn luyện mô hình **Bernoulli Naive Bayes** trên tập huấn luyện.
- Dùng tập test để tính toán biểu đồ **ROC**.

---
### 4. Dự đoán văn bản 
```python
X_input = vectorizer.transform([text])
pred_label = model.predict(X_input)[0]
```
- Nhận input từ người dùng.
- Dự đoán (`POSITIVE` hoặc `NEGATIVE`) và tính xác suất tương ứng.
- Trả về kết quả và vẽ 2 biểu đồ:
  - Biểu đồ **ROC** thể hiện độ phân biệt của mô hình.
  - Biểu đồ **Xác suất dự đoán** trực quan hóa mức độ tin cậy cho từng lớp.
---
### 5. **Giao diện người dùng với Gradio**
```python
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(...),
    outputs=[gr.Markdown(...), gr.Image(...), gr.Image(...)],
)
```
- Dùng `gr.Interface` để tạo một app có giao diện web đơn giản.
- Người dùng nhập văn bản, kết quả sẽ hiện ra cùng với 2 biểu đồ.
---
##  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/74f03c0e-f5a5-46dd-8f9b-09e3d0868d85" />

###  Kết quả dự đoán:
```
### Kết quả: POSITIVE
### Độ tin cậy: 77.88%
```
### Biểu đồ ROC:
<img width="747" height="499" alt="image" src="https://github.com/user-attachments/assets/adc0ee68-f233-4b42-b7c2-5e4cc46e9796" />

###  Biểu đồ xác suất:
<img width="746" height="555" alt="image" src="https://github.com/user-attachments/assets/11450769-6702-4faa-8042-43da07864079" />



```


```

##  Kết luận
- Ứng dụng Naive Bayes để phân loại cảm xúc, dự đoán thông qua mô hình đã train
- Biết cách dùng Gradio để demo mô hình dễ dàng


# DRUG
## Dự đoán loại thuốc bằng Gaussian Naive Bayes

Ứng dụng này giúp **dự đoán loại thuốc phù hợp** cho bệnh nhân dựa trên các thông tin y tế cơ bản như **tuổi, giới tính, huyết áp, cholesterol** và **tỉ lệ Na_to_K**.  
Mô hình sử dụng thuật toán **Gaussian Naive Bayes**, được huấn luyện trên tập dữ liệu `drug200.csv`.

Giao diện người dùng được xây dựng bằng **Gradio** – trực quan, dễ sử dụng, có thể chạy trực tiếp trên trình duyệt.

---

## Tính năng chính

- Nhập thông tin y tế của bệnh nhân (tuổi, giới tính, huyết áp, cholesterol, Na_to_K)
- Dự đoán loại thuốc (Drug A/B/C/X/Y) phù hợp
- Hiển thị **kết luận rõ ràng** và **biểu đồ xác suất dự đoán**
- Chạy nhanh, giao diện đơn giản
### 1. Nạp dữ liệu (`load_data`)
```python
def load_data():
    data = pd.read_csv('Naive_Bayes/drug200.csv')
```
- Đọc file CSV chứa văn bản và nhãn (Label: positive/negative).
---
### 2. Chia dữ liệu train/test (`split_train_test`)
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

```
- Trộn ngẫu nhiên dữ liệu và chia thành 80% để huấn luyện, 20% để kiểm tra.
---
### 3. **Huấn luyện mô hình** (`train_model`)
```python
model = GaussianNB()
model.fit(X_train, y_train)

```
- Vector hóa văn bản bằng `CountVectorizer` (biến văn bản thành ma trận nhị phân).
- Huấn luyện mô hình **Bernoulli Naive Bayes** trên tập huấn luyện.
- Dùng tập test để tính toán biểu đồ **ROC**.

---
### 4. Dự đoán kết quả
```python
y_pred = model.predict(input_df)[0]
y_proba = model.predict_proba(input_df)[0]
```
- Nhận input từ người dùng.
- Dự đoán (`POSITIVE` hoặc `NEGATIVE`) và tính xác suất tương ứng.
- Trả về kết quả và vẽ 2 biểu đồ:
  - Biểu đồ **ROC** thể hiện độ phân biệt của mô hình.
  - Biểu đồ **Xác suất dự đoán** trực quan hóa mức độ tin cậy cho từng lớp.
---
### 5. **Giao diện người dùng với Gradio**
```python
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(...),
    outputs=[gr.Markdown(...), gr.Image(...), gr.Image(...)],
)
```
- Dùng `gr.Interface` để tạo một app có giao diện web đơn giản.
- Người dùng nhập văn bản, kết quả sẽ hiện ra cùng với 2 biểu đồ.
---

## 6 Mô hình học máy

- **Thuật toán:** Gaussian Naive Bayes (`sklearn.naive_bayes.GaussianNB`)
- **Dữ liệu huấn luyện:** `drug200.csv` gồm các cột:
  - `Age`, `Sex`, `BP`, `Cholesterol`, `Na_to_K`, `Drug`
- **Xử lý dữ liệu:**
  - Chuyển đổi nhãn văn bản thành dạng one-hot (`get_dummies`)
  - Ánh xạ `Drug` thành số để mô hình học
- **Train/Test split:** 70% train – 30% test

---

##  Giao diện Gradio

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d72fb438-14ae-463b-8675-e3cf0a8c271f" />


### Ví dụ kết quả:
```
### Dự đoán loại thuốc: `drugA`
### Độ tin cậy: `100%`
```
<img width="762" height="669" alt="image" src="https://github.com/user-attachments/assets/51a325ce-d438-447b-ae58-f3da39d1e503" />


---

##  Thư viện sử dụng

- `pandas`, `numpy`: Xử lý dữ liệu
- `scikit-learn`: Mô hình GaussianNB
- `matplotlib`: Biểu đồ trực quan hóa
- `gradio`: Tạo giao diện người dùng đơn giản




