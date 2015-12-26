from django.shortcuts import render
from courses.forms import CourseForm, TopicForm

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    #category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': "course list"}

    # Render the response and send it back!
    return render(request, 'courses/index.html', context_dict)
	
	
	
def add_course(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()
    context_dict = {'form': form}

    # Render the response and send it back!
    return render(request, 'courses/add_course.html', context_dict)
	