# 📊 Dự án Thống kê Ứng dụng – Phân tích Web Attacks (Thursday Dataset)

## 🎯 Mục tiêu
Phân tích dữ liệu tấn công mạng (network traffic) từ một phần của bộ dữ liệu lớn, phục vụ môn học **Thống kê Ứng dụng**. Dữ liệu gốc chứa nhiều trường thông tin về lưu lượng mạng (flow features), với mục tiêu phân biệt giữa lưu lượng bình thường (`BENIGN`) và các cuộc tấn công (`ATTACK`).

---

## 🗂️ Dữ liệu đầu vào
- **File gốc**: `Thursday_Cleaned_WebAttacks.csv` (~170,000 dòng, 79 cột)
- Bao gồm nhiều đặc trưng mạng như:
  - `Flow Duration`, `Total Fwd Packets`, `Flow Bytes/s`, `Packet Length Mean`, v.v.
  - Nhãn (`Label`) với các giá trị như `BENIGN`, `Web Attack`,...

---

## 🧹 Bước 1 – Làm sạch và chuẩn hóa dữ liệu
Thực hiện các thao tác:
- Loại bỏ các dòng có `Destination Port = 0` (không hợp lệ)
- Bỏ các dòng không có lưu lượng (tổng gói gửi hoặc nhận = 0)
- Xử lý giá trị thiếu (NaN) bằng cách thay bằng **giá trị trung bình của cột**
- Chuyển đổi nhãn `Label`: 
  - `BENIGN` → `0`
  - Tất cả nhãn khác (tấn công) → `1`

Kết quả được lưu lại dưới dạng:  
📁 `Thursday_Cleaned_Processed.csv`

---

## 🔽 Bước 2 – Giảm kích thước và cân bằng tập dữ liệu
- Dữ liệu ban đầu mất cân bằng: ~146,000 BENIGN vs chỉ ~2,000 ATTACK
- Lấy mẫu ngẫu nhiên **2,163 dòng từ mỗi lớp** để:
  - Tăng tính công bằng khi phân tích thống kê/hồi quy
  - Giảm kích thước file (dễ chia sẻ, xử lý nhanh)

Kết quả được lưu lại:  
📁 `Thursday_Sampled_Balanced.csv` (~4,326 dòng)

---
