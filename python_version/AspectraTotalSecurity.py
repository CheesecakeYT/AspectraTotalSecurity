filename = input('Prosime, zadejte jmeno souboru: ')
sha256 = input('Prosime, zadejte SHA256 souboru: ')
threat = 'Zadna hrozba'
sha256.replace(' ', '')

if sha256 == 'f9855faa9de74bad527e685c774a4657074ac0413397e63c5543b587e7504156' threat = 'DOS/Virus.Cruncher.A'
if sha256 == '6dd6e06d6c7aea56b4d55c0207e7e825c33d5af67a546a0c2f37a767c79e54e1' threat = 'DOS/Virus.Fellow.A'
if sha256 == '88175d899be2458041895314e447b647811f2950ee30a6854f77a22b91a36df9' threat = 'DOS/Virus.Girls.A'
if sha256 == '54874e12ae06ef90e784b87adc6ae771240d09b527a9dc02ea8de527db3f6312' threat = 'DOS/Virus.Mummy.A'
if sha256 == 'f89345b3f5e45b76e49c61ab5db44db384350e20230de897dd548f2fd9c752c0' threat = 'DOS/Virus.Holiday.A'
if sha256 == '9233e922427985ad5fb2826ca7833148b57ce00a316d1611e1429e94ae4d5c93' threat = 'DOS/Virus.Virdem.A'
if sha256 == 'ff01fcc87a878d702261930565df55fbfd686f39345f362b830a530866002c06' threat = 'DOS/Virus.Wisconsin.A'
if sha256 == 'b860c85038a5e4278a887812fbc26d1588dd14087e2c44667fdd21ea76b62644' threat = 'Linux/Virus.Sickabs.A'
if sha256 == 'b9cb9b6547dd95b1e78ab335ff4768223b58478d261b3e8adc57541fa488955b' threat = 'Win32/Backdoor.Okrum.A'
if sha256 == 'd038b700388148cbf5d7a4192e123da0b6f15e3dbd28ebee3f2b263fdd6f6b85' threat = 'Win32/Backdoor.PoisonIvy.A'
if sha256 == 'cd13fc0d90311a2412effdbb314b61dd5bc42bd01d0a80c59d3bd51bcd1e578f' threat = 'Win32/Ransom.AWT.A'
if sha256 == 'c18a52f4a2064124f1bfff0757b1d7f7aa6df10bd3e4f2f4270cf3625c73831e' threat = 'Win32/Ransom.DirtyDecrypt.A'
if sha256 == 'e049d8f69ddee0c2d360c27b98fa9e61b7202bb0d3884dd3ca63f8aa288422dc' threat = 'Win32/Ransom.EternalRocks.A'
if sha256 == '8da8fb1e26164d18e849cfcad5ca222da395a1ef43f4a528ae758375372d13ef' threat = 'Win32/Ransom.NETCrypton.A'
if sha256 == 'df96eb9c4ef47f5c20662c037c32f11d777802e67df091c60d6fcd82ff1b818e' threat = 'Win32/Ransom.Phobos.A'
if sha256 == '23d3f8aa6e5d072259dd8aeeb4fbe70ca6bbfdfbb4be3b7166b6c399d836bee2' threat = 'Win32/Ransom.Rijndael.A'
if sha256 == '8ad873e8543935a9cc12317f90676019801257de4b0845414a7df058e03d6d7f' threat = 'Win32/Ransom.WannaCash.A'
if sha256 == '13c92506e1ec7986e4ead73470f5516bf1c01f25b46989551c67c22dba76bead' threat = 'Win32/Ransom.WannaCryptor.A'
if sha256 == '83ecb875f87150a88f4c3d496eb3cb5388cd8bafdff4879884ececdbd1896e1d' threat = 'Win32/Rogue.NavaShield.A'
if sha256 == '08b6f3ec3171995a4c96a8ba316543ca299502a3a5d8eecd6e37e3cf01cb7ae3' threat = 'Win32/Rogue.NavaShield.B'
if sha256 == 'd038ca188c724d148f878edfdeb39f35cc02d9c1e0ca3c5c1de5da9c79062c92' threat = 'Win32/Rogue.SystemSecurity.A'
if sha256 == '50200a4b836cc4b8a7503bf28fba98ebc54bdd423660dc890a6669cc097a5729' threat = 'Win32/Virus.Blackbat.A'
if sha256 == '59fe169797953f2046b283235fe80158ebf02ba586eabfea306402fba8473dae' threat = 'Win32/Worm.CodeRed.A'
if sha256 == 'cbadaf9825a8338853498cd9b299c987444d26f6bf7de0e6964d77fcdff1514a' threat = 'Win32/Worm.CodeRed.B'
if sha256 == '5b7228947b256f36bd98dde1622799cda8f7a7aa0f3196aba08200fe8439dfee' threat = 'Win32/Worm.Doomjuice.A'
if sha256 == '9173cb0476b7123fb0c2d46e0e73c3b3ece3f657ca98ed2264764d7b41bee132' threat = 'Win32/Worm.Doomjuice.B'
if sha256 == '6cd0666ee68849e57e054c6a009366868494c4ec73723f607473375518591496' threat = 'Win32/Worm.Doomjuice.C'
if sha256 == '608e4a3d458c72c5463cc26eaf2c6b560b02a3a53be40e59de3e4b222d30cb2a' threat = 'Win32/Worm.Doomjuice.D'
if sha256 == '8e879cbfab7f2af00dd1e6f21a322c409e929c4ce57e8fe7ab30ddce456b9576' threat = 'Win32/Worm.Doomjuice.E'
if sha256 == 'fc50cce8b75c8561ff073d697f51278b7638ceda4a9d3b6fe7ba89f0b322c002' threat = 'Win32/Worm.Doomjuice.F'
if sha256 == '181f864212bddd3099d2cb7089a291a4d470387c498e615bb6220de83bfb6a37' threat = 'Win32/Worm.LoveLetter.A'
if sha256 == '068f2ee28af7645dbf2a1684f0a5fc5ccb6aa1027f71da4468e0cba56c65e058' threat = 'Win32/Worm.Magistr.A'
if sha256 == 'e6cfdb31aa9a6a08bc428b2775be26eef7599cad0bb21948d280d5a3e5ddf150' threat = 'Win32/Worm.Totilix.A'

print(threat)

f = open(filename)

if "CONNECT %s:%i HTTP/1.0" in f.read() and "ws2_32" in f.read() and "thj@h" in f.read() and "cks=u" in f.read() and "advpack" in f.read() threat = 'Win32/Backdoor.PoisonIvy.Gen'
if "/[Aa]ccept\-[Ee]ncoding: [a-z\-]{1,16},([a-z\-\s]{1,16},|)*[\s]{1,20},/" in f.read() threat = 'Win32/Exploit.CVE-2021-31166.Gen'
if "EaseUSHelper" in f.read() and "WARNING" in f.read() and 'ARE YOU SURE YOU WANT TO EXECUTE THIS RANSOMWARE?' in f.read() threat = 'Win32/Ransom.NETCrypton.Gen'
if "AV Intelligent Updater" in f.read() and "Please select email address to send at your friend" in f.read() and 'Select email address with ' in f.read() threat = 'Win32/Worm.Totilix.Gen'
if "" 

print(threat)
