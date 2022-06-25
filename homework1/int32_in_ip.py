def int32_to_ip(int32):
    '''
    Convert int32 -> string IP
    :param int32: integer 32 bit
    :return: string in format IP address
    '''
    binary_str = f'{int32:b}'.rjust(32, '0')
    data = ''
    for i in range(0, len(binary_str), 8):
        data = data + str(int(binary_str[i:i + 8], 2))+'.'
    data = data[:-1]
    return data


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
