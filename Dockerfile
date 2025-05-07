# ベースとなるPythonの軽量イメージ
FROM python:3.12-slim

# システム更新 + git, build-essential をインストール
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを /src に設定
WORKDIR /src

# ライブラリをインストール（ファイルがあれば）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

# OpenCVのためにlibgl1をインストール
RUN apt update && apt install -y libgl1 libglib2.0-0



# 全ファイルをコンテナにコピー
COPY . .

# デフォルトでbashを使う
CMD ["/bin/bash"]
