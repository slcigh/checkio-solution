def checkio(time_string):
    dict2 = {0: ".. ", 1: ".- ", 2: "-. "}
    dict3 = {0: " ... ", 1: " ..- ", 2: " .-. ", 3: " .-- ", 4: " -.. ", 5: " -.- "}
    dict4 = {0: ".... ", 1: "...- ", 2: "..-. ", 3: "..-- ", 4: ".-.. ", 5: ".-.- ", 6: ".--. ", 7: ".--- ", 8: "-... ",
             9: "-..- "}

    h, m, s = map(lambda x: x.zfill(2), time_string.split(":"))

    return (dict2[int(h[0])] + dict4[int(h[1])] + ":" + dict3[int(m[0])] +
            dict4[int(m[1])] + ":" + dict3[int(s[0])] + dict4[int(s[1])]).strip()
