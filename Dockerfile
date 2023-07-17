FROM python:3.10

WORKDIR /web_app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY . /web_app

CMD streamlit run DOA_Analytics_Prediction.py