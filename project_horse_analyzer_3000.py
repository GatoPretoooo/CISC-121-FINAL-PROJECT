import keyboard
import pyperclip
import time
import re
import gradio as gr

#Global data
horses = []
horse_id_counter = 1

#check if entity is a horse
def extract_entity_type(data: str):
    if "minecraft:horse" in data:
        return "horse"
    else:
        keyboard.press('t')   #displays on the chat if it is a horse
        time.sleep(0.05)
        keyboard.write("Not a horse")
        keyboard.press_and_release('enter')
        return None

#extract the speed value from the text
def extract_speed(data: str):
    match = re.search(r'movement_speed.*?base: ([0-9.]+)', data)
    if match:
        return float(match.group(1))
    return None

#extract the jump value from the text
def extract_jump(data: str):
    match = re.search(r'jump_strength.*?base: ([0-9.]+)', data)
    if match:
        return float(match.group(1))
    return None

#extract the health value from the text
def extract_health(data: str):
    match = re.search(r'Health: ([0-9.]+)', data)
    if match:
        return float(match.group(1))
    return None

#Prevents the user to add duplicate horse values
def is_duplicate(new_horse):
    for h in horses:
        if (
            h["speed"] == new_horse["speed"] and
            h["jump"] == new_horse["jump"] and
            h["health"] == new_horse["health"]
        ):
            return True
    return False


def collect_horse():
    global horse_id_counter

    keyboard.press_and_release('f3+i')  #command to get the the values from the entities 
    time.sleep(0.5)

    clipboard_content = pyperclip.paste()
    
    if extract_entity_type(clipboard_content) is None:
        return
    
    speed = extract_speed(clipboard_content)
    jump = extract_jump(clipboard_content)
    health = extract_health(clipboard_content)


    if speed is not None and jump is not None and health is not None:

        new_horse = {
            "speed": speed,
            "jump": jump,
            "health": health
        }

        if is_duplicate(new_horse):
            keyboard.press('t')  #shows on chat that user pressed "k" twice on the same entity
            time.sleep(0.05)
            keyboard.write("Duplicate horse ignored.")
            keyboard.press_and_release('enter')
            return

        horse = {
            "id": horse_id_counter,
            **new_horse
        }

        horses.append(horse)

        print(f"Horse #{horse_id_counter} added: {horse}")

        horse_id_counter += 1

    else:
        keyboard.press('t')
        time.sleep(0.05)
        keyboard.write("Could not extract all values.")
        keyboard.press_and_release('enter')

# Key bind to collect the info
keyboard.add_hotkey('k', collect_horse)

#sorting algorithm
def bubble_sort_horses(horses_list, key):
    bah = horses_list.copy()
    n = len(bah)

    for i in range(n):
        for j in range(0, n - i - 1):
            if bah[j][key] > bah[j + 1][key]:
                bah[j], bah[j + 1] = bah[j + 1], bah[j]

    return bah

#analyzing the horses...
def analyze_horses(sort_key):
    if len(horses) == 0:
        return "No horses collected yet. Press 'K' in Minecraft."

    sorted_list = bubble_sort_horses(horses, sort_key)
    best = sorted_list[-1]

    result = "Sorted Horses:\n\n"

    for h in sorted_list:
        result += f"Horse #{h['id']} → Speed: {float(h['speed']):.4f}, Jump: {float(h['jump']):.4f}, Health: {float(h['health']):.2f}\n"

    result += f"\nBest Horse: #{best['id']}"

    return result

#Clears all values used 
def clear_horses():
    global horses, horse_id_counter
    horses = []
    horse_id_counter = 1
    return "All horses cleared."

#UI
with gr.Blocks() as interface:
    gr.Markdown("# Horse Analyzer 3000")

    dropdown = gr.Dropdown(["speed", "jump", "health"], label="Sort by")
    output = gr.Textbox()

    analyze_button = gr.Button("Analyze Horses")
    clear_button = gr.Button("Clear Horses")

    analyze_button.click(analyze_horses, inputs=dropdown, outputs=output)
    clear_button.click(clear_horses, outputs=output)

#Run app
interface.launch(share=True)