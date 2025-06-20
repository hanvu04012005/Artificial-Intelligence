#THỰC HÀNH 6:
Chương trình được viết bằng Python.
Thư viện sử dụng chính là:
NumPy: hỗ trợ tạo ma trận bàn cờ và thao tác dữ liệu dạng mảng nhanh chóng.
Built-in Python functions: sử dụng đệ quy và danh sách để tìm lời giải.
Bài toán sử dụng thuật toán Backtracking để tìm tất cả các cách đặt N quân hậu sao cho:
Không có hai quân hậu nào nằm cùng hàng, cùng cột, hoặc cùng đường chéo.
Quy trình:
Thử từng cột cho mỗi hàng
Nếu vị trí không hợp lệ thì bỏ qua và quay lại
Nếu hợp lệ thì tiếp tục sang hàng tiếp theo
Hàm này kiểm tra nếu đã đặt đủ N quân hậu thì là lời giải hợp lệ.


![image](https://github.com/user-attachments/assets/c77a3d93-23fa-4684-9596-b8ea876153a1)


hàm sinh các vị trí có thể đặt quân hậu tiếp theo
Hàm get_candidates loại bỏ những cột không hợp lệ:

![image](https://github.com/user-attachments/assets/42532623-3a65-45a7-9fb7-900fd0d19671)


Hàm đệ quy quay lại (Backtracking)


![image](https://github.com/user-attachments/assets/48f58ac8-b451-404d-bb6b-acef000456d4)


Hàm search sử dụng đệ quy để thử đặt từng quân hậu. Khi lời giải hợp lệ thêm vào danh sách.
Hàm tổng hợp lời giải

![image](https://github.com/user-attachments/assets/a4ebad2e-237d-4747-99db-29d8f60693fa)


Hàm main: chạy chương trình

![image](https://github.com/user-attachments/assets/5929b77a-ce80-4cd2-ad4c-d485c37a9e31)


#THỰC HÀNH 7:
Công nghệ sử dụng
Python
NumPy: để tạo mảng bàn cờ
Random: dùng chọn ngẫu nhiên lời giải để hiển thị
#Hàm kiểm tra trạng thái hợp lệ

![image](https://github.com/user-attachments/assets/a1b5a15d-5862-4071-88f2-51d9308eafdf)

state là danh sách lưu vị trí các quân hậu (cột đặt của mỗi hàng)
#Hàm lấy các vị trí cột có thể đặt tiếp theo

![image](https://github.com/user-attachments/assets/aca8c779-4257-4c94-a189-3cd03f2df3c9)

#Hàm tổng quát giải bài toán
![image](https://github.com/user-attachments/assets/a185ae4f-8ccf-4db4-98b7-c297de0a8a45)


Code dùng backtracking để tìm ra mọi cách đặt N quân hậu hợp lệ.
Dễ mở rộng,in ra rõ ràng bàn cờ, tọa độ.
