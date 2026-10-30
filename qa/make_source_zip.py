"""Đóng gói source và bằng chứng QA, bỏ dependency/build output."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
output = root / "TienLen_MidnightArena_Prototype_Source.zip"
excluded_dirs = {"node_modules", "dist", "dist-review", "test-results", "playwright-report", ".git", "__pycache__", ".vite"}
with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=6) as archive:
    for path in root.rglob("*"):
        if not path.is_file() or path == output:
            continue
        relative = path.relative_to(root)
        if any(part in excluded_dirs for part in relative.parts):
            continue
        archive.write(path, relative.as_posix())
print(output)

