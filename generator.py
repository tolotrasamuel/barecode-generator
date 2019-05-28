import barcode
from barcode.writer import ImageWriter
optionsSvg = {
    'module_height': 10,
    # 'quiet_zone': 10,
    'font_size':8,
    'text_distance': 3
}
optionsPng = {
    'module_height': 10,
    # 'quiet_zone': 10,
    'font_size':15,
    'text_distance': 1
}

imgWriter = ImageWriter()

options = optionsPng
# options = optionsSvg
# imgWriter = None #using with svg

imgWriter.set_options(options)
EAN = barcode.get('code128', options=options,)

def run(saveDir, text):
        print(text)
        ean = EAN(text,writer=imgWriter)
        fullname = ean.save(saveDir + text, options=options)
def main():
    filename = 'input.txt'
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            run('./output/', line)
def test():
    line = '23800143401321'
    fullname = run('./output-test/',line,)


main()
# test()