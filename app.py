import streamlit as st


st.set_page_config(page_title="Tính Điểm Học Phần", page_icon="📊", layout="centered")


st.title("📊 Chương Trình Tính Điểm Học Phần (ĐHP)")
st.write("Nhập số điểm của bạn vào các ô dưới đây để hệ thống tự động tính toán.")

st.markdown("---")


st.subheader("1. Điểm bài kiểm tra (Tính ĐTBKT)")
col1, col2, col3 = st.columns(3)

with col1:
    diem_hs1 = st.number_input("Điểm Hệ số 1", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
with col2:
    diem_hs2 = st.number_input("Điểm Hệ số 2", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
with col3:
    diem_khac = st.number_input("Điểm Khác (Hệ số 1)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)


ĐTBKT = (diem_hs1 * 1 + diem_hs2 * 2 + diem_khac * 1) / 4


st.subheader("2. Điểm Chuyên cần & Điểm Thi")
col4, col5 = st.columns(2)

with col4:
    ĐCC = st.number_input("Điểm Chuyên Cần (ĐCC)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
with col5:
    ĐTHP = st.number_input("Điểm Thi Kết Thúc (ĐTHP)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)


ĐHT = (4 * ĐTBKT + ĐCC) / 5
ĐHP = (ĐHT + ĐTHP) / 2

st.markdown("---")


st.subheader("📊 Kết Quả Điểm Số Chi Tiết:")


c1, c2, c3 = st.columns(3)
c1.metric(label="Điểm TB Kiểm Tra (ĐTBKT)", value=f"{ĐTBKT:.2f}")
c2.metric(label="Điểm Quá Trình (ĐHT)", value=f"{ĐHT:.2f}")
c3.metric(label="Điểm Thi Kết Thúc (ĐTHP)", value=f"{ĐTHP:.2f}")


st.success(f"🎯 ĐIỂM HỌC PHẦN CUỐI CÙNG (ĐHP): {ĐHP:.2f}")

st.markdown("---")

st.warning("⚠️ ĐÂY CHỈ LÀ KẾT QUẢ THAM KHẢO !")
