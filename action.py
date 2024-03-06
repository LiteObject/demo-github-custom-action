import sys
import os
import json

def main():
  name = 'World'
  user_input =  name = os.environ['INPUT_PERSON']
  print(f"user_input: {user_input}")
  
  if 'GITHUB_EVENT_PATH' in os.environ:
    event_path = os.environ['GITHUB_EVENT_PATH']
    with open(event_path) as fp:
      event = json.load(fp)
      if 'pull_request' in event:
        name = event['pull_request']['head']['repo']['name']

  print(f'Hello {name}!')

if __name__ == '__main__':
  main()