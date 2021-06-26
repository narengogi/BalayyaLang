class color:
    BOLD = '\033[1m'
    END = '\033[0m'


class errors:
    C404 = 'Arrey Balreddy, ee location lo file ledu kadara!'
    C405 = 'file extension' + color.BOLD + ' simha ' + \
        color.END + 'ani undaali ra bloody fool'


HELP = 'Sahaayam koraku:' + color.BOLD + \
    ' -help / help ' + color.END + 'vaadandi\n'
AUTHORS = 'Rachayitala vivarala koraku:' + color.BOLD + \
    ' -credits / credits ' + color.END + 'vaadandi\n'
DOCS = 'Poorti documentation vivaraala koraku:' + \
    color.BOLD + ' -docs / docs ' + color.END + 'vaadandi\n'


def showHelp():
    print(f'Vaadakam: \n {AUTHORS} {DOCS} {HELP}')


class Thappulu(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = args

    def __str__(self):
        return ('\n [THAPPU CHESTUNNAVU!!]: %s' % self.message)
