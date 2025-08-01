# thuật toán Minimax

## Thông tin sinh viên

* **Họ tên**: Nguyễn Hạn Vũ
* **MSSV**: 2374802010571
* **Môn học**: Nhập môn Trí tuệ nhân tạo
* **Giảng viên**: Nguyễn Thái Anh

---

## Nội dung bài thực hành

Mục tiêu của bài tập là xây dựng một AI có khả năng chơi trò chơi Tic Tac Toe (3x3) với người chơi bằng thuật toán **Minimax**. Bài làm được trình bày dưới hai dạng:

### 1. File `codeSlide.ipynb`

* Có cấu trúc như một bản slide trình bày các bước từ lý thuyết đến triển khai.
* Chia thành 4 câu hỏi chính:

  * Cài đặt luật chơi và bàn cờ.
  * Xây dựng Agent AI.
  * Áp dụng thuật toán Minimax.
  * Phân tích và truy vết lời giải.

### 2. File `caitien`

* Chứa đầy đủ mã lệnh để chạy một vòng chơi thực sự.
* AI và người chơi luân phiên đánh cờ trên bàn.
* Kết quả in ra bàn cờ sau mỗi lượt và kết thúc khi có người thắng hoặc hòa.

---

## Tổng quan thuật toán Minimax

Minimax là một giải thuật tìm kiếm được dùng trong các trò chơi mang tính đối kháng, như cờ caro. Ý tưởng là:

* AI (Max) muốn chọn nước đi có điểm cao nhất.
* Người chơi (Min) muốn chọn nước đi khiến AI bị điểm thấp nhất.
* Duyệt hết các trạng thái có thể xảy ra sau mỗi nước đi để đánh giá.
* Đệ quy quay lui về để lựa chọn nước đi tối ưu.

Kết hợp với kiểm tra điều kiện thắng/thua và sinh nước đi, AI sẽ không bao giờ thua nếu thuật toán được cài đặt đúng.

---

## Thư viện và công cụ

* **Python** (3.x)
* **Jupyter Notebook**
* **Thư viện sử dụng**:

  * `numpy`
  * `copy`
  * `IPython.display`

---
## So sánh 2 file

| Tiêu chí       | `codeSlide.ipynb`         | `cai tien.ipynb`                    |
| -------------- | ------------------------- | ------------------------------ |
| Mục đích       | Giải thích thuật toán     | Triển khai và tương tác        |
| Định hướng     | Dùng cho báo cáo trên lớp | Dùng để chạy và test trực tiếp |
| Tính tương tác | Không                     | Có                             |
| Thuận tiện cho | Slide thuyết trình        | Demo game AI vs người          |

---

---
## Kết luận
* Bài làm áp dụng đúng thuật toán Minimax.
* AI có khả năng đưa ra nước đi hợp lý.
* Có thể mở rộng sang các dạng trò chơi lớn hơn hoặc tối ưu bằng alpha-beta pruning.

