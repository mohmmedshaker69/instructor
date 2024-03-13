from django import forms

from .models import Course, Chapter, Lesson, Instructor

INPUT_CLASSES='w-full py-4 px-6 rounde-xl border'

class NewInstructorForm(forms.ModelForm):
    class Meta:
        model=Instructor
        fields=('category', 'name', 'phone_number', 'email', 'courses_teched_before' ,'description')

        widgets={
            'category':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
        'name':forms.TextInput(attrs={
        'class': INPUT_CLASSES
        }),
        'phone_number':forms.TextInput(attrs={
        'class': INPUT_CLASSES
        }),
        'email':forms.TextInput(attrs={
        'class': INPUT_CLASSES
        }),
         'description':forms.Textarea(attrs={
        'class': INPUT_CLASSES
        }),
         'courses_teched_before':forms.Select(attrs={
        'class': INPUT_CLASSES
        }),
        
        }


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('teached_by', 'category', 'name','description')

        widgets={

        'teached_by':forms.Select(attrs={
            'class':INPUT_CLASSES
        }),

        'category':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
        'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),

        }

class NewChapterForm(forms.ModelForm):
    class Meta:
        model=Chapter
        fields = ( 'name' ,)

        widgets={

        
        'name':forms.TextInput(attrs={
        'class': INPUT_CLASSES
        }),


        }

class NewLessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=( 'name', 'video', 'pdf')

        widgets={
        
        'name':forms.TextInput(attrs={
        'class': INPUT_CLASSES
        }),
        'video': forms.FileInput(attrs={
            'class': INPUT_CLASSES
        }),  
        'pdf': forms.FileInput(attrs={
            'class': INPUT_CLASSES
        }),


        }

# class AddLessonForm(forms.ModelForm):
#     class Meta:
#         model=Lesson
#         fields=( 'name', 'video', 'pdf')

#         widgets={
        
#         'name':forms.TextInput(attrs={
#         'class': INPUT_CLASSES
#         }),
#         'video': forms.FileInput(attrs={
#             'class': INPUT_CLASSES
#         }),  
#         'pdf': forms.FileInput(attrs={
#             'class': INPUT_CLASSES
#         }),





        # }



class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('teached_by', 'name','description')

        widgets={

        'teached_by':forms.Select(attrs={
            'class':INPUT_CLASSES
        }),

    
        'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),

        }