---
redirect_from:
  - "/vectors/section1-points-and-vectors"
interact_link: content/Vectors/section1_points_and_vectors.ipynb
kernel_name: python3
has_widgets: false
title: 'Points and vectors'
prev_page:
  url: /index.html
  title: 'Basics'
next_page:
  url: /Vectors/section2_magnitude.html
  title: 'The magnitude of a vector'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## 3d-Coordinate systems
---

To describe geometrical objects in space with the help of coordinates, we need a *three dimensional* coordinate system for reference. We use the convention that:
- the $x$-axis points forward
- the $y$-axis points to the right
- the $z$-axis points upwards

<img src="./pics/3d_coord.png" width="50%" align="center">



## Points
---

A __point__ $A$ with the __coordinates__ $x, y$ and $z$, written 

$$\nonumber A(x \vert y \vert z)$$ 

indicates a *position* in space relative to the coordinate system. For example, point $A(3 \vert 4 \vert 5)$ can be found as follows: Starting at the origin, 
- walk $3$ units along the $x$-direction (towards me), and from there
- walk $4$ units along the $y$-direction (to the right), and from there
- walk $5$ units along the $z$-direction (upwards)

Negative coordinates are also allowed and indicate to move into the opposite axis direction. For example, moving \(z=-3\) units along the \(z\)-direction means moving $3$ units downwards.

<img src="./pics/3d_point.png" width="65%" align="center">

Note:
 - The point with the coordinates $O(0 \vert 0 \vert 0)$ is called the __origin__ of the coordinate system.
 - We typically use capital letters to denote points $(A, B , U, ...)$



## Vectors
---

A __vector__ $\vec v$ with __components__ $x, y$, and $z$, written 

$$\nonumber\vec{u}=\left(\begin{array}{r} x\\y\\z \end{array}\right)$$

represents an *arrow* in space. An arrow has a tail, a head, and a specific length and direction.

<img src="./pics/arrow1.png" width="25%" align="center">

So how do three components define an arrow in space? We interpret the three numbers as instructions of how to get from the tail of the arrow its head. For example, take the vector 

$$\nonumber\vec{u}=\left(\begin{array}{r} 2\\4\\5 \end{array}\right)$$

We will draw the arrow as follows: Pick any location in space for the tail of the arrow, then find the arrow head by
- move $2$ units in $x$-direction, from there
- move $4$ units in $y$-direction, and from there
- move $5$ units in $z$-direction

<div class="important">
Note: the three components of a vector do not tell you where the arrow is in space.
</div>

We have seen that a vector represents an arrow. The opposite is also true. For every arrow we draw in space, we can find the three components of a vector that represents this arrow - just find out how to get from the tail of the arrow to the head of the arrow by following along the $x$-axis, $y$-axis and $z$-axis. For example, assume that for the arrow the tail is at $A(0 \vert 1 \vert 1)$ and the head at $B(0 \vert 5 \vert 3)$. 

<img src="./pics/AtoB.png" width="60%" align="center">

To get from $A$ to $B$, we have to walk along the $x$ axis by $0$ units, along the $y$-axis by $4$ units, and along the $z$-axis by $2$ units:
 
$$\nonumber
\begin{array}{lcl}
A & \rightarrow & B \\
\hline
0 & \overset{+0}{\rightarrow} & 0 \\ 
1 & \overset{+4}{\rightarrow} & 5 \\ 
1 & \overset{+2}{\rightarrow} & 3 \\ 
\end{array}
$$


So the vector representing this arrow is 

$$\nonumber\vec{u}=\left(\begin{array}{r} 0\\4\\2 \end{array}\right)$$

Notes:
 - We typically use small letters with an arrow pointing to the right on top of it to denote vectors $(\vec a, \vec u, ...)$. 
 - There is one exception: if the components of a vector arise from an arrow from a given point $A$ to a given point $B$, the vector is often denoted by $\overrightarrow{AB}$. In the example above, we could have written 
 
$$\nonumber\overrightarrow{AB}=\left(\begin{array}{r} 0\\4\\2 \end{array}\right)$$
 
 
 - Two vectors are called __equal__ if their corresponding $x$-, $y$-, and $z$-components are equal.



## Exercise
---

1. Determine all the coordinates of point $A$ that are zero. $A$ is either on the $xy$-plane, $xz$-plane, $yz$-plane, $x$-axis, $y$-axis, or $z$-axis.
<img src="./pics/exc_specPts.png" width="75%" align="center">

2. Indicate the following points in a 3d-coordinate system:
 - $P(0 \vert -2 \vert 5)$
 - $Q(2 \vert 5 \vert 5)$
 - $R(2 \vert 2 \vert 2)$
 - $S(-2 \vert -2 \vert 2)$
 - $T(0 \vert 0 \vert 0)$
 - $U(0 \vert 0 \vert -5)$

3. On which plane and/or axis are the following points: 
 - $U(0 \vert 1 \vert 2)$
 - $S(-1.3 \vert 1.2 \vert 0)$
 - $V(-13 \vert 0 \vert 0)$ 

4. Find the coordinates of all the corners of the cube of side length $5$, and of the pyramid of height $h=4$ and base side length $s=4$.
<img src="./pics/cube_pyr.png" width="70%" align="center">

