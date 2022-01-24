@echo off

if not exist flpth.aspectra (
  cls
  title Je požadována vaše akce - Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Je požadována vaše akce.
  echo.
  echo.
  echo Vzhledem k neznámé chybě od vás žádáme umístění složky, ze které
  echo je Aspectra Total Security spouštěn.
  echo.
  set /p aspectradir="Prosíme, zadejte umístění složky: "
  echo %aspectradir% > flpth.aspectra
  cls
)
set /p aspectradir=<flpth.aspectra

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
  cls
  title Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Jste zabezpečeni.
  echo.
  echo.
  echo (SKEN) - začne skenovat.
  echo (NASTAVENÍ) - zobrazí možnosti nastavení.
  echo (OPUSTIT) - zavře Aspectra Total Security.
  echo.
  set /p volba="Prosíme, zvolte volbu: "
  if /i "%volba%" == "sken" goto sken
  if /i "%volba%" == "nastavení" goto nastaveni
  if /i "%volba%" == "opustit" exit
  echo.
  echo Toto není platná volba.
  pause
  goto menu
  
:nastaveni
  cls
  echo Aspectra Total Security
  echo.
  echo Jste zabezpečeni.
  echo.
  echo.
  echo (INFO) - zobrazí informace o Aspectra Total Security.
  echo (NAHLÁSIT) - nahlásí chybu, špatně označený program apod.
  echo (ZPĚT) - přejde zpět do menu.
  echo.
  set /p volba="Prosíme, zvolte volbu: "
  if /i "%volba%" == "info" goto info
  if /i "%volba%" == "nahlásit" start https://martinekmatej.wixsite.com/aspectra/contact
  if /i "%volba%" == "zpět" goto menu
  
:info
  cls
  echo Aspectra Total Security
  echo.
  echo Informace
  echo.
  echo.
  echo Aspectra Total Security
  echo.
  echo Experimentální verze
  echo Edice c921b374-8e42-4bc5-bc49-a6b9842b207b
  echo.
  echo Copyright Aspectra 2022.
  pause
  goto nastaveni

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
  
  cls
  title Probíhá sken - Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Právě probíhá sken.
  echo.
  echo.
  echo Prosíme, vyčkejte, než se sken dokončí.
  echo.
  echo Načítání potřebných souborů...
  if exist win8sys.aspectra goto yara
  echo Kalkulace MD5 hashe...
  @CertUtil -hashfile %soubor% MD5 > md5.aspectra
  for /f "tokens=1*delims=:" %%G in ('findstr /n "^" md5.aspectra') do if %%G equ 2 set md5=%%H
  del md5.aspectra
  echo Nastavování potřebných parametrů...
  set hrozba=0

  rem --------------------------------------------------------------------------------------------------------------------

  set md5=%md5: =%
  
  echo Skenování MD5 hashe...

  if "%md5%" == "44d88612fea8a8f36de82e1278abb02f" set hrozba=EicarTestFile
  if "%md5%" == "9b533c3e1e028eff67c9f97ead1cf7c8" set hrozba=Win32.Ransom.7ev3n.A
  if "%md5%" == "768a4aa523b9d3f3bc44b4ebdee706dc" set hrozba=Win32.Ransom.7ev3n.B
  if "%md5%" == "7ab91e57a1e2752cd8abee3db10853c5" set hrozba=Win32.Ransom.AngryDuck.A
  if "%md5%" == "e76eca2f7d0450c84417a8ac242b424c" set hrozba=Win32.Ransom.Donut.A
  if "%md5%" == "63d4e4dac57bd7d2059587eba4162652" set hrozba=Win32.Ransom.SureRansom.A
  if "%md5%" == "50a1420208213d0ca9e1a24fd2806882" set hrozba=Win32.Ransom.XiaoBa.A
  if "%md5%" == "e4bb04fe99f81331aa57a5c17b4c9111" set hrozba=Win32.Ransom.Xorist.A
  if "%md5%" == "58c72587910a4f82c7942ee89fe227b7" set hrozba=Win32.RAT.Warzone.A
  if "%md5%" == "477d35e62bfe6045774ae74b616e4844" set hrozba=Win32.Trojan.Zeus.A
  if "%md5%" == "002fa5e60703f6178140ec644c298716" set hrozba=Win32.Virus.Gollum.A
  if "%md5%" == "05632175cc24f9253c06221a6faa5870" set hrozba=Win32.Virus.Winvir.A
  
  rem --------------------------------------------------------------------------------------------------------------------

  if not "%hrozba%" == "0" goto hrozba
  
  :yara
  echo Přesouvání do databáze...
  cd %aspectradir%
  cd yara
  
  echo Načítání potřebných souborů...
  echo 0 > yara.aspectra
  
  echo Skenování na základě pravidel YARA...
  
  rem --------------------------------------------------------------------------------------------------------------------
  
  yara EicarTestFile.yar %soubor% > yara.aspectra
  yara Win32-Adware-Mobogenie.yar %soubor% > yara.aspectra
  yara Win32-Trojan-Spectroid.yar %soubor% > yara.aspectra
  yara Win32-Trojan-Winnti.yar %soubor% > yara.aspectra
  
  rem --------------------------------------------------------------------------------------------------------------------

  set /p hrozba=<yara.aspectra
  del yara.aspectra
  if "%hrozba%" == "0" goto bezpecny
  
:hrozba
  cls
  title Je požadována vaše akce - Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Je požadována vaše akce.
  echo.
  echo.
  echo Soubor %soubor% byl označen jako infikovaný.
  echo.
  echo Detekováno: %hrozba%
  echo.
  echo (SMAZAT) - smaže soubor.
  echo (KARANTÉNA) - přesune soubor do karantény.
  echo (IGNOROVAT) - ignoruje hrozbu. (nedoporučeno)
  echo.
  set /p volba="Prosíme, zvolte volbu: "
  if /i "%volba%" == "smazat" (
    echo.
    del %soubor%
    if %errorlevel% equ 1 (
      echo.
      echo Soubor se nepodařilo smazat.
      pause
      goto hrozba
    ) else (
      echo.
      echo Soubor byl úspěšně smazán.
      pause
      goto sken
    )
  )
  if /i "%volba%" == "karanténa" (
    echo.
    cd %aspectradir%
    if not exist quarant\ mkdir quarant
    move /Y %soubor% quarant\%hrozba%.aspectraquarant
    cipher /e quarant\%hrozba%.aspectraquarant
    if %errorlevel% equ 1 (
      echo.
      echo Soubor se nepodařilo přesunout do karantény.
      pause
      goto hrozba
    ) else (
      echo.
      echo Soubor byl úspěšně přesunut do karantény.
      pause
      goto sken
    )
  )
  if /i "%volba%" == "ignorovat" (
    echo.
    echo Hrozba byla ignorována.
    pause
    goto sken
  )
  echo.
  echo Toto není platná volba.
  pause
  goto hrozba

:bezpecny
  cls
  title Sken byl dokončen - Aspectra Total Security
  echo Aspectra Total Security
  echo.
  echo Sken byl dokončen.
  echo.
  echo.
  echo Soubor %soubor% byl označen jako čistý.
  echo.
  pause
  goto sken
