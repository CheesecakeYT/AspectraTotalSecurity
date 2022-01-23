rule Win32/Trojan/Winnti/A {
   meta:
      description = "Winnti signature mentioned by Cylance"
      license = "Detection Rule License 1.1 https://github.com/Neo23x0/signature-base/blob/master/LICENSE"
      author = "Florian Roth"
      hash1 = "7c32885c258a6d5be37ebe83643f00165da3ebf963471503909781540204752e"
   strings:
      $s1 = "WOODTALE TECHNOLOGY INC" ascii
   condition:
      ( uint16(0) == 0x5a4d and filesize < 3000KB and 1 of them )
}
