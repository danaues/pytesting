# Program to test new function

RA3_SUNNATAKEYPAD_MODEL_MAP_TO_TYPE = {
    "RRST-W2B-XX": "SunnataKeypad_2Button",
    "RRST-W3RL-XX": "SunnataKeypad_3ButtonRaiseLower",
    "RRST-W4B-XX": "SunnataKeypad_4Button",
}

def _device_model_to_type(model: str) -> str:
    """Convert a lutron_caseta device registry entry model to type."""
    device_model, device_type = model.split(" ")
    if device_model in RA3_SUNNATAKEYPAD_MODEL_MAP_TO_TYPE:
            return RA3_SUNNATAKEYPAD_MODEL_MAP_TO_TYPE[device_model]
    return device_type.replace("(", "").replace(")", "")
