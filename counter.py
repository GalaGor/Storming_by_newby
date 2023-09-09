from time import sleep
t = 0
while True:
    t = t + 1
    hh = t // 3600
    mm = t % 3600 // 60
    ss = t % 60
    h1 = hh // 10
    h2 = hh % 10
    m1 = mm // 10
    m2 = mm % 10
    s1 = ss // 10
    s2 = ss % 10
    print(h1, h2, ':', m1, m2, ':', s1, s2, sep="")
    sleep(1)
