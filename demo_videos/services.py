import os
import httpx


YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

FIELD_QUERIES = {
    'backend': 'Backend Development tutorial',
    'frontend': 'Frontend Development tutorial',
    'data_science': 'Data Science tutorial beginners',
    'ml': 'Machine Learning tutorial beginners',
    'ai_engineering': 'AI Engineering tutorial',
    'flutter': 'Flutter tutorial beginners',
    'android': 'Android Development tutorial',
    'ios': 'iOS Swift tutorial beginners',
    'devops': 'DevOps tutorial beginners',
    'cybersecurity': 'Cybersecurity tutorial beginners',
    'blockchain': 'Blockchain Development tutorial',
    'game_dev': 'Game Development tutorial beginners',
    'ui_ux': 'UI UX Design tutorial',
    'cloud': 'Cloud Engineering AWS tutorial',
    'qa': 'QA Software Testing tutorial',
}


def get_videos(field_name):
    query = FIELD_QUERIES.get(field_name, field_name)

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "order": "relevance",
        "relevanceLanguage": "en",
        "key": YOUTUBE_API_KEY,
    }

    response = httpx.get(url, params=params)
    data = response.json()

    videos = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]
        videos.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "thumbnail": snippet["thumbnails"]["high"]["url"],
            "video_url": f"https://www.youtube.com/watch?v={video_id}",
            "video_id": video_id,
        })

    return videos
