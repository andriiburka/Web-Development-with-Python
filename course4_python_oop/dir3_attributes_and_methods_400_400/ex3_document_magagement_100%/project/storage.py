# from course4_python_oop.dir3_attributes_and_methods_400_400.ex3_document_magagement_100%.p4_wild_farm.category import Category
# from course4_python_oop.dir3_attributes_and_methods_400_400.ex3_document_magagement_100%.p4_wild_farm.document import Document
# from course4_python_oop.dir3_attributes_and_methods_400_400.ex3_document_magagement_100%.p4_wild_farm.topic import Topic


class Storage:
    categories, documents, topics = [], [], []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [category for category in self.categories if category.id == category_id][0]
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        if topic:
            topic.topic, topic.storage_folder = new_topic, new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [document for document in self.documents if document.id == document_id][0]
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        return [doc for doc in self.documents if doc.id == document_id][0]

    def __repr__(self):
        return "\n".join(d.__repr__() for d in self.documents)



# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize p4_wild_farm")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)



""" EXPECTED
Category 1: work
Topic 1: daily tasks in C:\work_documents
Document 1: finilize p4_wild_farm; category 1, topic 1, tags: urgent, work
Document 1: finilize p4_wild_farm; category 1, topic 1, tags: urgent, work
"""