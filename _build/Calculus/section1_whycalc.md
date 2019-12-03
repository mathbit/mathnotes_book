---
redirect_from:
  - "/calculus/section1-whycalc"
interact_link: content/Calculus/section1_whycalc.ipynb
kernel_name: python3
has_widgets: false
title: 'Why calculus?'
prev_page:
  url: /index.html
  title: 'Calculus'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Why calculus?
---

Calculus is a way of solving complicated problems: _"Divide the problem into little parts (differentiation), solve problem for each little part, which is easier, then assemble the parts to solve the complex problem (integration)."_

We start the discussionn with _differential_ calculus, followed by _integral_ calculus. But before we do this, let us give an example of how the strategy of dividing and assembling can solve a problem.


### Exercise
---

We know that the circumference of a circle of radius $r$ is $2\pi r$. Use this information to infer the area of a circle of radius $r$. _Hint: divide the circle into smaller and smaller segments, which you arrange in a clever way._ 

---

### Example

Johannes Kepler studied the planets moving around our sun. He found that each planet moves along an ellipse, but the speed varied  the same speed. Closer to the sun the speed was higher than if far away. What was the rule 



, and that a planet covers equal area in equal time intervals. In order to find this law, he had to determine the area bounded by _curved lines_.









<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%pylab inline

plt.xkcd()  # Yes...
plt.plot(sin(linspace(0, 10)))
plt.title('Whoo Hoo!!!')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Populating the interactive namespace from numpy and matplotlib
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
Text(0.5, 1.0, 'Whoo Hoo!!!')
```


</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../images/Calculus/section1_whycalc_1_2.png)

</div>
</div>
</div>



