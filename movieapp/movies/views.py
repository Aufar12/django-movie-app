from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Movie, Genre
import json, os

def movies(request):
    all_movies = Movie.objects.prefetch_related('genre').all()
    template = loader.get_template('all_movies.html')
    context = {
        'movies': all_movies,
    }
    
    return HttpResponse(template.render(context, request))

def movie_detail(request, id):
    movie = get_object_or_404(Movie.objects.prefetch_related('genre'), id=id)
    return render(request, 'movie_detail.html', {'movie': movie})

def populate_movies(request):
    if request.method == 'GET':
        try:
            json_path = os.path.join(os.path.dirname(__file__), '..', 'movies.json')
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            inserted = 0
            skipped = 0

            for entry in data:
                entry['genre'] = [g.strip(" '\"") for g in entry['genre'][0].split(",")]
                    
                movie_content = {
                        'description': entry['description'],
                        'imgPath': entry['imgPath'],
                        'duration': entry['duration'],
                        'language': entry['language'],
                        'mpaa_type': entry['mpaaRating']['type'],
                        'mpaa_label': entry['mpaaRating']['label'],
                        'userRating': float(entry['userRating']),
                        'genres' : entry['genre']
                }
                
                movie, created = Movie.objects.get_or_create(
                    name=entry['name'],
                    defaults=movie_content
                )
                
                for genre_name in entry['genre']:
                    genre_obj, _ = Genre.objects.get_or_create(name=genre_name)
                    movie.genre.add(genre_obj)
                    
                movie.save()
     
                if created:
                    inserted += 1
                else:
                    skipped += 1

            return JsonResponse({'status': 'success', 'inserted': inserted, 'skipped': skipped})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def debug_movie_genres(request):
    data = []

    for movie in Movie.objects.all():
        genres = list(movie.genre.values_list('name', flat=True))
        data.append({
            "name": movie.name,
            "genres": genres
        })

    return JsonResponse(data, safe=False)