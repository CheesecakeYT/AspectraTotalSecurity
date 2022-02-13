filename = input('Prosime, zadejte jmeno souboru: ')
sha256 = input('Prosime, zadejte SHA256 souboru: ')
threat = 'Zadna hrozba'
sha256.replace(' ', '')

if sha256 == '54874e12ae06ef90e784b87adc6ae771240d09b527a9dc02ea8de527db3f6312' threat = 'DOS/Virus.Mummy.A'
if sha256 == 'f89345b3f5e45b76e49c61ab5db44db384350e20230de897dd548f2fd9c752c0' threat = 'DOS/Virus.Holiday.A'
if sha256 == '9233e922427985ad5fb2826ca7833148b57ce00a316d1611e1429e94ae4d5c93' threat = 'DOS/Virus.Virdem.A'
if sha256 == 'd038b700388148cbf5d7a4192e123da0b6f15e3dbd28ebee3f2b263fdd6f6b85' threat = 'Win32/Backdoor.PoisonIvy.A'
if sha256 == '8da8fb1e26164d18e849cfcad5ca222da395a1ef43f4a528ae758375372d13ef' threat = 'Win32/Ransom.NETCrypton.A'
if sha256 == '13c92506e1ec7986e4ead73470f5516bf1c01f25b46989551c67c22dba76bead' threat = 'Win32/Ransom.WannaCryptor.A'
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
if sha256 == 'e6cfdb31aa9a6a08bc428b2775be26eef7599cad0bb21948d280d5a3e5ddf150' threat = 'Win32/Worm.Totilix.A'

print(threat)

f = open(filename)

if "CONNECT %s:%i HTTP/1.0" in f.read() and "ws2_32" in f.read() and "thj@h" in f.read() and "cks=u" in f.read() and "advpack" in f.read() threat = 'Win32/Backdoor.PoisonIvy.Gen'
if "EaseUSHelper" in f.read() and "WARNING" in f.read() and 'ARE YOU SURE YOU WANT TO EXECUTE THIS RANSOMWARE?' in f.read() threat = 'Win32/Ransom.NETCrypton.Gen'\
if "AV Intelligent Updater" in f.read() and "Please select email address to send at your friend" in f.read() and 'Select email address with ' in f.read() threat = 'Win32/Worm.Totilix.Gen'

print(threat)
