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

# Mini Challenge 3
## Override password change templates
### Acceptance Criteria
1. Override the template for password change (`"registration/password_change_form.html"`).
2. Override the template for password change done (`"registration/password_change_done.html"`)
3. Test, making sure your users can successfully change their password through this feature.
3.1. Make sure the templates are as intuitive as you can make them, offering instructions as needed.
4. Add a link to your navbar that is only displayed to logged in users for password change.


# Mini Challenge 4
## Password Reset Override
### Acceptance Criteria
1. Make the password reset flow look like the rest of your site by overriding all relevant templates.
1.1. Password reset form (email address): "registration/password_reset_form.html"
1.2. Password reset email subject line (txt): subject_"registration/password_reset_subject.txt"
1.3. Password reset email body: email_"registration/password_reset_email.html"
1.4. Password reset done (confirmation): "registration/password_reset_done.html"
1.5. Password reset confirm (new pass form): "registration/password_reset_confirm.html"
1.6. Password reset complete (final confirmation): "registration/password_reset_complete.html"
2. Test your changes, make sure the password reset flow works and matches the look and feel of your site.
3. Make sure you have an anchor tag _somewhere_ so that your users can access this feature.
------------------------------------
{% load i18n %}{% autoescape off %}
{% blocktranslate %}You're receiving this email because you requested a password reset for your user account at {{ site_name }}.{% endblocktranslate %}

{% translate "Please go to the following page and choose a new password:" %}
{% block reset_link %}
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
{% endblock %}
{% translate 'Your username, in case you’ve forgotten:' %} {{ user.get_username }}

{% translate "Thanks for using our site!" %}

{% blocktranslate %}The {{ site_name }} team{% endblocktranslate %}

{% endautoescape %}
----------------------------------
{% load i18n %}{% autoescape off %}
{% blocktranslate %}Password reset on {{ site_name }}{% endblocktranslate %}
{% endautoescape %}