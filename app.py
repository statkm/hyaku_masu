#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
100マス計算 Streamlitアプリ
"""

import streamlit as st
from datetime import datetime
import io
import os

# hyaku_masu.pyから関数をインポート
from hyaku_masu import generate_numbers, save_to_excel

st.set_page_config(
    page_title="100マス計算生成ツール",
    page_icon="📊",
    layout="centered"
)

st.title("📊 100マス計算プリント生成")
st.markdown("---")

# 計算の種類を選択
calc_type = st.radio(
    "計算の種類を選択してください",
    ["足し算", "掛け算", "両方"],
    horizontal=True
)

st.markdown("---")

# 生成ボタン
if st.button("📝 プリントを生成", type="primary", use_container_width=True):
    # outディレクトリを作成（存在しない場合）
    os.makedirs('out', exist_ok=True)
    
    # 数字を生成
    row_nums = generate_numbers(10)
    col_nums = generate_numbers(10)
    
    # 日付文字列を生成
    date_str = datetime.now().strftime('%Y%m%d')
    
    if calc_type == "足し算":
        filename = f"100masu_addition_{date_str}.xlsx"
        
        # 一時ファイルに保存
        save_to_excel(f"out/{filename}", "add", row_nums, col_nums)
        
        # ファイルを読み込んでダウンロードボタンを表示
        with open(f"out/{filename}", "rb") as f:
            st.success("✅ 足し算のプリントを生成しました！")
            st.download_button(
                label="⬇️ Excelファイルをダウンロード",
                data=f,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        # プレビュー情報を表示
        st.markdown("### 📋 プレビュー情報")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**行の数字:**")
            st.write(", ".join(map(str, row_nums)))
        with col2:
            st.write("**列の数字:**")
            st.write(", ".join(map(str, col_nums)))
    
    elif calc_type == "掛け算":
        filename = f"100masu_multiplication_{date_str}.xlsx"
        
        # 一時ファイルに保存
        save_to_excel(f"out/{filename}", "mul", row_nums, col_nums)
        
        # ファイルを読み込んでダウンロードボタンを表示
        with open(f"out/{filename}", "rb") as f:
            st.success("✅ 掛け算のプリントを生成しました！")
            st.download_button(
                label="⬇️ Excelファイルをダウンロード",
                data=f,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        # プレビュー情報を表示
        st.markdown("### 📋 プレビュー情報")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**行の数字:**")
            st.write(", ".join(map(str, row_nums)))
        with col2:
            st.write("**列の数字:**")
            st.write(", ".join(map(str, col_nums)))
    
    else:  # 両方
        files = []
        
        # 足し算
        filename_add = f"100masu_addition_{date_str}.xlsx"
        save_to_excel(f"out/{filename_add}", "add", row_nums, col_nums)
        
        # 掛け算
        filename_mul = f"100masu_multiplication_{date_str}.xlsx"
        save_to_excel(f"out/{filename_mul}", "mul", row_nums, col_nums)
        
        st.success("✅ 足し算と掛け算のプリントを生成しました！")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with open(f"out/{filename_add}", "rb") as f:
                st.download_button(
                    label="⬇️ 足し算をダウンロード",
                    data=f,
                    file_name=filename_add,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
        
        with col2:
            with open(f"out/{filename_mul}", "rb") as f:
                st.download_button(
                    label="⬇️ 掛け算をダウンロード",
                    data=f,
                    file_name=filename_mul,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
        
        # プレビュー情報を表示
        st.markdown("### 📋 プレビュー情報")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**行の数字:**")
            st.write(", ".join(map(str, row_nums)))
        with col2:
            st.write("**列の数字:**")
            st.write(", ".join(map(str, col_nums)))

st.markdown("---")
st.markdown("""
### 💡 使い方
1. 計算の種類（足し算、掛け算、両方）を選択
2. 「プリントを生成」ボタンをクリック
3. Excelファイルをダウンロード

生成されるExcelファイルには「問題」シートと「答え」シートが含まれています。
""")
