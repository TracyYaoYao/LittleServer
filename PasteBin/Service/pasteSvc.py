import markdown


class PasteSvcImpl():
    def PasteBin(self, content):
        if not content:
            return content
        return markdown.markdown(content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])

