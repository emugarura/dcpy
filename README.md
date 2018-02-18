### Descriptions
dcpy is a javascript charting library with native crossfilter support, allowing highly efficient exploration on large multi-dimensional datasets. It leverages d3 to render charts in CSS-friendly SVG format. Charts rendered using dc.js are data driven and reactive and therefore provide instant feedback to user interaction.
dcpy is an easy yet powerful python library for data visualization and analysis.

### Installation
<code>pip install dcpy</code>

### Uses
Open Jupyter notebook and place one by one in cell. Dcpy is recommended to use only in jupyter notebook for analysis only. Note dont try to split 4th cell into multiple cell which may not work.
```
from dcpy import widget
import pandas as pd
```
```
df = pd.DataFrame({"book":["A","B","C","D","E","F","G","H","I","J","K"],"scores":[45,34,54,27,70,25,92,22,40,10,40]})
data = df.to_json(orient="records")
```
```
crossfilter = ["var bookDimension=ndx.dimension(function(d){return d.book;});",
               "var bookscoresGroup=bookDimension.group().reduceSum(function(d){return d.scores;});",
               "var coreCount=ndx.dimension(function(d){\
                   if (d.scores > 80*0.5) {\
                       return 'High';\
                   }\
                   else{\
                       return 'Low';\
                   }\
               });",
               "var coreCountGroup=coreCount.group();",
               "var all = ndx.groupAll();"]

barchartoptions = ["xAxisLabel('book_id')",
                   "yAxisLabel('score')",
                   "width(320)",
                   "height(320)",
                   "x(d3.scale.ordinal())",
                   "xUnits(dc.units.ordinal)",
                   "dimension(bookDimension)",
                   "group(bookscoresGroup)",
                   "colors(['orange'])"]

piechartoptions = ["width(320)",
                   "height(320)",
                   "radius(120)",
                   "innerRadius(40)",
                   "dimension(coreCount)",
                   "group(coreCountGroup)",
                   "label(function(d){\
                       var label = d.key;\
                       if(all.value()){\
                           label += '(' + Math.floor(d.value/all.value()*100)+'%)';\
                       }\
                       return label;\
                   })"]
```
``` 
chart = widget.initiate(data)
chart.prepare(["pie","bar"],crossfilter)
chart.chart("pieChart","pie",piechartoptions)
chart.chart("barChart","bar",barchartoptions)
chart.save()
```
```
chart.output()
```
Output will be like this http://dc-js.github.io/dc.js/examples/adjustable-threshold.html
