class color:
    BOLD = '\033[1m'
    END = '\033[0m'


class err:
    C404 = 'Arrey Balreddy, ee location lo file ledu kadara!'
    C405 = 'file extension' + color.BOLD + ' simha ' + \
        color.END + 'ani undaali ra bloody fool'
    C101 = 'em ra Telugu matladadam marchipoyav enti ee incorrect character'

    def info(line):
        return f'ee line lo thappu undi ra Balaraju: \n--->\n{line}'


HELP = 'Sahaayam koraku:' + color.BOLD + \
    ' -help / help ' + color.END + 'vaadandi\n'
AUTHORS = 'Rachayitala vivarala koraku:' + color.BOLD + \
    ' -credits / credits ' + color.END + 'vaadandi\n'
DOCS = 'Poorti documentation vivaraala koraku:' + \
    color.BOLD + ' -docs / docs ' + color.END + 'vaadandi\n'


def showHelp():
    print(f'Vaadakam: \n {AUTHORS} {DOCS} {HELP}')


class Thappulu(Exception):
    def __init__(self, message, info=''):
        super().__init__(message)
        self.message = message
        self.info = info

    def __str__(self):
        return (self.info + '\n [THAPPU CHESTUNNAVU!!]: %s' % self.message)
