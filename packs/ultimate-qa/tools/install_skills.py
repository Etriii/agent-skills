"""Use the collection lifecycle tool with this Ultimate QA pack selected."""

from pathlib import Path
import sys

PACK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACK.parents[1] / "tools"))
from install_skills import main


if __name__ == "__main__":
    raise SystemExit(main(["--pack", PACK.name, "--source", str(PACK), *sys.argv[1:]]))
