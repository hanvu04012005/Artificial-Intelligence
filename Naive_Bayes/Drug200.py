import gradio as gr
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
# Load và xử lý dữ liệu
data = pd.read_csv('Naive_Bayes/drug200.csv')

X = data.drop(['Drug'], axis=1)
y = data['Drug']
X = pd.get_dummies(X, dtype=int)
y_map = {"drugA": 1, "drugB": 2, "drugC": 3, "drugX": 4, "DrugY": 5}
y_inv_map = {v: k for k, v in y_map.items()}
y = y.map(y_map)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Huấn luyện mô hình GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
classes = model.classes_
# Hàm dự đoán
def predict_drug(age, sex, bp, cholesterol, na_to_k):
    # Tạo dataframe input giống lúc train
    input_dict = {
        "Age": [age],
        "Na_to_K": [na_to_k],
        "Sex_F": [1 if sex == "F" else 0],
        "Sex_M": [1 if sex == "M" else 0],
        "BP_HIGH": [1 if bp == "HIGH" else 0],
        "BP_LOW": [1 if bp == "LOW" else 0],
        "BP_NORMAL": [1 if bp == "NORMAL" else 0],
        "Cholesterol_HIGH": [1 if cholesterol == "HIGH" else 0],
        "Cholesterol_NORMAL": [1 if cholesterol == "NORMAL" else 0],
    }
    input_df = pd.DataFrame(input_dict)
    # Dự đoán
    y_pred = model.predict(input_df)[0]
    y_proba = model.predict_proba(input_df)[0]
    drug_name = y_inv_map[y_pred]
    fig, ax = plt.subplots()
    ax.bar([y_inv_map[c] for c in classes], y_proba, color='lightgreen')
    ax.set_title("Xác suất dự đoán cho từng loại thuốc")
    ax.set_ylabel("Xác suất")
    for i, v in enumerate(y_proba):
        ax.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img = Image.open(buf)

    result = f"###  Dự đoán loại thuốc: `{drug_name}`\n###  Độ tin cậy: `{max(y_proba)*100:.2f}%`"
    return result, img
iface = gr.Interface(
    fn=predict_drug,
    inputs=[
        gr.Slider(15, 80, step=1, label="Tuổi (Age)"),
        gr.Radio(["F", "M"], label="Giới tính (Sex)"),
        gr.Radio(["LOW", "NORMAL", "HIGH"], label="Huyết áp (BP)"),
        gr.Radio(["NORMAL", "HIGH"], label="Cholesterol"),
        gr.Number(label="Nồng độ Na_to_K")
    ],
    outputs=[
        gr.Markdown(label="Kết quả dự đoán"),
        gr.Image(label="Biểu đồ xác suất")
    ],
    title=" Dự đoán ",
    description="Dự đoán loại thuốc phù hợp ",
    theme="soft"
)

iface.launch()
