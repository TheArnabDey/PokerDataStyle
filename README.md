# PokerDataStyle
The data and the code in this project is created from scratch by me.
The importance of this Bot lies in the training data.
The training data is generated first by the bot itself.
Random and unique cards are assigned to 5 players (P1, P2, P3, P4 and P5 - 2 cards per player) in pre-flop round.
3 random and unique cards are assigned to community cards in the flop round.
1 random and unique card is assigned to community cards in the turn round.
1 random and unique card is assigned to community cards in the turn round.
For each round, hands of 5 players are evaluated along with the community cards (whenever available).
These randomly generated combinations of hands, community cards and evaluations (win/lose) is stored as the training dataset.
The bot is trained on the training dataset which will play based on the prior random scenarios and their results.
