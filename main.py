from commands import commands_dict
from funcs  import *



'''Main'''
def main():
    print("[i] Здравствуйте, я ваш голосовой помощник, чем я могу помочь?")
    while True:
        query = listen_command()
        for key, value in commands_dict['commands'].items():
            if query in value:
                print(globals()[key]())
        if query in commands_dict['commands']['disconnect']:
            break


if __name__ == '__main__':
    main()