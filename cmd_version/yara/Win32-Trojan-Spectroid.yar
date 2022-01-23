rule Win32-Trojan-Spectroid-A {
   meta:
      description = "Unknown malware mentioned by Cylance"
      license = "Detection Rule License 1.1 https://github.com/Neo23x0/signature-base/blob/master/LICENSE"
      author = "Florian Roth"
   strings:
      $s1 = "Flyingbird Technology Limited" ascii
      $s2 = "Neoact Co., Ltd." ascii
      $s3 = "EMG Technology Limited" ascii
      $s4 = "Zemi Interactive Co., Ltd" ascii
      $s5 = "337 Technology Limited" ascii
      $s6 = "Runewaker Entertainment0" fullword ascii
   condition:
      ( uint16(0) == 0x5a4d and filesize < 3000KB and 1 of them )
}
