# DES
Data Encryption Standard from scratch in python3

This is a Data Encryption Standard implementation in python3 from scratch,
No imports of any modules except argparse to execute it from terminal

This DES operates in EBC (Electronic Code Book) mode, I will try to add CBC, CFB and other modes of operation.
Do not use this program to encrypt any confidential details. This is developed by me to understand the concepts and actual implementation of DES.

DATA ENCRYPTION STANDARD is a symmetric encryption algorithm developed by IBM with the inputs from NSA in 1970.
It has the Feistal Network approach, 
64 bit key length - (56 bits functional)
Any greater length keys are truncated to 64 bits

DES is easily vulnerable to today's computational power.
So, TRIPLE DES and AES are advised for actual encryption of data.

TRIPLE DES provides greater key length 112 bits in this model.

USAGE:

ENCRYPTION
``` python3 des.py --mode enc --algorithm des --key1 ***** --string 'Encrypt this text'
                              OR
    python3 des.py -m enc -a des -k1 ***** -s 'Encrypt this text'
    ------------------------------------------------------------------------------------------------
    python3 des.py --mode enc --algorithm 3des --key1 ***** --key2 ***** --string 'Encrypt this text'
                              OR
    python3 des.py -m enc -a 3des -k1 ***** -k2 ***** -s 'Encrypt this text'
```

DECRYPTION
``` python3 des.py --mode dec --algorithm des --key1 ***** --string 'Decrypt this text'
                              OR
    python3 des.py -m dec -a des -k1 ***** -s 'Decrypt this text'
    ------------------------------------------------------------------------------------------------
    python3 des.py --mode dec --algorithm 3des --key1 ***** --key2 ***** --string 'Decrypt this text'
                              OR
    python3 des.py -m dec -a 3des -k1 ***** -k2 ***** -s 'Decrypt this text'
```
   
