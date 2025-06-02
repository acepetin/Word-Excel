def multiplicative_hash(key: str, table_size: int, f: float = 0.6180339887) -> int:
    if not key:
        return 0
    key_sum = 0
    for c in key:
        key_sum += ord(c)
    return int(table_size * ((f * key_sum) % 1))

def shift_hash(s: str, table_size: int) -> int:
    hash_val = 0
    for c in s:
        hash_val = ((hash_val << 5) - hash_val + ord(c)) & 0xFFFFFFFF
    return hash_val % table_size

def bitmask_hash(s: str) -> int:
    result = 0
    for c in s:
        result |= (1 << (ord(c) % 64))
    return result

def simple_md5(s: str) -> int:
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    
    
    byte_data = [0] * (len(s) + 64)  
    for i in range(len(s)):
        byte_data[i] = ord(s[i])
    data_len = len(s)
    
    
    byte_data[data_len] = 0x80
    data_len += 1
    
    
    while (data_len * 8) % 512 != 448:
        byte_data[data_len] = 0x00
        data_len += 1
    
    
    bit_length = len(s) * 8
    for i in range(8):
        byte_data[data_len + i] = (bit_length >> (i * 8)) & 0xFF
    data_len += 8
    
    
    words = [0] * 16
    for i in range(16):
        j = i * 4
        words[i] = (byte_data[j] | (byte_data[j+1] << 8) | 
                   (byte_data[j+2] << 16) | (byte_data[j+3] << 24)) & 0xFFFFFFFF
    
    AA, BB, CC, DD = A, B, C, D
    
    def F(x, y, z): return (x & y) | ((~x) & z)
    def G(x, y, z): return (x & z) | (y & (~z))
    def H(x, y, z): return x ^ y ^ z
    def I(x, y, z): return y ^ (x | (~z))
    
   
    T = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
         0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
         0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
         0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821]
    
    for i in range(16):
        if i < 4:
            func = F(B, C, D)
            k = i
            s = [7, 12, 17, 22][i % 4]
        elif i < 8:
            func = G(B, C, D)
            k = (5*i + 1) % 16
            s = [5, 9, 14, 20][i % 4]
        elif i < 12:
            func = H(B, C, D)
            k = (3*i + 5) % 16
            s = [4, 11, 16, 23][i % 4]
        else:
            func = I(B, C, D)
            k = (7*i) % 16
            s = [6, 10, 15, 21][i % 4]
        
        temp = (A + func + words[k] + T[i]) & 0xFFFFFFFF
        temp = ((temp << s) | (temp >> (32 - s))) & 0xFFFFFFFF
        A, B, C, D = D, (B + temp) & 0xFFFFFFFF, B, C
    
    A = (A + AA) & 0xFFFFFFFF
    B = (B + BB) & 0xFFFFFFFF
    C = (C + CC) & 0xFFFFFFFF
    D = (D + DD) & 0xFFFFFFFF
    
    return A


input_file = open('sets.txt', 'r')
lines = input_file.readlines()
input_file.close()


test_strings = []
for line in lines:
    stripped_line = line.strip()
    if stripped_line:
        test_strings.append(stripped_line)


output_file = open('output.txt', 'w')
output_file.write("Строка\t\tMultiplicative\tShift\tBitmask\tSimple MD5\n")
output_file.write("="*60 + "\n")

for s in test_strings:
    mult = multiplicative_hash(s, 1000)
    shft = shift_hash(s, 1000)
    bmask = bitmask_hash(s)
    md5 = simple_md5(s)
    
    output_line = f"{s[:16]:<16}\t{mult:<12}\t{shft:<6}\t{bmask:<8}\t{hex(md5)}\n"
    output_file.write(output_line)

output_file.close()