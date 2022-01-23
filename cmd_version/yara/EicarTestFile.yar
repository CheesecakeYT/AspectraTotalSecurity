rule EicarTestFile_A {
    meta:
        description = "EICAR test file string"
        author = "Austin Byers | Airbnb CSIRT"
    strings:
        $s1 = /^X5O!P%@AP\[4\\PZX54\(P\^\)7CC\)7\}\$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!\$H\+H\*\s*$/
    condition:
        all of them
}

rule EicarTestFile_B {
    meta:
        description = "EICAR test file substring"
        author = "Austin Byers | Airbnb CSIRT"
    strings:
        $s2 = "$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!"
    condition:
        all of them
}
