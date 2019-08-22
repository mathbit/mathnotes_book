---
redirect_from:
  - "/vectors/section4-basic-operations"
interact_link: content/Vectors/section4_basic_operations.ipynb
kernel_name: python3
has_widgets: false
title: 'Basic vector operations'
prev_page:
  url: /Vectors/section3_special_vectors.html
  title: 'Some special vectors'
next_page:
  url: /Vectors/section3_multiplying_with_scalar.html
  title: 'Multiplying vectors with a scalar'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Adding a point and a vector
---

Consider a point $A(A_x \vert A_y \vert A_z)$ and a vector $\vec v =\left(\begin{array}{r} v_x\\\ v_y\\\ v_z \end{array}\right)$.

If we start at point $A$ and follow the instructions given by vector $\vec v$

$$\nonumber
\begin{array}{lcl}
A & \rightarrow & B \\
\hline
A_x & \overset{+v_x}{\rightarrow} & A_x+v_x \\ 
A_y & \overset{+v_y}{\rightarrow} & A_y+v_y \\ 
A_z & \overset{+v_z}{\rightarrow} & A_z+v_z \\ 
\end{array}
$$

we end up at new point with the coordinates 

$$\nonumber (A_x+v_x \vert A_y+v_y \vert A_z + v_z) $$


We denote this new point by 

$$\nonumber\boxed{A+\vec v}$$

or, if give it a new name, e.g. $B$, we write

$$\nonumber B = A+\vec v$$







## Adding two vectors
---

Consider two vectors $\vec v = \left(\begin{array}{r} v_x\\\ v_y\\\ v_z \end{array}\right)$ and $\vec w = \left(\begin{array}{r} w_x\\\ w_y\\\ w_z \end{array}\right)$. The __sum__ of the two vectors, denoted by 

$$\nonumber \boxed{\vec v+\vec w}$$

is a new vector with the components

$$\vec v+\vec w = \nonumber\left(\begin{array}{r} v_x+w_x\\\ v_y+w_y\\\ v_z+w_z \end{array}\right)$$

What is the relationship between the arrows represented by $\vec v$, $\vec w$, and $\vec v+\vec w$? We can actually construct the arrow of $\vec v+\vec w$ with the help of the arrows of $\vec v$ and $\vec w$ as follows: 
 - arrange the arrows of $\vec v$ and $\vec w$ such that the tail of $\vec w$ is attached to the head of $\vec v$
 - the arrow of $\vec v+\vec w$ is obtained by drawing an arrow from the tail of $\vec v$ to the head of $\vec w$

This construction is called *completing the triangle*.

<img src="./pics/completeTriangle.png" width="20%" align="center">

Note: To find the arrow that is represented by the sum of three vectors $\vec u+\vec v+\vec w$, we form a chain of of the arrows (attach tail of $\vec v$ to head of $\vec u$, and tail of $\vec w$ to head of $\vec v$ and form the arrow from the tail of $\vec u$ to the head of  
<img src="./pics/addThreeVec.png" width="30%" align="center">



## Subtracting two vectors
---

The __subtraction__ of $\vec w$ from $\vec v$ is defined as adding to $\vec v$ the opposite vector of $\vec w$: 

$$\nonumber \boxed{\vec v-\vec w = \vec v+ (-\vec w)}$$

The components are therefore 

$$\nonumber \vec v  - \vec w = \left(\begin{array}{r} v_x-w_x\\\ v_y-w_y\\\ v_z-w_z \end{array}\right)$$

It also follows that we can construct the arrow representing the vector $\vec v-\vec w$ by simply completing the triangle of the vector $\vec v$ and $-\vec w$. Recall that the arrow of $-\vec w$  is obtained by reflected the arrow of $\vec w$ about its tail.

<img src="./pics/subtractVectors.png" width="25%" align="center">



## Multiplication of a vector with a scalar
---

Consider a vector $\vec v = \left(\begin{array}{r} v_x\\\ v_y\\\ v_z \end{array}\right)$ and a constant $c$, where $c$ can by any real number. In the context of vectors, a number is called a __scalar__. The __multiplication__ of $\vec v$ with $c$, denoted by 

$$\nonumber\boxed{c\cdot \vec{v}}$$

is defined as the vector with the components

$$\nonumber\vec v = \left(\begin{array}{r} c\cdot v_x\\\ c \cdot v_y\\\ c \cdot v_z \end{array}\right)$$

Thus each component of $\vec v$ is multiplied by the constant $c$. Make sure yu understand that 
- The arrow that is represented by $c \cdot \vec{v}$ is $c$ times longer than $\vec v$. 
- If $c$ is positive, the arrows point in the same direction, if $c$ is negative, the arrow point in opposite direction (see figure below).


<img src="./pics/multiplicWithConst.png" width="95%" align="center">



