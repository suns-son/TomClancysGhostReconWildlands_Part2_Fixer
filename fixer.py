from os.path import abspath, exists, join
from time import sleep
from hashlib import sha256

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")
    return join(base_path, relative_path)

def checker (file_name):
    print('\nDosya inceleniyor, lutfen bekleyin...\n')
    sha256_hash = sha256()
    with open(file_name, 'rb') as file:
        for byte_block in iter(lambda: file.read(4096), b''):
            sha256_hash.update(byte_block)
    if sha256_hash.hexdigest() == '43a295e669234bd1009c7cc26b79c37369db87c98ea48a5da8aa690952f728ca':
        print('Dosya duzeltilebilir. Duzeltme islemi baslatiliyor, lutfen bekleyin...\n')
        fixer()
        terminator()
    else:
        print('Baska bir dosya girdiniz veya dosya duzeltilemez durumda.\n')
        terminator()

def fixer():
    with open(file_name, 'rb+') as file:
        with open(resource_path('data.bin'), 'rb') as data:
            file.seek(312147644)
            for byte_block in iter(lambda: data.read(4096), b''):
                file.write(byte_block)
    print('Dosya duzeltme islemi basariyla tamamlandi.\n')


def terminator():
    remaining_time = 5
    while remaining_time > 0:
        print(f'Program {remaining_time} saniye içinde kapanacaktir.', end = '\r')
        sleep(1)
        remaining_time -= 1

print('Bu program Tom Clancys Ghost Recon Wildlands oyunu icin indirmis oldugunuz \
dort parttan ikincisindeki hatali veriyi duzeltmeyi amaclar.\n')
print('Lutfen bu exe dosyasinin duzeltmek istediginiz part2 dosyasiyla \
ayni klasorde yer aldigindan emin olun.\n')
print('Lutfen duzeltmek istediginiz part2 dosyasinin tam adini girin (ornegin TCGRW-part2.rar).\n')

part2 = input(':    ')
part2rar = part2 + '.rar'

while not (exists(part2) or exists(part2rar)):
    print('\nGirdiginiz ada sahip bir dosya bulunamadi. Lutfen dosya adini tekrar giriniz.\n')
    part2 = input(':    ')
    part2rar = part2 + '.rar'

if exists(part2): file_name = part2
else: file_name = part2rar

checker(file_name)
