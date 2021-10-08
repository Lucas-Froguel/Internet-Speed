import speedtest


def get_speed(threads=1):
    s = speedtest.Speedtest()

    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()
    speed = s.results.dict()
    speed["download"] = speed["download"] / 10 ** 6
    speed["upload"] = speed["upload"] / 10 ** 6

    return speed
