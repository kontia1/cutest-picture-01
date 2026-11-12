import os, shutil
from pathlib import Path

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).with_name("entry.png"), OUT / "entry.png")
