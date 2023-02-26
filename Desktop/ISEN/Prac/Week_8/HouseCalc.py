# Python production code for ISE worksheet 6B.

def roomVolume(width, length, height):
    """
    Calculates the volume of a room, but only if the imported width, length and 
    height are valid. To be valid, width must be at least 2 (metres), length 
    2.5, and height 3. For invalid imports, this submodule will return 0.
    """
    volume = 0.0
    if width >= 2.0 or length >= 2.5 or height >= 3.0:
        volume = width * length * height
        
    return volume
