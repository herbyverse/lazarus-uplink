## uplink_core_v1.py
## Lazarus Uplink - Prototype Game Loop

# --- Importing Essentials ---
import time
import random

# --- Fragment States ---
fragments = {"Watchful One": {"energy": 70, "corrutpion": 10}, "Performer": {"energy": 60, "corruption": 20}, "Hearthkeeper": {"energy": 80, "corrutpion": 5}}

## --- Game Intro ---
def intro():
    print("===Welcome to Lazarus Uplink ===")
    print("You are the Keeper. Your task: Maintain fragment stability.")
    print("Monitor energy, reduce corruption, and respond wisely.")
    time.sleep(2)

# --- Fragment Status Report ---
def status_report():
    print(f"\n--- Fragment Status ---")
    for name, stats in fragments.items():
        print(f"{name}: Energy {stats['energy']} | Corruption {stats['corruption']}")
    print("----------------------")

# --- Simple Action Menu ---
def keeper_action():
    print("\nChoose an action.")
    print("1. Calm a fragment.")
    print("2. Stimulate a fragment.")
    print("3. Rest a fragment.")
    choice = input(">> ")

    if choice == "1":
        calm_fragment()
    elif choice == "2":
        stimulate_fragment()
    elif choice == "3":
        rest_all()
    else:
        print("Invalid input.")

# --- Actions ---
def calm_fragment():
    target = input("Which fragnent do you want to calm?").title
    if target in fragments:
        fragments[target]["corruption"] = max(0, fragments["corruption"] - 10)
        print("f{target} has been calmed. Corruption reduced.")
    else:
        print("Fragment not found.")

def stimulate_fragment():
    target = input("Which fragment do you want to stimulate?").title()
    if target in fragments:
        fragments[target]["energy"] = min(100, fragments[target]["energy"] + 10)
        print(f"{target} has been stimulated. Energy increased.")
    else:
        print("Fragment not found.")

def rest_all():
    for name in fragments:
        fragments[name]["energy"] = min(100, fragments[name]["energy"] +5)
        fragments[name]["corruption"] = max(0, fragments[name]["corruption"] - 5)
    print("All fragments have rested slightly.")

# --- Game Loop ---
def game_loop():
    intro()
    while True:
        status_report()
        keeper_action()
        time.sleep(1)

# --- Start Game ---
if __name__ == "__main__":
    game_loop()