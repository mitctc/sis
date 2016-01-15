from django.shortcuts import render,render_to_response
from courses.forms import CourseForm, TopicForm
from courses.models import Course
# Create your views here.
def index(request): #Define our function, accept a request
 
    items = Course.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render_to_response('courses\index.html', {'items': items}) #Responds with passing the object items (contains info from the DB) to the template index.html


	
	
	
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

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
        form = CourseForm()
    context_dict = {'form': form}

    # Render the response and send it back!
    return render(request, 'courses/add_course.html', context_dict)
	