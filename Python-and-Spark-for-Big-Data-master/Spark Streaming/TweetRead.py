import tweepy
import os
import socket

bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

class TweetSender(tweepy.StreamingClient):

    def __init__(self, csocket):
        super().__init__()
        self.client_socket = csocket
    
    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        self.client_socket.send(tweet.text.encode('utf-8'))
        print("-"*50)

def sendData(c_socket): 
    sender = TweetSender(bearer_token=bearer_token, csocket=c_socket)
    
    # add new rules    
    rule = tweepy.StreamRule(value="Python")
    sender.add_rules(rule)
    
    sender.sample()

if __name__ == "__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 9999                # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print("Received request from: " + str(addr))

  sendData(c)
