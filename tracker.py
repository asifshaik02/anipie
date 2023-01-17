import requests

URL = "https://graphql.anilist.co"

def load_query(path):
    with open(path) as f:
        return f.read()

def get_title(d):
    if d['english'] is not None:
        return d['english']
    elif d['romaji'] is not None:
        return d['romaji']
    else:
        return d['native']

def get_img(d):
    pass

def get_shedule():
    url = 'https://subsplease.org/api/?f=schedule&tz=Asia/Calcutta'
    re = requests.get(url=url).json()
    shedule = {}
    for day in re['schedule']:
        shedule[day] = re['schedule'][day]
    return shedule

class User:
    def __init__(self,name) -> None:
        self.uname = name
        self.get_details()
    
    def get_details(self):
        q = load_query('queries/user.graphql')
        var = {'name':self.uname}
        r = requests.post(URL,json={'query':q,'variables':var})

        if r.status_code == 200:
            data = r.json()['data']['User']
            self.id = data['id']
            self.image = data['avatar']['medium']
            self.banner = data['bannerImage']
            self.animeWatched = data['statistics']['anime']['count']
            self.episodesWatched = data['statistics']['anime']['episodesWatched']
            self.minutesWatched = data['statistics']['anime']['minutesWatched']
            self.animeMeanScore = data['statistics']['anime']['meanScore']
            self.mangaRead = data['statistics']['manga']['count']
            self.volumesRead = data['statistics']['manga']['volumesRead']
            self.chaptersRead = data['statistics']['manga']['chaptersRead']
            self.mangaMeanScore = data['statistics']['manga']['meanScore']
            self.favAnime = []
            for fav in data['favourites']['anime']['nodes']:
                self.favAnime.append({'id':fav['id'],'name':fav['title']['english']})

            self.favManga = []
            for fav in data['favourites']['manga']['nodes']:
                self.favManga.append({'id':fav['id'],'name':fav['title']['english']})
            
            self.favCharacter = []
            for fav in data['favourites']['characters']['nodes']:
                self.favCharacter.append({'id':fav['id'],'name':fav['name']['full']})
        else:
            print(r.status_code)
    
    def get_watch_list(self,type,status,page=1):
        q = load_query('queries/watchlist.graphql')
        var = {
            'name':self.uname,
            'type':type,
            'status':status,
            'page':page
        }
        r = requests.post(URL,json={'query':q,'variables':var})
        d = {}

        if r.status_code == 200:
            data = r.json()['data']['Page']
            d['type'] = type
            d['currentPage'] = data['pageInfo']['currentPage']
            d['hasNext'] = data['pageInfo']['hasNextPage']
            d['list'] = []

            for med in data['mediaList']:
                name = get_title(med['media']['title'])
                
                if med['media']['episodes'] is None:
                    med['media']['episodes'] = '?'

                d['list'].append({
                    'id' : med['media']['id'],
                    'name' : name,
                    'episodes' : med['media']['episodes'],
                    'progress' : med['progress'],
                    'score' : med['score']
                })
        else:
            print(r.status_code)
        
        return d
    
    def get_current_anime(self,page=1):
        return self.get_watch_list('ANIME','CURRENT',page)

    def get_paused_anime(self,page=1):
        return self.get_watch_list('ANIME','PAUSED',page)
    
    def get_dropped_anime(self,page=1):
        return self.get_watch_list('ANIME','DROPPED',page)
    
    def get_planning_anime(self,page=1):
        return self.get_watch_list('ANIME','PLANNING',page)
    
    def get_completed_anime(self,page=1):
        return self.get_watch_list('ANIME','COMPLETED',page)

    def get_currently_manga(self,page=1):
        return self.get_watch_list('MANGA','CURRENT',page)

    def get_paused_manga(self,page=1):
        return self.get_watch_list('MANGA','PAUSED',page)
    
    def get_dropped_manga(self,page=1):
        return self.get_watch_list('MANGA','DROPPED',page)
    
    def get_planning_manga(self,page=1):
        return self.get_watch_list('MANGA','PLANNING',page)
    
    def get_completed_manga(self,page=1):
        return self.get_watch_list('MANGA','COMPLETED',page)

