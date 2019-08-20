---
redirect_from:
  - "/vectors/section2-magnitude"
interact_link: content/Vectors/section2_magnitude.ipynb
kernel_name: python3
has_widgets: false
title: 'The magnitude of a vector'
prev_page:
  url: /Vectors/section1_points_and_vectors.html
  title: 'Points and vectors'
next_page:
  url: /Vectors/section3_special_vectors.html
  title: 'Three special vectors'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## The magnitude of a vector
---

The __magnitude__ of a vector $\vec u$, written $|\vec{u}|$, is the *length of the arrow* that this vector represents. 

<img src="./pics/length.png" width="20%" align="center">

If the vector has the components $$\vec{u} =\left(\begin{array}{r} x\\y\\z \end{array}\right)$$ we can apply the theorem of Pythagoras twice to find the following formula for the magnitude: $$\boxed{|\vec u| = \sqrt{x²+y²+z²}}$$ A more detailed derivation of this formula is given in the figure below, for the vector with the components 
$$\vec{u} =\left(\begin{array}{r} 3\\4\\5 \end{array}\right)$$ In this case, the magnitude is $$|\vec{u}| = \sqrt{3²+4²+5²}=\sqrt{50}=7.071...$$

<img src="./pics/magnitude.png" width="70%" align="center">



<div class="exc">Exercise</div>

1. Determine the magnitude of the vectors $\vec{w}=\left(\begin{array}{r} -1\\1\\-1 \end{array}\right)\,\,$ and $\vec{s}=\left(\begin{array}{r} 1.5\\0\\-2 \end{array}\right)$

2. Vector $\vec{u}$ has the $x$-component $2$ and the $y$-component $-3$. Determine the $z$-component such that the magnitude of the vector is $32$ .

3. Determine the distance between the points $A(2|1|0)\,$  and $B(-7|2|5 )$ . 



<div class="sol">Solutions</div>

1. $|\vec{w}|=\sqrt{3}, |\vec{s}|=\sqrt{6.25}=2.5$

2. $|\vec{w}|=\sqrt{2^2+(-3)^2+z^2}=32 \rightarrow 2^2+(-3)^2+z^2=32^2=1024 \rightarrow z=\sqrt{1011}=31.796...$

3. The arrow from $A$ to $B$ has the components $\overrightarrow{AB}=\left(\begin{array}{r} -9\\1\\5 \end{array}\right)\,$ . The distance between $A$ and $B$ is the length of this arrow: $|\overrightarrow{AB}|=\sqrt{(-9)^2+1^2+5^2}=\sqrt{107}\,$.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#needs to be in the last cell for css styling
from IPython.core.display import HTML
def css_styling():
    styles = open("../styles/custom.css", "r").read()
    return HTML(styles)
css_styling()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<style>
    @font-face {
        font-family: "Computer Modern";
        src: url('http://9dbb143991406a7c655e-aa5fcb0a5a4ec34cff238a2d56ca4144.r56.cf5.rackcdn.com/cmunss.otf');
    }
    @font-face {
        font-family: "Computer Modern";
        font-weight: bold;
        src: url('http://9dbb143991406a7c655e-aa5fcb0a5a4ec34cff238a2d56ca4144.r56.cf5.rackcdn.com/cmunsx.otf');
    }
    @font-face {
        font-family: "Computer Modern";
        font-style: oblique;
        src: url('http://9dbb143991406a7c655e-aa5fcb0a5a4ec34cff238a2d56ca4144.r56.cf5.rackcdn.com/cmunsi.otf');
    }
    @font-face {
        font-family: "Computer Modern";
        font-weight: bold;
        font-style: oblique;
        src: url('http://9dbb143991406a7c655e-aa5fcb0a5a4ec34cff238a2d56ca4144.r56.cf5.rackcdn.com/cmunso.otf');
    }
    div.cell{
        width:800px;
        margin-left:16% !important;
        margin-right:auto;
    }
    h1 {
        font-family: Helvetica, serif;
    }
    h2 {
        font-family: Helvetica, sans-serif;
	color: blue
    }
    h3 {
        
	color: gray
    }
    h4{
        margin-top:12px;
        margin-bottom: 3px;
       }
    div.text_cell_render{
        font-family: Computer Modern, serif;
        line-height: 145%;
        font-size: 130%;
        width:800px;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror{
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
    .prompt{
        display: None;
    }
    .text_cell_render h5 {
        font-weight: 300;
        font-size: 22pt;
        color: #4057A1;
        font-style: italic;
        margin-bottom: .5em;
        margin-top: 0.5em;
        display: block;
    }
    
    .warning{
        color: rgb( 240, 20, 20 )
        }
  
    .MathJax {
        font-size: 0.9em;
    }

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

    div.sol {    
       background-color: lightgray;
       border-color: lightgray;
       border-left: 5px solid gray;
       padding: 0.5em;
    }

</style>
<script>
    MathJax.Hub.Config({
                        TeX: {
                           extensions: ["AMSmath.js"]
                           },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                },
                displayAlign: 'center', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 4}}
                },
        });
</script>

</div>


</div>
</div>
</div>

