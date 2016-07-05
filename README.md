# fightingGameInputs-tti

Text-to-image for fightning game inputs.

# Requirements:
* Python 2.7
* pygame

# How to use
python inputs-tti.py "string"

# How to compose the input string
Recognized commands:
* P, LP, MP, HP, 3P
* K, LK, MK, HK, 3K
* DB, D, DF, B, F, FF, UB, U, UF
* QCF, QFB
* HCF, HCB
* SPD
* DP, RDP
* and (== '+')

# Example strings and outputs
SF5 Ken advanced combo : "DMPBMPHPQCBMKQCFQCF3K"

Output: http://i.imgur.com/pTm2UMR.png

SF4 Viper bnb : "HPQCBHP3PDHPDP3PDUFQCBLKQCFQCF3P"

Output: http://i.imgur.com/ryiTiiH.png (incorrect, performs up then forward instead of up-forward)

SF4 Ryu solar plexus uppercut FADC to victory : "FFFHPDMPDHPDPHPMPandMKQCFQCF3P"

Output: http://i.imgur.com/x0los6T.png
