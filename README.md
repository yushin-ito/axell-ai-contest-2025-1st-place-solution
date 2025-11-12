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

**1. 仮想環境の構築**

以下のコマンドを実行してください。

```bash
python -m venv .venv 
source .venv/bin/activate
```

<br/>

**2. 依存関係のインストール**

以下のコマンドを実行してください。

```bash
pip install -r requirements.txt
```

<br/>

**3. データセットの配置**

- `data/raw`に提供されたデータセットを展開してください。
- 以下のようなディレクトリになっていることを確認してください。

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

**4. generate.ipynbの実行**

合成によるデータ拡張に使用する背景の画像の生成を行います。

- すべてのセルを上から順番に実行してください。
- 上から2つ目のセルの`<HF_TOKEN>`を[Hugging Face](https://huggingface.co)のアクセストークンに置き換えてください。
- 事前に[Stable Diffusion 3.5 Large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)の利用規約に同意してください。
- 以下のようなディレクトリになっていることを確認してください。

```
data/
└── generated/
    ├── T1.jpg
    ├── T2.jpg
    └── ...
```

保存されるデータは、ご連絡いただければ提供いたします。

<br/>

**5. segment.ipynbの実行**

合成によるデータ拡張に使用するための物体の画像のセグメンテーションを行います。

- すべてのセルを上から順番に実行してください。
- 以下のようなディレクトリになっていることを確認してください。

```
data/
└── segmented/
    ├── T1.png
    ├── T2.png
    └── ...
```

保存されるデータは、ご連絡いただければ提供いたします。

<br/>

**6. prepare.ipynbの実行**

学習に使用するデータセットの作成を行います。

- すべてのセルを上から順番に実行してください。
- 以下のようなディレクトリになっていることを確認してください。

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

保存されるデータは、ご連絡いただければ提供いたします。

<br/>

**7. train.ipynbの実行**

事前学習重みを用いてファインチューニングを行います

- すべてのセルを上から順番に実行してください。
- 上から4つ目のセルの`name`の値を適宜変更してください。

<br/>

**8. optimize.ipynbの実行**

不要な情報を削除することでモデルの最適化を行います。

- すべてのセルを上から順番に実行してください。
- 上から3つ目のセルの`model_path`の値を適宜変更してください。

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

## 🤝 Contributer

<a href="https://github.com/yushin-ito">
  <img  src="https://avatars.githubusercontent.com/u/75526539?s=48&v=4" width="64px">
</a>

<br/>

## 📜 LICENSE

[MIT LICENSE](LICENSE)