@echo off

systeminfo | findstr /B /C:"OS Name" > operacnisystem.aspectra
find /i /c "Microsoft Windows 8" operacnisystem.aspectra >NUL
if %errorlevel% equ 0 (
  del operacnisystem.aspectra
  Microsoft Windows 8 > win8sys.aspectra
  cls
  title Je požadována vaše akce - Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Je požadována vaše akce.
  echo.
  echo.
  echo Bylo detekováno, že používáte Microsoft Windows 8.
  echo Tento operační systém nemusí být plně kompatibilní s Aspectra Total
  echo Security, a proto budou některé funkce vypnuty a na skeny bude
  echo užívána pouze jedna ze dvou metod. Toto může mít za následek
  echo označení viru jako bezpečný soubor. Využívání Aspectra Total
  echo Security však nebude omezeno úplně a všechny kompatibilní funkce
  echo budou přístupné.
  echo.
  echo Pokračováním s tímto počítáte.
  pause
) else (
  del operacnisystem.aspectra
)

if exist lcncklc.aspectra goto menu

:licencni_klic
cls
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
goto licencni_klic

:menu
  exit
  cls
  title Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Jste zabezpečeni.
  echo.
  echo.
  echo (SKEN) - začne skenovat.
  echo (OPUSTIT) - zavře Aspectra Total Security.
  echo.
  set /p volba="Prosíme, zadejte vaši volbu: "
  if /i "%volba%" == "sken" goto sken
  if /i "%volba%" == "opustit" exit
  echo.
  echo Toto není platná volba.
  pause
  goto menu

:sken
  cls
  echo Aspectra Total Security
  echo.
  echo Jste zabezpečeni.
  echo.
  echo.
  echo (ZPĚT) - přejde zpět do menu.
  echo.
  set /p soubor="Prosíme, zadejte umístění skenovaného souboru nebo zvolte volbu: "
  if /i "%soubor%" == "zpět" goto menu
  if exist win8sys.aspectra exit
  @CertUtil -hashfile %soubor% MD5 > md5.aspectra
  for /f "tokens=1*delims=:" %%G in ('findstr /n "^" md5.aspectra') do if %%G equ 2 set md5=%%H
  del md5.aspectra

  rem --------------------------------------------------------------------------------------------------------------------

  set md5=%md5: =%

  if "%md5%" == "9b533c3e1e028eff67c9f97ead1cf7c8" set hrozba=Win32.Ransom.7ev3n.A
  if "%md5%" == "768a4aa523b9d3f3bc44b4ebdee706dc" set hrozba=Win32.Ransom.7ev3n.B
  if "%md5%" == "63d4e4dac57bd7d2059587eba4162652" set hrozba=Win32.Ransom.SureRansom.A
  if "%md5%" == "50a1420208213d0ca9e1a24fd2806882" set hrozba=Win32.Ransom.XiaoBa.A
  if "%md5%" == "58c72587910a4f82c7942ee89fe227b7" set hrozba=Win32.RAT.Warzone.A
  if "%md5%" == "477d35e62bfe6045774ae74b616e4844" set hrozba=Win32.Trojan.Zeus.A
  if "%md5%" == "e76eca2f7d0450c84417a8ac242b424c" set hrozba=Win32.Ransom.Donut.A
  if "%md5%" == "05632175cc24f9253c06221a6faa5870" set hrozba=Win32.Virus.Winvir.A
  rem --------------------------------------------------------------------------------------------------------------------
