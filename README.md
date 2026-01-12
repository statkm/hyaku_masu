# 100マス計算プリント生成ツール

100マス計算のプリントをExcelファイルで生成するStreamlitアプリケーションです。

## デモ

🌐 **[https://hyakumasu.streamlit.app/](https://hyakumasu.streamlit.app/)**

ブラウザから直接アクセスして、すぐに100マス計算プリントを生成できます。

## 特徴

- 足し算・掛け算の100マス計算プリントを自動生成
- 問題シートと答えシートを含むExcelファイルを出力
- ランダムな数字（1-9）を使用して毎回異なる問題を生成
- シンプルで使いやすいWebインターフェース

## 必要な環境

- Python 3.7以上
- pip（Pythonパッケージマネージャー）

## インストール

1. リポジトリをクローン

```bash
git clone <repository-url>
cd hyaku_masu
```

2. 必要なパッケージをインストール

```bash
pip install -r requirements.txt
```

必要なパッケージ:
- streamlit
- openpyxl

## 使い方

### オンラインで使用（推奨）

インストール不要で、以下のURLからすぐに利用できます：

**[https://hyakumasu.streamlit.app/](https://hyakumasu.streamlit.app/)**

### ローカルでWebアプリとして起動

```bash
streamlit run app.py
```

ブラウザが自動的に開き、アプリケーションが表示されます（通常は http://localhost:8501）。

### アプリの操作方法

1. **計算の種類を選択**
   - 足し算
   - 掛け算
   - 両方

2. **「プリントを生成」ボタンをクリック**
   - ランダムな数字で問題が生成されます

3. **Excelファイルをダウンロード**
   - 生成されたファイルには「問題」シートと「答え」シートが含まれています

### コマンドラインで使用

Streamlitを使わずに、コマンドラインで直接実行することもできます：

```bash
python hyaku_masu.py
```

このコマンドを実行すると、足し算と掛け算の両方のプリントがExcelファイルとして生成されます。

## ファイル構成

```
hyaku_masu/
├── app.py              # Streamlitアプリケーション
├── hyaku_masu.py       # コア機能（数字生成・Excel出力）
├── requirements.txt    # 必要なパッケージのリスト
└── out/                # 生成されたExcelファイルの保存先
```

## 生成されるファイル

- ファイル名: `100masu_addition_YYYYMMDD.xlsx`（足し算）
- ファイル名: `100masu_multiplication_YYYYMMDD.xlsx`（掛け算）
- 保存場所: `out/` ディレクトリ
- 形式: Excel形式（.xlsx）

各Excelファイルには以下のシートが含まれます：
- **問題シート**: 空欄の100マス計算シート
- **答えシート**: 答えが記入された100マス計算シート

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 開発者

kotaromizuma

## 貢献

プルリクエストや問題の報告を歓迎します。

## 更新履歴

### v1.0.0 (2026-01-13)
- 初回リリース
- Streamlit Webインターフェースの実装
- 足し算・掛け算プリントの生成機能
- Excel形式での出力
