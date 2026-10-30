#!/usr/bin/env python3
"""Geometry aid, not a perceptual similarity score. Requires Pillow."""
import argparse
from pathlib import Path
from PIL import Image, ImageChops, ImageEnhance, ImageStat

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reference', type=Path)
    parser.add_argument('actual', type=Path)
    parser.add_argument('--out', type=Path, default=Path('qa/comparison'))
    args = parser.parse_args()
    ref = Image.open(args.reference).convert('RGB')
    actual = Image.open(args.actual).convert('RGB')
    if ref.size != actual.size:
        parser.error(f'Size mismatch: reference={ref.size}, actual={actual.size}. Capture at correct viewport/DPR; do not resize.')
    args.out.mkdir(parents=True, exist_ok=True)
    Image.blend(ref, actual, .5).save(args.out / 'overlay.png')
    diff = ImageChops.difference(ref, actual)
    ImageEnhance.Contrast(diff).enhance(3).save(args.out / 'diff-x3.png')
    combined = Image.new('RGB', (ref.width * 2, ref.height))
    combined.paste(ref, (0, 0))
    combined.paste(actual, (ref.width, 0))
    combined.save(args.out / 'side-by-side.png')
    mae = sum(ImageStat.Stat(diff).mean) / 3
    print(f'RGB mean absolute difference (0..255): {mae:.3f}; NOT a similarity percentage.')
    print(f'Inspect outputs visually: {args.out.resolve()}')

if __name__ == '__main__':
    main()
