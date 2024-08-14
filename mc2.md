# Mini Challenge 2
## Full CRUD(S) support for Post
### Acceptance Criteria
1. Users should be able to create new posts.
2. Users should be able to view a detail page for a specific post (via its ID).
3. Users should be able to edit an existing (specific) post (via its ID).
4. Users should be able to delete an existing (specific) post (via its ID).
5. Users should be able to see a list of posts on the platform (list view).
### Note
To power the edit or update feature, you will need to import and extend UpdateView. You should expose all fields except the author field on this.
To power the delete feature, you will need to import and extend DeleteView. DeleteView does not require the fields attribute, but will require a success_url.
### Example of DeleteView
```
from django.urls import reverse_lazy
...
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    success_url = reverse_lazy("list")
```