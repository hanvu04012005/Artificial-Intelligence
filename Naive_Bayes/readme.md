
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
### Độ tin cậy: 85.34%
```
### Biểu đồ ROC:
<img width="747" height="499" alt="image" src="https://github.com/user-attachments/assets/adc0ee68-f233-4b42-b7c2-5e4cc46e9796" />

###  Biểu đồ xác suất:
<img width="746" height="555" alt="image" src="https://github.com/user-attachments/assets/11450769-6702-4faa-8042-43da07864079" />
---
---
##  Kết luận
- Ứng dụng Naive Bayes để phân loại cảm xúc, dự đoán thông qua mô hình đã train
- Biết cách dùng Gradio để demo mô hình dễ dàng
