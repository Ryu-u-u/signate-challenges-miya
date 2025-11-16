# Signate Challenges

このリポジトリは、[Signate](https://signate.jp/)の機械学習コンペティションに参加するためのプロジェクトです。各チャレンジは`challenges/`ディレクトリ配下に独立した構造で管理されています。

## 技術スタック

- **Python**: 3.14+
- **パッケージマネージャー**: uv
- **ML/DL フレームワーク**: PyTorch, torchvision, scikit-learn
- **データサイエンス**: pandas, numpy, matplotlib, seaborn, opencv-python
- **開発ツール**: Jupyter (notebook/lab), ruff (linting/formatting), mypy (type checking), pytest (testing)

## 環境要件

- uv（[インストールガイド](https://uv.dev/)を参照）
- Python 3.14 以上
- make（macOS/Linux には通常プリインストール済み）

## セットアップ

### 初回セットアップ

```bash
make init              # 依存関係のインストールとJupyterカーネルの登録
```

このコマンドで以下が実行されます：

- `uv sync`で依存関係をインストール
- プロジェクト専用の Jupyter カーネルを登録

## 使い方

### 依存関係の管理

```bash
make add pkg="package-name"           # ランタイム依存関係を追加
make add-dev pkg="package-name"       # 開発依存関係を追加
```

### 開発ツール

```bash
make format            # ruffでコードをフォーマット
make lint              # ruffでコードをリント
make typecheck         # mypyでsrc/の型チェック
make test              # pytestでテストを実行
```

### Jupyter

```bash
make notebook                   # Jupyter Notebookを起動（NOTEBOOK_DIRを開く）
make notebook CHALLENGE=mnist   # 指定チャレンジのノートブックを起動
make lab                        # Jupyter Labを起動（NOTEBOOK_DIRを開く）
make lab CHALLENGE=mnist        # 指定チャレンジのJupyter Labを起動
```

### カーネル管理

```bash
make reinstall-kernel  # Jupyterカーネルを再作成
make remove-kernel     # Jupyterカーネルを削除
```

### クリーンアップ

```bash
make clean             # __pycache__ディレクトリを削除
```

## チャレンジの構成

### ディレクトリ構造

プロジェクトルートには`challenges/`ディレクトリがあり、各チャレンジはサブディレクトリとして配置されます。

```txt
.
├── challenges      # チャレンジ固有のディレクトリ
├── CLAUDE.md       # Claude AIに関する情報
├── Makefile        # 開発用Makefile
├── pyproject.toml  # uv依存関係定義
├── README.md
├── utils           # ユーティリティモジュール
└── uv.lock         # uvロックファイル
```

各チャレンジは以下の標準構造に従います：

```txt
challenges/<challenge-name>/
├── assets/           # チャレンジ提供のアセット（CSVファイルなど）
├── data/             # 学習/テストデータ（gitignore対象、zipから展開）
├── notebook/         # 実験用Jupyterノートブック
├── output/           # モデル出力、提出ファイル（gitignore対象）
├── src/              # 再利用可能なPythonモジュール（必要に応じて）
└── README.md         # チャレンジ固有のドキュメント
```

### チャレンジの切り替え

特定のチャレンジで作業する場合は、Makefile の`CHALLENGE`変数を更新します：

```makefile
CHALLENGE := mnist  # チャレンジ名に変更
```

これにより、Jupyter コマンドの`NOTEBOOK_DIR`が自動的に調整されます。

### データファイル

- チャレンジデータ（train/test 画像、CSV など）は`challenges/<challenge-name>/data/`に配置
- data ディレクトリは gitignore 対象（`.keep`ファイルを除く）
- `challenges/<challenge-name>/assets/`に提供された zip ファイルからデータを展開

## 開発パターン

### ノートブック開発

このリポジトリではノートブックは実験的なコードのために使用され、先頭付番された命名規則に従います：

**ファイル名例**

- `0_data_exploration.ipynb`
- `1_architecture_experiment.ipynb`
- `2_training_tuning.ipynb`
- `3_submission.ipynb`

## カーネル設定

プロジェクトは、プロジェクトディレクトリ名（`signate-challenges`）に基づいた表示名`"signate-challenges (uv)"`のカスタム Jupyter カーネルを登録します。これにより、ノートブックが正しい uv 環境を使用することが保証されます。

## コード品質基準

- コミット前に ruff でコードをフォーマット（`make format`）
- コミット前にリント問題を修正（`make lint`）
- `src/`内のコードには型ヒントを付け、mypy でチェック（`make typecheck`）
- ノートブックは厳密なフォーマット/リントから除外されますが、一般的なベストプラクティスに従う必要があります
