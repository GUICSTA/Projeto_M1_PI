
import numpy as np


def fill_ratio(mask):
    area = np.count_nonzero(mask)
    box_area = mask.shape[0] * mask.shape[1]
    return area / box_area if box_area > 0 else 0.0


def vertical_symmetry(mask):
    """1.0 = perfeitamente simétrico verticalmente, 0.0 = nada simétrico."""
    h = mask.shape[0]
    top = mask[: h // 2, :]
    bottom = mask[h - h // 2 :, :]
    bottom_flipped = np.flipud(bottom)

    # garante mesmo shape para comparação
    min_h = min(top.shape[0], bottom_flipped.shape[0])
    top = top[:min_h]
    bottom_flipped = bottom_flipped[:min_h]

    total = top.size
    if total == 0:
        return 0.0
    agreement = np.count_nonzero((top > 0) == (bottom_flipped > 0))
    return agreement / total


def width_profile_ratio(mask):
    """Razão entre largura média do símbolo na metade de cima e na de baixo."""
    h = mask.shape[0]
    top = mask[: h // 2, :]
    bottom = mask[h // 2 :, :]

    def mean_width(region):
        widths = []
        for row in region:
            xs = np.where(row > 0)[0]
            if len(xs) > 0:
                widths.append(xs.max() - xs.min() + 1)
        return np.mean(widths) if widths else 0.0

    top_w = mean_width(top)
    bottom_w = mean_width(bottom)
    if bottom_w == 0:
        return 0.0
    return top_w / bottom_w


def extract_features(mask):
    return {
        "fill_ratio": fill_ratio(mask),
        "vertical_symmetry": vertical_symmetry(mask),
        "width_profile_ratio": width_profile_ratio(mask),
    }
