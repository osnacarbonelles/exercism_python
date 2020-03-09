def recite(start, take=1):
    song = []
    for n in range(0, take):
        for line in verse(start-n):
            song.append(line)
        if n != take-1:
            song.append("")
    return song

def verse(num):
    if num == 0:
        return ("No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.")
    elif num == 1:
        return ("1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.")
    elif num > 2:
        return (str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer.",
            "Take one down and pass it around, " + str(num-1) + " bottles of beer on the wall.")
    elif num == 2:
        return (str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer.",
            "Take one down and pass it around, " + str(num-1) + " bottle of beer on the wall.")
