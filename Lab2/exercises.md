# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*
Good examples:
len(), del dict[key], clear(), append(), copy(), extend(), remove(), reverse()
sort()

Bad examples:
pop(key[, default]) would better be popAndReturnValue(key[, default])
popitem() would better be popAndReturnItem()
sorted() would better be ReturnNewSorted()
*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*
Dictionary is a mapping type which maps hashable values(as keys) to arbitrary objects(as values). It actually stores key-value pair and uses hash table to implement. It doesn't have an order and we access the value by an unique key.

List uses array to store a collection of homogeneous items and we can access a value/element by its index, which is fixed and is assigned based on the order in which elements were added. We can say list is ordered by insertion order.
*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*yes. But the index should be within the range(-len(list) <= i < len(list)), otherwise it will raise "IndexError: list index out of range"*

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*pros:
It allows us to reuse a variable or a bunch of codes without throwing any errors, and we can store different data type in one container which allows more flexibility(codes can be short and clean compared to strict type).
cons:
It may leads to some unintentional overwrite/insertion/changes if the container is flexible to data types and doesn't throw an error for thus activity, making debugging harder.
*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*
I find request(), options(), head(), get(), post(), put(), patch(), delete() describe what kind/type of request the function will send, but didn't include the information that they will return a response object. Take get() for example, it would better be GetAndReturn() which means sending a get request and return a response object.
*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*No. I find a maximum number of 2 for positional arguments in member functions. If a function takes a large number of arguments, it may be hard for user to understand and call them. Sometimes it's just telling us we may have to break it down to several structured functions.*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*
**kwargs signifies the function may receive elements of a dictionary, which represent a collection of keyworded arguments.
Good because we cannot decide the number of keyworded arguments at the time thus it leaves flexibility for users. When they call the function, they can pass any kwargs they'd like.
Bad because it's not clear what kind of arguments are expected and if we don't know what kind of kwargs will the function receive, it's hard for us to write the codes to deal with potential arguments.
*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

*
"url" is not set to anything since it's a necessary argument that users should pass to indicate the web address they want to interact with. However, "data" is set to None since it's optional. When we send a request to the endpoint, we can add data in the body of the request or leave it as the default "None".

yes. arguments can be set to integer, list, string and other values.

By predetermining value, if it's a meaningful value, it suggests a value that would be commonly used for the parameter. If it's none, it sugeests users may or may not use this parameter. In both ways, it avoids errors when users omit these predetermined parameters because it will use the default value we assgin to it, making it flexible for users to decide what kind of parameters they are going to use and pass.
*
