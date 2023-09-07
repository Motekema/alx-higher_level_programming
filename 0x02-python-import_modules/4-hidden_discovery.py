#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name1 in names:
        if name1[:2] != "__":
            print(name1)
