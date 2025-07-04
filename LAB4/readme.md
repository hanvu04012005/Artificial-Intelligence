
# Lab 4: Thuật Toán Di Truyền  
**Họ tên:** Nguyễn Hạn Vũ    
**MSSV:** 2374802010571
**Môn học:** Nhập môn Trí tuệ nhân tạo  
**Giảng viên:** Nguyễn Thái Anh  

---

## Mục tiêu của lab  
Trong bài lab này, em học cách dùng thuật toán di truyền để giải một số bài toán tối ưu đơn giản. Mục tiêu chính là hiểu được cách hoạt động của GA (Genetic Algorithm) và thử viết code mô phỏng nó bằng Python.

---

## Ý tưởng chính về thuật toán di truyền  
Thuật toán di truyền bắt chước cơ chế tiến hóa tự nhiên. Mỗi "cá thể" đại diện cho một lời giải, và qua từng thế hệ, thuật toán chọn ra các cá thể tốt để tạo ra thế hệ sau tốt hơn.  

Các bước chính gồm:  
- Khởi tạo một quần thể ban đầu ngẫu nhiên  
- Đánh giá từng cá thể dựa vào hàm fitness  
- Chọn ra các cá thể tốt (selection)  
- Lai ghép 2 cá thể với nhau (crossover)  
- Đột biến một vài điểm trong cá thể (mutation)  
- Lặp lại nhiều vòng để cải thiện lời giải

---

## Nội dung thực hành

### Bài 1: Tối ưu hàm 1 biến  
Bài toán là tìm giá trị x (trong khoảng 0 đến 10) sao cho hàm  
f(x) = -x² + 10x + 50  
đạt giá trị lớn nhất.  

Em dùng GA để biểu diễn x thành chuỗi nhị phân, sau đó tính fitness bằng f(x). Chạy nhiều thế hệ để tìm x tốt nhất. Kết quả cuối cùng sẽ vẽ ra biểu đồ cho thấy fitness tăng dần.

---

### Bài 2: Tối ưu hàm 2 biến  
Bài này là tìm cặp (x, y) sao cho  
g(x, y) = x² + y²  
là nhỏ nhất (tức là càng gần gốc tọa độ càng tốt).  

Cũng dùng GA để mã hóa x và y rồi áp dụng tương tự như bài 1. Kết quả em được là điểm (x, y) gần 0 nhất sau nhiều thế hệ.

---

## Dụng cụ sử dụng  
- Python: ngôn ngữ lập trình  
- NumPy: để xử lý mảng và tạo ngẫu nhiên  
- Matplotlib: để vẽ đồ thị


---

## Kết luận  
Qua bài lab này em hiểu rõ hơn cách hoạt động của thuật toán di truyền. Mặc dù đơn giản nhưng nó rất hay, có thể áp dụng cho nhiều bài toán tìm kiếm lời giải tối ưu. Việc tự viết mã giúp em nhớ lâu hơn và hiểu từng bước GA hoạt động như thế nào.

---

## Tài liệu tham khảo  
- xem lý thuyết phần lab, bài giảng   

