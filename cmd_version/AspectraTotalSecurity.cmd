@echo off
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

:menu
  exit

rem --------------------------------------------------------------------------------------------------------------------

set md5=%md5: =%

if "%md5%" == "63d4e4dac57bd7d2059587eba4162652" set threat=Win32.Ransom.SureRansom.A

rem --------------------------------------------------------------------------------------------------------------------
