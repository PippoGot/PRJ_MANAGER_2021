1 - create basic window for the display, addition and deletion of most simple nodes
the components at their simplest will have a name and a description, as well as a parent and children list
the window should be a main window with just the 2 functions for addition and deletion implemented
create a widget to input the details of the node

2 - upgrade the main window to predispose it to different pages
one of these pages should be the components page, aka the previous main window,
but now structured as a standalone page
add an editor for the node when selected

3 - upgrade the node and the node editor to have more features and widgets
the editor will have widgets for all the fields of the node
upgrade the node structure to be composed with different type of data
for example the idea of RootNode, HardwareNode etc...

4 - add a label to define the level of a node (now a component)
create a standalone class for the ID number (examples #000-001, #MEH-001 etc...)

---

add tests for:

- add strategy to create component trees

recomment and docstring:

- components
- comp_model
- all tests

refactoring:

- try to simplify CompModel.removeRows function
- rename Component.get_index to Component.get_row
