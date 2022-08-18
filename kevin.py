# Program to test new function

def _device_model_to_type(model: str) -> str:
    """Convert a lutron_caseta device registry entry model to type."""
    device_model, device_type = model.split(" ")
    if "SunnataKeypad" in device_type:
            _, model_key,_ = device_model.split("-")
            return "_".join((device_type.replace("(", "").replace(")", ""), model_key))  
    return device_type.replace("(", "").replace(")", "")

tstmodel = "RRST-W4B-XX SunnataKeypad"
print(tstmodel.split(" "))

print("PJ2-3BRL-GXX-X01 Pico3ButtonRaiseLower")
print(_device_model_to_type("PJ2-3BRL-GXX-X01 Pico3ButtonRaiseLower"))
print("")

print("CS-YJ-4GC-WH FourGroupRemote")
print(_device_model_to_type("CS-YJ-4GC-WH FourGroupRemote"))
print("")

print("RRST-W4B-XX SunnataKeypad")
print(_device_model_to_type("RRST-W4B-XX SunnataKeypad"))
print("")

