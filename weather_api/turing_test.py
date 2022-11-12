cards_1 = [[5, 5], [2,2]]
cards_2 = [[5,3,8,9,7,9,4,2,1], [1,4,2,3], [1,3,2,5]]
cards_3 = [[5,3,8,9,7,8,4,2,1], [1,4,2,4,5,5,6,6,3], [1,3,2,5,5]]




def winning_card(cards):
    
    bad_cards = []
    for card in cards:
        for num in card : 
            if card.count(num) > 1 :
                bad_cards.append(num)
        good_cards  = list(set(card) - set(bad_cards))
        return -1 if good_cards == [] else max(good_cards)
           

print(winning_card(cards_3))