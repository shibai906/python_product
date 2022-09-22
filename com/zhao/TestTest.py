import os

fileName = '/Users/zhaohuan/.ssh/'


def main():
    for i, j, k in os.walk(fileName):
        for g in k:
            filePath = os.path.join(i, g)
            print(filePath)


if __name__ == '__main__':
    main()
