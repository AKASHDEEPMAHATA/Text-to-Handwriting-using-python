step 1 : install the python module pywhatkit
step 2 : start coding
  
  
  
import pywhatkit
txt = input("Enter the text : ")
pywhatkit.text_to_handwriting(txt, "filename.png", (0, 0, 138))

# text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 0)) 

# This is used to convert a string to an Image with Handwritten Characters.
# Example: pywhatkit.text_to_handwriting("Hello")

# By default the output filename is pywhatkit.png but you can change it by specifying a value for the parameter.
# Example: pywhatkit.text_to_handwriting("Hello", "filename.png")

# The default color value for the handwritten text is Black rgb(0, 0, 0) which can be changed as per choice.

# Note: There is no support for custom hand writings currently.

# Example: pywhatkit.text_to_handwriting("Hello", "filename.png", (0, 0, 138))

print("Handwriting created successfully")
