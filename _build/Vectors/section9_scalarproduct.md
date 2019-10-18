---
redirect_from:
  - "/vectors/section9-scalarproduct"
interact_link: content/Vectors/section9_scalarproduct.ipynb
kernel_name: python3
has_widgets: false
title: 'The intersection of straight lines'
prev_page:
  url: /Vectors/section8_intersectionStraightLines.html
  title: 'The intersection of straight lines'
next_page:
  url: /Vectors/section10_angles.html
  title: 'The intersection of straight lines'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


We already now one kind of product involving vectors. It is the multiplication of a scalar with a vector, and the result is a new (stretched) vector: 

$$c\cdot \vec a = c\cdot \left(\begin{array}{r} a_x\\\ a_y\\\ a_z \end{array}\right) = \left(\begin{array}{r} c\cdot a_x\\\ c\cdot a_y\\\ c\cdot a_z \end{array}\right)$$

Now we introduce a multiplication between two vectors, and the result is a scalar.

## The scalar product of two vectors
---
Consider two vectors $\vec{a}=\left(\begin{array}{r} a_x\\\ a_y\\\ a_z \end{array}\right)$ and $\vec{b}=\left(\begin{array}{r} b_x\\\ b_y\\\ b_z \end{array}\right)$. The __scalar product__ of $\vec{a}$ and $\vec{b}$, written $\vec{a} \bullet \vec{b}$, is defined by multiplying component-wise, and then adding the three resulting products to form a single number: 

$$\boxed{\vec{a} \bullet \vec{b}=a_x b_x+a_y b_y+a_z b_z}$$ 

So we take two vectors (six numbers), and by forming the scalar product we obtain __one__ number! 
	
### Example
---
- $\left(\begin{array}{r} 3\\\ -4\\\ 1 \end{array}\right) \bullet \left(\begin{array}{r} 2\\\ 5\\\ -3 \end{array}\right)=3\cdot 2 + (-4)\cdot 5 + 1\cdot (-3)=-17$

- $\left(\begin{array}{r} 3\\\ -4\\\ 1 \end{array}\right) \bullet \left(\begin{array}{r} 2\\\ 5\\\ 14 \end{array}\right)=3\cdot 2 + (-4)\cdot 5 + 1\cdot 14=0$
---

Note that in the second example we have $\vec{a}\neq 0$ and $\vec{b}\neq 0$ but $\vec{a}\bullet \vec{b} =0$. This is a key difference to the normal product between two numbers. If we have two numbers $a\neq 0$ and $b\neq 0$ it always follows $a\cdot b\neq 0$. However, many other properties are similar, e.g.

1. $\vec{a}\bullet\vec{a} = |\vec{a}|^2 \geq 0$ (squares are not negative)
2. $\vec{a}\bullet\vec{b} = \vec{b}\bullet\vec{a}$ (product is commutative)
3. $(c \cdot \vec{a})\bullet \vec{b} =c\cdot (\vec{a}\bullet \vec{b})$ where $c$ is s scalar (product is associative, that is, you can group)
4. $\vec{a}\bullet (\vec{b}+\vec{c}) = (\vec{a}\bullet\vec{c}) + (\vec{b}\bullet\vec{c})$ (product is distributive, that is, the product distributes over the sum)



## Exercise
---

Prove the properties 1-4-above.



## Solution
---

1. $\vec{a}\bullet\vec{a} = a_x a_x+a_y a_y+a_z a_z =a_x^2+ a_y^2 +a_z^2= |\vec{a}|^2$
2. $\vec{a}\bullet\vec{b} = a_x b_x+a_y b_y+a_z b_z = b_x a_x + b_y a_y+b_z a_z = \vec{b}\bullet\vec{a}$
3. $(c \vec{a})\bullet \vec{b} =(c a_x)\cdot b_x+ (c a_y)\cdot  b_y+ (c a_z)\cdot b_z = c\cdot  (a_x b_x+ a_y b_y+ a_z b_z) = c\cdot (\vec{a}\bullet \vec{b})$

4. We have 

    $$\begin{array}{rl} \vec{a}\bullet (\vec{b} + \vec{c}) &=& a_x  (b_x+ c_x) + a_y (b_y+ c_y) + a_z (b_z+ c_z)\\\ 
		& = & a_x b_x + a_x c_x + a_y b_y+ a_y c_y+ a_z b_z + a_z c_z \\\
		& = & (a_x b_x+ a_y b_y + a_z b_z) +  (a_x c_x +  a_y c_y +  a_z c_z)\\\
		& = & (\vec{a}\bullet\vec{b}) + (\vec{a}\bullet\vec{c})
		\end{array}$$



