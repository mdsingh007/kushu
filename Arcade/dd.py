from deuces import Card

board = [
    Card.new('Ah'),
    Card.new('Kd'),
    Card.new('Jc')
]
hand = [
   Card.new('Qs'),
   Card.new('Th')
]

print (Card.print_pretty_cards(board + hand))
Card.print

