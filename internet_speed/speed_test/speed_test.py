import speedtest


def get_speed(threads=1):
    s = speedtest.Speedtest()

    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    return s.results.dict()
