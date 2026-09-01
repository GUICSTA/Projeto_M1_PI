
import numpy as np


def bounding_box(binary_array):
    """Retorna (y_min, y_max, x_min, x_max) da região não-zero (símbolo)."""
    ys, xs = np.where(binary_array > 0)
    if len(ys) == 0:
        raise ValueError("Nenhum pixel de símbolo encontrado na imagem binarizada.")
    return ys.min(), ys.max(), xs.min(), xs.max()


def crop_symbol(rgb_array, binary_array, margin=5):
    """Recorta a região do símbolo (com margem) tanto no RGB quanto na máscara binária."""
    y_min, y_max, x_min, x_max = bounding_box(binary_array)
    h, w = binary_array.shape
    y_min = max(0, y_min - margin)
    x_min = max(0, x_min - margin)
    y_max = min(h, y_max + margin)
    x_max = min(w, x_max + margin)

    rgb_crop = rgb_array[y_min:y_max, x_min:x_max]
    mask_crop = binary_array[y_min:y_max, x_min:x_max]
    return rgb_crop, mask_crop


def dominant_color(rgb_array, mask):
    symbol_pixels = rgb_array[mask > 0]
    if len(symbol_pixels) == 0:
        raise ValueError("Máscara vazia — nenhum pixel de símbolo para analisar cor.")

    mean_r = symbol_pixels[:, 0].mean()
    mean_g = symbol_pixels[:, 1].mean()
    mean_b = symbol_pixels[:, 2].mean()

    # Vermelho: canal R significativamente maior que G e B.
    if mean_r - ((mean_g + mean_b) / 2) > 15:
        return "vermelho"
    return "preto"
