import tweepy
import config

def authenticate():
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
    return tweepy.API(auth)

def post_images_to_twitter(image_paths, caption="Resized Images!"):
    api = authenticate()
    media_ids = [api.media_upload(img).media_id_string for img in image_paths]
    api.update_status(status=caption, media_ids=media_ids)
