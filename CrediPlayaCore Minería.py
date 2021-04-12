from hashlib import sha256

MAX_NONCE = 100000000000
def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previos_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previos_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Felicitaciones, ¡Has minado tu crypto CrediPlaya exitosamente con valor NúmCero:{nonce}")
            return new_hash

    raise BaseException(f"No pudimos encontrar el correcto hash hasta probar con el NúmCero {MAX_NONCE} veces")

if __name__=='__main__':
    transactions='''
    Felipe -> Andres -> 20,
    Rooftop -> Underground ->4
    '''
    dificultad = 5
    import time
    start = time.time()
    print("Iniciar Minando CrediPlaya")
    new_hash = mine(5,transactions,'000000b74f3d7b5618622abb5158cccf1586b91f1fcda1d466b025119efc3693',dificultad)
    total_time = str((time.time() - start))
    print(f"Finalizar Minería. Se tardó en minar en total: {total_time} segundos " )
    print(new_hash)
