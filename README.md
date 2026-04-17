# 🌤️ AI Weather Scraper（天気レポート自動生成ツール）

> Webから天気情報を自動取得し、AIが読みやすいレポートに変換・保存するツールです。

---

## 📌 このツールで解決できること

- 毎日手動で天気サイトを確認する手間をなくしたい
- 天気情報を自動でテキストにまとめてほしい
- 日付ごとにレポートを自動保存・管理したい

---

## 🎬 デモ

ブラウザで `http://127.0.0.1:8000/make-report` にアクセスすると以下が返ります：

```json
{
  "status": "成功！",
  "saved_file": "report_20260417_2139.txt",
  "content": "長岡市の天気は晴れ、気温は昼間21℃です。"
}
```

同時に `report_実行日時.txt`（例：`report_20260417_2139.txt`）がローカルに自動保存されます。ファイル名は実行のたびに自動で変わります。

**保存されるテキストファイルの中身：**
```
【AI自動取得レポート】
長岡市の天気は晴れ、気温は昼間21℃です。
```

---

## ⚙️ 使用技術

| カテゴリ | 技術 |
|---|---|
| 言語 | Python 3.12 |
| APIサーバー | FastAPI |
| スクレイピング | BeautifulSoup4 |
| AI要約 | OpenAI API（GPT-4o-mini） |

---

## 🚀 セットアップ・使い方

### 1. リポジトリをクローン
```bash
git clone https://github.com/Miriotto-39/ai-weather-scraper.git
cd ai-weather-scraper
```

### 2. 必要なライブラリをインストール
```bash
pip install -r requirements.txt
```

### 3. 環境変数を設定
`.env` ファイルを作成し、以下を記入してください：
```
OPENAI_API_KEY=your_api_key_here
```

### 4. サーバーを起動
```bash
uvicorn main:app --reload
```

### 5. レポートを生成
ブラウザまたはcurlで以下にアクセス：
```
http://localhost:8000/make-report
```

---

## 📁 ファイル構成

```
ai-weather-scraper/
├── main.py          # メイン処理（スクレイピング＋AI要約＋保存）
├── .env             # APIキー（gitignore済み）
├── .gitignore
└── README.md
```

---

## 🗺️ 今後の追加予定（Roadmap）

- [x] 天気情報の自動スクレイピング
- [x] GPT-4o-miniによるレポート自動生成
- [x] 日付付きテキストファイルへの自動保存
- [ ] LINE / メールへの通知機能（実装予定）
- [ ] 複数都市への対応
- [ ] 定時自動実行（スケジューラー対応）

---

## 📝 カスタマイズについて

取得対象の都市・サイト・レポートのフォーマットは柔軟に変更可能です。
業務用途へのカスタマイズも対応できます。お気軽にご相談ください。

---

## 👤 作者

**Miriotto-39**
- GitHub: [@Miriotto-39](https://github.com/Miriotto-39)
- クラウドワークス：(https://crowdworks.jp/public/employees/6513601)
