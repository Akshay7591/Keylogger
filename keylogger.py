import pynput.keyboard

def on_press(key):
    print(f"Key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")


listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()

listener.join()
