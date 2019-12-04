def caps_lock(text: str) -> str:
    new_text = ''
    CAPSLOCK = -1
    for char in text:
        if char in ('a', 'z'):
            CAPSLOCK *= -1
        else:
            if CAPSLOCK < 0:
                new_text += char
            else:
                new_text += char.title()
    return new_text


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
