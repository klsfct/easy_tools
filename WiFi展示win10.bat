@echo off
echo.
echo.
echo.
echo -------win10中已保存的wifi密码查看------
echo.
echo.
echo.
set /p wifi_name="请输入要查看密码的wifi名称："
netsh wlan show profile name=%wifi_name% key=clear >%wifi_name%.txt

for /f "skip=32 delims=" %%a in (%wifi_name%.txt) do (
set txt=%%~a
goto :Show
)
:Show
set wifi_key=%txt:    关键内容            =为%
echo.
echo.
echo.
echo.
echo 无线网%wifi_name%的密码%wifi_key%
echo.
echo.
echo.
echo.
echo 记好了密码，按任意键退出cmd
del /f %wifi_name%.txt
pause 127.0.1>nul 
exit
