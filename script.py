from pathlib import Path
import os
import shutil
import zipfile
import sys


def main():
    # Папка назначения: C:\Users\Public
    target_dir = Path(r"C:\Users\Public")
    target_dir.mkdir(parents=True, exist_ok=True)

    # Источник архива: %TMP%\a.zip
    tmp_dir = os.getenv("TMP")
    if not tmp_dir:
        print("Ошибка: переменная окружения TMP не найдена.")
        sys.exit(1)

    source_zip = Path(tmp_dir) / "a.zip"
    if not source_zip.exists():
        print(f"Ошибка: архив не найден: {source_zip}")
        sys.exit(1)

    # Куда перемещаем архив
    target_zip = target_dir / "a.zip"

    # Если уже есть a.zip в C:\Users\Public — удаляем
    if target_zip.exists():
        target_zip.unlink()

    # Перемещение архива
    shutil.move(str(source_zip), str(target_zip))
    print(f"Архив перемещен: {target_zip}")

    # Распаковка архива в C:\Users\Public
    with zipfile.ZipFile(target_zip, "r") as zf:
        zf.extractall(target_dir)

    print(f"Архив распакован в: {target_dir}")


if __name__ == "__main__":
    main()
