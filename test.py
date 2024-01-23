url = '/en/products/2/?page=12'

lang_code = input('Code: ')

parts = url.split('/en/')
url = f'/{lang_code}/{parts[1]}'

print('Updated URL:', url)
