# Text-to-Handwriting-using-python
This is used to convert a string to an Image with Handwritten Characters.

text_to_handwriting(string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 0))
This is used to convert a string to an Image with Handwritten Characters.
Example: pywhatkit.text_to_handwriting("Hello")

By default the output filename is pywhatkit.png but you can change it by specifying a value for the parameter.
Example: pywhatkit.text_to_handwriting("Hello", "filename.png")

The default color value for the handwritten text is Black rgb(0, 0, 0) which can be changed as per choice.

Note: There is no support for custom hand writings currently.

Example: pywhatkit.text_to_handwriting("Hello", "filename.png", (0, 0, 138))



<img width="960" alt="msd t2h" src="https://user-images.githubusercontent.com/90324172/144710662-f0d2c1d1-a559-4511-955e-588c41127065.png">

<img width="960" alt="msd.png" src="https://user-images.githubusercontent.com/90324172/144710727-09f3ad9d-42ea-4489-b8a8-569fa971b754.png">
