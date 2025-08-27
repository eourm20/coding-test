from collections import Counter, defaultdict

def solution(genres, plays):
    best_g = ""
    best_v = 0
    genre_dict = defaultdict(int)
    genre_song = defaultdict(list)
    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        genre_song[genres[i]].append((plays[i], i))
    print(genre_song)
    best_album = []
    
    sorted_genres = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_genres)
    for genre, _ in sorted_genres:
        genre_song[genre].sort(key=lambda x: (-x[0], x[1])) # 재생횟수 같으면 인덱스 순으로 출력
        print(genre_song)
        # 장르별로 최대 두 개 노래를 선택
        best_album.extend([song[1] for song in genre_song[genre][:2]])
    
    return best_album