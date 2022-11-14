cards_1 = [[5, 5], [2,2]]
cards_2 = [[5,3,8,9,7,9,4,2,1], [1,4,2,3], [1,3,2,5]]
cards_3 = [[5,3,8,9,7,9,4,2,1], [1,4,2,4,5,5,6,6,3], [10,3,2,5,5]]




def winning_card(cards):
    
    final_cards = []
    multiple_cards = []
    for card in cards:
        for num in card : 
            if card.count(num) > 1 :
                multiple_cards.append(num)
                good_cards  = set(card) - set(multiple_cards)
                if good_cards != set(): final_cards.append(max(list(good_cards)))
    return -1 if final_cards == [] else max(final_cards)
       

print(winning_card(cards_1))