from pathlib import Path
import os
import shutil
import zipfile
import sys
import subprocess
from datetime import datetime


def log_message(log_path: Path, message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


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

    # Папка для распаковки: C:\Users\Public\a
    extract_dir = target_dir / "a"
    extract_dir.mkdir(parents=True, exist_ok=True)
    log_path = extract_dir / "install.log"

    # Распаковка архива в C:\Users\Public\a
    with zipfile.ZipFile(target_zip, "r") as zf:
        zf.extractall(extract_dir)
    log_message(log_path, f"Архив распакован в: {extract_dir}")

    # Проверяем наличие win.py
    win_script = extract_dir / "win.py"
    if not win_script.exists():
        log_message(log_path, f"Ошибка: не найден файл {win_script}")
        sys.exit(1)

    # Единоразовый запуск win.py через python.exe
    python_exe = Path(sys.executable)
    log_message(log_path, f"Запуск: {python_exe} {win_script}")

    try:
        process = subprocess.Popen(
            [str(python_exe), str(win_script)],
            cwd=str(extract_dir),
        )
    except OSError as exc:
        log_message(log_path, f"Ошибка запуска win.py: {exc}")
        sys.exit(1)

    log_message(log_path, f"win.py запущен, PID: {process.pid}")


if __name__ == "__main__":
    main()
