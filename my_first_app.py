import streamlit as st
import pandas as pd
from PIL import Image

# タイトル
st.title("センター5号館 3F 教室マップ & 時間割")

# 画像表示（マップ）
st.subheader("3F フロアマップ")
image = Image.open("5goukan3F.jpg")
st.image(image, use_column_width=True)

# データ読み込み
df = pd.read_csv("data.csv")

# 教室一覧（重複を除く）
rooms = sorted(df["room"].unique())

# 教室選択
st.subheader("教室を選択してください")
selected_room = st.selectbox("教室番号", rooms)

# 授業表示
room_data = df[df["room"] == selected_room]

if not room_data.empty:
    st.markdown(f"### {selected_room} 教室の授業")
    display_df = room_data[["day", "period", "class_name", "teacher"]]
    display_df.columns = ["曜日", "時限", "授業名", "担当教員"]
    display_df = display_df.sort_values(["day", "period"])
    st.table(display_df)
else:
    st.info("この教室には授業が登録されていません。")
