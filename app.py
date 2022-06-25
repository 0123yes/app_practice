import random
import time

omikuji = ["大吉", "吉", "凶", "中吉"]

result = random.choice(omikuji)

print(f"今日の運勢は... {result}")

# Windowsは処理終了時にターミナルが閉じてしまうので、`sleep`などを追加する
time.sleep(5)  # time=5秒間待ってください
