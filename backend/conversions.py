# for all conversions


def abs():
    print("not supposed to see this")


def meters_to_miles(meters):
    miles_const = .0006214
    miles = round((meters * miles_const), 1)
    return miles


def seconds_to_hours(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


if __name__ == '__main__':
    abs()

