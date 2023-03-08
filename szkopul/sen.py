DOBA = 24 * 60


def time_to_int(time: str):
    hours, minutes = time.split(sep=":")
    hours = int(hours)
    minutes = int(minutes)
    minutes += hours * 60
    return minutes


def int_to_time(tm: int):
    minutes = tm % 60
    hours = (tm - minutes) / 60

    minutes = int(minutes)
    hours = int(hours)

    if minutes < 10:
        minutes = f'0{minutes}'
    if hours < 10:
        hours = f'0{hours}'

    return f'{hours}:{minutes}'


def main():
    cur_time = input()
    sleep_time = input()

    cur_time = time_to_int(cur_time)
    sleep_time = time_to_int(sleep_time)

    prop_time = cur_time - sleep_time

    top = None
    if prop_time >= 0:
        top = int_to_time(prop_time)
    else:
        top = int_to_time(DOBA + prop_time)
    print(top)


main()



