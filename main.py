import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.get("/make-report")
def make_report():
    # URL取得
    url = "https://weather.yahoo.co.jp/weather/jp/15/5420/15202.html"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    short_text = soup.get_text()[:2000]

    # AI要約
    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "テキストから長岡市の天気と気温を読み取り、1行で教えてください。"},
            {"role": "user", "content": short_text}
        ]
    )
    result_text = ai_response.choices[0].message.content

    # テキストファイルで保存
    # 現在の時刻を取得してファイル名にする
    now = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"report_{now}.txt"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("【AI自動取得レポート】\n")
        file.write(result_text)
    
    return {"status": "成功！", "saved_file": filename, "content": result_text}
