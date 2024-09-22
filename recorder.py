import pickle
from pynput import mouse

clicks = []

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Click captured at ({x}, {y})")
        clicks.append((x, y))

def record_clicks(filename="clicks.pkl"):
    print("Recording clicks. Press 'Ctrl+C' to stop.")

    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join() 
        except KeyboardInterrupt:
            pass  
    
    if clicks:
        with open(filename, 'wb') as f:
            pickle.dump(clicks, f)
        print(f"Clicks saved to {filename}")
    else:
        print("No clicks were recorded.")

if __name__ == "__main__":
    record_clicks()

