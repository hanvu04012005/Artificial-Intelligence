1. Sử dụng BFS và DFS trên **Đồ thị mẫu 2** . Thêm chú thích chi tiết vào mã của bạn.
Đồ thị 2 BFS:
![image](https://github.com/user-attachments/assets/5ebaf10c-42f0-475d-8018-b44e5d1fe413)
Đồ thị 2 DFS:
![image](https://github.com/user-attachments/assets/e064c0d8-e7a7-4cc8-a954-a04ad5302d60)
2. Sửa mã BFS để đếm số nút đã thăm trên **Đồ thị mẫu 4**. In ra kết quả và đảm bảo mã có chú thích đầy đủ.
Đồ thị 4 BFS (THÊM NÚT ĐÃ THĂM)
   Nút đã thăm:
   ![image](https://github.com/user-attachments/assets/d2de4c86-d647-4d94-9656-08d16c8a659e)
   Đồ thị sau khi chạy:
   ![image](https://github.com/user-attachments/assets/1fbb5d4f-f3d4-4ed2-b6f5-e91edce65e91)
1. Viết mã Python để chạy BFS và DFS trên **Đồ thị mẫu 6** và **Đồ thị mẫu 7**. Định nghĩa đồ thị dưới dạng từ điển và thêm chú thích chi tiết.
   Đồ thị 6 BFS:
    ![image](https://github.com/user-attachments/assets/7633588f-e76c-469e-bc62-4226f39d249c)
   Đồ thị 6 DFS:
    ![image](https://github.com/user-attachments/assets/70a33e94-63ba-45dc-b225-146d27ec8b73)
   Đồ thị 7 BFS:
    ![image](https://github.com/user-attachments/assets/8dd11869-0f5a-4255-a2dd-8fd5fe863681)
   Đồ thị 7 DFS:
    ![image](https://github.com/user-attachments/assets/04fb2351-bdc0-4d4e-928c-bce5d83d5caa)
2. Sửa mã BFS để lưu và in tất cả các đường đi từ S đến H trên **Đồ thị mẫu 7** (không trọng số). Đảm bảo mã có chú thích đầy đủ.
![image](https://github.com/user-attachments/assets/40feebaf-4ff0-453a-9c36-dafc9ebaba86)
![image](https://github.com/user-attachments/assets/bc8dfd4b-de43-41fe-be4e-d5e91bcd7f95)
3. Thêm một cạnh mới vào **Đồ thị mẫu 6** (ví dụ: B-H với trọng số 20). Chạy lại BFS và DFS, phân tích sự thay đổi trong đường đi và tổng trọng số.
   BFS đồ thị 6 sau khi thêm B-H với trọng số 20:
   ![image](https://github.com/user-attachments/assets/9c4916b0-aac3-4f6d-8d6e-aca1656880b8)
    thay đổi từ S-A-B-E-H thành S-A-B-H
    lí do : BFS ƯU TIÊN DÒ THEO CẠNH KHÔNG DÒ THEO TRỌNG SỐ NÊN TRỌNG SỐ CỦA S-A-B-H LỚN HƠN S-A-B-E-H (25>21)
   DFS đồ thị 6 sau khi thêm B-H với trọng số 20:
   ![image](https://github.com/user-attachments/assets/9e107505-147a-4ec5-8bf4-412ca4351c07)
    không thay đổi đường đi và trọng số :S-A-B-E-H (tổng trọng số 21)
   lí do: vì nó duyệt theo chiều sâu và tùy vào cạnh nó duyệt
   Trong đồ thị, DFS duyệt A trước, khi đến A thì sẽ thấy B và D nếu ở đây, chọn xét B đầu tiên thì đường đi sẽ đi theo B E H vì B nối với E với H và H là điểm đến
    Tóm tại, tùy thuộc vào đỉnh nào được xét trước
### Bài Tập Nâng Cao
1. Đo thời gian chạy của BFS và DFS trên **Đồ thị mẫu 6** và **Đồ thị mẫu 7** bằng thư viện `time`. So sánh hiệu suất và thêm chú thích vào mã.
   Phần được thêm vào :
   Đồ thị 6:
     ![image](https://github.com/user-attachments/assets/d5ff0004-c2f9-408a-9198-448d555a0fd3)
     ![image](https://github.com/user-attachments/assets/80088b91-3d58-4b68-8e4d-c35ce1c23755)
   kết quả đồ thị 6:
     ![image](https://github.com/user-attachments/assets/33301794-28e6-44ca-b219-7b054e2f66f2)
   Đồ thị 7:
     ![image](https://github.com/user-attachments/assets/efc87a50-2b0e-487f-a827-e3a62d79ef13)
     ![image](https://github.com/user-attachments/assets/7398c29d-2c93-428e-8732-32935acbfa8d)
   kết quả đồ thị 7:
     ![image](https://github.com/user-attachments/assets/a492ca43-9a29-4f6b-8286-1aa50ed53cdf)
 
3. Thiết kế một đồ thị có trọng số với ít nhất 10 nút và 15 cạnh. Chạy BFS và DFS, phân tích đường đi và tổng trọng số. Đảm bảo mã có chú thích chi tiết.
   Đồ thị mới được thiết kế :
   ![image](https://github.com/user-attachments/assets/ad891bd7-a416-4cc1-a6cf-1c8baac887bc)
   code phần kết quả chi tiết và phân tích đường đi :
   ![image](https://github.com/user-attachments/assets/de93216f-0865-4c77-bbec-ff1ee6f0d0dc)
  kết quả kèm phân tích:
![image](https://github.com/user-attachments/assets/343f92c7-16c9-44bb-afe7-528a825c9777)

   

   



