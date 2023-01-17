# Welcome to Anipie

This is an REST-API made using [Anilist graphql API](https://anilist.gitbook.io/anilist-apiv2-docs/)

# Endpoints

A list of Endpoints provided:
**Base url**: `http://anipie.glitch.me`

## User

**Endpoint** : `/<username>`

**Output**: 
```
    - id :Int
    - uname :String
    - image :Link
    - animeWatched :Int
    - minutesWatched :Int
    - animeMeanScore :Float
    - episodesWatched :Int
    - mangaRead :Int
    - volumesRead :Int
    - chaptersRead :Int
    - mangaMeanScore :Float
    - favAnime :[{id :Int, name :String}]
    - favManga :[{id :Int, name :String}]
    - favcharacter :[{id :Int, name :String}]
```

**Note**:
```
    username :user name of the anilist account
```

## watchlist

**Endpoint** : `/<username>/<type>/<status>/<page>`

**Output**:
```
    - currentPage :Int
    - hasNext :Bool
    - type :String
    - list :[{episodes: String, id: Int, name: String, progress: Int, score :Int}]
```

**Note**:

```
    username: user name of the anilist account
    type: "anime" or "manga"
    status: "current" or "paused" or "dropped" or "planning" or "completed"
    page: int
```

## Anime

**Endpoint**: `/anime/<id>`

**Output**:
```
    - id :Int
    - name :String
    - image :link
    - descrption :String
    - format :String //takes only ["TV","TV_SHORT","MOVIE","SPECIAL","OVA","ONA","MUSIC","MANGA","NOVEL","ONE_SHOT"]
    - genres :[String]
    - tags :[String]
    - score :Int
    - status :String //takes only ["FINISHED","RELEASING","NOT_YET_RELEASED","CANCELLED","HIATUS"]
    - episodes :Int
    - duration :Int
    - season :String //takes only ["WINTER","SPRING","SUMMER","FALL"]
    - year :int
    - characters :[{id :Int, image :Link, name :String}]
```

**Note**:
```
    id: id of the anime assigned by anilist
```

## Manga

**Endpoint**: `/manga/<id>`

**Output**:
```
    - id :Int
    - name :String
    - image :link
    - descrption :String
    - format :String //takes only ["TV","TV_SHORT","MOVIE","SPECIAL","OVA","ONA","MUSIC","MANGA","NOVEL","ONE_SHOT"]
    - genres :[String]
    - tags :[String]
    - score :Int
    - status :String //takes only ["FINISHED","RELEASING","NOT_YET_RELEASED","CANCELLED","HIATUS"]
    - volumes :Int
    - chapters :Int
    - country :String //takes only ["South korea","China","Japan","Taiwan"]
    - characters :[{id :Int, image :Link, name :String}]
```

**Note**:
```
    id: id of the manga assigned by anilist
```

## Character

**Endpoint**: `/character/<id>`

**Output**:
```
    - id :Int
    - name :String
    - age :String
    - descrption :String
    - gender :String
    - image :Link
    - Media :[{id :Int, name :String, image :Link}]
```

**Note**:
```
    id: id of the character assigned by anilist
```

## Search

**Endpoint**: `/search/<query>/<page>`

**Output**:
```
    - currentPage :Int
    - hasNext :Int
    - lastPage :Bool
    - results :[{id :Int, name :String, type :String}]
```

**Note**:
```
    query: search keyword
    page: result page number
```