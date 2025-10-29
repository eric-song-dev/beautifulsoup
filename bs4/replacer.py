class SoupReplacer:
    """
    A simple tag replacer that swaps one tag name for another.
    """
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def get_replacement_tag(self, name):
        if name == self.og_tag:
            return self.alt_tag
        return name