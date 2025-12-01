class SoupReplacer:
    """
    A tag replacer that can swap and modify tags during parsing.

    simple replacement:
        SoupReplacer(og_tag="b", alt_tag="blockquote")

    functional replacement:
        SoupReplacer(
            name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name,
            attrs_xformer=lambda tag: {'class': 'new'} if tag.name == 'p' else tag.attrs,
            xformer=lambda tag: tag.attrs.pop('style', None),
        )
    """

    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def get_replacement_tag(self, name):
        """
        Calculate the replacement tag name.
        """
        # name_xformer takes priority
        if self.name_xformer:
            class DummyTag:
                def __init__(self, tag_name):
                    self.name = tag_name

            dummy = DummyTag(name)
            return self.name_xformer(dummy)

        # Check if same tag name first, if so, just return directly
        if self.og_tag == self.alt_tag:
            return name

        if self.og_tag and name == self.og_tag:
            return self.alt_tag

        return name

    def apply_tag_xformers(self, tag):
        """
        Apply all tag xformers (name_xformer, attrs_xformer, xformer)
        """
        if self.name_xformer:
            tag.name = self.name_xformer(tag)

        if self.attrs_xformer:
            tag.attrs = self.attrs_xformer(tag)

        if self.xformer:
            self.xformer(tag)