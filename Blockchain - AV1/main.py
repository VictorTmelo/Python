from hash import Blockchain

if __name__ == '__main__':
    bc = Blockchain()

    bc.add_new_block('Bloco A')
    bc.add_new_block('Bloco B')
    bc.add_new_block('Bloco C')

    for i in bc.get_all_hashes():
        print(i)
