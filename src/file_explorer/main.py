import streamlit as st
import os


st.markdown("# Uploader")

uploaded_file = st.file_uploader("対象のExcelファイルを選んでください。", type="xlsx")
submit_btn_xlsx = st.button("Upload")

if submit_btn_xlsx:
    # TODO: Excelファイルが選択されていない場合にボタンを押すとエラーになる
    # TODO: アップロードされたかどうかのステータスが表示される
    pass



st.markdown("# Downloader")

folder_path = st.text_input("Input folder path")
file_paths = []
if os.path.isdir(folder_path):
    for fn in os.listdir(folder_path):
        fp = f'{folder_path}/{fn}'
        if os.path.isfile(fp):
            file_paths.append(fp)

selected_file = st.selectbox('Select file', options=file_paths)
st.write(f'selected file: {selected_file}')