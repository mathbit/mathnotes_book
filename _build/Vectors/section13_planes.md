---
redirect_from:
  - "/vectors/section13-planes"
interact_link: content/Vectors/section13_planes.ipynb
kernel_name: python3
has_widgets: false
title: 'The plane'
prev_page:
  url: /Vectors/section12_orthogonalVectors.html
  title: 'Orthogonal vectors'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Planes

The position of a given plane $E$ in space is completely determined by a point $A$ on this plane, and any vector $\vec n$ that forms a right angle with the plane. 

<img src="./pics/plane1.png" width="80%" align="center">

Note:

- Even though we draw borders to indicate a plane, it has no border and extends in all directions to infinity.
- You can think of a plane as a set of infinitely many points. The statement "$A$ is on plane $E$" can therefore be rewritten as $A \in E$.

### Example
---
1. The plane containing point $A(0\vert 0\vert 1)$ and with normal vector $\vec{n}=\left(\begin{array}{r} 0\\\ 0\\\ 1 \end{array}\right)$ is parallel to the $xy$-plane.

2. The plane containing point $A(0\vert 0\vert 1)$ and with normal vector $\vec{n}=\left(\begin{array}{r} 0\\\ 0\\\ -10 \end{array}\right)$ is the same plane as above.

3. The $yz$-plane has the normal vector $\vec{n}=\left(\begin{array}{r} 1\\\ 0\\\ 0 \end{array}\right)$ or $\vec{n}=\left(\begin{array}{r} -0.1\\\ 0\\\ 0 \end{array}\right)$ or $\vec{n}=\left(\begin{array}{r} 140.321\\\ 0\\\ 0 \end{array}\right)$.

---

Consider a plane $E$ containing point $A$ and with normal vector $\vec n$. How can we decide if some other point $P$ in also on the plane? 

<img src="./pics/plane2.png" width="80%" align="center">

From the figure below we see that 
$$\nonumber\boxed{P \in E\,\mbox{ if }\, \overrightarrow{AP} \perp \vec{n}}$$ 


### Example
---

A plane $E$ passes through the point $A(1\vert 0\vert 1)$ and has normal vector $\left(\begin{array}{r} 7\\\ -4\\\ 5 \end{array}\right)$. Is point $P(3\vert 1\vert 2)$ in $E$? No, because 

$$\nonumber\overrightarrow{AP} \bullet \vec{n} = \left(\begin{array}{r} 3-1\\ 1-0\\ 2-1 \end{array}\right) \bullet \left(\begin{array}{r} 7\\ -4\\ 5 \end{array}\right) = 14-4+5=15\neq 0$$ 

thus $\overrightarrow{AP} \not\perp \vec{n}$.




## Exercise
---

1. A plane $E$ passes through the point $A(1\vert 0 \vert 1)$ and has normal vector $\left(\begin{array}{r} 7\\\ -4\\\ 5 \end{array}\right)$. Find another point $Q$ in $E$.

2. A plane $F$ contains the point $A(3\vert 0\vert 0)$ and has normal vector $\vec{n}=\left(\begin{array}{r} 6\\\ 3\\\ 2 \end{array}\right)$. 
	
   1. Is the point $P(1\vert 2\vert 3)$ in $F$?
   2. Is the point $Q(2\vert 4\vert 6)$ in $F$?
   3. Where does $F$ intersect the y-axis?
 
3. A plane $E$ contains the given point $A(A_x\vert A_y \vert A_z)$ and has the given normal vector $\vec{n}=\left(\begin{array}{r} n_x\\\ n_y\\\ n_z \end{array}\right)$. Show that a point $P(x\vert y\vert z)$ is in $E$ if, and only if, the coordinates $x$, $y$, and $z$ satisfy the following equation:

   $$ \nonumber n_x\cdot x + n_y\cdot y + n_z\cdot z = d $$

   where $d=n_x\cdot A_x + n_y\cdot A_y + n_z\cdot A_z$. This equation is called the __normal form of the equation__ of plane $E$. 
   
