# Axell AI Contest 2025 - 1st Place Solution

![version](https://img.shields.io/badge/version-1.0.0-red.svg)
![stars](https://img.shields.io/github/stars/yushin-ito/axell-ai-contest-2025-1st-place-solution?color=yellow)
![commit-activity](https://img.shields.io/github/commit-activity/t/yushin-ito/axell-ai-contest-2025-1st-place-solution)
![license](https://img.shields.io/badge/license-MIT-green)

<br/>

## 📝 Overview

本リポジトリは、Axell AI Contest 2025において1位を獲得した解法を公開しています。
本コンテストは、「飲料パッケージの物体検出」を行うモデルの開発に挑戦するものでした。
実践的開発を想定するため、実行処理する際の演算能力には一定の制限が設けられていました。

<br/>
<br/>

## 🏆 Result

**暫定評価**

| 順位 | スコア | 推論時間（秒） | 投稿日 |
|------|--------|----------------|--------|
| 4   | 	0.9951116415437499 | 0.015816154 | 2025-08-26 22:02:10 |

<br/>

**最終評価**

| 順位 | スコア | 推論時間（秒） | 投稿日 |
|------|--------|----------------|--------|
| 1    | 0.9976518443331074 | 0.015804611 | 2025-08-26 22:02:10 |


## 📂 Structure

```
axell-ai-contest-2025-1st-place-solution/
├── data/
│   ├── generated/       # 生成した画像
│   ├── prepared/        # 学習用のデータセット
│   ├── raw/             # 配布されたデータセット
│   ├── segmented/       # セグメンテーションした画像
│   └── prompts.csv      # プロンプト
├── notebooks/
│   ├── generate.ipynb   # 背景の生成
│   ├── segment.ipynb    # 物体のセグメンテーション
│   ├── prepare.ipynb    # データセットの準備
│   ├── train.ipynb      # モデルの学習
│   └── optimize.ipynb   # モデルの最適化
├── runs/
│   └── exp1/            # 提出したモデルの学習ログ
├── submit/
│   ├── model/
│   │   └── best.pt      # 提出したモデルの重み
│   └── src/
│       ├── config.py    # 設定
│       └── predictor.py # 推論モジュール
├── weights/             # 事前学習済みモデル
├── LICENSE              # ライセンス
├── pyproject.toml       # プロジェクトの設定
├── README.md            # 本ファイル
└── requirements.txt     # 依存関係
```


## 🚀　Usage

1. リポジトリをクローンする

```bash
git clone https://github.com/yushin-ito/axell-ai-contest-2025-1st-place-solution.git
```

2. リポジトリに移動する

```bash
cd axell-ai-contest-2025-1st-place-solution
```

3. 仮装環境を作成する

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

4. データセットの準備

```
data/
└── raw/
    ├── images/
    │   ├── T1.jpg
    │   ├── T2.jpg
    │   └── ...
    └── annotations/
        └── train.json
```

<br/>

5. generate.ipynbの実行

合成によるデータ拡張に使用する背景の画像の生成を行います。

```bash
jupyter nbconvert --execute generate.ipynb
```

```
data/
└── generated/
    ├── T1.jpg
    ├── T2.jpg
    └── ...
```

> [!CAUTION]
> 上から2つ目のセルの`<HF_TOKEN>`を[Hugging Face](https://huggingface.co)のアクセストークンに置き換えてください。

<br/>

6. segment.ipynbの実行

合成によるデータ拡張に使用するための物体の画像のセグメンテーションを行います。

```bash
jupyter nbconvert --execute segment.ipynb
```

```
data/
└── segmented/
    ├── T1.png
    ├── T2.png
    └── ...
```

<br/>

7. prepare.ipynbの実行

学習に使用するデータセットの作成を行います。

```bash
jupyter nbconvert --execute prepare.ipynb
```

```
data/
└── prepared/
    ├── images/
    │   ├── A1.jpg
    │   ├── A2.jpg
    │   ├── ...
    │   ├── T1.jpg
    │   ├── T2.jpg
    │   └── ...
    ├── labels/
    │   ├── A1.txt
    │   ├── A2.txt
    │   ├── ...
    │   ├── T1.txt
    │   ├── T2.txt
    │   └── ...
    └── data.yaml
```

<br/>

8. train.ipynbの実行

モデルのファインチューニングを行います

```bash
jupyter nbconvert --execute train.ipynb
```

<br/>

9. optimize.ipynbの実行

不要な情報を削除することでモデルの最適化を行います。

```bash
jupyter nbconvert --execute optimize.ipynb
```

<br/>
<br/>

## Submission

1. モデルのコピー

```bash
cp runs/exp/weights/best.pt submit/model/best.pt
```

2. ZIPファイルの作成

```bash
zip -r submit.zip submit
```

<br/>
<br/>

## 🤝 Contributer

<a href="https://github.com/yushin-ito">
  <img  src="https://avatars.githubusercontent.com/u/75526539?s=48&v=4" width="64px">
</a>

<br/>
<br/>

## 📜 LICENSE

[MIT LICENSE](LICENSE)