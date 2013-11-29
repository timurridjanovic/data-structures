import math
import re
import hashlib #for testing only

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.append(i)
    return i

def generate_primes(n):
    primes = []
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1

sixty_four_primes = generate_primes(64)
eight_primes = generate_primes(8)
hashes = {'h0': 0, 'h1': 0, 'h2': 0, 'h3': 0, 'h4': 0, 'h5': 0, 'h6': 0, 'h7': 0}
round_constants = []

def initialize_hash_values(eight_primes, hashes):
	for i, prime in enumerate(eight_primes):
		# first 32 bits of the fractional parts of the square roots of the first 8 primes
		hashes['h' + str(i)] = int(math.modf(math.sqrt(prime))[0]*(1<<32))
	return hashes	


def initialize_round_constants(sixty_four_primes):
	for prime in sixty_four_primes:
		round_constants.append(hex(int(math.modf(prime**(1.0/3.0))[0]*(1<<32))))
	return round_constants

def ch(x, y, z):
        return ((x & y) ^ (~x & z))

def maj(x, y, z):
        return ((x & y) ^ (x & z) ^ (y & z))

def rotr(n, x):
	return ((x >> n) | (x << (32 - n)) & 0xffffffff)

def sigma0(x):
        return rotr(2, x)  ^ rotr(13, x) ^ rotr(22, x)

def sigma1(x):
        return rotr(6, x) ^ rotr(11, x) ^ rotr(25, x)

def gamma0(x):
	return rotr(7, x) ^ rotr(18, x) ^ ((x & 0xffffffff) >> 3)

def gamma1(x):
	return rotr(17, x) ^ rotr(19, x) ^ ((x & 0xffffffff) >> 10)

def sha_256(message):
	initialize_hash_values(eight_primes, hashes)
	initialize_round_constants(sixty_four_primes)
	bin_block = []

	#append binary representation of each character into bin_block
	for char in message:
		bin_block.append(bin(ord(char)).replace('b', '').zfill(8))
	
	#append 1 to bin_block
	bin_block.append('1')
	message_length_in_bits = len(message) * 8
	zeros_to_append = 448 - ((message_length_in_bits + 1) % 512)
	
	#append n zeros so that message length + 1 % 512 = 448
	bin_block.append(zeros_to_append * '0')
	
	#append 64 bit representation of message length
	bin_block.append(bin(message_length_in_bits).replace('b', '').zfill(64))
	binary_message = ''.join(bin_block)

	#break message into 512-bit chunks
	binary_message_chunks = re.findall('.{%s}' % 512, binary_message)
	
	for chunk in binary_message_chunks:
		
		hex_message = hex(int(chunk, 2))
		hex_chunks = re.findall('........', hex_message[2:])	
		hex_to_int = []
		for i in range(len(hex_chunks)):
			hex_to_int.append(int(hex_chunks[i], 16))


		for i in range(16, 64):
			g0 =  gamma0(hex_to_int[i-15])

			g1 = gamma1(hex_to_int[i-2])

			hex_to_int.append((hex_to_int[i-16] + g0 + hex_to_int[i-7] + g1) & 0xffffffff)

		a = hashes['h0'] & 0xffffffff
		b = hashes['h1'] & 0xffffffff
		c = hashes['h2'] & 0xffffffff
		d = hashes['h3'] & 0xffffffff
		e = hashes['h4'] & 0xffffffff
		f = hashes['h5'] & 0xffffffff
		g = hashes['h6'] & 0xffffffff
		h = hashes['h7'] & 0xffffffff
		

		for i in range(0, 64):
			_s1 = sigma1(e)
			_ch = ch(e, f, g)
			_temp1 = (h + _s1 + _ch + int(round_constants[i], 16) + hex_to_int[i]) & 0xffffffff		
			_s0 = sigma0(a)
			_maj = maj(a, b, c)
			_temp2 = (_s0 + _maj) & 0xffffffff

			h = g
			g = f
			f = e
			e = (d + _temp1) & 0xffffffff
			d = c
			c = b
			b = a
			a = (_temp1 + _temp2) & 0xffffffff

		hashes['h0'] = (hashes['h0'] + a) & 0xffffffff
		hashes['h1'] = (hashes['h1'] + b) & 0xffffffff
		hashes['h2'] = (hashes['h2'] + c) & 0xffffffff
		hashes['h3'] = (hashes['h3'] + d) & 0xffffffff
		hashes['h4'] = (hashes['h4'] + e) & 0xffffffff
		hashes['h5'] = (hashes['h5'] + f) & 0xffffffff
		hashes['h6'] = (hashes['h6'] + g) & 0xffffffff
		hashes['h7'] = (hashes['h7'] + h) & 0xffffffff

	digest = ''.join([hex(hashes['h' + str(i)])[2:].zfill(8) for i in range(len(hashes))])

	return digest

	
		

		
