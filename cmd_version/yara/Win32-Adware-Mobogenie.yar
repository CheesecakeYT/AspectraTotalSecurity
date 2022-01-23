rule Win32-Adware-Mobogenie-A {
   meta:
      description = "Mobogenie signature mentioned by Cylance"
      license = "Detection Rule License 1.1 https://github.com/Neo23x0/signature-base/blob/master/LICENSE"
      author = "Florian Roth"
   strings:
      $s1 = "AmazGame Age Internet Technology Co., Ltd" ascii
   condition:
      ( uint16(0) == 0x5a4d and filesize < 3000KB and 1 of them )
}
