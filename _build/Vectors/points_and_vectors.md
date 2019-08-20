---
redirect_from:
  - "/vectors/points-and-vectors"
interact_link: content/Vectors/points_and_vectors.ipynb
kernel_name: python3
has_widgets: false
title: 'Points and vectors'
prev_page:
  url: /msg.html
  title: 'Vectors'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import numpy as np

```
</div>

</div>



$\newcommand{\vct}[3]{ \left(\begin{array}{r} #1\\#2\\#3 \end{array}\right) }$



## 3d-Coordinate systems

To describe geometrical objects in space with the help of coordinates, we need a *three dimensional* coordinate system for reference. We use the convention that:
- the $x$-axis points forward
- the $y$-axis points to the right
- the $z$-axis points upwards

<img src="./pics/3d_coord.png" width="35%" align="center">



## Points

A __point__ $A$ with the __coordinates__ $x, y$ and $z$, written $A(x|y|z)$, indicates a *position* in space relative to the coordinate system. For example, point $A(3|4|5)$ can be found as follows: Starting at the origin, 
- walk $3$ units along the $x$-direction (towards me), and from there
- walk $4$ units along the $y$-direction (to the right), and from there
- walk $5$ units along the $z$-direction (upwards)

Negative coordinates are also allowed and indicate to move into the opposite axis direction. For example, moving $z=-3$ units along the $z$-direction means moving $3$ units downwards.

<img src="./pics/3d_point.png" width="40%" align="center">

Note:
 - The point with the coordinates $O(0|0|0)$ is called the __origin__ of the coordinate system.
 - We typically use capital letters to denote points ($A, B , U, ...$)



## Vectors

A __vector__ $\vec v$ with components $x, y$, and $z$, written $$\vec{u}=\left(\begin{align} x \\ y \\ z \end{align}\right)$$ represents an *arrow* in space. An arrow has a tail, a head, and a specific length and direction.

<img src="./pics/arrow1.png" width="20%" align="center">

So how do three numbers define an arrow in space? For example, take the vector $$\vec{u}=\left(\begin{align} 2 \\ 4 \\ 5 \end{align}\right)$$. We will draw the arrow as follows: Pick any location in space for the tail of the arrow, then find the arrow head by
- move $2$ units in $x$-direction, from there
- move $4$ units in $y$-direction, and from there
- move $5$ units in $z$-direction

<div class="important">
Note: the three components of a vector do not tell you where the arrow is in space.
</div>

We have seen that a vector represents an arrow. The opposite is also true. For every arrow we draw in space, we can find the three components of a vector that represents this arrow - just find out how to get from the tail of the arrow to the head of the arrow by following along the $x$-axis, $y$-axis and $z$-axis. For example, assume that for the arrow the tail is at $A(0|1|1)$ and the head at $B(0|5|3)$. 

<img src="./pics/AtoB.png" width="30%" align="center">

To get from $A$ to $B$, we have to walk along the $x$ axis by $0$ units, along the $y$-axis by $4$ units, and along the $z$-axis by $2$ units:

 $A$ | $\rightarrow$  | $B$
 ---|---|---
 $0$  | $\overset{+0}{\rightarrow}$  | $0$
 $1$  | $\overset{+4}{\rightarrow}$  | $5$
 $1$  | $\overset{+2}{\rightarrow}$  | $3$
 
So the vector representing this arrow is $$\vec{u}=\left(\begin{align} 0 \\ 4 \\ 2 \end{align}\right)$$

Note:
 - We typically use small lettters with an arrow pointing to the right on top of it to denote vectors ($\vec a, \vec u, ...$). 
 - There is one exception: if the components of a vector arise from an arrow from a given point $A$ to a given point $B$, the vector is often denoted by $\overrightarrow{AB}$. In the example above, we culd have written $$\overrightarrow{AB}=\left(\begin{align} 0 \\ 4 \\ 2 \end{align}\right)$$



## Exercises

1. Determine the coordinates $A$ that are zero.
<img src="./pics/exc_specPts.png" width="70%" align="center">

2. Indicate the following points in a 3d-coordinate system: $P(3|-4|5)$, $Q(3|-4|5)$, $R(3|-4|5)$, $S(3|-4|5)$, $T(3|-4|5)$, and $U(3|-4|5)$.

3. On which plane and/or axis are the following points: $U(0|1|2)$,  $S(-1.3|1.2|0)$,  $V(-13|0|0)$. 

4. Find the coordinates of all the corners of the cube of side length $5$, and of the pyramid of height $h=4$ and base side length $s=4$.
<img src="./pics/cube_pyr.png" width="60%" align="center">

5. Draw the vectors $\vct{1}{0}{3}$ and $\vct{1}{2}{3}$ as arrows. Start anywhere in space.

6. Determine the vector $\overrightarrow{UV}$:
    - $U(1|2|-1)$, $V(2|10|-3)$
    - $U(0|0|0)$, $V(3|1|10)$
    - $U(-1.2|-3.1|5)$, $V(2|2|1)$


7. If I start at point $A(0|1|0)$ and follow the components given by vector $\vec{u}=\vct{1}{-1}{1}$, where do I end up? Find the coordinates of this point $B$. Starting at $B$, what vector do I have to follow to get back to point $A$?

8. Consider the parallelogram with the vertices $A(1|4|1)$, $B(0|3|2)$, $C$, and $D(2|3|0)$, what are the coordinates of point $C$?
<img src="./pics/parallelogram.png" width="20%" align="center">

9. Determine the components of the arrows shown in the figure below. Vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ are on the x-axis, y-axis, and z-axis, and vectors $\vec{d}$ and $\vec{e}$ are in the yz-plane.
<img src="./pics/arrowTOvec.png" width="30%" align="center">

10. Consider the vectors $\vct{0}{3}{4}$ and $\vct{1}{4}{6}$. Determine their lengths. Can you find a general formula for determining the length of a vector $\vct{x}{y}{z}$?

11. Coonsider the vector $\vct{0}{3}{4}$. Find another vector that 
 - points into the same direction, and has twice the length.
 - points in the opposite direction and has half the length.
 - More generally, given a vector $\vct{x}{y}{z}$, what are the components of vector pointing in the same direction but is $s$ times longer?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#needs to be in the last cell for css styling
from IPython.core.display import HTML
def css_styling():
    styles = open("/home/tom/jupyter/mathnotes/styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<style>
div.important {    
    background-color: #fcf2f2;
    border-color: #dFb5b4;
    border-left: 5px solid #dfb5b4;
    padding: 0.5em;
    }

div.exc {    
    background-color: lightgray;
    border-color: lightgray;
    border-left: 5px solid gray;
    padding: 0.5em;
    }

 </style>

</div>


</div>
</div>
</div>

