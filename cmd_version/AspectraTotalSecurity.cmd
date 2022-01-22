@echo off

:licencni_klic
title Je požadována vaše akce - Aspectra Total Security
echo Aspectra Total Security
echo.
echo Je požadována vaše akce.
echo.
echo.
echo Prosíme, zadejte váš licenční klíč.
echo Pokud ještě nemáte zakoupený potřebný licenční klíč, prosíme, zakupte si ho
echo na oficiálních stránkách Aspectra.
echo.
set /p "klic=Zde zadejte váš licenční klíč: "
if /i "%klic%" == "SAXHP-IY7DC-ORJU5-6HG7A-LQVCC" (
  echo.
  echo Vyčkejte, právě zpracováváme zadaný klíč.
  echo Klic pridan > lcncklc.aspectra
  echo.
  echo Dokončeno. Váš klíč byl přijat.
  echo Aspectra Total Security je nyní odemčen.
  pause
  goto menu
)
echo.
echo Vámi zadaný klíč nebyl přijat.
pause
goto 

:menu
  exit
  cls
  title Aspectra Total Security

rem --------------------------------------------------------------------------------------------------------------------

set md5=%md5: =%

if "%md5%" == "9b533c3e1e028eff67c9f97ead1cf7c8" set hrozba=Win32.Ransom.7ev3n.A
if "%md5%" == "768a4aa523b9d3f3bc44b4ebdee706dc" set hrozba=Win32.Ransom.7ev3n.B
if "%md5%" == "63d4e4dac57bd7d2059587eba4162652" set hrozba=Win32.Ransom.SureRansom.A
if "%md5%" == "477d35e62bfe6045774ae74b616e4844" set hrozba=Win32.Ransom.Zeus
if "%md5%" == "50a1420208213d0ca9e1a24fd2806882" set hrozba=Win32.Ransom.XiaoBa
if "%md5%" == "58c72587910a4f82c7942ee89fe227b7" set hrozba=Win32.Trojan.Warzone
if "%md5%" == "307edbdde039109e64e0b0c651efae4d" set hrozba=Win32.Ransom.Ekans
rem --------------------------------------------------------------------------------------------------------------------
