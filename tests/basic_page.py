import os
from nitrogen import Nitrogen

nitro = Nitrogen(source_dir = os.path.join(os.path.dirname(__file__), "src"))

@nitro.on("click")
def on_click(button_name: str) -> None:
    return print(f"Button clicked: {button_name}!")

nitro.start()
