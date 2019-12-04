---
redirect_from:
  - "/vectors/section18-lightreflection"
interact_link: content/Vectors/section18_lightreflection.ipynb
kernel_name: python3
has_widgets: false
title: 'Reflection of light'
prev_page:
  url: /Vectors/section16_vectorproduct.html
  title: 'Vector product'
next_page:
  url: /Vectors/section17_furtherProblems.html
  title: 'Further problems'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Reflection of light
---

It is well known from physics that if a ray of light hits a mirror, they ray is reflected in such a way that the angle between the mirror and the incoming ray equals the angle between the mirror and the outgoing ray. This fact makes it possible to actually calculate the outgoing ray. Consider the construction below.





### Exercise
---

A ray of light passes through the point $A(0\vert -2\vert 1)$, and hits a mirror. The reflected light passes through point $B(4\vert 3\vert -5)$. Find the point of reflection $S$ on the mirror, given that the mirror contains the point $P(6 \vert 2\vert 0)$ and has a normal vector $\vec n = \left(\begin{array}{r} 1 \\\  3\\\ 2 \end{array}\right)$.

---

### Solution
---
$A^\prime(4\vert 10 \vert 9)$, $S(4\vert 6\vert 1)$




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

    div.cell {
        width:800px;
        margin-left:16% !important;
        margin-right:auto;
    }
    h1 {
        font-family: "Times New Roman" !important;
    }
    h2 {
        font-family: "Times New Roman" !important;
	      color: green
    }
    h3 {
      font-family: "Times New Roman" !important;
        color: gray
    }
    h4 {
      font-family:  "Times New Roman" !important;
        margin-top:12px;
        margin-bottom: 3px;
    }
    div.text_cell_render {
        font-family: "Times New Roman" !important;
        line-height: 145%;
        font-size: 18px;
        width:800px;
        margin-left:auto;
        margin-right:auto;
    }
    .CodeMirror {
            font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
    }
    .prompt {
        display: None;
    }
    .text_cell_render h5 {
        font-weight: 300;
        /* font-size: 22pt; */
        color: #4057A1;
        font-style: italic;
        margin-bottom: .5em;
        margin-top: 0.5em;
        display: block;
    }

    .warning{
        color: rgb( 240, 20, 20 )
        }

    /* .MathJax {
        font-size: 1em;
    } */

    div.important {
       background-color: #fcf2f2;
       border-color: #dFb5b4;
       border-left: 5px solid #dfb5b4;
       padding: 0.5em;
    }

    /* div.exc {
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
    } */

    li{
       margin: 10px 0;
    }

    ol ol { list-style-type: upper-alpha; important! }
    ol ol ol { list-style-type: lower-alpha; important! }

</style>


<script type="text/x-mathjax-config">
    jax: ["input/TeX","output/HTML-CSS"],
    MathJax.Hub.Config({
                TeX: {
                        extensions: ["AMSmath.js"],
			                  Macros: {
      				                RR: '{\\bf TOM}',
      				                bold: ['\\boldsymbol{#1}',1],
    			              },
                },
		            tex2jax: {
            		    inlineMath: [ ["$","$"], ["\\(","\\)"] ],
                    displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
            		    processEscapes: true,
            		    processEnvironments: true,
        	     },
               MatchWebFonts: {
                 fontCheckDelay: 5 * 1000,
                 fontCheckTimeout: 30 * 1000,
               }
               "HTML-CSS": {
                    /* scale: 130 */
                    styles: {'.MathJax_Display': {"margin": 0}},
                    availableFonts: ["STIX-Web","TeX","Latin-Modern"],
                    preferredFont: "STIX-Web",
                    webFont: "STIX-Web",
                    matchFontHeight: true,
                    /* minScaleAdjust: 55, */
                },
        });
</script>

</div>


</div>
</div>
</div>

