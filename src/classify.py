"""
Classificação do naipe a partir da cor dominante + descritores de forma.

Regra (baseada em regras/limiares, não aprendizado de máquina — compatível
com o estágio de M1, que pede um pipeline classico e explicável):

1. Cor vermelha:
   - alta simetria vertical + width_profile_ratio próximo de 1 -> ouros (losango)
   - simetria vertical mais baixa (por causa do "vale" no topo) -> copas
2. Cor preta:
   - width_profile_ratio < 0.9 (símbolo mais largo na base, pelos 3 lóbulos
     de paus) -> paus
   - width_profile_ratio >= 0.9 (símbolo mais largo/igual no topo, formato
     afilado de espadas) -> espadas

Os limiares abaixo foram calibrados nas imagens SINTÉTICAS de desenvolvimento
(src/generate_synthetic_cards.py) e precisarão ser reajustados com fotos reais
do baralho físico — isso está documentado como próximo passo em docs/proposta.md.
"""
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
