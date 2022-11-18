def Indent(string: str, amount: int):
    indent = "-" * amount
    indent += "> "
    indent += string

    return indent

