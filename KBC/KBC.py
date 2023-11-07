Contestant_name = input("Enter your name:")
print(f"Hello {Contestant_name}, welcome to KBC!")

questions = [
    "1. Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
    "2. Who, in 1978, became the first person to be born in the continent of Antarctica?",
    "3. Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868?",
    "4. Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
    "5. Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?",
    "6. The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla?"
]

Options = [
    ['A. Solicitor General', 'B. Attorney General', 'C. Cabinet Secretary', 'D. Chief Justice'],
    ['A. Emilio Palma', 'B. James Weddell', 'C. Nathaniel Palmer', 'D. Charles Wilkes'],
    ['A. Belgium', 'B. Italy', 'C. Denmark', 'D. France'],
    ['A. Junko Tabei', 'B. Wanda Rutkiewicz', 'C. Tamae Watanabe', 'D. Chantal Mauduit'],
    ['A. Mir Taqi Mir', 'B. Mohammad Ibrahim Zauq', 'C. Zahir Dehlvi', 'D. Abul-Qasim Ferdowsi'],
    ['A. Viceregal Lodge', 'B. Gorton Castle', 'C. Barnes Court', 'D. Cecil Hotel']
]

Answers = ["B", "A", "C", "B", "C", "C"]

amount=0
for i in range(len(questions)):
    print(questions[i])
    print(Options[i])
    user_answer=input("choose an option from A to D: ").capitalize()
    if user_answer!=Answers[i]:
        print("wrong answer!")
        if i < 2:
            amount = i*100
        elif i >= 2 and i < 4:
            amount = 200+(i-2)*200
        elif i >= 4:
            amount = 600+(i-4)*300
        break
    if i == 5:
        amount=1800

if amount == 0:
    print("Better Luck next time!")
else:
    print(f"Congrats! You won ${amount}")