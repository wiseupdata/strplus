from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class MonokaiStyle(Style):
    """
    This style mimics the Monokai color scheme.
    """

    background_color = "#272822"
    highlight_color = "#49483e"

    styles = {
        Comment: 'italic #75715e',
        Keyword: 'bold #f92672',
        Operator: '#f92672',
        String: '#e6db74',
        Number: '#ae81ff',
        Name.Function: '#a6e22e',
        Name.Class: 'bold #a6e22e',
        Name.Namespace: 'bold #a6e22e',
        Name.Variable: '#a6e22e',
        Name.Constant: '#a6e22e',
        Generic.Heading: 'bold #66d9ef',
        Generic.Subheading: 'bold #a6e22e',
        Generic.Emph: 'italic #fd971f',
        Error: 'border:#f00',
    }