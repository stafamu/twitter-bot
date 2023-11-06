import time
import twitter_bot

def main():
    while True:
        twitter_bot.run()
        time.sleep(15 * 60)

if __name__ == '__main__':
    main()