4. A plane contains the point $C(2\vert 4\vert -1)$ and has normal vector $\vec{n}=\left(\begin{array}{r} 10\\\ -5\\\ 20 \end{array}\right)$. 

    1. Find the normal form of the equation of $E$.
    2. Use this equation to decide if point $P(1\vert 3\vert -2)$ is in $E$.




## Solutions
---

1. In order to find a point $Q(x\vert y\vert z)$ on $E$, we have to find $x$, $y$, and $z$ with

   $$\nonumber\overrightarrow{AQ} \perp \vec{n}$$
   
   that is, with 
   
   $$\nonumber\left(\begin{array}{r} x-1\\ y\\ z-1 \end{array}\right) \bullet \left(\begin{array}{r} 7\\\ -4\\\ 5 \end{array}\right) = 0$$
   
   Thus, we obtain the following equation for $x$, $y$, and $z$: 

   $$\nonumber 7(x-1)-4y+5(z-1)=7x-4y+5z-12=0$$ 
   
  There are infinitely many solutions. For example, set $x=1$, $y=0$, so that $7+5z-12=0$ and therefore $z=1$. Thus $Q(1\vert 0\vert 1)$ is a point in $E$.

2. We have ...

   1. $P\in F$ because $\overrightarrow{AP} \bullet \vec{n} = \left(\begin{array}{r} 1-3\\\ 2-0\\\ 3-0 \end{array}\right) \bullet \left(\begin{array}{r} 6\\\ 3\\\ 2 \end{array}\right) = -12+6+6=0$.
   
   2. $Q \not\in F$ because $\overrightarrow{AQ} \bullet \vec{n} = \left(\begin{array}{r} 2-3\\\ 4-0\\\ 6-0 \end{array}\right) \bullet \left(\begin{array}{r} 6\\\ 3\\\ 2 \end{array}\right)  = -6+12+12=18 \neq 0$.

   3. Let us denote by $S$ the intersection point between $F$ and the y-axis.   

      - $S$ on the y-axis $\rightarrow S(0\vert y\vert 0)$
      
      - $S \in F \rightarrow \overrightarrow{AS} \bullet \vec{n} = \left(\begin{array}{r} 0-3\\\ y-0\\\ 0-0 \end{array}\right)  \bullet \left(\begin{array}{r} 6\\\ 3\\\ 2             \end{array}\right)  = -18+3y+0=0$.
      
      Thus $y=6$ and therefore $S(0\vert 6\vert 0)$.
      
3. $P$ is on $E$ if, and only if, $\overrightarrow{AP} \bullet \vec{n} = 0$

   $$\nonumber \leftrightarrow \left(\begin{array}{r} x-A_x\\\ y-A_y\\\ z-A_z \end{array}\right) \bullet \left(\begin{array}{r} n_x\\\ n_y\\\ n_z \end{array}\right) = 0$$
   
   $$\nonumber \leftrightarrow (x-A_x)\cdot n_x + (y-A_y)\cdot n_y + (z-A_z)\cdot n_z =0$$
   
   $$\nonumber \leftrightarrow n_x\cdot x+ n_y\cdot y+n_z\cdot z = n_x\cdot A_x + n_y\cdot A_y + n_z\cdot A_z$$
   
   And with $d=A_x\cdot n_x + A_y\cdot n_y + A_z\cdot n_z$ we obtain the normal form of the equation.
   
4. . 
   1. The normal form of the equation is 
      
      $$\nonumber 10\cdot x -5\cdot y+ 20\cdot z =d$$ 
      
      where
      
      $$\nonumber d=10\cdot 2 -5\cdot 4 + 20\cdot (-1) = -20$$ 
   
      so every point $P(x\vert y\vert z)$ with
      
      $$\nonumber 10 x -5 y+ 20 z = -20$$ 
      
      is in the plane.
      
   2. Inserting $P(1\vert 3\vert -2)$ into the equation we get 
    
      $$\nonumber 10\cdot 1 - 5\cdot 3 + 20\cdot (-2) =-45 \neq -20$$
      
      so $P$ is not in the plane.
       



