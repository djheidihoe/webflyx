from typing import Dict, Union


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: Union["HTMLNode", None] = None,
        props: Union[Dict[str, str], None] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    # pyright: ignore[]
    def __repr__(self):
        return self.tag, self.value, self.children, self.props
