# Thực hành: Reinforcement Learning – Giải bài toán Mê cung 6x6

## Sinh viên thực hiện:

* Nguyễn Hạn Vũ
* Mã sinh viên: 2374802010571
* Môn học: **Nhập môn Trí tuệ nhân tạo**
* Giảng viên hướng dẫn: Nguyễn Thái Anh

---

## Công nghệ sử dụng

* **Ngôn ngữ lập trình**: Python
* **Môi trường thực thi**: Jupyter Notebook
* **Thư viện hỗ trợ**:

  * `numpy`: để xử lý tính toán và mảng số
  * `matplotlib`: dùng để trực quan hóa mê cung và đường đi
  * `collections`: tận dụng `deque` để quản lý hàng đợi trong quá trình tìm đường

---

## Các thuật toán được áp dụng:

### 1. Q-Learning

* Là thuật toán thuộc nhóm học tăng cường không mô hình (model-free RL).
* Mục tiêu chính: tìm được chính sách tối ưu để đưa ra hành động tại mỗi trạng thái sao cho tổng phần thưởng nhận được là lớn nhất.
* Công thức cập nhật Q-value:

![Q-learning Equation](https://github.com/user-attachments/assets/b9ab090b-399a-4603-9816-2a95047336e6)

**Trong đó:**

* Q(s, a): giá trị Q của trạng thái s khi thực hiện hành động a
* alpha: tốc độ học (learning rate)
* R: phần thưởng tức thời khi thực hiện hành động a tại trạng thái s
* gamma: hệ số chiết khấu (discount factor)
* maxQ(s', a'): giá trị Q lớn nhất tại trạng thái kế tiếp

---

### 2. Thiết lập mê cung và các bước tìm đường

#### Bước 1: Cấu hình mê cung

* Kích thước: 6x6
* Vị trí các vật cản (obstacles) được định nghĩa bằng danh sách toạ độ
* Điểm xuất phát: (0, 0)
* Mục tiêu: (0, 5)

```python
maze_size = 6
obstacles = [(0,1), (2,2), (3,2), (4,2), (5,2), (0,3), (2,4), (5,4)]
start = (0,0)
goal = (0,5)
```

#### Bước 2: Hàm kiểm tra hợp lệ `is_valid()`

```python
def is_valid(self, position):
    r, c = position
    return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0
```

#### Bước 3: Tìm kiếm bằng DFS (Depth-First Search)

```python
def dfs(current, visited, path):
    x, y = current
    if current == goal:
        path.append(current)
        return True
    visited.add(current)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for move in moves:
        if is_valid(*move) and move not in visited:
            if dfs(move, visited, path):
                path.append(current)
                return True
    return False
```

#### Bước 4: BFS (Breadth-First Search)

```python
def bfs(self):
    queue = deque([(self.start, [self.start])])
    visited = set([self.start])
    while queue:
        current, path = queue.popleft()
        if current == self.goal:
            return path
        for move in MOVES:
            next_r, next_c = current[0] + move[0], current[1] + move[1]
            next_position = (next_r, next_c)
            if self.is_valid(next_position) and next_position not in visited:
                visited.add(next_position)
                queue.append((next_position, path + [next_position]))
    return None
```

#### Bước 5: Gọi hàm tìm đường

**Dùng BFS:**

```python
planner = FSSP_BFS(grid, start, goal)
path = planner.bfs()

if path:
    print(f"Path found: {path}")
    planner.visualize(path)
else:
    print("No path found")
```

**Dùng DFS:**

```python
if dfs(start, visited, path):
    path.reverse()
    print("Path found")
    for position in path:
        print(position)
else:
    print("No path found!")
```

---

## Hướng dẫn sử dụng

1. Mở tệp notebook: `2374802010571_NguyenHanVu.ipynb`
2. Thực hiện chạy lần lượt từng ô lệnh trong notebook.
3. Kết quả thu được:

 * Bảng Q-table cuối cùng sau khi học
 * Lộ trình đường đi tối ưu từ vị trí bắt đầu đến đích
 * Biểu đồ trực quan mô phỏng đường đi trong mê cung

