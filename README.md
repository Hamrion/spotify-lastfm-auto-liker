# spotify-lastfm-auto-liker


**"spotify-lastfm-auto-liker"** code is a Python script that automatically likes the songs you have liked on **Spotify** on your **Last.fm** account using the **Last.fm API**. The script authenticates with both the **Spotify and Last.fm APIs** using your **API** credentials, retrieves the list of your liked songs from **Spotify**, and likes the same songs on **Last.fm** using the pylast library. The script also prints the names of the liked songs on the console for your reference. With this script, you can save time and effort by automatically syncing your liked songs between **Spotify and Last.fm** without having to manually like the same songs on both platforms.



## Requirements


1. **Python:** This code is written in Python, so you will need to have Python installed on your computer. You can download and install Python from the official Python website: https://www.python.org/downloads/

2. **Spotify API credentials:** To authenticate with the **Spotify API**, you will need to obtain a `client_id`, `client_secret`, and `redirect_uri` from the **Spotify Developer Dashboard**. You can create a **Spotify Developer account** and obtain these credentials by following the instructions here: https://developer.spotify.com/documentation/general/guides/app-settings/

3. **Last.fm API credentials:** To authenticate with the **Last.fm API**, you will need to obtain an `api_key`, `api_secret`, `username`, and `password_hash` from the **Last.fm Developer Website**. You can create a **Last.fm Developer account** and obtain these credentials by following the instructions here: https://www.last.fm/api/account/create



## How to use?


1. Install **spotipy** and **pylast** Python libraries. You can do this by running `pip install spotipy` and `pip install pylast` in your terminal or command prompt.

2. Copy and paste the code provided above into your preferred Python editor or IDE.

3. **Replace** the placeholders (`your_client_id`, `your_client_secret`, `your_redirect_uri`, `your_api_key`, `your_api_secret`, `your_username`, and `your_password`) with your actual **API** credentials.

5. **Run the code**. The code will authenticate with the **Spotify and Last.fm APIs** using your credentials, retrieve the list of your liked songs from Spotify, like the same songs on Last.fm, and print the names of the liked songs on the console.



## License


![GitHub](https://img.shields.io/github/license/Hamrion/spotify-lastfm-auto-liker)
