"""PyTorch utility functions for device management and reproducibility."""

import random

import numpy as np
import torch


def set_seed(seed: int = 777) -> None:
    """Set random seeds for reproducibility across all libraries.

    Args:
        seed: Random seed value to use. Defaults to 777.

    Example:
        >>> set_seed(42)
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    if torch.cuda.is_available():
        torch.backends.cudnn.deterministic = True


def get_device() -> str:
    """Automatically detect and return the best available device.

    Returns:
        Device string: "cuda" if NVIDIA GPU is available,
                      "mps" if Apple Silicon GPU is available,
                      "cpu" otherwise.

    Example:
        >>> device = get_device()
        >>> print(f"Using device: {device}")
        Using device: mps
    """
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def count_parameters(model: torch.nn.Module) -> tuple[int, int]:
    """Calculate the total and trainable parameters in a model.

    Args:
        model: PyTorch model to analyze.

    Returns:
        Tuple of (total_params, trainable_params).

    Example:
        >>> model = nn.Linear(10, 5)
        >>> total, trainable = count_parameters(model)
        >>> print(f"Total: {total:,}, Trainable: {trainable:,}")
        Total: 55, Trainable: 55
    """
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return total_params, trainable_params


def print_model_summary(model: torch.nn.Module, model_name: str = "Model") -> tuple[int, int]:
    """Print a summary of model parameters.

    Args:
        model: PyTorch model to summarize.
        model_name: Name to display in the summary. Defaults to "Model".

    Returns:
        Tuple of (total_params, trainable_params).

    Example:
        >>> model = nn.Linear(10, 5)
        >>> total, trainable = print_model_summary(model, "Linear Layer")
        ============================================================
        Linear Layer のパラメータ数
        ============================================================
        総パラメータ数:       55
        訓練可能パラメータ数: 55
        ============================================================
    """
    total, trainable = count_parameters(model)
    print(f"\n{'='*60}")
    print(f"{model_name} のパラメータ数")
    print(f"{'='*60}")
    print(f"総パラメータ数:       {total:,}")
    print(f"訓練可能パラメータ数: {trainable:,}")
    print(f"{'='*60}\n")
    return total, trainable


def print_layer_details(model: torch.nn.Module, model_name: str = "Model") -> None:
    """Print detailed parameter information for each layer.

    Args:
        model: PyTorch model to analyze.
        model_name: Name to display in the summary. Defaults to "Model".

    Example:
        >>> model = nn.Sequential(nn.Linear(10, 5), nn.Linear(5, 2))
        >>> print_layer_details(model, "Two-Layer Network")
        ================================================================================
        Two-Layer Network - レイヤー別パラメータ詳細
        ================================================================================
        Layer Name                                    Parameters         Shape
        --------------------------------------------------------------------------------
        0.weight                                              50 [5, 10]
        0.bias                                                 5 [5]
        1.weight                                              10 [2, 5]
        1.bias                                                 2 [2]
        --------------------------------------------------------------------------------
        Total                                                 67
        ================================================================================
    """
    print(f"\n{'='*80}")
    print(f"{model_name} - レイヤー別パラメータ詳細")
    print(f"{'='*80}")
    print(f"{'Layer Name':<40} {'Parameters':>15} {'Shape':<20}")
    print(f"{'-'*80}")

    total = 0
    for name, param in model.named_parameters():
        param_count = param.numel()
        total += param_count
        shape_str = str(list(param.shape))
        print(f"{name:<40} {param_count:>15,} {shape_str:<20}")

    print(f"{'-'*80}")
    print(f"{'Total':<40} {total:>15,}")
    print(f"{'='*80}\n")
