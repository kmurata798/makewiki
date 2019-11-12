from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageListView(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    # context_object_name = "pages"
    # template_name = "page.html"

    def get(self, request):
        """ Returns a list of wiki pages. """
        # pages = self.model.objects.all()
        pages = self.get_queryset().all()
        context = {"list_of_pages": pages}
        print(context)
        return render(request, 'wiki/list.html', context)
        


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what thos accomplishes.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        # pages = self.get_queryset().all()
        detail = self.get_queryset().get(slug__iexact=slug)
        # page = self.model.objects.get(slug=slug)
        return render(request, 'wiki/page.html', {'detail': detail})

    def post(self, request, slug):
        pass
