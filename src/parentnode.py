from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super()

        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        children_template = ""
        for child in self.children:
            children_template = children_template + child.to_html()
        if not self.props:
            return f"<{self.tag}>{children_template}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{children_template}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

