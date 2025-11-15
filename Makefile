# ===============================
# Project Settings
# ===============================
PROJECT_NAME := $(notdir $(shell pwd))
KERNEL_NAME := $(PROJECT_NAME)
PYTHON := uv run python

# ===============================
# Environment Setup
# ===============================

# 初期セットアップ：依存インストール & カーネル登録
init:
	uv sync
	$(PYTHON) -m ipykernel install --user --name $(KERNEL_NAME) \
		--display-name "$(PROJECT_NAME) (uv)"

# カーネルを再作成したい場合
reinstall-kernel:
	jupyter kernelspec remove -f $(KERNEL_NAME) || true
	$(PYTHON) -m ipykernel install --user --name $(KERNEL_NAME) \
		--display-name "$(PROJECT_NAME) (uv)"

# カーネル削除だけしたい場合
remove-kernel:
	jupyter kernelspec remove -f $(KERNEL_NAME)

# ===============================
# Dependencies
# ===============================

# 通常の依存を追加: make add pkg="pandas numpy"
add:
	uv add $(pkg)

# dev 依存を追加（ruff, mypy, pytest など）
# 例: make add-dev pkg="pytest pytest-cov"
add-dev:
	uv add --dev $(pkg)

# ===============================
# Development Tools
# ===============================

format:
	uv run ruff format .

lint:
	uv run ruff check .

typecheck:
	uv run mypy src

test:
	uv run pytest

# ===============================
# Jupyter
# ===============================
notebook:
	uv run jupyter notebook

lab:
	uv run jupyter lab

# ===============================
# Utility
# ===============================
clean:
	find . -name "__pycache__" -exec rm -rf {} +
