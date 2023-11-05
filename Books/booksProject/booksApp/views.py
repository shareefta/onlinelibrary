from django.shortcuts import render
# Create your views here.


def library(request):
    books_library = {
        'books': [
            {
                'name': '.Net',
                'author': 'Author',
                'image': '.net.jpeg'
            },
            {
                'name': 'C#',
                'author': 'Mark J. Price',
                'image': 'cSharp.jpeg'
            },
            {
                'name': 'Python',
                'author': 'Author',
                'image': 'python.jpeg'
            },
            {
                'name': 'Python with SQL',
                'author': 'Tony',
                'image': 'sql.jpeg'
            },
            {
                'name': 'AI & Robotics',
                'author': 'Stem',
                'image': 'robotic.jpeg'
            },
            {
                'name': 'Web Designing',
                'author': 'Jennifer Robbins',
                'image': 'web.jpeg'
            }
        ]}
    return render(request, 'home.html', books_library)


def content(request):
    return render(request, 'content.html')
