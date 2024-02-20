budgets = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memories = int(input())
video_cards_price = number_of_video_cards * 250
one_processor_price = video_cards_price * 0.35
processors_price = number_of_processors * one_processor_price
one_ram_memory_price = video_cards_price * 0.10
ram_memories_price = number_of_ram_memories * one_ram_memory_price
needed_money = video_cards_price + processors_price + ram_memories_price
if number_of_video_cards > number_of_processors:
    needed_money *= 0.85
difference = abs(needed_money - budgets)
if budgets >= needed_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")


