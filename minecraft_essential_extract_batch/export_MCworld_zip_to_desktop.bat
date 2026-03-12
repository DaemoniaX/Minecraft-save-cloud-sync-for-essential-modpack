@echo off
REM this project serve to export a minecraft world after playing it for your friends, after using the essential mod
REM it works only on CurseForge and if you have not changed the destination path of the modpack
REM CR2026 @DaemoniaX https://github.com/DaemoniaX

REM I was thinking of a script that was going to creat a new script, while asking you the variables like the name of the modpack or the full link so that you have to edit the file...but that's not a great idea
echo Hey there, if there is any issue, make sure to change the SOURCE to the real one.
echo To do that, open the modpack on Curseforge, next to the Play button, click on the three dots and click on Open Folder.
echo Then grab the path/link, and make sur to keep the USERPROFILE part if it's inside your user folder, and the name of the save inside of saves.
echo Note : I didn't want to make ppl install rclone because it would be a hell for each ppl to setup this. So just dragging it to the drive yourself is better.

echo.
echo Starting the export...

REM SOURCE is the path to the source save and the name of the save
set "NAME=SAVENAME"
set "SOURCE=%USERPROFILE%\curseforge\minecraft\Instances\MODPACKNAME\saves\SAVENAME"
set "DESTINATION=%USERPROFILE%\Desktop\Backup_Minecraft\%NAME%"

REM Get the date for versionning
set "CURRENT_DATE=%DATE:/=-%"


set "ZIP_DESTINATION=%USERPROFILE%\Desktop\Backup_Minecraft\%NAME%_%CURRENT_DATE%.zip"

REM Copy and compress
xcopy "%SOURCE%" "%DESTINATION%" /E /I /H /Y
powershell -Command "Compress-Archive -Path '%DESTINATION%' -DestinationPath '%ZIP_DESTINATION%' -Force"

echo.
echo Export finished : Backup_Minecraft_%CURRENT_DATE%.zip is on the Desktop.
echo You can depose it on a google drive folder.
pause
