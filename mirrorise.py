def mirror_text(text):
    # Define a mapping of characters to their mirrored counterparts

    upside_down_mirror_chars = {
    'a': 'g', 'b': 'p', 'c': 'c', 'd': 'q', 'e': '6', 'f': 'ɟ', 'g': '𝞉', 'h': '𝞵', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'k',
    'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'b', 'q': 'd', 'r': 'ɹ', 's': '2', 't': 'f', 'u': 'n', 'v': 'ʌ',
    'w': 'ʍ', 'x': 'x', 'y': '𝞴', 'z': '≶',
    'A': '∀', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': '|=', 'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'K',
    'L': '𝛤', 'M': 'W', 'N': 'И', 'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': '2', 'T': '⊥', 'U': '∩', 'V': 'Λ',
    'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': '≶',
    '0': '0', '1': 'Ɩ', '2': '5', '3': '3', '4': 'ㄣ', '5': 'ᄅ', '6': 'e', '7': 'ㄥ', '8': '8', '9': '𝞉',
    ',': "'", '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
    '<': '>', '>': '<', '&': '⅋', '_': '‾'
}
    upside_down_chars = {
    'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ',
    'l': 'ʃ', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ',
    'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
    'A': '∀', 'B': '𐐒', 'C': 'Ↄ', 'D': '◖', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': '⋊',
    'L': '⅃', 'M': 'W', 'N': 'И', 'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': 'S', 'T': '⊥', 'U': '∩', 'V': 'Λ',
    'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
    '0': '0', '1': 'Ɩ', '2': '5', '3': '3', '4': 'ㄣ', '5': 'ᄅ', '6': '9', '7': 'ㄥ', '8': '8', '9': 'e',
    ',': "'", '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
    '<': '>', '>': '<', '&': '⅋', '_': '‾'
}
    
    mirror_mapping  = {
    'A': 'A', 'B': '𐐒', 'C': 'Ↄ', 'D': '◖', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': '⋊',
    'L': '⅃', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'C|', 'Q': 'Ό', 'R': 'r', 'S': '5', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'z',
    'a': 'ɒ', 'b': 'd', 'c': 'ↄ', 'd': 'b', 'e': 'Ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'H', 'i': 'i', 'j': 'j', 'k': 'ʞ',
    'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'q', 'q': 'p', 'r': 'r', 's': '5', 't': 'T', 'u': 'u', 'v': 'v',
    'w': 'w', 'x': 'x', 'y': 'Y', 'z': 'z',
    '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6',
    ',': "'", '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": "'", '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
    '<': '>', '>': '<', '&': '⅋', '_': '‾'
}
    
    # Reverse the text and map each character to its mirrored counterpart
    mirrored_upside_down_text = ''.join(upside_down_mirror_chars.get(char, char) for char in text)
    return mirrored_upside_down_text

mess="""
This I just can't tell 
how much I'm into it. 
Back in the days it was 
like when ever I think 
of you the radio was playing 
this song as a perfect BGM.
I have got a very special 
relation ship with this 
song about you. 
"""

mess="""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789

"""

# def mirror_text(text):
#     # Reverse the text
#     reversed_text = text[::-1]
#     return reversed_text

# Example usage
def mirror_encode(mess):
    outt=""
    for line_of_text in mess.split("\n")[::-1]:
        mirrored_text = mirror_text(line_of_text)
        outt+=mirrored_text+"\n"

    return(outt)