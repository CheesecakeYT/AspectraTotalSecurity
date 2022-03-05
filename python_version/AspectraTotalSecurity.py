import tkinter as tk
import hashlib

filename = tk.filedialog.askopenfilename(title="Prosíme, vyberte soubor pro kontrolu:")
if filename:
  sha256 = hashlib.sha256(filename)
  threat = 'Žádná hrozba'
  sha256.replace(' ', '')
  tk.messagebox.showinfo('Aspectra Total Security', 'Hledáme viry a malware.')

  def f(threat):
      return {
          '79e602a062d05fbb1409afc16e6d41ac0645576b2b5c1899dc93e6852c30a71f': 'Android/Ransom.DoubleLocker.A',
          '929cf1806157df25d78c6fae4461c6d67bd6dd129e276995e7bf7ffe7aa88786': 'Android/Ransom.DoubleLocker.B',
          '3fa13b22b716ade35153a7330dc1873a9f411445d4ed2a834e8fb011262ed2bc': 'DOS/Virus.Cosenza.A',
          'f9855faa9de74bad527e685c774a4657074ac0413397e63c5543b587e7504156': 'DOS/Virus.Cruncher.A',
          '6dd6e06d6c7aea56b4d55c0207e7e825c33d5af67a546a0c2f37a767c79e54e1': 'DOS/Virus.Fellow.A',
          'adf6ec168a36bc1b2820cc72220fa2b4236c07435d140e667791f69f25e660b6': 'DOS/Virus.Freddy.A',
          '88175d899be2458041895314e447b647811f2950ee30a6854f77a22b91a36df9': 'DOS/Virus.Girls.A',
          'f89345b3f5e45b76e49c61ab5db44db384350e20230de897dd548f2fd9c752c0': 'DOS/Virus.Holiday.A',
          '54874e12ae06ef90e784b87adc6ae771240d09b527a9dc02ea8de527db3f6312': 'DOS/Virus.Mummy.A',
          'bd9aa78e769210aa68361e07f0a7580b026c005ac8798845fafd23d331865699': 'DOS/Virus.Nygus.A',
          '22acc9a31fd805921c943d0bb7d951565e835d5000cae2ff188ae9a802fdb97b': 'DOS/Virus.Selectron.A',
          '9233e922427985ad5fb2826ca7833148b57ce00a316d1611e1429e94ae4d5c93': 'DOS/Virus.Virdem.A',
          'ff01fcc87a878d702261930565df55fbfd686f39345f362b830a530866002c06': 'DOS/Virus.Wisconsin.A',
          'b860c85038a5e4278a887812fbc26d1588dd14087e2c44667fdd21ea76b62644': 'Linux/Virus.Sickabs.A',
          'f7f1e54f77ef454b557715576bf220e14cfb678a4de4a5fd29cf50e42c57ee80': 'Win32/Adware.Adload.A',
          '1bfcdbfd55a3868662972436e062833ea63c852a48fe3b2cc615e32f5a387028': 'Win32/Adware.Adposhel.A',
          '0a104928dda5b6e4a04c050d33bf75fec29fe7b843d47f7f89c527cce5e1d456': 'Win32/Adware.Adposhel.B',
          'fecaa7ac86c4301544c6004bc2c3b6a73f88fe6a625c3c8bee43187c988e4b47': 'Win32/Adware.Adposhel.C',
      }[threat]

  if sha256 == 'dc176b80aadebdfa96a8e55867fb0f3778c80ec94a99ff9751b49bce441c51ca': threat = 'Win32/Adware.Linkury.A'
  if sha256 == '11bebe94ad92e094f42052ed9b52f26c28b76660ff2c6fc5292f81a525d4e768': threat = 'Win32/Adware.Linkury.B'
  if sha256 == '552a5eeb89f450c448e7cede3233bb04d69e0b106d356f0257634581e9f0aa71': threat = 'Win32/Adware.MegaSearch.A'
  if sha256 == '1074cbc810766e42cd8b875c7492432479406e7d1c6ba8d4b7a01b268544abc1': threat = 'Win32/Adware.Techsnab.A'
  if sha256 == 'ba863c7cd5f95e2aa79ab9d99f138bf697f59b3bf7a0df697113d47bb7a106c8': threat = 'Win32/Adware.Toptools.A'
  if sha256 == 'f6c62cda8576e3662498bed18196e1fd038e26ed46c7da8bbeb4e68e49ec0a27': threat = 'Win32/Backdoor.BackConstruction.A'
  if sha256 == '54cc576e2acd83ed9e530184d481c5b7e3423056b81aac072c367426d7319617': threat = 'Win32/Backdoor.Caphaw.A'
  if sha256 == 'b9cb9b6547dd95b1e78ab335ff4768223b58478d261b3e8adc57541fa488955b': threat = 'Win32/Backdoor.Okrum.A'
  if sha256 == 'd038b700388148cbf5d7a4192e123da0b6f15e3dbd28ebee3f2b263fdd6f6b85': threat = 'Win32/Backdoor.PoisonIvy.A'
  if sha256 == '10bfd9746863fd90e7c7b204a2a0a0c529f12b5a7dea51858e81f32698c168f8': threat = 'Win32/CoinMiner.Herxmin.A'
  if sha256 == 'c1ab3fa03646265f270708704c596bf22e871fa0efafb4816cc8ceba9ee8965e': threat = 'Win32/Hacktool.AutoKMS.A'
  if sha256 == 'f9b6015249a88411772a6631078938e96024c5cf6f83f1ed69437eb7947731a0': threat = 'Win32/PUP.EndermanchMalwareDatabase.A'
  if sha256 == 'af61423563ef11b1430dfffb0e12fe26b0dbf54deee76a69e2ffb2643c84f296': threat = 'Win32/PUP.SystweakPCFixer.A'
  if sha256 == 'cd13fc0d90311a2412effdbb314b61dd5bc42bd01d0a80c59d3bd51bcd1e578f': threat = 'Win32/Ransom.AWT.A'
  if sha256 == '08cf8ed94cc1ef6ae23133f3e506a50d8aad9047c6fa74568a0373d991261aa4': threat = 'Win32/Ransom.Defray.A'
  if sha256 == '71089d862e3bb4c3a351252fcd6d9018866c265707508ed397f3efcdf3702723': threat = 'Win32/Ransom.Defray.B'
  if sha256 == '6543ad7d8b6701448a45072b2133bb24dc53a23247e1815a8e6d9bfe9cfc28c6': threat = 'Win32/Ransom.Defray.C'
  if sha256 == 'c18a52f4a2064124f1bfff0757b1d7f7aa6df10bd3e4f2f4270cf3625c73831e': threat = 'Win32/Ransom.DirtyDecrypt.A'
  if sha256 == 'e049d8f69ddee0c2d360c27b98fa9e61b7202bb0d3884dd3ca63f8aa288422dc': threat = 'Win32/Ransom.EternalRocks.A'
  if sha256 == '7f1d3ed805910aa90172d72e7923d129d2967bfe50398e863ec48b71c952b199': threat = 'Win32/Ransom.Ims00ry.A'
  if sha256 == '55f1ce7d7b3cf941ea355a07623b02a6ec2007d1f5069717a449dd31405bb86b': threat = 'Win32/Ransom.Keslan.A'
  if sha256 == 'd969116e7897b5a99cc28cfdc274191816e09e5d84d07da4cdbd3825552c3417': threat = 'Win32/Ransom.Keslan.B'
  if sha256 == '8da8fb1e26164d18e849cfcad5ca222da395a1ef43f4a528ae758375372d13ef': threat = 'Win32/Ransom.NETCrypton.A'
  if sha256 == '26b4699a7b9eeb16e76305d843d4ab05e94d43f3201436927e13b3ebafa90739': threat = 'Win32/Ransom.Petya.A'
  if sha256 == 'df96eb9c4ef47f5c20662c037c32f11d777802e67df091c60d6fcd82ff1b818e': threat = 'Win32/Ransom.Phobos.A'
  if sha256 == '23d3f8aa6e5d072259dd8aeeb4fbe70ca6bbfdfbb4be3b7166b6c399d836bee2': threat = 'Win32/Ransom.Rijndael.A'
  if sha256 == 'a949bdbfa8255741acf437b34b506310c7210707f84aef6d8ef85e9c2ff1993a': threat = 'Win32/Ransom.SadComputer.A'
  if sha256 == 'c49eb3f83f94347d223338a13a2a57387ac689dc16d64f3d41a251b3a3325e5d': threat = 'Win32/Ransom.Spartacus.A'
  if sha256 == '8ad873e8543935a9cc12317f90676019801257de4b0845414a7df058e03d6d7f': threat = 'Win32/Ransom.WannaCash.A'
  if sha256 == '13c92506e1ec7986e4ead73470f5516bf1c01f25b46989551c67c22dba76bead': threat = 'Win32/Ransom.WannaCryptor.A'
  if sha256 == 'd793f37eb89310ddfc6d0337598c316db0eccda4d30e34143c768235594a169c': threat = 'Win32/RAT.AsyncRAT.A'
  if sha256 == '4717ee69d28306254b1affa7efc0a50c481c3930025e75366ce93c99505ded96': threat = 'Win32/RAT.AsyncRAT.B'
  if sha256 == '246333f2fac7a9a4c7b3b7d4b68b7c00effe9bf0f1019187270bafc9a2f86f7a': threat = 'Win32/Rogue.GoldAntivirus.A'
  if sha256 == '83ecb875f87150a88f4c3d496eb3cb5388cd8bafdff4879884ececdbd1896e1d': threat = 'Win32/Rogue.NavaShield.A'
  if sha256 == '08b6f3ec3171995a4c96a8ba316543ca299502a3a5d8eecd6e37e3cf01cb7ae3': threat = 'Win32/Rogue.NavaShield.B'
  if sha256 == 'd038ca188c724d148f878edfdeb39f35cc02d9c1e0ca3c5c1de5da9c79062c92': threat = 'Win32/Rogue.SystemSecurity.A'
  if sha256 == '86068d1d63e88ed79e32c95036aa41a5f5e7bba108ef4d8c25c919fb213fb10a': threat = 'Win32/Rootkit.Agent.A'
  if sha256 == '9d3fe04d88c401178165f7fbdf307ac0fb690cc5fef8b70ee7f380307d4748f8': threat = 'Win32/Trojan.000.A'
  if sha256 == '569cf8b606e33cfc34c8bd97839b8b827758051ff696ebaddf26ea9fd953ce98': threat = 'Win32/Trojan.Agent.A'
  if sha256 == '662ed4a2153333a2789f3b5e5b5af9e8b1cf1c8a9656e73bb9ee3e28e9046172': threat = 'Win32/Trojan.Agent.B'
  if sha256 == 'e438b2b103d363631f1339b6441dec1f86b50739cfa8e7476ad2e4e0061874c3': threat = 'Win32/Trojan.Agent.C'
  if sha256 == '422c932d36addc9f706109bd99544f43014518f83cc489b3d09e888f305cb8b6': threat = 'Win32/Trojan.Agent.D'
  if sha256 == 'f070893ea7ba643dabb4900f1971920830d0afabac44050e6bd46c30e26b47f8': threat = 'Win32/Trojan.Agent.E'
  if sha256 == '47f6d3a11ffd015413ffb96432ec1f980fba5dd084990dd61a00342c5f6da7f8': threat = 'Win32/Trojan.NoEscape.A'
  if sha256 == 'b0611cd3dadd441bc00145be8a08b480e60022a5b0da21533ffd313394efedbc': threat = 'Win32/Trojan.Staser.A'
  if sha256 == 'b090e99e4b74ca679895a724548c1a256fbb613524a9addec81eff17008c76c7': threat = 'Win32/Trojan.Tasker.A'
  if sha256 == 'ebd7809cacae62bc94dfb8077868f53d53beb0614766213d48f4385ed09c73a6': threat = 'Win32/Trojan.Zephyr.A'
  if sha256 == '67250d5e5cb42df505b278e53ae346e7573ba60a06c3daac7ec05f853100e61c': threat = 'Win32/Trojan.Zephyr.B'
  if sha256 == '50200a4b836cc4b8a7503bf28fba98ebc54bdd423660dc890a6669cc097a5729': threat = 'Win32/Virus.Blackbat.A'
  if sha256 == '05ca0bc0c76403d2dea6009cf246514ce830957b8cc2b9d49efc547808213c34': threat = 'Win32/Virus.Neshta.A'
  if sha256 == 'cf12828badd536fc759358b3ca6684090ba9907a1e6b2571cb7f7a52f8c094cf': threat = 'Win32/Virus.Neshta.B'
  if sha256 == '980bac6c9afe8efc9c6fe459a5f77213b0d8524eb00de82437288eb96138b9a2': threat = 'Win32/Virus.Neshta.C'
  if sha256 == '59fe169797953f2046b283235fe80158ebf02ba586eabfea306402fba8473dae': threat = 'Win32/Worm.CodeRed.A'
  if sha256 == 'cbadaf9825a8338853498cd9b299c987444d26f6bf7de0e6964d77fcdff1514a': threat = 'Win32/Worm.CodeRed.B'
  if sha256 == '5b7228947b256f36bd98dde1622799cda8f7a7aa0f3196aba08200fe8439dfee': threat = 'Win32/Worm.Doomjuice.A'
  if sha256 == '9173cb0476b7123fb0c2d46e0e73c3b3ece3f657ca98ed2264764d7b41bee132': threat = 'Win32/Worm.Doomjuice.B'
  if sha256 == '6cd0666ee68849e57e054c6a009366868494c4ec73723f607473375518591496': threat = 'Win32/Worm.Doomjuice.C'
  if sha256 == '608e4a3d458c72c5463cc26eaf2c6b560b02a3a53be40e59de3e4b222d30cb2a': threat = 'Win32/Worm.Doomjuice.D'
  if sha256 == '8e879cbfab7f2af00dd1e6f21a322c409e929c4ce57e8fe7ab30ddce456b9576': threat = 'Win32/Worm.Doomjuice.E'
  if sha256 == 'fc50cce8b75c8561ff073d697f51278b7638ceda4a9d3b6fe7ba89f0b322c002': threat = 'Win32/Worm.Doomjuice.F'
  if sha256 == '09ce6f92f47cb07d66434bea7860fb543483e09b0ee7585723e5ae6f2e7b993a': threat = 'Win32/Worm.Fizzer.A'
  if sha256 == '181f864212bddd3099d2cb7089a291a4d470387c498e615bb6220de83bfb6a37': threat = 'Win32/Worm.LoveLetter.A'
  if sha256 == '6c65feef8c7fd68585e3b91cd4180211889d75c47776057d996717a7f0699d23': threat = 'Win32/Worm.LoveLetter.B'
  if sha256 == '068f2ee28af7645dbf2a1684f0a5fc5ccb6aa1027f71da4468e0cba56c65e058': threat = 'Win32/Worm.Magistr.A'
  if sha256 == '88376cc51b37ab8c335f821c1129a0e8600dab9605e5d775933bcd7ceedfac8c': threat = 'Win32/Worm.Nimda.A'
  if sha256 == 'e6cfdb31aa9a6a08bc428b2775be26eef7599cad0bb21948d280d5a3e5ddf150': threat = 'Win32/Worm.Totilix.A'
  if sha256 == 'a8ccb7159dbf2f3d4703be46b805f8554e2e191cf4e7f43a419e33965b483b42': threat = 'Win64/Adware.MultiPlug.A'
  if sha256 == '4735b18c263cd1d29c96b64b26e7f4f54f9bf862286339a87f8d08db1fd1ca2e': threat = 'Win64/Adware.MultiPlug.B'
  if sha256 == 'fde9e3251cc1237aa3b2ad89acfb5691e8fee5a434989d9a9308ab41b774b672': threat = 'Win64/Adware.MultiPlug.C'
  if sha256 == 'a758ad4fdc8949ea005258075457a972eb0672d69d98d688117b85221fca096a': threat = 'Win64/Adware.MultiPlug.D'
  if sha256 == 'df26a06b2fffc5a491e3bd39bfac6a97bbc4f90ab4e1f85e32f1e1602094f850': threat = 'Win64/Adware.MultiPlug.E'
  if sha256 == 'bd5125467c5803679bd8139889a091731b7e10f097d3b4ced7fb8b56a968545b': threat = 'Win64/Adware.MultiPlug.F'
  if sha256 == 'a701ceb01833883ba36c205295d176f16fb378051ae6a18677c80327c5188331': threat = 'Win64/CoinMiner.Agent.A'
  if sha256 == '3f8f2face06ccf57353547c8865709bc7a6cf9dbdd2544ffdfd6fe7b7a0e5f96': threat = 'Win64/CoinMiner.Agent.B'
  if sha256 == '8e1260bbf43e54ef60672fc2efac525e961b5dee67146063aefcfda2d7161d89': threat = 'Win64/Trojan.Crackonosh.A'
  if sha256 == '3335ec57681b238846e0d19a3459dc739d11dfaf36722b7f19e609a96b97ad92': threat = 'Win64/Trojan.NSSManager.A'

  with open(filename) as f:
    contents = f.read()
  def f(threat):
    return {
      'Win32/Ransom.SadComputer.Gen': ['Sad Computer', 'Are You Sure You want to install Antivirus software?'],
    }[threat]

  if "CONNECT %s:%i HTTP/1.0" in f.read() and "ws2_32" in f.read() and "thj@h" in f.read() and "cks=u" in f.read() and "advpack" in f.read(): threat = 'Win32/Backdoor.PoisonIvy.Gen'
  if "/[Aa]ccept\-[Ee]ncoding: [a-z\-]{1,16},([a-z\-\s]{1,16},|)*[\s]{1,20},/" in f.read(): threat = 'Win32/Exploit.CVE-2021-31166.Gen'
  if "Online KMS" in f.read() and "Thanks to pawel97 for the patch ODT" in f.read() and "Thanks to DiamondMonday" in f.read(): threat = 'Win32/Hacktool.AutoKMS.Gen'
  if "EaseUSHelper" in f.read() and "WARNING" in f.read() and 'ARE YOU SURE YOU WANT TO EXECUTE THIS RANSOMWARE?' in f.read(): threat = 'Win32/Ransom.NETCrypton.Gen'
  if "Sad Computer" in f.read() and "Are You Sure You want to install Antivirus software?" in f.read(): threat = 'Win32/Ransom.SadComputer.Gen'
  if 'https://paste.ee/r/gk49i/0' in f.read() and "UserClient.DownloadFileTaskAsync" in f.read(): threat = 'Win32/RAT.AsyncRAT.Gen'
  if "Kaspersky Tweaker for KFA2018" in f.read() and "2020202020202020202020202020202020202020302E2082EBE5AE3F0D0A" in f.read(): threat = 'Win32/Trojan.Agent.C'
  if "There's no Epic Games folder!!! Do you even Fortnite, bro?" in f.read() and "Trojan.Win32.Fonite" in f.read() and "by Valzentia" in f.read() and "Epic Games is a disease" in f.read(): threat = 'Win32/Trojan.Fonite.Gen'
  if "Best regards 2 Tommy Salo." in f.read() and "Neshta 1.0 Made in Belarus." in f.read() and "Dziadulja Apanas" in f.read(): threat = 'Win32/Virus.Neshta.Gen'
  if "AV Intelligent Updater" in f.read() and "Please select email address to send at your friend" in f.read() and 'Select email address with ' in f.read(): threat = 'Win32/Worm.Totilix.Gen'
  if "NSSM: The non-sucking service manager" in f.read() and "To show service installation GUI: nssm install" in f.read(): threat = 'Win64/Trojan.NSSManager.Gen'
    
  tk.messagebox.showinfo.destroy()

  if threat == 'Žádná hrozba':
    print('Test byl dokončen.')
    print('Nebyla nalezena žádná hrozba.')

  else:

    print('Test byl dokončen.')
    print('Byly nalezeny hrozby.')
    print()
    print('Hrozba: ' + threat)
    print()
    print('Solver se pokouší problém vyřešit. Vyčkejte prosím.') 
    if 'Win32/Ransom.Petya' in threat:
      print('Solver dokončil práci.')
      print('Dešifrovací klíč: iBD5ohFBbUb3Aa1f')
    else:
      try: os.remove(filename)
