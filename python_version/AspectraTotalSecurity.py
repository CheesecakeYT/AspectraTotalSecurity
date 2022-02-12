sha256 = input('Prosime, zadejte SHA256 souboru: ')
threat = 'Zadna hrozba'
sha256.replace(' ', '')

if sha256 == 'f89345b3f5e45b76e49c61ab5db44db384350e20230de897dd548f2fd9c752c0' threat = 'DOS/Virus.Holiday.A'
if sha256 == '13c92506e1ec7986e4ead73470f5516bf1c01f25b46989551c67c22dba76bead' threat = 'Win32/Ransom.WannaCryptor.A'
if sha256 == '59fe169797953f2046b283235fe80158ebf02ba586eabfea306402fba8473dae' threat = 'Win32/Worm.CodeRed.A'
if sha256 == 'cbadaf9825a8338853498cd9b299c987444d26f6bf7de0e6964d77fcdff1514a' threat = 'Win32/Worm.CodeRed.B'
if sha256 == '5b7228947b256f36bd98dde1622799cda8f7a7aa0f3196aba08200fe8439dfee' threat = 'Win32/Worm.Doomjuice.A'
if sha256 == '9173cb0476b7123fb0c2d46e0e73c3b3ece3f657ca98ed2264764d7b41bee132' threat = 'Win32/Worm.Doomjuice.B'
if sha256 == '6cd0666ee68849e57e054c6a009366868494c4ec73723f607473375518591496' threat = 'Win32/Worm.Doomjuice.C'
if sha256 == '608e4a3d458c72c5463cc26eaf2c6b560b02a3a53be40e59de3e4b222d30cb2a' threat = 'Win32/Worm.Doomjuice.D'
if sha256 == '8e879cbfab7f2af00dd1e6f21a322c409e929c4ce57e8fe7ab30ddce456b9576' threat = 'Win32/Worm.Doomjuice.E'
if sha256 == 'fc50cce8b75c8561ff073d697f51278b7638ceda4a9d3b6fe7ba89f0b322c002' threat = 'Win32/Worm.Doomjuice.F'
if sha256 == '181f864212bddd3099d2cb7089a291a4d470387c498e615bb6220de83bfb6a37' threat = 'Win32/Worm.LoveLetter.A'

print(threat)

 f = open(filename)
 if "CONNECT %s:%i HTTP/1.0" in f.read() and "ws2_32" in f.read() and "thj@h" in f.read() and "cks=u" in f.read() and "advpack" in f.read threat = 'Win32/Backdoor.PoisonIvy.Gen'

print(threat)
