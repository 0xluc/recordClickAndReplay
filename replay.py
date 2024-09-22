import pyautogui
import pickle
import numpy as np
import time

def load_and_replay_clicks(filename="clicks.pkl", min_delay=0.5, max_delay=1.0):
    with open(filename, 'rb') as f:
        clicks = pickle.load(f)

    print(f"Replaying {len(clicks)} clicks")

    for x, y in clicks:
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        delay = np.random.uniform(min_delay, max_delay)
        time.sleep(delay)

if __name__ == "__main__":
    load_and_replay_clicks()

