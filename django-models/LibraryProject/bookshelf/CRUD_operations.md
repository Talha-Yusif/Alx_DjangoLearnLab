# CREATE BOOK

```python
Book.objects.create(title='1984',author='George Orwell',publication_year=1949)
```
```text
<Book: 1984>
```
# retrieve book
```python
Book.objects.all()
```
```text
<QuerySet [<Book: 1984>]>
```
# update book
```python
book=Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
```
```text
<Book: Nineteen Eighty-Four>
```
# delete book
```python 
book.delete()
```
```text
(1, {'bookshelf.Book': 1})
<QuerySet []>
```