from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
graph = pydot.graph_from_dot_data(dot_data.getvalue())
>>> graph.write_pdf("iris.pdf")