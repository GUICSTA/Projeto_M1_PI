"""
Uso:
    python -m src.main caminho/para/imagem.png

"""
import sys
from . import classify


def main():
    if len(sys.argv) != 2:
        print("Uso: python -m src.main <caminho_da_imagem>")
        sys.exit(1)

    path = sys.argv[1]
    result = classify.classify_suit(path)

    print(f"Imagem: {path}")
    print(f"Naipe identificado: {result['naipe']}")
    print(f"Cor detectada: {result['cor']}")
    print(f"Threshold (Otsu): {result['threshold_otsu']}")
    print(f"Características: {result['features']}")


if __name__ == "__main__":
    main()
