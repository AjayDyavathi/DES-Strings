# DES ENCRYPTION OF STRINGS FROM SCRATCH
import argparse


def hexToBin(h):
    return ''.join(['{:04b}'.format(int(i, 16)) for i in h])


def binToHex(b):
    return ''.join(['{:x}'.format(int(b[i:i + 4], 2)) for i in range(0, len(b), 4)])


def binToInt(b):
    return int(b, 2)


def intToBin(i):
    return bin(i)


def binToStr(b):
    return ''.join(chr(int(b[i:i + 8], 2)) for i in range(0, len(b), 8))


def strToBin(s):
    return ''.join(['{:08b}'.format(ord(i)) for i in s])


def bit_xor(a, b):
    return ''.join([str(int(i) ^ int(j)) for i, j in zip(a, b)])


def initial_permutation(block):
    result = [''] * len(block)
    ref = [58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6,
           64, 56, 48, 40, 32, 24, 16, 8,
           57, 49, 41, 33, 25, 17, 9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7, ]
    for en, i in enumerate(ref):
        result[en] = block[i - 1]
    result = ''.join(result)
    # print('Initial permutation', result)
    return result


def inverse_initial_permutation(block):
    result = [''] * len(block)
    ref = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25, ]
    for en, i in enumerate(ref):
        result[en] = block[i - 1]
    result = ''.join(result)
    # result = binToStr(''.join(result))
    return result


def PC2(C, D):
    CD = C + D
    ref = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32, ]
    res = [''] * len(ref)
    for en, i in enumerate(ref):
        res[en] = CD[i - 1]
    return ''.join(res)


def PC1(key):
    ref = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    res = [''] * len(ref)
    for en, i in enumerate(ref):
        res[en] = key[i - 1]
    key_np = ''.join(res)
    return key_np


def key_schedule(key):
    if len(key) < 8:
        key += ' ' * (8 - len(key))
    key = strToBin(key)
    key = key[:64]

    key_np = PC1(key)

    keys = []

    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    C = key_np[:len(key_np) // 2]
    D = key_np[len(key_np) // 2:]

    for each in shifts:
        head_c = C[:each]
        head_d = D[:each]

        C = C[each:] + head_c
        D = D[each:] + head_d

        keys.append(PC2(C, D))

    return keys


def expansion(block):
    ref = [32, 1, 2, 3, 4, 5,
           4, 5, 6, 7, 8, 9,
           8, 9, 10, 11, 12, 13,
           12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25,
           24, 25, 26, 27, 28, 29,
           28, 29, 30, 31, 32, 1, ]
    res = [''] * len(ref)
    for en, i in enumerate(ref):
        res[en] = block[i - 1]
    result = ''.join(res)
    # print('Expanded', result, len(result))
    return result


def substitution_blocks(block):
    blocks = [block[i:i + 6] for i in range(0, len(block), 6)]

    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, ],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, ],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, ],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13, ], ]

    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, ],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, ],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, ],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9, ], ]

    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, ],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, ],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, ],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12, ], ]

    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, ],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, ],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, ],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14, ], ]

    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, ],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, ],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, ],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3, ], ]

    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, ],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, ],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, ],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13, ], ]

    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, ],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, ],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, ],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12, ], ]

    S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, ],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, ],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, ],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11, ], ]

    S = [S1, S2, S3, S4, S5, S6, S7, S8]

    result = []

    for blk, each in enumerate(blocks):
        row = int(each[0] + each[-1], 2)
        col = int(each[1:-1], 2)

        sub_block = S[blk]
        value = sub_block[row][col]
        result.append('{:04b}'.format(value))

    return ''.join(result)


def sub_permutation(block):
    ref = [16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25, ]

    res = [''] * len(ref)
    for en, i in enumerate(ref):
        res[en] = block[i - 1]
    return ''.join(res)


def transform(block, key):
    # EXPANSION
    expanded_block = expansion(block)

    # XOR WITH KEY
    xored_block = bit_xor(expanded_block, key)

    # S - BLOCKS
    subtd_block = substitution_blocks(xored_block)

    # PREMUTATION
    final_block = sub_permutation(subtd_block)

    return final_block


def encrypt_des(message, key):
    cipher = ''
    # print('MESSAGE:', message)

    message = strToBin(message)

    message = [message[i:i + blocksize] for i in range(0, len(message), blocksize)]

    if len(message[-1]) < blocksize:
        message[-1] += '{:08b}'.format(ord(' ')) * ((blocksize - len(message[-1])) // 8)

    keys = key_schedule(key)

    for block in message:
        # print(block)
        bin_block = initial_permutation(block)

        L = [''] * (rounds + 1)
        R = [''] * (rounds + 1)

        L[0] = bin_block[:len(bin_block) // 2]
        R[0] = bin_block[len(bin_block) // 2:]

        for i in range(1, rounds + 1):
            key = keys[i - 1]

            L[i] = R[i - 1]
            R[i] = bit_xor(L[i - 1], transform(R[i - 1], key))

        ciph_blk = R[-1] + L[-1]
        ciph_blk = inverse_initial_permutation(ciph_blk)

        cipher += ciph_blk
    return binToHex(cipher)


def decrypt_des(message, key):
    plain = ''

    message = hexToBin(message)
    message = [message[i:i + blocksize] for i in range(0, len(message), blocksize)]

    if len(message[-1]) < blocksize:
        message[-1] += '{:08b}'.format(ord(' ')) * ((blocksize - len(message[-1])) // 8)
    # print(message)

    keys = key_schedule(key)[::-1]

    for block in message:

        bin_block = initial_permutation(block)

        L = [''] * (rounds + 1)
        R = [''] * (rounds + 1)

        L[0] = bin_block[:len(bin_block) // 2]
        R[0] = bin_block[len(bin_block) // 2:]

        for i in range(1, rounds + 1):
            key = keys[i - 1]
            L[i] = R[i - 1]
            R[i] = bit_xor(L[i - 1], transform(R[i - 1], key))

        plain_blk = R[-1] + L[-1]
        plain_blk = inverse_initial_permutation(plain_blk)

        plain += plain_blk
    return binToStr(plain)


rounds = 16
blocksize = 8 * 8

parser = argparse.ArgumentParser(description='Encrypts/Decrypts DES and 3DES strings')
parser.add_argument('-m', '--mode', choices=['enc', 'dec'], help='Encryption(enc) or Decryption(dec)', required=True)
parser.add_argument('-a', '--algorithm', choices=['des', '3des'], help='DES or 3DES', default='DES')
parser.add_argument('-k1', '--key1', help='Key1', required=True)
parser.add_argument('-k2', '--key2', help='Key2 only for 3DES')
parser.add_argument('-s', '--string', help='String', required=True)

args = parser.parse_args()

if args.mode == 'enc':
    if args.algorithm == 'des':
        print('Hex Digest:', encrypt_des(args.string, args.key1))
    elif args.algorithm == '3des':
        print('Hex Digest:', encrypt_des(decrypt_des(encrypt_des(args.string, args.key1), args.key2), args.key1))
    else:
        print('Invalid choice')

elif args.mode == 'dec':
    if args.algorithm == 'des':
        print('Hex Digest:', decrypt_des(args.string, args.key1))
    elif args.algorithm == '3des':
        print('Hex Digest:', decrypt_des(encrypt_des(decrypt_des(args.string, args.key1), args.key2), args.key1))
    else:
        print('Invalid choice')
else:
    print('Invalid choice')