class Anime:
    def __init__(self,id,name=None) -> None:
        self.id = id
        self.name = name
        self.get_details()

        # replace None values with empty string
        # for k,v in self.__dict__.items():
        #     if v == None:
        #         self.__dict__[k] = ''
    
    def get_details(self):
        q = load_query('queries/anime.graphql')

        var = {
            'id':self.id
        }

        r = requests.post(URL, json={'query': q, 'variables': var})
        if r.status_code == 200:
            data = r.json()['data']['Media']
            self.name = get_title(data['title'])
            self.episodes = data['episodes']
            self.duration = data['duration']
            self.descrption = data['description']
            self.format = data['format']
            self.score = data['averageScore']
            self.image = data['coverImage']['medium']
            self.genres = data['genres']
            self.season = data['season']
            self.year = data['seasonYear']
            self.status = data['status']
            self.tags = []
            for i in data['tags']:
                self.tags.append(i['name'])
            
            self.characters = []
            for chr in data['characters']['nodes']:
                self.characters.append({
                    'id' : chr['id'],
                    'name' : chr['name']['full'],
                    'image' : chr['image']['medium']
                })
        else:
            print(r.status_code)

class Manga:
    def __init__(self,id,name=None) -> None:
        self.id = id
        self.name = name
        self.get_details()

        # replace None values with empty string
        # for k,v in self.__dict__.items():
        #     if v == None:
        #         self.__dict__[k] = ''
    
    def get_details(self):
        cou = {
            'KR' : 'South Korea',
            'CN' : 'China',
            'JP' : 'Japan',
            'TW' : 'Taiwan'
        }
        q = load_query('queries/manga.graphql')
        var = {
            'id' : self.id
        }
        r = requests.post(URL, json={'query': q, 'variables': var})
        if r.status_code == 200:
            data = r.json()['data']['Media']
            self.name = get_title(data['title'])
            self.descrption = data['description']
            self.format = data['format']
            self.score = data['averageScore']
            self.image = data['coverImage']['medium']
            self.genres = data['genres']
            self.status = data['status']
            self.volumes = data['volumes']
            self.chapters = data['chapters']
            self.country = cou[data['countryOfOrigin']]
            self.tags = []
            for i in data['tags']:
                self.tags.append(i['name'])
            
            self.characters = []
            for chr in data['characters']['nodes']:
                self.characters.append({
                    'id' : chr['id'],
                    'name' : chr['name']['full'],
                    'image' : chr['image']['medium']
                })
        else:
            print(r.status_code)

class Character:
    def __init__(self,id) -> None:
        self.id = id
        self.get_details()

        # replace None values with empty string
        # for k,v in self.__dict__.items():
        #     if v == None:
        #         self.__dict__[k] = ''
    
    def get_details(self):
        q = load_query('queries/character.graphql')

        var = {
            'id' : self.id
        }
        r = requests.post(URL,json={'query': q, 'variables': var})

        if r.status_code == 200:
            data = r.json()['data']['Character']
            self.name = data['name']['full']
            self.age = data['age']
            self.gender = data['gender']
            self.descrption = data['description']
            self.image = data['image']['medium']
            self.media = []

            for med in data['media']['nodes']:
                self.media.append({
                    'id' : med['id'],
                    'name' : get_title(med['title']),
                    'image' : med['coverImage']['medium']
                })
        else:
            print(r.status_code)

class MyAnimeList:
    def __init__(self) -> None:
        pass

class Anilist:
    def __init__(self, uname=None) -> None:
        self.uname = uname
    
    def searchMedia(self,query,page=1):
        q = load_query('queries/searchMedia.graphql')
        var = {
            'query':query,
            'page':page,
        }

        r = requests.post(URL,json={'query':q,'variables':var})
        d = {}
        if r.status_code == 200:
            data = r.json()['data']['Page']
            d['currentPage'] = data['pageInfo']['currentPage']
            d['hasNext'] = data['pageInfo']['hasNextPage']
            d['lastPage'] = data['pageInfo']['lastPage']
            d['results'] = []


            for res in data['media']:
                title = res['title']
                if title['english']:
                    name = title['english']
                elif title['romaji']:
                    name = title['romaji']
                else:
                    name = title['native']
                d['results'].append({
                    'id':res['id'],
                    'name' :name,
                    'type' :res['format']
                })
        else:
            print(r.status_code)
        
        return d




# obj = User('fukun02')
# print(obj.search('jujutsu'))
# obj.get_details()
# print(obj.__dict__)