from . import preprocessing, segmentation, features


def classify_suit(image_path):
    rgb = preprocessing.load_rgb(image_path)
    gray = preprocessing.to_grayscale(rgb)
    binary, threshold = preprocessing.binarize(gray)

    rgb_crop, mask_crop = segmentation.crop_symbol(rgb, binary)
    color = segmentation.dominant_color(rgb_crop, mask_crop)
    feats = features.extract_features(mask_crop)

    if color == "vermelho":
        suit = "ouros" if feats["vertical_symmetry"] > 0.75 else "copas"
    else:
        suit = "paus" if feats["width_profile_ratio"] < 0.9 else "espadas"

    return {
        "naipe": suit,
        "cor": color,
        "threshold_otsu": threshold,
        "features": feats,
    }
