@echo off
REM CR2026 @DaemoniaX https://github.com/DaemoniaX

echo Hi, please don't forget to edit the path if needed.
echo.
echo Starting import process...
echo.

REM Edit the name and path if needed
set "NAME=SAVENAME"
set "BACKUP_DIR=%USERPROFILE%\Desktop\Backup_Minecraft"
set "MODPACK_TARGET=%USERPROFILE%\curseforge\minecraft\Instances\MODPACKNAME\saves\SAVENAME"
set "EXTRACT_TEMP=%BACKUP_DIR%\Temp_Extract"

echo Searching for latest version...

set /p "LATEST_ZIP=What is the exact name of the zip file (including the .zip)? "
set "ZIP_SOURCE=%USERPROFILE%\Desktop\Backup_Minecraft\%LATEST_ZIP%"

REM checking if the file exist
if not exist "%ZIP_SOURCE%" (
    echo.
    echo ERROR: The file "%LATEST_ZIP%" was not found in the Backup_Minecraft folder.
    pause
    exit /b
)

echo.
echo Extracting the save...

powershell -Command "Expand-Archive -Path '%ZIP_SOURCE%' -DestinationPath '%EXTRACT_TEMP%' -Force"
xcopy "%EXTRACT_TEMP%\%NAME%" "%MODPACK_TARGET%" /E /I /H /Y > nul

REM Clean up
rmdir /S /Q "%EXTRACT_TEMP%"

echo.
echo Restore finished.
pause