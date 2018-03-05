# python-ebi
EBI - Entity-Boundary-Interactor Architecture in Python

#### This project is an experiment!! Studying best ways of concerns separation

### Requirements

Python 3.6.2

### Description

It's not easy find resources about EBI on the web...But I'll try to explain what i get. Feel free to contact me about any information on this matter.

### EBI

EBI - Entity-Boundary-Interactor is an architectural style coined by Ivar Jacobson in 1992. A lot of people confuse EBI with MVC, but they aren't the same. Ones say that MVC is to User Interface and EBI is to business logics.

You have three concepts:

#### Entity

Entity is where you hold you application data and all the behavior coupled to it. Each Entity object represents a relevant concept in you domain. Entity object should contain the logic that would change when the Entity itself changes.

### Boundary

All functionality dependent on the system environment (tools and delivery mechanisms) belongs to Boundary objects.

Any interaction of the system with any actor goes through a Boundary object. It can be a human user or a non-human "user".

### Interactors

