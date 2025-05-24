import os
import importlib

bookies_dir = 'bookies'
results = []

for filename in os.listdir(bookies_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"{bookies_dir}.{filename[:-3]}"  # Remove .py
        module = importlib.import_module(module_name)

        try:
            odds = module.get_odds()
            results.append(odds)
        except Exception as e:
            print(e)
            exit()

for result in results:
    print("{bookmaker}:".format(bookmaker=result['bookmaker']))
    print('Trzaskowski:', result['trzaskowski'])
    print('Nawrocki:', result['nawrocki'])
    print("\n")

average_trzaskowski = sum(el['trzaskowski'] for el in results) / len(results)
average_nawrocki = sum(el['nawrocki'] for el in results) / len(results)
total_odds = average_trzaskowski + average_nawrocki

print('Średnia:')
print("Trzaskowski:", round(average_trzaskowski, 2),
      "{probability}%".format(probability=round(average_nawrocki / total_odds * 100, 2)))
print("Nawrocki:", round(average_nawrocki, 2), "{probability}%".format(
    probability=round(average_trzaskowski / total_odds * 100, 2)))
