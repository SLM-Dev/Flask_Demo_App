set flask_env=development

built in type error good for debugging


render template so make a directory 
making folder called templated then .html
 #


 flask comes with a template engine called ginga 2 seperate poything prjoect

 refernece vaibrles use ginga h1{{ title}}</h1>
 shows dynaic value the variable


 Note

 looping over data with template 





 stuff explain 

<!-- <h1>Testing does this render template </h1> -->
<!-- tells ginga template engine anythig goes in side % % python logic implmenetion -->

<h1>{{ title }}</h1>
<!-- inside loop can refernce items inside of it example   tag-->





<!-- starting percent {% begiining %} and other logic need closing statement -->

<!-- end of statement {% endfor %} -->
<!-- result loops over all elements in the list out put html element  -->
{% for item in states_to_visit  %}
<p>{item}}</p>
{% endfor %}

