
from PIL import Image, ImageDraw
import random
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images", "input", "sinteticas")
os.makedirs(OUT_DIR, exist_ok=True)

RED = (200, 20, 20)
BLACK = (20, 20, 20)
CANVAS = 200


def draw_heart(draw, cx, cy, size, color):
    # dois círculos + triângulo formando um coração simplificado
    r = size // 3
    draw.ellipse([cx - r, cy - r, cx, cy], fill=color)
    draw.ellipse([cx, cy - r, cx + r, cy], fill=color)
    draw.polygon(
        [(cx - r, cy - r // 3), (cx + r, cy - r // 3), (cx, cy + r)],
        fill=color,
    )


def draw_diamond(draw, cx, cy, size, color):
    r = size // 2
    draw.polygon(
        [(cx, cy - r), (cx + r // 2, cy), (cx, cy + r), (cx - r // 2, cy)],
        fill=color,
    )


def draw_club(draw, cx, cy, size, color):
    r = size // 4
    draw.ellipse([cx - r, cy - r - r, cx + r, cy + r - r], fill=color)
    draw.ellipse([cx - r - r, cy - r // 2, cx + r - r, cy + r - r // 2 + r], fill=color)
    draw.ellipse([cx + r - r, cy - r // 2, cx + r + r, cy + r - r // 2 + r], fill=color)
    draw.polygon([(cx - r // 2, cy + r), (cx + r // 2, cy + r), (cx, cy + 2 * r)], fill=color)


def draw_spade(draw, cx, cy, size, color):
    r = size // 3
    draw.ellipse([cx - r, cy, cx, cy + r], fill=color)
    draw.ellipse([cx, cy, cx + r, cy + r], fill=color)
    draw.polygon(
        [(cx - r, cy + r // 3), (cx + r, cy + r // 3), (cx, cy - r)],
        fill=color,
    )
    draw.polygon([(cx - r // 2, cy + r), (cx + r // 2, cy + r), (cx, cy + 2 * r)], fill=color)


SUITS = {
    "copas": (draw_heart, RED),
    "ouros": (draw_diamond, RED),
    "paus": (draw_club, BLACK),
    "espadas": (draw_spade, BLACK),
}


def generate(n_per_suit=5, seed=42):
    random.seed(seed)
    paths = []
    for suit, (fn, color) in SUITS.items():
        for i in range(n_per_suit):
            img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
            draw = ImageDraw.Draw(img)
            cx = CANVAS // 2 + random.randint(-10, 10)
            cy = CANVAS // 2 + random.randint(-10, 10)
            size = random.randint(70, 100)
            fn(draw, cx, cy, size, color)
            path = os.path.join(OUT_DIR, f"{suit}_{i:02d}.png")
            img.save(path)
            paths.append(path)
    return paths


if __name__ == "__main__":
    paths = generate()
    print(f"Geradas {len(paths)} imagens sintéticas em {OUT_DIR}")
