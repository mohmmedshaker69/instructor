from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Chapter, Lesson
from django.views.generic import UpdateView
from .forms import NewInstructorForm, NewCourseForm, NewChapterForm, NewLessonForm, EditCourseForm
from django.views.decorators.csrf import ensure_csrf_cookie

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html',
                   {'courses': courses})




def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = Chapter.objects.filter(course_id=course_id)
    chapter_count=chapters.count()

    return render(request, 'course_detail.html',
                   {'course': course, 'chapters': chapters, 'chapter_count':chapter_count})



def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    lessons = Lesson.objects.filter(chapter_id=chapter_id)
    lesson_count = lessons.count()  

    return render(request, 'chapter_detail.html', 
                  {'chapter': chapter, 'lessons': lessons, 'lesson_count': lesson_count})



def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id) 
    return render(request, 'lesson_detail.html', 
                  {'lesson': lesson})





def create_instructor(request):
    if request.method == 'POST':
        form = NewInstructorForm(request.POST)
        if form.is_valid():
            instructor = form.save()
            return redirect('instructor_detail', instructor_id=instructor.id)
    else:
        form = NewInstructorForm()
    return render(request, 'create_instructor.html', 
                  {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('create_chapter', course_id=course.id)  
    else:
        form = NewCourseForm()
    return render(request, 'create_course.html', 
                  {'form': form})





def create_chapter(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = NewChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.course = course
            chapter.save()
            return redirect('create_lesson', chapter_id=chapter.id)
    else:
        form = NewChapterForm()
    return render(request, 'create_chapter.html', 
                  {'form': form, 'course': course})



# @ensure_csrf_cookie
# def create_lesson(request, chapter_id):
#     chapter = Chapter.objects.get(id=chapter_id)
#     if request.method == 'POST':
#         form = NewLessonForm(request.POST, request.FILES)
#         if form.is_valid():
#             video = request.FILES['videos/']
#             pdfs=request.FILES['pdfs/']
#             handle_uploaded_file(video)
#             handle_uploaded_file(pdfs)
#             lesson = form.save(commit=False)  
#             lesson.chapter = chapter  
#             lesson.save()
#             return redirect('chapter_detail', chapter_id=chapter_id)
#     else:
#         form = NewLessonForm()
#     return render(request, 'create_lesson.html', 
#                   {'form': form, 'chapter': chapter, 'video':video, 'pdfs':pdfs})


# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def create_lesson(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    
    if request.method == 'POST':
        form = NewLessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.chapter = chapter
            lesson.save()
            return redirect('chapter_detail', chapter_id=chapter_id)
    else:
        form = NewLessonForm()
    
    return render(request, 'create_lesson.html', {'form': form, 'chapter': chapter})

def edit_course(request,course_id):
    course=get_object_or_404(Course, pk=course_id)

    if request.method=='POST':
        form=EditCourseForm(request.POST, instance=course)
        if form.is_valid():
         
            form.save()
            return redirect('create_chapter', course_id=course.id)  
        
    else:

                form=EditCourseForm(instance=course)
                return render(request, 'edit_course.html', {
                    'form':form
                    
    })

def add_chapters(request,  course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = NewChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.course = course
            chapter.save()
            return redirect('chapter_detail', chapter_id=chapter.id )
    else:
        form = NewChapterForm()
    
    return render(request, 'create_chapter.html', {'form': form})
    


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect('course_list')






def lesson_video(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_video.html', {'lesson': lesson})