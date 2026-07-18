"""Build a small ZIP artifact using only the Python standard library."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


FILES_TO_PACKAGE = ("app.py", "src/__init__.py", "src/greeting.py")


def main() -> None:
    output_directory = Path("build")
    output_directory.mkdir(exist_ok=True)
    artifact = output_directory / "multibranch-practice.zip"

    with ZipFile(artifact, "w", ZIP_DEFLATED) as archive:
        for file_name in FILES_TO_PACKAGE:
            archive.write(file_name)

    print(f"Created {artifact}")


if __name__ == "__main__":
    main()

