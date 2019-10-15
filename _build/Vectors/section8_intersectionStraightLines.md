---
redirect_from:
  - "/vectors/section8-intersectionstraightlines"
interact_link: content/Vectors/section8_intersectionStraightLines.ipynb
kernel_name: python3
has_widgets: false
title: 'The intersection of straight lines'
prev_page:
  url: /Vectors/section7_furtherProblems.html
  title: 'Further problems'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


Consider two straight lines $g$ and $h$ in a three dimensional space. Assume that $g$ passes through point $A$ and has direction vector $\vec v$, and $h$ passes through point $B$ and has direction vector $\vec w$. The two lines can have the following position relative to each other:


## The straight lines  *intersect* at one point $S$:
---

<img src="./pics/line2.png" width="50%" align="center">

From all the points in the 3-d space, the following is only true for the intersection point $S$:
    
$$\nonumber\boxed{\overrightarrow{AS} \parallel \vec v \mbox{ and } \overrightarrow{BS} \parallel \vec w}$$ 
    
Again, we can also rephrase this as follows (compare with the previous section):
    
$$\nonumber\boxed{\mbox{there is a $c$ with } S=A+c\cdot \vec v \mbox{ and a $d$ with } S=B+d\cdot \vec w}$$





## The straight lines are *parallel*
---

They are parallel, if they either never intersect or if they form the same lines. 

<img src="./pics/line1.png" width="70%" align="center">

From the figure it follows that $g$ and $h$ are parallel if
    
$$\nonumber\boxed{\vec v\parallel \vec w}$$ 

And they form the same line if, and only if
    
$$\nonumber\boxed{\overrightarrow{AB} \parallel \vec v \mbox{ or } \overrightarrow{AB} \parallel \vec w}$$ 
    



    
##  The straight lines are  *skew*
---

Two straight lines are said to be __skew__, if they neither intersect nor are they parallel. Obviousely this is not possible in a 2d-space, we need the third dimension for this.

<img src="./pics/line3.png" width="70%" align="center">

To find out if the two lines are skew or do intersect, we first make verify that they are not parallel. Then we simply try to find the point of intersection. If there is one, we know they intersect. If there is no such point  




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#needs to be in the last cell for css styling
from IPython.core.display import HTML
def css_styling():
    styles = open("../assets/custom/custom.css", "r").read()
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
        font-size: 1em;
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

    li{
       margin: 10px 0;
    }

    ol ol { list-style-type: upper-alpha; important! }
    ol ol ol { list-style-type: lower-alpha; important! }

</style>
<script>
    MathJax.Hub.Config({
                TeX: {
                        extensions: ["AMSmath.js"],
			Macros: {
      				RR: '{\\bf TOM}',                // a simple string replacement
      				bold: ['\\boldsymbol{#1}',1]   // this macro has one parameter
    			}
                },
		tex2jax: {
            		inlineMath: [ ["$","$"], ["\\(","\\)"] ],
                        displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
            		processEscapes: true,
            		processEnvironments: true
        	},
                "HTML-CSS": {
                    styles: {'.MathJax_Display': {"margin": 0}},
                    availableFonts: ["TeX","STIX-Web","Neo-Euler"],
                    preferredFont: "Neo-Euler",
                },
        });
</script>

</div>


</div>
</div>
</div>

