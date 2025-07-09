import streamlit as st
import pandas as pd

# CSVファイルを読み込み（Shift-JIS対応）
df = pd.read_csv("data.csv", encoding="shift_jis")

# タイトル
st.title("センター5号館 3F 曜日別時間割")

# 曜日を日本語で表示するための変換
day_mapping = {
    "Monday": "月",
    "Tuesday": "火",
    "Wednesday": "水",
    "Thursday": "木",
    "Friday": "金"
}

# 日本語の曜日リスト
days_jp = ["月", "火", "水", "木", "金"]

# ユーザーに曜日を選択させる
selected_day_jp = st.radio("曜日を選んでください", days_jp, horizontal=True)

# 英語に逆変換（内部のデータと一致させるため）
selected_day_en = [k for k, v in day_mapping.items() if v == selected_day_jp][0]

# 選択された曜日の授業だけ抽出
filtered = df[df["Day"] == selected_day_en]

# 表示用に列を整える
if not filtered.empty:
    display_df = filtered[["Room", "Class name", "Teacher", "Period"]]
    display_df.columns = ["教室", "授業名", "担当教員", "時限"]
    display_df = displa_