5. Draw the vectors $\left(\begin{array}{r} 1\\\ 0\\\ 3 \end{array}\right)$ and $\left(\begin{array}{r} 1\\\ 2\\\ 3 \end{array}\right)$ as arrows. Start anywhere in space.

6. Determine the vector $\overrightarrow{UV}$ from point $U$ to point $V$:
 - $U(1 \vert 2 \vert -1)$ and $V(2 \vert 10 \vert -3)$
 - $U(0 \vert 0 \vert 0)$ and $V(3 \vert 1 \vert 10)$
 - $U(-1.2 \vert -3.1 \vert 5)$ and $V(2 \vert 2 \vert 1)$

7. If I start at point $A(0 \vert 1 \vert 0)$ and follow the components given by vector $\vec{u}=\left(\begin{array}{r} 1\\\ -1\\\ 1 \end{array}\right)$, where do I end up? Find the coordinates of this point $B$. Starting at $B$, what vector do I have to follow to get back to point $A$?

8. Consider the parallelogram with the vertices $A(1 \vert 4 \vert 1)$, $B(0 \vert 3 \vert 2)$, $C$, and $D(2 \vert 3 \vert 0)$, what are the coordinates of point $C$?
<img src="./pics/parallelogram.png" width="35%" align="center">

9. Determine the components of the arrows shown in the figure below. Vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ are on the $x$-axis, $y$-axis, and $z$-axis, and vectors $\vec{d}$ and $\vec{e}$ are in the $yz$-plane.
<img src="./pics/arrowTOvec.png" width="45%" align="center">

10. Consider the vectors $\vec a = \left(\begin{array}{r} 0\\\ 3\\\ 4 \end{array}\right)$ and $\vec b = \left(\begin{array}{r} 1\\\ 4\\\ 6 \end{array}\right)$. Determine their lengths. Can you find a general formula for determining the length of a vector $\vec c = \left(\begin{array}{r} x\\\ y\\\ z \end{array}\right)$?

11. Consider the vector $\left(\begin{array}{r} 0\\\ 3\\\ 4 \end{array}\right)$. Find another vector that 
 - points into the same direction, and has twice the length.
 - points in the opposite direction and has half the length.
 - More generally, given a vector $\left(\begin{array}{r} x\\\ y\\\ z \end{array}\right)$, what are the components of the vector pointing in the same direction and is $s$ times longer?



## Solutions
---

1. a) $A_z=0$, b) $A_y=0$, c) $A_x=0$, d) $A_y=A_z=0$, e) $A_x=A_z=0$, f) $A_x=A_y=0$

2. <img src="./pics/sol_pts.png" width="60%" align="center">

3. $U$: $yz$-plane, $S$: $xy$-plane, $V$: $x$-axis, $xy$-plane, $xz$-plane.

4. Cube: $A(5 \vert 0 \vert 0)$, $B(5 \vert 5 \vert 0)$, $C(0 \vert 5 \vert 0)$, $D(0 \vert 0 \vert 0)$, $E(5 \vert 0 \vert 5)$, $F(5 \vert 5 \vert 5)$, $G(0 \vert 5 \vert 5)$, $H(0 \vert 0 \vert 5)$ <br> 
Pyramid: $A(2 \vert -2 \vert 0)$, $B(2 \vert 2 \vert 0)$, $C(-2 \vert 2 \vert 0)$, $D(-2 \vert -2 \vert 0)$, $E(0 \vert 0 \vert 4)$

5. <img src="./pics/solVec1.png" width="45%" align="center">

6. a) $\overrightarrow{UV}=\left(\begin{array}{r} 1\\\ 8\\\ -2 \end{array}\right)$, 
   b) $\overrightarrow{UV}=\left(\begin{array}{r} 3\\\ 1\\\ 10 \end{array}\right)$, 
   c) $\overrightarrow{UV}=\left(\begin{array}{r} 3.2 \\\ 5.1\\\ -4 \end{array}\right)$

7. $B(1 \vert 0 \vert 1)$

8. $C(1 \vert 2 \vert 1)$

9. $\vec a =\left(\begin{array}{r} 1\\\ 0\\\ 0 \end{array}\right)$,
   $\vec b =\left(\begin{array}{r} 0\\\ 2\\\ 0 \end{array}\right)$,
   $\vec c =\left(\begin{array}{r} 0\\\ 0\\\ 2 \end{array}\right)$,
   $\vec d =\left(\begin{array}{r} 0\\\ 4\\\ -3 \end{array}\right)$,
   $\vec e =\left(\begin{array}{r} 0\\\ 3\\\ 5 \end{array}\right)$

10. Length of $\vec a$ is (Pythagoras) $\sqrt{3²+4²}=5$, length of $\vec b$ is (applying Pythagoras twice) $\sqrt{1²+4²+6²}=\sqrt{53}$, and the length of vector $\vec c$ is $\sqrt{x²+y²+z²}$  

11. The vectors are $\left(\begin{array}{r} 0\\\ 6\\\ 8 \end{array}\right)$, $\left(\begin{array}{r} 0\\\ -1.5\\\ -2 \end{array}\right)$, and $\left(\begin{array}{r} s\cdot x\\\ s\cdot y\\\ s\cdot z \end{array}\right)$ 



