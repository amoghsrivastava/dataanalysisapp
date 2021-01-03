from graphviz import *

# A dot object which we can create a graph in.
dot = Digraph(comment='Task 6 graph')


def _render(view_option='pdf'):
    """
    Renders the current graph called dot and views it to the user.
    Can optionally set the view options
    """
    dot.format = view_option # View as png or pdf
    dot.render('task6-graph.gv', view=True)
    'task6-graph-output/graph.png'


def _clean_graph():
    """Creates a new graph object when called."""
    global dot
    dot = Digraph(comment='Task 6 graph')


def draw_graph(value, input_doc, input_visitor):
    """
    Draw a graph based on a dictionary result returned from get_documents.
    
    The dictionary contains readers as keys and documents they've read in a set as value.

    The function iterates over the dictionary and creates nodes and edges based on the
    pair's key-value relationship in the dictionary.

    If a document is read by a reader, an edge is created between them.

    If the document or reader are input documents, then these are styled differently.
    """
    _clean_graph()  # Clean the graph before writing new's graphs values.
    # Iterate through the values
    for readers, documents in value.items():
        # If reader is empty string, then no need to create a node for it.
        if readers != "":
            # Node attribute denote's the style of the nodes.
            dot.attr("node", shape="box", style="none", color="black")
            if readers == input_visitor:
                # If the reader is the input reader, create a node with the below attribute.
                dot.attr("node", shape="box", style="filled", color=".3 .9 .7")
                # Creates a node.
                dot.node(readers[-4:])
            else:
                # If reader is not the input reader, add it without any styles.
                dot.attr("node", shape="box", style="none", color="black")
                dot.node(readers[-4:])
            for document in documents:
                # Iterate through the set of documents for a reader (document nodes)
                if document == input_doc:
                    # If the document is the input document, create the document node with the below attribute.
                    dot.attr("node", shape="circle", style="filled", color=".3 .9 .7")
                    # Creates an edge between the document node and the reader node.
                    dot.edge(readers[-4:], document[-4:])
                else:
                    # If document is not the input document, add it without any styles.
                    dot.attr("node", shape="circle", style="none", color="black")
                    # Creates an edge between the document node and the reader node.
                    dot.edge(readers[-4:], document[-4:])
        else:
            pass # Do nothing
    # Render the dot graph after created all the nodes and edges.
    _render()