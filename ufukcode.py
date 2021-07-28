from argparse import ArgumentParser


def forward(code: str):
    letters = [letter.replace('A', '1') for letter in code.split()]
    letters = [letter.replace('.', '0') for letter in letters]
    letters = [chr(ord('@')+int(letter, 2)) for letter in letters]
    sentence = ' '.join(letters)
    return sentence


def reversed(code: str):
    letters = [ord(letter) - 96 for letter in code.lower().replace(' ', '')]
    letters = [format(letter, '05b') for letter in letters]
    letters = [letter.replace('1', 'A') for letter in letters]
    letters = [letter.replace('0', '.') for letter in letters]
    sentence = ' '.join(letters)
    return sentence


def main(code: str, reverse: bool = False):
    if not reverse:
        return forward(code)
    return reversed(code)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("code",
                        help="The string of text (code or alphabetical text"
                        ", which can include spaces) that you want to en- or"
                        " decode",
                        nargs="+",
                        type=str)
    parser.add_argument("--reverse",
                        help="Set this flag to convert text into code",
                        action="store_true")
    args = parser.parse_args()
    args.code = ' '.join(args.code)
    if args.reverse:
        print(main(args.code, reverse=True))
    else:
        print(main(args.code))
