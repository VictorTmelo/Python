from hash import Hash

if __name__ == '__main__':
    hash = Hash()

    hash.add_new_block('Bloco 2')
    hash.add_new_block('Bloco 3')
    hash.add_new_block('Bloco 4')

    print(hash.get_all())