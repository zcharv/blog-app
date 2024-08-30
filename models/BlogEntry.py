class BlogEntry:
    def __init__(self, id, blogId, tagId, title, content, timeCreated, timeEdited):
        self.id = id
        self.blogId = blogId
        self.tagId = tagId
        self.title = title
        self.content = content
        self.timeCreated = timeCreated
        self.timeEdited = timeEdited

    def api_format(self):
        edited = ''
        if self.timeEdited:
            edited = self.timeEdited.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        return {'id': self.id, 'blogId': self.blogId, 'tagId': self.tagId, 'title': self.title, 'content': self.content, 'created': self.timeCreated.strftime('%Y-%m-%dT%H:%M:%S.%f%z'), 'edited': edited}
