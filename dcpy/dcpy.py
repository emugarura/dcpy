from IPython.core.display import display,HTML
class dcpy:
    def __init__(self, source):
        self.source = source
        self.html = []
        self.html.append("""<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="../resources/dc.min.css"><link rel="stylesheet" type="text/css" href="../resources/bootstrap.min.css"><script type="text/javascript" src="../resources/d3.min.js"></script><script type="text/javascript" src="../resources/crossfilter.min.js"></script><script type="text/javascript" src="../resources/dc.min.js"></script></head><body>""")
    
    def prepare(self,identifier,crossfilter):
        for element in identifier:
            self.html.append("<div id='{}'></div>".format(element))
        self.html.append("<script>")
        self.html.append("var data={};".format(self.source))
        self.html.append("var ndx=crossfilter(data);")
        self.html.append("".join(crossfilter))
    
    def chart(self,name,identifier,options):
        self.html.append("dc.{}('#{}').{};".format(name,identifier,".".join(options)))
    
    def save(self):
        self.html.append("dc.renderAll()")
        self.html.append("</script></body></html>")
        fp = open("../data/dcpy.html", "w")
        fp.write("".join(self.html))
        fp.close()
    
    def output(self,width=700,height=350):
        display(HTML('<iframe frameborder=0 src="../data/dcpy.html" width="{}" height="{}"></iframe>'.format(width,height)))