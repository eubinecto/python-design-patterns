# The Builder Pattern in Python
## What?


## When?

> We use builder pattern when we know:
> - an object must be created in **multiple steps**.
> - and **the same constructions** are required for different representations.

Any examples?
- an HTML page generator.
  - inside `<html>..</html>`, there exists `<title>...</title>`, ... etc. An HTML page
    object consists of multiple parts (tags, in this case).
  - But each page has different representations. Google, Naver, YouTube, etc.
  - Note that the page must be constructed step by step. first the title tag, then the html tag.
    It is only after all parts are complete that the page can be shown to the client.
- document converters
- user interface form creators
- "telescopic constructor problem"
  
## How?
As for the HTML page generator example, we could employ two 
main participants:
 - The Builder: defines the logics for the construction of an object 
 - The Director: **uses** builders to construct an object, step-by-step.



## Relations to other patterns

What's the difference between this and Factory method? "The distinction between
the builder pattern and the factory pattern might not be very clear".
the difference:
 - factory pattern: builds an object in **single step**.
 - builder pattern: builds an object in **multiple steps**, almost through the use 
   of a **director**.
   - One exception to this rule: Java's `StringBuilder` does not employ a director for building Strings.
   
another difference (not sure what this means?):
 - factory pattern: returns the created instance immediately.
 - builder pattern: the client asks the director **when it needs it**. <- what does this mean?
 


