# Lab 4: Thuật Toán Di Truyền  
**Họ tên:** Nguyễn Hạn Vũ  
**MSSV:** 2374802010571  
**Môn học:** Nhập môn Trí tuệ nhân tạo  
**Giảng viên:** Nguyễn Thái Anh  

---

## Mục tiêu của lab  
Trong lab này, em được làm quen với cách thuật toán di truyền hoạt động và cách áp dụng nó vào một số bài toán đơn giản. Chủ yếu là để hiểu các bước chính của thuật toán như chọn lọc, lai ghép, đột biến, và thử nghiệm thực tế bằng Python.
---

## Ý tưởng cơ bản về thuật toán di truyền  
Thuật toán di truyền (Genetic Algorithm – GA) là một cách để giải bài toán tối ưu, được lấy ý tưởng từ quá trình tiến hóa trong sinh học.
Mỗi lời giải trong GA được coi là một “cá thể” trong quần thể. Qua từng thế hệ, các cá thể tốt (có giá trị tốt theo hàm đánh giá) sẽ được chọn ra, lai với nhau và có thể bị đột biến để tạo ra các cá thể mới. Mục tiêu là sau nhiều thế hệ, ta tìm được cá thể tốt nhất, tức là lời giải tối ưu cho bài toán.
Các bước cơ bản em hiểu được như sau:  
- Khởi tạo ban đầu một đám cá thể random  
- Tính mức độ “tốt” (fitness) của từng cá thể  
- Chọn ra các cá thể khỏe (fitness cao)  
- Lai ghép 2 cá thể lại với nhau  
- Đôi khi đột biến để tăng sự đa dạng  
- Cứ làm vậy lặp đi lặp lại, hy vọng đời sau sẽ tốt hơn đời trước  
---

## Nội dung bài làm  
### Bài 1: Tối ưu hàm bậc hai một biến  
Bài này tìm x sao cho hàm **f(x) = -x² + 10x + 50** đạt giá trị lớn nhất, trong đoạn từ 0 đến 10.  
- Em dùng chuỗi nhị phân để mã hóa x  
- Tính f(x) làm fitness  
- Qua nhiều thế hệ, em thấy giá trị x càng ngày càng gần với điểm cực đại  
- Có vẽ biểu đồ fitness theo từng thế hệ nên cũng dễ theo dõi tiến trình  

---
### Bài 2: Tối ưu hàm 2 biến  
Ở bài này, hàm là **g(x, y) = x² + y²**, yêu cầu tìm giá trị nhỏ nhất (tức là gần điểm (0, 0) nhất).  
- Em cũng mã hóa x và y bằng bit  
- Fitness là g(x, y) nhưng phải lấy dấu âm hoặc nghịch đảo vì GA muốn giá trị lớn  
- Kết quả ra được (x, y) nhỏ gần như bằng 0, đúng yêu cầu  

---
### Bài 3: Tối ưu hàm sin(x) + cos(x)  
Hàm này: **h(x) = sin(x) + cos(x)**, giới hạn x trong đoạn từ 0 đến 2π.  
- Khác với 2 bài đầu, x lần này được giữ nguyên là số thực  
- Quá trình chọn lọc dùng cách chọn theo giải đấu (tournament selection)  
- Sau vài chục thế hệ, giá trị x dần tiệm cận gần π/4, vì tại đó sin + cos đạt cực đại  
- Kết quả biểu đồ fitness tăng dần theo từng thế hệ nhìn rất dễ hiểu  

---
### Bài 4: Tối ưu chuỗi bit  
Bài này đơn giản nhưng rất hay. Mục tiêu là tìm ra chuỗi bit toàn số 1 (kiểu như 111111...).  
- Mỗi cá thể là một chuỗi bit (0 hoặc 1) độ dài cố định  
- Fitness = số lượng số 1 trong chuỗi đó  
- Thuật toán sẽ chọn các chuỗi có nhiều số 1, lai ghép lại và thêm chút đột biến  
- Cuối cùng hầu hết cá thể đều là chuỗi toàn 1  

---
### Bài 5: Tối ưu có ràng buộc  
Bài này khó hơn vì có thêm điều kiện ràng buộc (kiểu như x + y ≤ 10).  
- Trong code em phải kiểm tra sau mỗi lần lai ghép hoặc đột biến xem có thỏa mãn ràng buộc không  
- Nếu không thì bỏ qua hoặc chỉnh sửa lại  
- Đây là bài giúp em hiểu rõ hơn cách áp dụng GA vào các bài toán thực tế có giới hạn  
- Kết quả cho ra lời giải vừa tối ưu vừa hợp lệ  

---

## Công cụ dùng trong lab  
- **Python:** viết toàn bộ thuật toán  
- **NumPy:** để xử lý mảng và random số  
- **Matplotlib:** để vẽ biểu đồ theo dõi kết quả  
- **random:** để làm các bước chọn ngẫu nhiên  

---
## Kết luận  
Làm xong 5 bài trong lab, em thấy thuật toán di truyền tuy ban đầu nhìn có vẻ lạ, nhưng thực ra hiểu quy trình rồi thì làm cũng không quá khó. Chủ yếu là nắm được mấy phần chính như khởi tạo quần thể, tính fitness, chọn cá thể, lai ghép với đột biến là làm được.
Trong lúc làm em cũng nhận ra, mỗi bài lại có cái khác nhau, nên không thể áp dụng y chang nhau được. Ví dụ như có bài thì dùng bit, có bài dùng số thực, rồi có bài còn phải xử lý ràng buộc nữa.
Tự tay code từng phần làm em hiểu kỹ hơn về thuật toán, chứ không chỉ đọc lý thuyết rồi quên. Em thấy GA khá thú vị, dễ tùy biến và có thể dùng cho nhiều dạng bài toán tối ưu khác nhau.

---

## Tài liệu tham khảo  
- bài giảng lab  
- Wikipedia về Genetic Algorithm  

