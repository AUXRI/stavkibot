import schedule
import time
from dataloader import fetch_data

def job():
    fetch_data()
    print("Данные обновлены")

schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
