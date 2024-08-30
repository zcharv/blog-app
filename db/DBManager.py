import uuid
import mysql.connector
from models.BlogEntry import BlogEntry
from models.Blog import Blog
from models.Tag import Tag

class DBManager:
    def __init__(self, database='blog', user='root', password='RootPass1@'):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            database=database,
        )
        self.cursor = self.connection.cursor()

    def list_entries(self, blog_id):
        if blog_id is not None:
            query = ('SELECT * FROM blog_entry WHERE blog_id=%s')
            self.cursor.execute(query, (blog_id,))
        else:
            query = ('SELECT * FROM blog_entry')
            self.cursor.execute(query)
        recs = []
        for (id, blogId, tagId, title, content, timeCreated, timeEdited) in self.cursor:
            entry = BlogEntry(id, blogId, tagId, title, content, timeCreated, timeEdited)
            recs.append(entry)
        self.cursor.close()
        self.connection.close()
        return recs

    def list_blogs(self):
        self.cursor.execute('SELECT * FROM blog')
        recs = []
        for (id, name) in self.cursor:
            blog = Blog(id, name)
            recs.append(blog)
        self.cursor.close()
        self.connection.close()
        return recs

    def list_tags(self):
        self.cursor.execute('SELECT * FROM tag')
        recs = []
        for (id, name) in self.cursor:
            tag = Tag(id, name)
            recs.append(tag)
        self.cursor.close()
        self.connection.close()
        return recs

    def get_blog(self, id=''):
        query = ('SELECT * FROM blog WHERE id=%s')
        self.cursor.execute(query, (id,))
        recs = []
        for (id, name) in self.cursor:
            blog = Blog(id, name)
            recs.append(blog)
        self.cursor.close()
        self.connection.close()
        return recs[0]

    def get_entry(self, id=''):
        query = ('SELECT * FROM blog_entry WHERE id=%s')
        self.cursor.execute(query, (id,))
        recs = []
        for (id, blogId, tagId, title, content, timeCreated, timeEdited) in self.cursor:
            entry = BlogEntry(id, blogId, tagId, title, content, timeCreated, timeEdited)
            recs.append(entry)
        self.cursor.close()
        self.connection.close()
        return recs[0]

    def create_blog(self, name='default'):
        new_id = uuid.uuid4()
        query = ('INSERT INTO blog (id, name) VALUES (%s, %s)')
        self.cursor.execute(query, (str(new_id), name))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        return new_id

    def create_entry(self, blog_id='', tag_id='', title='', content=''):
        new_id = uuid.uuid4()
        query = ('INSERT INTO blog_entry (id, blog_id, tag_id, title, content) VALUES (%s, %s, %s, %s, %s)')
        self.cursor.execute(query, (str(new_id), blog_id, tag_id, title, content))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        return new_id

    def update_entry(self, entry_id = '', title='', content=''):
        if title != '':
            query = 'UPDATE blog_entry SET title = %s WHERE id = %s'
        else:
            query = 'UPDATE blog_entry SET content= %s WHERE id = %s'
        self.cursor.execute(query, (title, entry_id))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def delete_entry(self, entry_id = ''):
        query = 'DELETE FROM blog_entry WHERE id = %s'
        self.cursor.execute(query, (entry_id,))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
