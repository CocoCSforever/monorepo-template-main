**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>
**Use Case**: *Create sized Canvas*

**Primary Actor**: *User*

**Goal in Context**: *To create a window that is 600 pixels wide and 400 pixels high when the program starts and maintain the window while program is running.*

**Preconditions**: *The program must be started and running in a responsive state.*

**Trigger**: *(1) A  user starts the program by double-clicking the application icon. (2) A  user starts the program by [some reserved actions].*
  
**Scenario 1**: *A user will double-click the application icon to start the program.*

**Scenario 2**: *A user will press [reversed composite key] to start the program.*
 
**Exceptions**: *The program may become potentially unresponsive. In this case, prompt the user to restart the program/exit&start and send error report back to developers.*

**Priority**: *High-priority*

**When available**: *First release*

**Channel to actor**: *The primary actor communicates through I/O devices. This includes the keyboard and the mouse. The system is responsible for creating a window with pre-decided size(should respond within 3 seconds) and maintain it during the execution. The user is responsible for the  input action to start the program.*

**Secondary Actor**: *N/A*

**Channels to Secondary Actors**: *N/A*

**Open Issues**: *We may need to allow users to set canvas dimensions based on their preference in the future: (1) provide some common canvas sizes that users can choose from. In addition, allow users to set canvas to any dimensions they'd like. (2) save user preference so that users can default their canvas to a certain size every time they run the app.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
