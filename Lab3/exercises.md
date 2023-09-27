# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is a concrete class:
		- abstract class should use abc module including abstarct base class. Besides, MObject doesn't have abstarct methods.
		- MObject can be instantiated through its __init__ method.
2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- It's called when an instance X of Image class is about to be destroyed. X.__del__ is only called when X's reference reaches zero.
3. What class does Texture inherit from?
	- Image class
4. What methods and attributes does the Texture class inherit from 'Image'? 
	- Since Texture class inherits from Image class, it inherits all the methods and attributes from the Image class including:
		- m_width, m_height, m_colorChannels, m_Pixels
		- __init__, getWidth(), getHeight(), getPixelColorR(), getPixels(), and setPixelsToRandomValue()
		- will NOT inherit __del__ unless define it in Texture class and explicitly call Image.__del__ within the method to ensure proper deletion.
5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I think 'Texture' should have a is-a relationship with 'Image' since I understand 'Texture' as an image or a collection of images used to construct 3D models. It just adds more details like texture coordinates(u, v) which associates with each vertex and defines how it is mapped to a surface. I classify Texture as Image but it's a more advanced version.
6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- No. since Texture inherits from Image, it will use the constructor of Image class.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

2. Are singleton's in Python thread safe? Why or why not?
	It's not thread-safe, subject to race conditions in a multithreaded environment. If more than one thread attempt to create an instance of the singleton
	simultaneously, it can result in multiple instances being created unless we implement synchronizatuion mechanisms such as adding locks.
