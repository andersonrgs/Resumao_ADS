#!/usr/bin/env python3
"""Gera 2 GIFs animados simples: gifs/Acertou_7.gif e gifs/Errou_7.gif."""
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent / "gifs"
S = 3            # supersampling para suavizar as bordas
W = H = 200
N = 24           # quadros
BG = (244, 247, 246)


def novo():
    im = Image.new("RGB", (W * S, H * S), BG)
    return im, ImageDraw.Draw(im)


def c(v):
    return int(v * S)


def rosto(d, cx, cy, cor, sorriso, olhos_fechados=False):
    r = 55
    d.ellipse([c(cx - r), c(cy - r), c(cx + r), c(cy + r)], fill=cor, outline=(60, 60, 60), width=c(3))
    for dx in (-20, 20):
        if olhos_fechados:   # olhos "^" ou "x"
            d.arc([c(cx + dx - 9), c(cy - 22), c(cx + dx + 9), c(cy - 2)], 200, 340, fill=(40, 40, 40), width=c(4))
        else:
            d.ellipse([c(cx + dx - 6), c(cy - 18), c(cx + dx + 6), c(cy - 4)], fill=(40, 40, 40))
    if sorriso:
        d.arc([c(cx - 28), c(cy - 5), c(cx + 28), c(cy + 38)], 15, 165, fill=(40, 40, 40), width=c(5))
    else:
        d.arc([c(cx - 24), c(cy + 18), c(cx + 24), c(cy + 52)], 195, 345, fill=(40, 40, 40), width=c(5))


def acertou():
    random.seed(1)
    cores = [(231, 76, 60), (52, 152, 219), (241, 196, 15), (46, 204, 113), (155, 89, 182)]
    confetes = [(random.uniform(10, 190), random.uniform(-200, 0), random.uniform(3, 6),
                 random.choice(cores), random.uniform(0, 6.28)) for _ in range(28)]
    frames = []
    for i in range(N):
        t = i / N
        im, d = novo()
        pulo = abs(math.sin(t * math.pi * 2)) * 28
        rosto(d, 100, 112 - pulo, (255, 214, 64), True, olhos_fechados=True)
        for x, y0, tam, cor, ph in confetes:
            y = (y0 + t * 200 * 1.0 + 200) % 220 - 10
            xx = x + math.sin(t * 6.28 * 2 + ph) * 6
            d.rectangle([c(xx), c(y), c(xx + tam), c(y + tam * 1.6)], fill=cor)
        d.text((c(60), c(168)), "", fill=(0, 0, 0))
        frames.append(im.resize((W, H), Image.LANCZOS))
    return frames


def errou():
    frames = []
    for i in range(N):
        t = i / N
        im, d = novo()
        bal = math.sin(t * math.pi * 4) * 6      # balança de um lado para o outro
        cx, cy = 100 + bal, 100
        rosto(d, cx, cy, (140, 190, 235), False)
        # lágrima descendo
        ty = (t * 2 % 1) * 55
        for dx in (-20, 20):
            x, y = cx + dx, cy + 2 + ty
            d.ellipse([c(x - 5), c(y), c(x + 5), c(y + 14)], fill=(70, 130, 220))
        # nuvem de chuva
        for nx in (60, 100, 140):
            d.ellipse([c(nx - 22), c(12), c(nx + 22), c(40)], fill=(170, 175, 185))
        frames.append(im.resize((W, H), Image.LANCZOS))
    return frames


def salvar(frames, nome, ms):
    p = OUT / nome
    pal = [f.convert("P", palette=Image.ADAPTIVE, colors=64) for f in frames]
    pal[0].save(p, save_all=True, append_images=pal[1:], duration=ms, loop=0, optimize=True, disposal=2)
    print(nome, p.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    salvar(acertou(), "Acertou_7.gif", 50)
    salvar(errou(), "Errou_7.gif", 60)
