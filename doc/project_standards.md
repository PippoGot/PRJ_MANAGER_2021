- for imports use # --- LIBRARIES --- and # --- CUSTOM MODULES ---
- snake notation for files, methods and variables names when possible
- camel notation for classes
- Args:
  arg_name (arg_type): arg_description.
  Returns:
  return_type: return_description.
  Raises:
- if the type of data can be any object use PyObject
- kwarg = value when passing keyword arguments
- when creating and subdividing code in namespacing use # --- NAMESPACE NAME ---
- when possible, include a link to the docstring of subclassed methods that
  leads to the online doc
- ui objects and widgets inside the ui file use the prefix ui and camel notation

  - uiBtnName for buttons
  - uiActName for actions

- workflow:

  - write code
  - comment code
  - rename things (if the standards aren't respected)
  - commit new features

  - write test and test code
  - comment test code
  - commit test code

  - update class diagrams

  - refactor code
  - re-test
  - commit refactored code
