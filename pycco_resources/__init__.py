import pycco_resources.classic as classic
import pycco_resources.linear as linear

themes = {
  'classic': (classic.css, classic.pycco_template),
  'linear': (linear.css, linear.pycco_template),
}

pycco_template = classic.pycco_template
css = classic.css
