import gradio as gr
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

def load_data():
    return pd.read_csv('Naive_Bayes/Education.csv')
data = load_data()
def split_train_test(data, ratio_test=0.2):
    np.random.seed(0)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu) * ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set.reset_index(drop=True), test_set.reset_index(drop=True)
def train_model():
    train_set, test_set = split_train_test(data, 0.2)
    X_train, y_train = train_set['Text'], train_set['Label']
    y_train_bin = y_train.map({"positive": 1, "negative": 0})
    count_vect = CountVectorizer(binary=True, stop_words='english')
    X_train_vect = count_vect.fit_transform(X_train)
    model = BernoulliNB()
    model.fit(X_train_vect, y_train_bin)
    X_test, y_test = test_set['Text'], test_set['Label'].map({"positive": 1, "negative": 0})
    X_test_vect = count_vect.transform(X_test)
    y_score = model.predict_proba(X_test_vect)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)

    return model, count_vect, (fpr, tpr, roc_auc)

model, vectorizer, roc_data = train_model()
def predict_sentiment(text):
    if not text.strip():
        return "Vui lòng nhập nội dung văn bản.", None, None
    X_input = vectorizer.transform([text])
    pred_label = model.predict(X_input)[0]
    pred_proba = model.predict_proba(X_input)[0]

    label_text = "POSITIVE" if pred_label == 1 else "NEGATIVE"
    confidence = round(pred_proba[pred_label] * 100, 2)
    result = f"###  Kết quả: `{label_text}`\n###  Độ tin cậy: `{confidence}%`"
    fpr, tpr, roc_auc = roc_data
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    ax1.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {roc_auc:.2f}')
    ax1.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
    ax1.set_xlim([0.0, 1.0])
    ax1.set_ylim([0.0, 1.05])
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.set_title('Biểu đồ ROC (Tập test)')
    ax1.legend(loc="lower right")
    buf1 = BytesIO()
    plt.tight_layout()
    plt.savefig(buf1, format="png")
    plt.close()
    buf1.seek(0)
    img1 = Image.open(buf1)
    fig2, ax2 = plt.subplots()
    ax2.bar(['Negative', 'Positive'], pred_proba, color=['red', 'green'], alpha=0.7)
    ax2.set_title('Xác suất dự đoán cho văn bản')
    ax2.set_ylabel('Độ tin cậy')
    for i, v in enumerate(pred_proba):
        ax2.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom', fontweight='bold')
    buf2 = BytesIO()
    plt.tight_layout()
    plt.savefig(buf2, format="png")
    plt.close()
    buf2.seek(0)
    img2 = Image.open(buf2)

    return result, img1, img2
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label=" Nhập văn bản cần phân loại", lines=5, placeholder=""),
    outputs=[
        gr.Markdown(label=" Kết quả dự đoán"),
        gr.Image(label=" Biểu đồ ROC tổng hợp"),
        gr.Image(label=" Biểu đồ xác suất (văn bản nhập)")
    ],
    title=" Phân loại văn bản Giáo dục với Naive Bayes",
    description="Nhận diện cảm xúc văn bản (positive/negative) bằng mô hình Bernoulli Naive Bayes, trực quan hóa ROC & xác suất.",
    theme="soft"
)

iface.launch(share=False)
