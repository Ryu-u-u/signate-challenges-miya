# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains solutions for Signate machine learning challenges. Each challenge is organized in a self-contained directory structure under `challenges/`. The project uses **uv** for Python dependency management and Jupyter notebooks for experimentation and model development.

## Technology Stack

- **Python**: 3.14+
- **Package Manager**: uv
- **ML/DL Frameworks**: PyTorch, torchvision, scikit-learn
- **Data Science**: pandas, numpy, matplotlib, seaborn, opencv-python
- **Development Tools**: Jupyter (notebook/lab), ruff (linting/formatting), mypy (type checking), pytest (testing)

## Common Commands

### Initial Setup

```bash
make init              # Install dependencies and register Jupyter kernel
```

### Dependency Management

```bash
make add pkg="package-name"           # Add runtime dependency
make add-dev pkg="package-name"       # Add development dependency
```

### Development Tools

```bash
make format            # Format code with ruff
make lint              # Lint code with ruff
make typecheck         # Type check src/ with mypy
make test              # Run pytest tests
```

### Jupyter

```bash
make notebook          # Launch Jupyter Notebook (opens NOTEBOOK_DIR)
make lab               # Launch Jupyter Lab (opens NOTEBOOK_DIR)
```

### Kernel Management

```bash
make reinstall-kernel  # Recreate Jupyter kernel
make remove-kernel     # Remove Jupyter kernel
```

### Cleanup

```bash
make clean             # Remove __pycache__ directories
```

## Working with Challenges

### Challenge Directory Structure

Each challenge follows this standard structure:

```
challenges/<challenge-name>/
├── assets/           # Challenge-provided assets (CSV files, etc.)
├── data/             # Training/test data (gitignored, extracted from zips)
├── notebook/         # Jupyter notebooks for experimentation
├── output/           # Model outputs, submissions (gitignored)
├── src/              # Reusable Python modules (if needed)
└── README.md         # Challenge-specific documentation
```

### Switching Between Challenges

To work on a specific challenge, update the `CHALLENGE` variable in the Makefile:

```makefile
CHALLENGE := mnist  # Change this to the challenge name
```

This automatically adjusts `NOTEBOOK_DIR` for Jupyter commands.

### Data Files

- Challenge data (train/test images, CSVs) goes in `challenges/<challenge-name>/data/`
- Data directories are gitignored (except `.keep` files)
- Extract data from zips provided in `challenges/<challenge-name>/assets/`

## Architecture Patterns

### Notebook-Driven Development

This repository follows a **notebook-first approach**:

1. **Exploration notebooks** (`0_*.ipynb`): Data visualization and exploratory data analysis
2. **Architecture notebooks** (`1_*.ipynb`): Model architecture experimentation
3. **Training notebooks** (`2_*.ipynb`): Training methodology and hyperparameter tuning
4. **Submission notebooks**: Generate final predictions for competition submission

### PyTorch Dataset Pattern

Notebooks use custom `torch.utils.data.Dataset` classes for data loading:

- `__init__`: Initialize with dataframe, mode (train/test), and transforms
- `__getitem__`: Load images with cv2, apply transforms, return (image, label) tensors
- Combine with `DataLoader` for batching and shuffling

### Model Training Pattern

Training follows this structure:

1. Define model class extending `nn.Module`
2. Set device (cuda/mps/cpu) for hardware acceleration
3. Create train/validation split from training data
4. Implement `training_validation()` function that:
   - Trains for specified epochs
   - Tracks train/validation loss and accuracy
   - Returns trained model and history dict
5. Use `predict_img()` for validation analysis (predictions + probabilities + loss per sample)
6. Use `model_predict()` for test set predictions

## Python Execution

All Python commands should use `uv run python` (aliased as `$(PYTHON)` in Makefile) to ensure they run in the correct uv-managed virtual environment.

## Kernel Configuration

The project registers a custom Jupyter kernel named after the project directory (`signate-challenges`) with display name `"signate-challenges (uv)"`. This ensures notebooks use the correct uv environment.

## Code Quality Standards

- Format code with ruff before committing (`make format`)
- Fix linting issues before committing (`make lint`)
- Type hints should be checked with mypy (`make typecheck`) for code in `src/`
- Notebooks are excluded from strict formatting/linting but should follow general best practices
