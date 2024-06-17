def mirror_text(text):
    # Define a mapping of characters to their mirrored counterparts
    mirror_upside_down_mapping = {
        'A': '∀', 'B': '𐐒', 'C': 'Ↄ', 'D': '◖', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ᒋ', 'K': '⋊',
        'L': '⅃', 'M': 'W', 'N': 'И', 'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ᴚ', 'S': 'S', 'T': '⊥', 'U': '∩', 'V': 'Λ',
        'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        'a': 'ɒ', 'b': 'd', 'c': 'ↄ', 'd': 'b', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ı', 'j': 'ɾ', 'k': 'ʞ',
        'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'q', 'q': 'p', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ',
        'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
        '0': '0', '1': '1', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6',
        ',': "'", '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
        '<': '>', '>': '<'
    }
    
    # Reverse the text and map each character to its mirrored counterpart
    mirrored_upside_down_text = ''.join(mirror_upside_down_mapping.get(char, char) for char in text[::-1])
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

# Example usage
outt=""
for line_of_text in mess.split("\n")[::-1]:
    mirrored_text = mirror_text(line_of_text)
    outt+=mirrored_text+"\n"

print(outt)

