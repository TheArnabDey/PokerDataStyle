import random
import pandas as pd
import numpy as np
df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('train.csv')
df3 = pd.read_csv('train.csv')
df4 = pd.read_csv('train.csv')
df5 = pd.read_csv('train.csv')
for i in range(0,1):
        for k in range (1,5):
            x = 0
            # Create Pre-Flop round
            if k == 1:
                df1.loc[i * 4 + k-1] = -1
                df2.loc[i * 4 + k-1] = -1
                df3.loc[i * 4 + k - 1] = -1
                df4.loc[i * 4 + k - 1] = -1
                df5.loc[i * 4 + k - 1] = -1
                # Generate first card for P1
                df1.iloc[i * 4 + k-1, 0] = random.randrange(1,5)
                df1.iloc[i * 4 + k-1, 1] = random.randrange(2,15)
                while x == 0:
                    print "Step 1"
                    # Generate 2nd card for P1
                    df1.iloc[i * 4 + k-1, 2] = random.randrange(1,5)
                    df1.iloc[i * 4 + k-1, 3] = random.randrange(2,15)
                    #Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k-1, 2] == df1.iloc[i * 4 + k-1, 0] and df1.iloc[i * 4 + k-1, 3] == df1.iloc[i * 4 + k-1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 2"
                    # Generate 2nd card for P2
                    df2.iloc[i * 4 + k - 1, 2] = random.randrange(1, 5)
                    df2.iloc[i * 4 + k - 1, 3] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df2.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 0] and df2.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 1])\
                        or (df2.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 3] == \
                        df1.iloc[i * 4 + k - 1, 3]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 3"
                    # Generate 2nd card for P3
                    df3.iloc[i * 4 + k - 1, 2] = random.randrange(1, 5)
                    df3.iloc[i * 4 + k - 1, 3] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df3.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 0] and df3.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 1])\
                            or (df3.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 3])\
                            or (df3.iloc[i * 4 + k - 1, 2] == df2.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 3] ==
                        df2.iloc[i * 4 + k - 1, 3]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 4"
                    # Generate 2nd card for P4
                    df4.iloc[i * 4 + k - 1, 2] = random.randrange(1, 5)
                    df4.iloc[i * 4 + k - 1, 3] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df4.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 0] and df4.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 1])\
                            or (df4.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 3])\
                            or (df4.iloc[i * 4 + k - 1, 2] == df2.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 3] ==
                        df2.iloc[i * 4 + k - 1, 2])\
                            or (df4.iloc[i * 4 + k - 1, 2] == df3.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 3] ==
                        df3.iloc[i * 4 + k - 1, 3]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 5"
                    # Generate 2nd card for P5
                    df5.iloc[i * 4 + k - 1, 2] = random.randrange(1, 5)
                    df5.iloc[i * 4 + k - 1, 3] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df5.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 0] and df5.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 1])\
                            or (df5.iloc[i * 4 + k - 1, 2] == df1.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 3] ==
                        df1.iloc[i * 4 + k - 1, 3])\
                            or (df5.iloc[i * 4 + k - 1, 2] == df2.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 3] ==
                        df2.iloc[i * 4 + k - 1, 3])\
                            or (df5.iloc[i * 4 + k - 1, 2] == df3.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 3] ==
                        df3.iloc[i * 4 + k - 1, 3])\
                            or (df5.iloc[i * 4 + k - 1, 2] == df4.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 3] ==
                        df4.iloc[i * 4 + k - 1, 3]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 6"
                    # Generate 1st card for P2
                    df2.iloc[i * 4 + k - 1, 0] = random.randrange(1, 5)
                    df2.iloc[i * 4 + k - 1, 1] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df2.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 0] and df2.iloc[i * 4 + k - 1, 1] ==
                        df1.iloc[i * 4 + k - 1, 1]) \
                            or (df2.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 1] ==
                                df1.iloc[i * 4 + k - 1, 3]) \
                            or (df2.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 3]) \
                            or (df2.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 3]) \
                            or (df2.iloc[i * 4 + k - 1, 0] == df4.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 1] ==
                                df4.iloc[i * 4 + k - 1, 3]) \
                            or (df2.iloc[i * 4 + k - 1, 0] == df5.iloc[i * 4 + k - 1, 2] and df2.iloc[i * 4 + k - 1, 1] ==
                                df5.iloc[i * 4 + k - 1, 3]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 7"
                    # Generate 1st card for P3
                    df3.iloc[i * 4 + k - 1, 0] = random.randrange(1, 5)
                    df3.iloc[i * 4 + k - 1, 1] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df3.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 0] and df3.iloc[i * 4 + k - 1, 1] ==
                        df1.iloc[i * 4 + k - 1, 1]) \
                            or (df3.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 1] ==
                                df1.iloc[i * 4 + k - 1, 3]) \
                            or (df3.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 3]) \
                            or (df3.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 3]) \
                            or (df3.iloc[i * 4 + k - 1, 0] == df4.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 1] ==
                                df4.iloc[i * 4 + k - 1, 3]) \
                            or (df3.iloc[i * 4 + k - 1, 0] == df5.iloc[i * 4 + k - 1, 2] and df3.iloc[i * 4 + k - 1, 1] ==
                                df5.iloc[i * 4 + k - 1, 3])\
                            or (df3.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 0] and df3.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 8"
                    # Generate 1st card for P4
                    df4.iloc[i * 4 + k - 1, 0] = random.randrange(1, 5)
                    df4.iloc[i * 4 + k - 1, 1] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df4.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 0] and df4.iloc[i * 4 + k - 1, 1] ==
                        df1.iloc[i * 4 + k - 1, 1]) \
                            or (df4.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 1] ==
                                df1.iloc[i * 4 + k - 1, 3]) \
                            or (df4.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 3]) \
                            or (df4.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 3]) \
                            or (df4.iloc[i * 4 + k - 1, 0] == df4.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 1] ==
                                df4.iloc[i * 4 + k - 1, 3]) \
                            or (df4.iloc[i * 4 + k - 1, 0] == df5.iloc[i * 4 + k - 1, 2] and df4.iloc[i * 4 + k - 1, 1] ==
                                df5.iloc[i * 4 + k - 1, 3])\
                            or (df4.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 0] and df4.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 1])\
                            or (df4.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 0] and df4.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 9"
                    # Generate 1st card for P5
                    df5.iloc[i * 4 + k - 1, 0] = random.randrange(1, 5)
                    df5.iloc[i * 4 + k - 1, 1] = random.randrange(2, 15)
                    # Check if this card is already generated in this game, then re-generate
                    if (df5.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 0] and df5.iloc[i * 4 + k - 1, 1] ==
                        df1.iloc[i * 4 + k - 1, 1]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df1.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 1] ==
                                df1.iloc[i * 4 + k - 1, 3]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 3]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 3]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df4.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 1] ==
                                df4.iloc[i * 4 + k - 1, 3]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df5.iloc[i * 4 + k - 1, 2] and df5.iloc[i * 4 + k - 1, 1] ==
                                df5.iloc[i * 4 + k - 1, 3])\
                            or (df5.iloc[i * 4 + k - 1, 0] == df2.iloc[i * 4 + k - 1, 0] and df5.iloc[i * 4 + k - 1, 1] ==
                                df2.iloc[i * 4 + k - 1, 1])\
                            or (df5.iloc[i * 4 + k - 1, 0] == df3.iloc[i * 4 + k - 1, 0] and df5.iloc[i * 4 + k - 1, 1] ==
                                df3.iloc[i * 4 + k - 1, 1]) \
                            or (df5.iloc[i * 4 + k - 1, 0] == df4.iloc[i * 4 + k - 1, 0] and df5.iloc[i * 4 + k - 1, 1] ==
                                df4.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                list = []
                df1.iloc[i * 4 + k - 1, 14] = 0
                df2.iloc[i * 4 + k - 1, 14] = 0
                df3.iloc[i * 4 + k - 1, 14] = 0
                df4.iloc[i * 4 + k - 1, 14] = 0
                df5.iloc[i * 4 + k - 1, 14] = 0
                #Pre-flop Hand evaluation
                #Evaluate each player's hand for a pair
                if df1.iloc[i * 4 + k - 1, 1] == df1.iloc[i * 4 + k - 1, 3]:
                    list.append(df1.iloc[i * 4 + k - 1, 1])
                if df2.iloc[i * 4 + k - 1, 1] == df2.iloc[i * 4 + k - 1, 3]:
                    list.append(df2.iloc[i * 4 + k - 1, 1])
                if df3.iloc[i * 4 + k - 1, 1] == df3.iloc[i * 4 + k - 1, 3]:
                    list.append(df3.iloc[i * 4 + k - 1, 1])
                if df4.iloc[i * 4 + k - 1, 1] == df4.iloc[i * 4 + k - 1, 3]:
                    list.append(df4.iloc[i * 4 + k - 1, 1])
                if df5.iloc[i * 4 + k - 1, 1] == df5.iloc[i * 4 + k - 1, 3]:
                    list.append(df5.iloc[i * 4 + k - 1, 1])
                #Check if more than one player have a pair
                if (len(list) > 1):
                    winner = max(list)
                    if df1.iloc[i * 4 + k - 1, 1] == winner and df1.iloc[i * 4 + k - 1, 3] == winner:
                        df1.iloc[i * 4 + k - 1, 14] = 1
                    if df2.iloc[i * 4 + k - 1, 1] == winner and df2.iloc[i * 4 + k - 1, 3] == winner:
                        df2.iloc[i * 4 + k - 1, 14] = 1
                    if df3.iloc[i * 4 + k - 1, 1] == winner and df3.iloc[i * 4 + k - 1, 3] == winner:
                        df3.iloc[i * 4 + k - 1, 14] = 1
                    if df4.iloc[i * 4 + k - 1, 1] == winner and df4.iloc[i * 4 + k - 1, 3] == winner:
                        df4.iloc[i * 4 + k - 1, 14] = 1
                    if df5.iloc[i * 4 + k - 1, 1] == winner and df5.iloc[i * 4 + k - 1, 3] == winner:
                        df5.iloc[i * 4 + k - 1, 14] = 1
                #Check if only one player has a pair
                elif (len(list) == 1):
                    winner = max(list)
                    if df1.iloc[i * 4 + k - 1, 1] == winner and df1.iloc[i * 4 + k - 1, 3] == winner:
                        df1.iloc[i * 4 + k - 1, 14] = 1
                    elif df2.iloc[i * 4 + k - 1, 1] == winner and df2.iloc[i * 4 + k - 1, 3] == winner:
                        df2.iloc[i * 4 + k - 1, 14] = 1
                    elif df3.iloc[i * 4 + k - 1, 1] == winner and df3.iloc[i * 4 + k - 1, 3] == winner:
                        df3.iloc[i * 4 + k - 1, 14] = 1
                    elif df4.iloc[i * 4 + k - 1, 1] == winner and df4.iloc[i * 4 + k - 1, 3] == winner:
                        df4.iloc[i * 4 + k - 1, 14] = 1
                    elif df5.iloc[i * 4 + k - 1, 1] == winner and df5.iloc[i * 4 + k - 1, 3] == winner:
                        df5.iloc[i * 4 + k - 1, 14] = 1
                #Evaluate for the high card
                else:
                     winner = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                  df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                  df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                  df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                  df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],)
                     if df1.iloc[i * 4 + k - 1, 1] == winner or df1.iloc[i * 4 + k - 1, 3] == winner:
                         df1.iloc[i * 4 + k - 1, 14] = 1
                     if df2.iloc[i * 4 + k - 1, 1] == winner or df2.iloc[i * 4 + k - 1, 3] == winner:
                         df2.iloc[i * 4 + k - 1, 14] = 1
                     if df3.iloc[i * 4 + k - 1, 1] == winner or df3.iloc[i * 4 + k - 1, 3] == winner:
                         df3.iloc[i * 4 + k - 1, 14] = 1
                     if df4.iloc[i * 4 + k - 1, 1] == winner or df4.iloc[i * 4 + k - 1, 3] == winner:
                         df4.iloc[i * 4 + k - 1, 14] = 1
                     if df5.iloc[i * 4 + k - 1, 1] == winner or df5.iloc[i * 4 + k - 1, 3] == winner:
                         df5.iloc[i * 4 + k - 1, 14] = 1

            # Create Flop Round
            if k == 2:
                df1.loc[i * 4 + k-1] = df1.loc[i * 4 + k - 2]
                df2.loc[i * 4 + k - 1] = df2.loc[i * 4 + k - 2]
                df3.loc[i * 4 + k - 1] = df3.loc[i * 4 + k - 2]
                df4.loc[i * 4 + k - 1] = df4.loc[i * 4 + k - 2]
                df5.loc[i * 4 + k - 1] = df5.loc[i * 4 + k - 2]
                while x == 0:
                    print "Step 10"
                    #Generate 1st community card
                    df1.iloc[i * 4 + k-1, 4] = random.randrange(1, 5)
                    df1.iloc[i * 4 + k-1, 5] = random.randrange(2, 15)
                    df2.iloc[i * 4 + k - 1, 4] = df1.iloc[i * 4 + k - 1, 4]
                    df2.iloc[i * 4 + k - 1, 5] = df1.iloc[i * 4 + k - 1, 5]
                    df3.iloc[i * 4 + k - 1, 4] = df1.iloc[i * 4 + k - 1, 4]
                    df3.iloc[i * 4 + k - 1, 5] = df1.iloc[i * 4 + k - 1, 5]
                    df4.iloc[i * 4 + k - 1, 4] = df1.iloc[i * 4 + k - 1, 4]
                    df4.iloc[i * 4 + k - 1, 5] = df1.iloc[i * 4 + k - 1, 5]
                    df5.iloc[i * 4 + k - 1, 4] = df1.iloc[i * 4 + k - 1, 4]
                    df5.iloc[i * 4 + k - 1, 5] = df1.iloc[i * 4 + k - 1, 5]
                    # Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k-1, 4] == df1.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 5] == df1.iloc[i * 4 + k-1, 3]) \
                            or (df1.iloc[i * 4 + k-1, 4] == df1.iloc[i * 4 + k-1, 0] and df1.iloc[i * 4 + k-1, 5] == df1.iloc[i * 4 + k-1, 1])\
                            or (df1.iloc[i * 4 + k-1, 4] == df2.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 5] == df2.iloc[i * 4 + k-1, 3])\
                            or (df1.iloc[i * 4 + k-1, 4] == df3.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 5] == df3.iloc[i * 4 + k-1, 3])\
                            or (df1.iloc[i * 4 + k-1, 4] == df4.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 5] == df4.iloc[i * 4 + k-1, 3])\
                            or (df1.iloc[i * 4 + k-1, 4] == df5.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 5] == df5.iloc[i * 4 + k-1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 4] == df2.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 5] == df2.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 4] == df3.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 5] == df3.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 4] == df4.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 5] == df4.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 4] == df5.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 5] == df5.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 11"
                    # Generate 2nd community card
                    df1.iloc[i * 4 + k-1, 6] = random.randrange(1, 5)
                    df1.iloc[i * 4 + k-1, 7] = random.randrange(2, 15)
                    df2.iloc[i * 4 + k-1, 6] = df1.iloc[i * 4 + k-1, 6]
                    df2.iloc[i * 4 + k-1, 7] = df1.iloc[i * 4 + k-1, 7]
                    df3.iloc[i * 4 + k-1, 6] = df1.iloc[i * 4 + k-1, 6]
                    df3.iloc[i * 4 + k-1, 7] = df1.iloc[i * 4 + k-1, 7]
                    df4.iloc[i * 4 + k-1, 6] = df1.iloc[i * 4 + k-1, 6]
                    df4.iloc[i * 4 + k-1, 7] = df1.iloc[i * 4 + k-1, 7]
                    df5.iloc[i * 4 + k-1, 6] = df1.iloc[i * 4 + k-1, 6]
                    df5.iloc[i * 4 + k-1, 7] = df1.iloc[i * 4 + k-1, 7]
                    # Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k-1, 6] == df1.iloc[i * 4 + k-1, 4] and df1.iloc[i * 4 + k-1, 7] == df1.iloc[i * 4 + k-1, 5]) \
                        or (df1.iloc[i * 4 + k-1, 6] == df1.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 7] == df1.iloc[i * 4 + k-1, 3]) \
                        or (df1.iloc[i * 4 + k-1, 6] == df1.iloc[i * 4 + k-1, 0] and df1.iloc[i * 4 + k-1, 7] == df1.iloc[i * 4 + k-1, 1])\
                        or (df1.iloc[i * 4 + k-1, 6] == df2.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 7] == df2.iloc[i * 4 + k-1, 3])\
                        or (df1.iloc[i * 4 + k-1, 6] == df3.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 7] == df3.iloc[i * 4 + k-1, 3])\
                        or (df1.iloc[i * 4 + k-1, 6] == df4.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 7] == df4.iloc[i * 4 + k-1, 3])\
                        or (df1.iloc[i * 4 + k-1, 6] == df5.iloc[i * 4 + k-1, 2] and df1.iloc[i * 4 + k-1, 7] == df5.iloc[i * 4 + k-1, 3]) \
                        or (df1.iloc[i * 4 + k - 1, 6] == df2.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                        i * 4 + k - 1, 7] == df2.iloc[i * 4 + k - 1, 1]) \
                        or (df1.iloc[i * 4 + k - 1, 6] == df3.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                        i * 4 + k - 1, 7] == df3.iloc[i * 4 + k - 1, 1]) \
                        or (df1.iloc[i * 4 + k - 1, 6] == df4.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                        i * 4 + k - 1, 7] == df4.iloc[i * 4 + k - 1, 1]) \
                        or (df1.iloc[i * 4 + k - 1, 6] == df5.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                        i * 4 + k - 1, 7] == df5.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                x = 0
                while x == 0:
                    print "Step 12"
                    #Generate 3rd community card
                    df1.iloc[i * 4 + k-1, 8] = random.randrange(1, 5)
                    df1.iloc[i * 4 + k-1, 9] = random.randrange(2, 15)
                    df2.iloc[i * 4 + k-1, 8] = df1.iloc[i * 4 + k-1, 8]
                    df2.iloc[i * 4 + k-1, 9] = df1.iloc[i * 4 + k-1, 9]
                    df3.iloc[i * 4 + k-1, 8] = df1.iloc[i * 4 + k-1, 8]
                    df3.iloc[i * 4 + k-1, 9] = df1.iloc[i * 4 + k-1, 9]
                    df4.iloc[i * 4 + k-1, 8] = df1.iloc[i * 4 + k-1, 8]
                    df4.iloc[i * 4 + k-1, 9] = df1.iloc[i * 4 + k-1, 9]
                    df5.iloc[i * 4 + k-1, 8] = df1.iloc[i * 4 + k-1, 8]
                    df5.iloc[i * 4 + k-1, 9] = df1.iloc[i * 4 + k-1, 9]
                    # Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k - 1, 8] == df1.iloc[i * 4 + k - 1, 6] and df1.iloc[i * 4 + k - 1, 9] == df1.iloc[
                                    i * 4 + k - 1, 7]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df1.iloc[i * 4 + k - 1, 4] and df1.iloc[i * 4 + k - 1, 9] ==
                                df1.iloc[i * 4 + k - 1, 5]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df1.iloc[i * 4 + k - 1, 2] and df1.iloc[i * 4 + k - 1, 9] ==
                                df1.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df1.iloc[i * 4 + k - 1, 0] and df1.iloc[i * 4 + k - 1, 9] ==
                                df1.iloc[i * 4 + k - 1, 1])\
                            or (df1.iloc[i * 4 + k - 1, 8] == df2.iloc[i * 4 + k - 1, 2] and df1.iloc[i * 4 + k - 1, 9] ==
                                df2.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 8] == df3.iloc[i * 4 + k - 1, 2] and df1.iloc[i * 4 + k - 1, 9] ==
                                df3.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 8] == df4.iloc[i * 4 + k - 1, 2] and df1.iloc[i * 4 + k - 1, 9] ==
                                df4.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 8] == df5.iloc[i * 4 + k - 1, 2] and df1.iloc[i * 4 + k - 1, 9] ==
                                df5.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df2.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 9] == df2.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df3.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 9] == df3.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df4.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 9] == df4.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 8] == df5.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 9] == df5.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                df2.iloc[i * 4 + k - 1, 4] = df3.iloc[i * 4 + k - 1, 4] = df4.iloc[i * 4 + k - 1, 4] = df5.iloc[
                    i * 4 + k - 1, 4] = df1.iloc[i * 4 + k - 1, 4]
                df2.iloc[i * 4 + k - 1, 5] = df3.iloc[i * 4 + k - 1, 5] = df4.iloc[i * 4 + k - 1, 5] = df5.iloc[
                    i * 4 + k - 1, 5] = df1.iloc[i * 4 + k - 1, 5]
                df2.iloc[i * 4 + k - 1, 6] = df3.iloc[i * 4 + k - 1, 6] = df4.iloc[i * 4 + k - 1, 6] = df5.iloc[
                    i * 4 + k - 1, 6] = df1.iloc[i * 4 + k - 1, 6]
                df2.iloc[i * 4 + k - 1, 7] = df3.iloc[i * 4 + k - 1, 7] = df4.iloc[i * 4 + k - 1, 7] = df5.iloc[
                    i * 4 + k - 1, 7] = df1.iloc[i * 4 + k - 1, 7]
                df2.iloc[i * 4 + k - 1, 8] = df3.iloc[i * 4 + k - 1, 8] = df4.iloc[i * 4 + k - 1, 8] = df5.iloc[
                    i * 4 + k - 1, 8] = df1.iloc[i * 4 + k - 1, 8]
                df2.iloc[i * 4 + k - 1, 9] = df3.iloc[i * 4 + k - 1, 9] = df4.iloc[i * 4 + k - 1, 9] = df5.iloc[
                    i * 4 + k - 1, 9] = df1.iloc[i * 4 + k - 1, 9]
                #Flop hand evaluation
                x = 0
                list = [-1,-1,-1,-1,-1]
                df1.iloc[i * 4 + k - 1, 14] = 0
                df2.iloc[i * 4 + k - 1, 14] = 0
                df3.iloc[i * 4 + k - 1, 14] = 0
                df4.iloc[i * 4 + k - 1, 14] = 0
                df5.iloc[i * 4 + k - 1, 14] = 0
                #Straight Flush Evaluation
                SF = 0
                a1 = 0
                a2 = 0
                a3 = 0
                a4 = 0
                a5 = 0
                #P1 Evaluation
                #With Ace Low
                list[0] = df1.iloc[i * 4 + k - 1, 1]
                list[1] = df1.iloc[i * 4 + k - 1, 3]
                list[2] = df1.iloc[i * 4 + k - 1, 5]
                list[3] = df1.iloc[i * 4 + k - 1, 7]
                list[4] = df1.iloc[i * 4 + k - 1, 9]
                for m in range (0,5):
                    if list[m] == 14:
                        list[m] = 1
                list = np.sort(list).tolist()
                if list[0]+1 == list[1] and list[1]+1 == list[2] and list[2]+1 == list[3] and list[3]+1 == list[4]:
                    a1 = max(list[0],list[1],list[2],list[3],list[4])
                    list[0] = df1.iloc[i * 4 + k - 1, 0]
                    list[1] = df1.iloc[i * 4 + k - 1, 2]
                    list[2] = df1.iloc[i * 4 + k - 1, 4]
                    list[3] = df1.iloc[i * 4 + k - 1, 6]
                    list[4] = df1.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a1 = 0
                # With Ace High
                list[0] = df1.iloc[i * 4 + k - 1, 1]
                list[1] = df1.iloc[i * 4 + k - 1, 3]
                list[2] = df1.iloc[i * 4 + k - 1, 5]
                list[3] = df1.iloc[i * 4 + k - 1, 7]
                list[4] = df1.iloc[i * 4 + k - 1, 9]
                list = np.sort(list).tolist()
                if list[0]+1 == list[1] and list[1]+1 == list[2] and list[2]+1 == list[3] and list[3]+1 == list[4]:
                    a1 = max(list[0],list[1],list[2],list[3],list[4])
                    list[0] = df1.iloc[i * 4 + k - 1, 0]
                    list[1] = df1.iloc[i * 4 + k - 1, 2]
                    list[2] = df1.iloc[i * 4 + k - 1, 4]
                    list[3] = df1.iloc[i * 4 + k - 1, 6]
                    list[4] = df1.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a1 = 0
                #P2 Evaluation
                #With Ace Low
                list[0] = df2.iloc[i * 4 + k - 1, 1]
                list[1] = df2.iloc[i * 4 + k - 1, 3]
                list[2] = df2.iloc[i * 4 + k - 1, 5]
                list[3] = df2.iloc[i * 4 + k - 1, 7]
                list[4] = df2.iloc[i * 4 + k - 1, 9]
                for m in range(0, 5):
                    if list[m] == 14:
                        list[m] = 1
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[
                    4]:
                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df2.iloc[i * 4 + k - 1, 0]
                    list[1] = df2.iloc[i * 4 + k - 1, 2]
                    list[2] = df2.iloc[i * 4 + k - 1, 4]
                    list[3] = df2.iloc[i * 4 + k - 1, 6]
                    list[4] = df2.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a2 = 0
                #With Ace High
                list[0] = df2.iloc[i * 4 + k - 1, 1]
                list[1] = df2.iloc[i * 4 + k - 1, 3]
                list[2] = df2.iloc[i * 4 + k - 1, 5]
                list[3] = df2.iloc[i * 4 + k - 1, 7]
                list[4] = df2.iloc[i * 4 + k - 1, 9]
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4]:
                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df2.iloc[i * 4 + k - 1, 0]
                    list[1] = df2.iloc[i * 4 + k - 1, 2]
                    list[2] = df2.iloc[i * 4 + k - 1, 4]
                    list[3] = df2.iloc[i * 4 + k - 1, 6]
                    list[4] = df2.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a2 = 0
                # P3 Evaluation
                # With Ace Low
                list[0] = df3.iloc[i * 4 + k - 1, 1]
                list[1] = df3.iloc[i * 4 + k - 1, 3]
                list[2] = df3.iloc[i * 4 + k - 1, 5]
                list[3] = df3.iloc[i * 4 + k - 1, 7]
                list[4] = df3.iloc[i * 4 + k - 1, 9]
                for m in range(0, 5):
                    if list[m] == 14:
                        list[m] = 1
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == \
                        list[
                            4]:
                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df3.iloc[i * 4 + k - 1, 0]
                    list[1] = df3.iloc[i * 4 + k - 1, 2]
                    list[2] = df3.iloc[i * 4 + k - 1, 4]
                    list[3] = df3.iloc[i * 4 + k - 1, 6]
                    list[4] = df3.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a3 = 0
                #With Ace High
                list[0] = df3.iloc[i * 4 + k - 1, 1]
                list[1] = df3.iloc[i * 4 + k - 1, 3]
                list[2] = df3.iloc[i * 4 + k - 1, 5]
                list[3] = df3.iloc[i * 4 + k - 1, 7]
                list[4] = df3.iloc[i * 4 + k - 1, 9]
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4]:
                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df3.iloc[i * 4 + k - 1, 0]
                    list[1] = df3.iloc[i * 4 + k - 1, 2]
                    list[2] = df3.iloc[i * 4 + k - 1, 4]
                    list[3] = df3.iloc[i * 4 + k - 1, 6]
                    list[4] = df3.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a3 = 0
                # P4 Evaluation
                # With Ace Low
                list[0] = df4.iloc[i * 4 + k - 1, 1]
                list[1] = df4.iloc[i * 4 + k - 1, 3]
                list[2] = df4.iloc[i * 4 + k - 1, 5]
                list[3] = df4.iloc[i * 4 + k - 1, 7]
                list[4] = df4.iloc[i * 4 + k - 1, 9]
                for m in range(0, 5):
                    if list[m] == 14:
                        list[m] = 1
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == \
                        list[4]:
                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df4.iloc[i * 4 + k - 1, 0]
                    list[1] = df4.iloc[i * 4 + k - 1, 2]
                    list[2] = df4.iloc[i * 4 + k - 1, 4]
                    list[3] = df4.iloc[i * 4 + k - 1, 6]
                    list[4] = df4.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a4 = 0
                #With Ace High
                list[0] = df4.iloc[i * 4 + k - 1, 1]
                list[1] = df4.iloc[i * 4 + k - 1, 3]
                list[2] = df4.iloc[i * 4 + k - 1, 5]
                list[3] = df4.iloc[i * 4 + k - 1, 7]
                list[4] = df4.iloc[i * 4 + k - 1, 9]
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4]:
                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df4.iloc[i * 4 + k - 1, 0]
                    list[1] = df4.iloc[i * 4 + k - 1, 2]
                    list[2] = df4.iloc[i * 4 + k - 1, 4]
                    list[3] = df4.iloc[i * 4 + k - 1, 6]
                    list[4] = df4.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a4 = 0
                # P5 Evaluation
                # With Ace Low
                list[0] = df5.iloc[i * 4 + k - 1, 1]
                list[1] = df5.iloc[i * 4 + k - 1, 3]
                list[2] = df5.iloc[i * 4 + k - 1, 5]
                list[3] = df5.iloc[i * 4 + k - 1, 7]
                list[4] = df5.iloc[i * 4 + k - 1, 9]
                for m in range(0, 5):
                    if list[m] == 14:
                        list[m] = 1
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == \
                        list[4]:
                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df5.iloc[i * 4 + k - 1, 0]
                    list[1] = df5.iloc[i * 4 + k - 1, 2]
                    list[2] = df5.iloc[i * 4 + k - 1, 4]
                    list[3] = df5.iloc[i * 4 + k - 1, 6]
                    list[4] = df5.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a5 = 0
                #With Ace High
                list[0] = df5.iloc[i * 4 + k - 1, 1]
                list[1] = df5.iloc[i * 4 + k - 1, 3]
                list[2] = df5.iloc[i * 4 + k - 1, 5]
                list[3] = df5.iloc[i * 4 + k - 1, 7]
                list[4] = df5.iloc[i * 4 + k - 1, 9]
                list = np.sort(list).tolist()
                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4]:
                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                    list[0] = df5.iloc[i * 4 + k - 1, 0]
                    list[1] = df5.iloc[i * 4 + k - 1, 2]
                    list[2] = df5.iloc[i * 4 + k - 1, 4]
                    list[3] = df5.iloc[i * 4 + k - 1, 6]
                    list[4] = df5.iloc[i * 4 + k - 1, 8]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                        SF = SF + 1
                    else:
                        a5 = 0
                #Check for Straight flush
                if (SF > 0):
                    print "Straight Flush"
                    b = max(a1,a2,a3,a4,a5)
                    if a1 == b:
                        df1.iloc[i * 4 + k - 1, 14] = 1
                    if a2 == b:
                        df2.iloc[i * 4 + k - 1, 14] = 1
                    if a3 == b:
                        df3.iloc[i * 4 + k - 1, 14] = 1
                    if a4 == b:
                        df4.iloc[i * 4 + k - 1, 14] = 1
                    if a5 == b:
                        df5.iloc[i * 4 + k - 1, 14] = 1
                else:
                    # Check for four of a kind
                    FK = 0
                    a1 = 0
                    a2 = 0
                    a3 = 0
                    a4 = 0
                    a5 = 0
                    #Evaluate for P1
                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[4] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[0] == list[4] and list[4] == list[2] and list[2] == list[3] \
                        or list[0] == list[1] and list[1] == list[4] and list[4] == list[3] \
                        or list[0] == list[1] and list[1] == list[2] and list[2] == list[4]:
                        FK = FK + 1
                        a1 = list[0]
                    #Evaluate for P2
                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[4] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[0] == list[4] and list[4] == list[2] and list[2] == list[3] \
                        or list[0] == list[1] and list[1] == list[4] and list[4] == list[3] \
                        or list[0] == list[1] and list[1] == list[2] and list[2] == list[4]:
                        FK = FK + 1
                        a2 = list[0]
                    #Evaluate for P3
                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[4] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[0] == list[4] and list[4] == list[2] and list[2] == list[3] \
                        or list[0] == list[1] and list[1] == list[4] and list[4] == list[3] \
                        or list[0] == list[1] and list[1] == list[2] and list[2] == list[4]:
                        FK = FK + 1
                        a3 = list[0]
                    #Evaluate for P4
                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[4] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[0] == list[4] and list[4] == list[2] and list[2] == list[3] \
                        or list[0] == list[1] and list[1] == list[4] and list[4] == list[3] \
                        or list[0] == list[1] and list[1] == list[2] and list[2] == list[4]:
                        FK = FK + 1
                        a4 = list[0]
                    #Evaluate for P5
                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                    if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[4] == list[1] and list[1] == list[2] and list[2] == list[3] \
                        or list[0] == list[4] and list[4] == list[2] and list[2] == list[3] \
                        or list[0] == list[1] and list[1] == list[4] and list[4] == list[3] \
                        or list[0] == list[1] and list[1] == list[2] and list[2] == list[4]:
                        FK = FK + 1
                        a5 = list[0]
                    #Checking for Four of a kind
                    if(FK > 0):
                        print "Four of a kind"
                        b = max(a1, a2, a3, a4, a5)
                        if a1 == b:
                            df1.iloc[i * 4 + k - 1, 14] = 1
                        if a2 == b:
                            df2.iloc[i * 4 + k - 1, 14] = 1
                        if a3 == b:
                            df3.iloc[i * 4 + k - 1, 14] = 1
                        if a4 == b:
                            df4.iloc[i * 4 + k - 1, 14] = 1
                        if a5 == b:
                            df5.iloc[i * 4 + k - 1, 14] = 1
                    else:
                        #Check for full house
                        FH = 0
                        a1i = 0
                        a1ii = 0
                        a2i = 0
                        a2ii = 0
                        a3i = 0
                        a3ii = 0
                        a4i = 0
                        a4ii = 0
                        a5i = 0
                        a5ii = 0
                        # Evaluate for P1
                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                        if list[0] == list[1] and list[1] == list[2] and list[3] == list[4]:
                            a1i = list[0]
                            a1ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[3] and list[2] == list[4]:
                            a1i = list[0]
                            a1ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[4] and list[3] == list[2]:
                            a1i = list[0]
                            a1ii = list[2]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[2] and list[1] == list[4]:
                            a1i = list[0]
                            a1ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[4] and list[4] == list[2] and list[3] == list[1]:
                            a1i = list[0]
                            a1ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[2] and list[0] == list[4]:
                            a1i = list[3]
                            a1ii = list[4]
                            FH = FH + 1
                        elif list[4] == list[1] and list[1] == list[2] and list[3] == list[0]:
                            a1i = list[4]
                            a1ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[4] and list[1] == list[2]:
                            a1i = list[0]
                            a1ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[4] and list[2] == list[0]:
                            a1i = list[3]
                            a1ii = list[2]
                            FH = FH + 1
                        elif list[3] == list[4] and list[4] == list[2] and list[0] == list[1]:
                            a1i = list[3]
                            a1ii = list[1]
                            FH = FH + 1
                        # Evaluate for P2
                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                        if list[0] == list[1] and list[1] == list[2] and list[3] == list[4]:
                            a2i = list[0]
                            a2ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[3] and list[2] == list[4]:
                            a2i = list[0]
                            a2ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[4] and list[3] == list[2]:
                            a2i = list[0]
                            a2ii = list[2]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[2] and list[1] == list[4]:
                            a2i = list[0]
                            a2ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[4] and list[4] == list[2] and list[3] == list[1]:
                            a2i = list[0]
                            a2ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[2] and list[0] == list[4]:
                            a2i = list[3]
                            a2ii = list[4]
                            FH = FH + 1
                        elif list[4] == list[1] and list[1] == list[2] and list[3] == list[0]:
                            a2i = list[4]
                            a2ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[4] and list[1] == list[2]:
                            a2i = list[0]
                            a2ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[4] and list[2] == list[0]:
                            a2i = list[3]
                            a2ii = list[2]
                            FH = FH + 1
                        elif list[3] == list[4] and list[4] == list[2] and list[0] == list[1]:
                            a2i = list[3]
                            a2ii = list[1]
                            FH = FH + 1
                        # Evaluate for P3
                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                        if list[0] == list[1] and list[1] == list[2] and list[3] == list[4]:
                            a3i = list[0]
                            a3ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[3] and list[2] == list[4]:
                            a3i = list[0]
                            a3ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[4] and list[3] == list[2]:
                            a3i = list[0]
                            a3ii = list[2]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[2] and list[1] == list[4]:
                            a3i = list[0]
                            a3ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[4] and list[4] == list[2] and list[3] == list[1]:
                            a3i = list[0]
                            a3ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[2] and list[0] == list[4]:
                            a3i = list[3]
                            a3ii = list[4]
                            FH = FH + 1
                        elif list[4] == list[1] and list[1] == list[2] and list[3] == list[0]:
                            a3i = list[4]
                            a3ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[4] and list[1] == list[2]:
                            a3i = list[0]
                            a3ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[4] and list[2] == list[0]:
                            a3i = list[3]
                            a3ii = list[2]
                            FH = FH + 1
                        elif list[3] == list[4] and list[4] == list[2] and list[0] == list[1]:
                            a3i = list[3]
                            a3ii = list[1]
                            FH = FH + 1
                        # Evaluate for P4
                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                        if list[0] == list[1] and list[1] == list[2] and list[3] == list[4]:
                            a4i = list[0]
                            a4ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[3] and list[2] == list[4]:
                            a4i = list[0]
                            a4ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[4] and list[3] == list[2]:
                            a4i = list[0]
                            a4ii = list[2]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[2] and list[1] == list[4]:
                            a4i = list[0]
                            a4ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[4] and list[4] == list[2] and list[3] == list[1]:
                            a4i = list[0]
                            a4ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[2] and list[0] == list[4]:
                            a4i = list[3]
                            a4ii = list[4]
                            FH = FH + 1
                        elif list[4] == list[1] and list[1] == list[2] and list[3] == list[0]:
                            a4i = list[4]
                            a4ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[4] and list[1] == list[2]:
                            a4i = list[0]
                            a4ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[4] and list[2] == list[0]:
                            a4i = list[3]
                            a4ii = list[2]
                            FH = FH + 1
                        elif list[3] == list[4] and list[4] == list[2] and list[0] == list[1]:
                            a4i = list[3]
                            a4ii = list[1]
                            FH = FH + 1
                        # Evaluate for P5
                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                        if list[0] == list[1] and list[1] == list[2] and list[3] == list[4]:
                            a5i = list[0]
                            a5ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[3] and list[2] == list[4]:
                            a5i = list[0]
                            a5ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[1] and list[1] == list[4] and list[3] == list[2]:
                            a5i = list[0]
                            a5ii = list[2]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[2] and list[1] == list[4]:
                            a5i = list[0]
                            a5ii = list[4]
                            FH = FH + 1
                        elif list[0] == list[4] and list[4] == list[2] and list[3] == list[1]:
                            a5i = list[0]
                            a5ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[2] and list[0] == list[4]:
                            a5i = list[3]
                            a5ii = list[4]
                            FH = FH + 1
                        elif list[4] == list[1] and list[1] == list[2] and list[3] == list[0]:
                            a5i = list[4]
                            a5ii = list[3]
                            FH = FH + 1
                        elif list[0] == list[3] and list[3] == list[4] and list[1] == list[2]:
                            a5i = list[0]
                            a5ii = list[1]
                            FH = FH + 1
                        elif list[3] == list[1] and list[1] == list[4] and list[2] == list[0]:
                            a5i = list[3]
                            a5ii = list[2]
                            FH = FH + 1
                        elif list[3] == list[4] and list[4] == list[2] and list[0] == list[1]:
                            a5i = list[3]
                            a5ii = list[1]
                            FH = FH + 1
                        #Evaluating for Full House
                        if (FH > 1):
                            print "Full House"
                            b = max(a1i, a2i, a3i, a4i, a5i)
                            c = 0
                            if a1i == b:
                                c = c + 1
                            elif a2i == b:
                                c = c + 1
                            elif a3i == b:
                                c = c + 1
                            elif a4i == b:
                                c = c + 1
                            elif a5i == b:
                                c = c + 1
                            if c > 1:
                                print "Full House"
                                b = max(a1ii, a2ii, a3ii, a4ii, a5ii)
                                if a1ii == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                if a2ii == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                if a3ii == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                if a4ii == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                if a5ii == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                print "Full House"
                                b = max(a1i, a2i, a3i, a4i, a5i)
                                if a1i == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                if a2i == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                if a3i == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                if a4i == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                if a5i == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                        elif (FH == 1):
                            print "Full House"
                            b = max(a1i,a2i,a3i,a4i,a5i)
                            if a1i == b:
                                df1.iloc[i * 4 + k - 1, 14] = 1
                            elif a2i == b:
                                df2.iloc[i * 4 + k - 1, 14] = 1
                            elif a3i == b:
                                df3.iloc[i * 4 + k - 1, 14] = 1
                            elif a4i == b:
                                df4.iloc[i * 4 + k - 1, 14] = 1
                            elif a5i == b:
                                df5.iloc[i * 4 + k - 1, 14] = 1
                        else:
                            #Evaluate for Flush
                            F = 0
                            a1 = 0
                            a2 = 0
                            a3 = 0
                            a4 = 0
                            a5 = 0
                            #Evaluate P1
                            list[0] = df1.iloc[i * 4 + k - 1, 0]
                            list[1] = df1.iloc[i * 4 + k - 1, 2]
                            list[2] = df1.iloc[i * 4 + k - 1, 4]
                            list[3] = df1.iloc[i * 4 + k - 1, 6]
                            list[4] = df1.iloc[i * 4 + k - 1, 8]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3], df1.iloc[i * 4 + k - 1, 5],
                                            df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 9])
                            # Evaluate P2
                            list[0] = df2.iloc[i * 4 + k - 1, 0]
                            list[1] = df2.iloc[i * 4 + k - 1, 2]
                            list[2] = df2.iloc[i * 4 + k - 1, 4]
                            list[3] = df2.iloc[i * 4 + k - 1, 6]
                            list[4] = df2.iloc[i * 4 + k - 1, 8]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3], df2.iloc[i * 4 + k - 1, 5],
                                            df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 9])
                            # Evaluate P3
                            list[0] = df3.iloc[i * 4 + k - 1, 0]
                            list[1] = df3.iloc[i * 4 + k - 1, 2]
                            list[2] = df3.iloc[i * 4 + k - 1, 4]
                            list[3] = df3.iloc[i * 4 + k - 1, 6]
                            list[4] = df3.iloc[i * 4 + k - 1, 8]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == \
                                    list[4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3], df3.iloc[i * 4 + k - 1, 5],
                                            df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 9])
                            # Evaluate P4
                            list[0] = df4.iloc[i * 4 + k - 1, 0]
                            list[1] = df4.iloc[i * 4 + k - 1, 2]
                            list[2] = df4.iloc[i * 4 + k - 1, 4]
                            list[3] = df4.iloc[i * 4 + k - 1, 6]
                            list[4] = df4.iloc[i * 4 + k - 1, 8]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[
                                3] == list[4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3], df4.iloc[i * 4 + k - 1, 5],
                                            df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 9])
                            # Evaluate P5
                            list[0] = df5.iloc[i * 4 + k - 1, 0]
                            list[1] = df5.iloc[i * 4 + k - 1, 2]
                            list[2] = df5.iloc[i * 4 + k - 1, 4]
                            list[3] = df5.iloc[i * 4 + k - 1, 6]
                            list[4] = df5.iloc[i * 4 + k - 1, 8]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and \
                                            list[3] == list[4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3], df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 9])
                            if F > 0:
                                print "Flush"
                                b = max(a1, a2, a3, a4, a5)
                                if a1 == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                elif a2 == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                elif a3 == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                elif a4 == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                elif a5 == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                #Check for Straight
                                SF = 0
                                a1 = 0
                                a2 = 0
                                a3 = 0
                                a4 = 0
                                a5 = 0
                                # P1 Evaluation
                                # With Ace Low
                                list[0] = df1.iloc[i * 4 + k - 1, 1]
                                list[1] = df1.iloc[i * 4 + k - 1, 3]
                                list[2] = df1.iloc[i * 4 + k - 1, 5]
                                list[3] = df1.iloc[i * 4 + k - 1, 7]
                                list[4] = df1.iloc[i * 4 + k - 1, 9]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                for m in range(0, 5):
                                    if list[m] == 1:
                                        list[m] = 14
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P2 Evaluation
                                # With Ace Low
                                list[0] = df2.iloc[i * 4 + k - 1, 1]
                                list[1] = df2.iloc[i * 4 + k - 1, 3]
                                list[2] = df2.iloc[i * 4 + k - 1, 5]
                                list[3] = df2.iloc[i * 4 + k - 1, 7]
                                list[4] = df2.iloc[i * 4 + k - 1, 9]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                for m in range(0, 5):
                                    if list[m] == 1:
                                        list[m] = 14
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P3 Evaluation
                                # With Ace Low
                                list[0] = df3.iloc[i * 4 + k - 1, 1]
                                list[1] = df3.iloc[i * 4 + k - 1, 3]
                                list[2] = df3.iloc[i * 4 + k - 1, 5]
                                list[3] = df3.iloc[i * 4 + k - 1, 7]
                                list[4] = df3.iloc[i * 4 + k - 1, 9]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[
                                                    4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                for m in range(0, 5):
                                    if list[m] == 1:
                                        list[m] = 14
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P4 Evaluation
                                # With Ace Low
                                list[0] = df4.iloc[i * 4 + k - 1, 1]
                                list[1] = df4.iloc[i * 4 + k - 1, 3]
                                list[2] = df4.iloc[i * 4 + k - 1, 5]
                                list[3] = df4.iloc[i * 4 + k - 1, 7]
                                list[4] = df4.iloc[i * 4 + k - 1, 9]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                for m in range(0, 5):
                                    if list[m] == 1:
                                        list[m] = 14
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P5 Evaluation
                                # With Ace Low
                                list[0] = df5.iloc[i * 4 + k - 1, 1]
                                list[1] = df5.iloc[i * 4 + k - 1, 3]
                                list[2] = df5.iloc[i * 4 + k - 1, 5]
                                list[3] = df5.iloc[i * 4 + k - 1, 7]
                                list[4] = df5.iloc[i * 4 + k - 1, 9]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                for m in range(0, 5):
                                    if list[m] == 1:
                                        list[m] = 14
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # Check for Straight
                                if (SF > 0):
                                    print "Straight"
                                    b = max(a1, a2, a3, a4, a5)
                                    if a1 == b:
                                        df1.iloc[i * 4 + k - 1, 14] = 1
                                    if a2 == b:
                                        df2.iloc[i * 4 + k - 1, 14] = 1
                                    if a3 == b:
                                        df3.iloc[i * 4 + k - 1, 14] = 1
                                    if a4 == b:
                                        df4.iloc[i * 4 + k - 1, 14] = 1
                                    if a5 == b:
                                        df5.iloc[i * 4 + k - 1, 14] = 1
                                else:
                                    #Check for 3 of a kind
                                    FH = 0
                                    a1i = 0
                                    a2i = 0
                                    a3i = 0
                                    a4i = 0
                                    a5i = 0
                                    # Evaluate for P1
                                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                                    if list[0] == list[1] and list[1] == list[2]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[3]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[4]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[2]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[4] and list[4] == list[2]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[2]:
                                        a1i = list[3]
                                        FH = FH + 1
                                    elif list[4] == list[1] and list[1] == list[2]:
                                        a1i = list[4]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[4]:
                                        a1i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[4]:
                                        a1i = list[3]
                                        FH = FH + 1
                                    # Evaluate for P2
                                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                                    if list[0] == list[1] and list[1] == list[2]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[3]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[4]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[2]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[4] and list[4] == list[2]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[2]:
                                        a2i = list[3]
                                        FH = FH + 1
                                    elif list[4] == list[1] and list[1] == list[2]:
                                        a2i = list[4]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[4]:
                                        a2i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[4]:
                                        a2i = list[3]
                                        FH = FH + 1
                                    # Evaluate for P3
                                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                                    if list[0] == list[1] and list[1] == list[2]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[3]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[4]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[2]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[4] and list[4] == list[2]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[2]:
                                        a3i = list[3]
                                        FH = FH + 1
                                    elif list[4] == list[1] and list[1] == list[2]:
                                        a3i = list[4]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[4]:
                                        a3i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[4]:
                                        a3i = list[3]
                                        FH = FH + 1
                                    # Evaluate for P4
                                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                                    if list[0] == list[1] and list[1] == list[2]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[3]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[4]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[2]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[4] and list[4] == list[2]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[2]:
                                        a4i = list[3]
                                        FH = FH + 1
                                    elif list[4] == list[1] and list[1] == list[2]:
                                        a4i = list[4]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[4]:
                                        a4i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[4]:
                                        a4i = list[3]
                                        FH = FH + 1
                                    # Evaluate for P5
                                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                                    if list[0] == list[1] and list[1] == list[2]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[3]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[1] and list[1] == list[4]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[2]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[0] == list[4] and list[4] == list[2]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[2]:
                                        a5i = list[3]
                                        FH = FH + 1
                                    elif list[4] == list[1] and list[1]:
                                        a5i = list[4]
                                        FH = FH + 1
                                    elif list[0] == list[3] and list[3] == list[4]:
                                        a5i = list[0]
                                        FH = FH + 1
                                    elif list[3] == list[1] and list[1] == list[4]:
                                        a5i = list[3]
                                        FH = FH + 1
                                    # Evaluating for 3 of a kind
                                    if (FH > 0):
                                        print "3 of a kind"
                                        if a1i == a2i and a1i != 0:
                                            b = max (df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                     df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],)
                                            if b == df1.iloc[i * 4 + k - 1, 1] or b == df1.iloc[i * 4 + k - 1, 3]:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                        elif a1i == a3i and a1i != 0:
                                            b = max (df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                     df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],)
                                            if b == df1.iloc[i * 4 + k - 1, 1] or b == df1.iloc[i * 4 + k - 1, 3]:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                        elif a1i == a4i and a1i != 0:
                                            b = max (df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                     df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],)
                                            if b == df1.iloc[i * 4 + k - 1, 1] or b == df1.iloc[i * 4 + k - 1, 3]:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                        elif a1i == a5i and a1i != 0:
                                            b = max (df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                     df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],)
                                            if b == df1.iloc[i * 4 + k - 1, 1] or b == df1.iloc[i * 4 + k - 1, 3]:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        elif a2i == a3i and a2i != 0:
                                            b = max (df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                     df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],)
                                            if b == df2.iloc[i * 4 + k - 1, 1] or b == df2.iloc[i * 4 + k - 1, 3]:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                        elif a2i == a4i and a2i != 0:
                                            b = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                    df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3], )
                                            if b == df2.iloc[i * 4 + k - 1, 1] or b == df2.iloc[i * 4 + k - 1, 3]:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                        elif a2i == a5i and a2i != 0:
                                            b = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                    df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3], )
                                            if b == df2.iloc[i * 4 + k - 1, 1] or b == df2.iloc[i * 4 + k - 1, 3]:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        elif a3i == a4i and a3i != 0:
                                            b = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                                    df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3], )
                                            if b == df3.iloc[i * 4 + k - 1, 1] or b == df3.iloc[i * 4 + k - 1, 3]:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                        elif a3i == a5i and a3i != 0:
                                            b = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                                    df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3], )
                                            if b == df3.iloc[i * 4 + k - 1, 1] or b == df3.iloc[i * 4 + k - 1, 3]:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        elif a4i == a5i and a4i != 0:
                                            b = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                                    df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3], )
                                            if b == df4.iloc[i * 4 + k - 1, 1] or b == df4.iloc[i * 4 + k - 1, 3]:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            else:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        else:
                                            b = max(a1i, a2i, a3i, a4i, a5i)
                                            if a1i == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            elif a2i == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            elif a3i == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            elif a4i == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            elif a5i == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                    else:
                                        #Evaluate for two pair and one pair
                                        f1 = [0]
                                        f2 = [0]
                                        f3 = [0]
                                        f4 = [0]
                                        f5 = [0]
                                        a1 = [0]
                                        a2 = [0]
                                        a3 = [0]
                                        a4 = [0]
                                        a5 = [0]
                                        Fin = 0
                                        # Evaluate P1
                                        TP1 = 0
                                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                                        if (list[0] == list[2] or list[0] == list[3] or list[
                                            0] == list[4]):
                                            TP1 = TP1 + 1
                                            f1.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if TP1 > 1:
                                            f1 = np.sort(f1[::-1]).tolist()
                                            a1.append(f1[0])
                                            a1.append(f1[1])
                                            Fin = Fin + 1
                                        # Evaluate P2
                                        TP2 = 0
                                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                                        if (list[0] == list[2] or list[0] == list[3] or
                                                    list[0] == list[4]):
                                            TP2 = TP2 + 1
                                            f2.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4]):
                                            TP2 = TP2 + 1
                                            f2.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f2.append(list[1])
                                        if TP2 > 1:
                                            f2 = np.sort(f2[::-1]).tolist()
                                            a2.append(f2[0])
                                            a2.append(f2[1])
                                            Fin = Fin + 1
                                        # Evaluate P3
                                        TP3 = 0
                                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                                        if (list[0] == list[2] or list[0] == list[
                                            3] or list[0] == list[4]):
                                            TP3 = TP3 + 1
                                            f3.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4]):
                                            TP3 = TP3 + 1
                                            f3.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f3.append(list[1])
                                        if TP3 > 1:
                                            f3 = np.sort(f3[::-1]).tolist()
                                            a3.append(f3[0])
                                            a3.append(f3[1])
                                            Fin = Fin + 1
                                        # Evaluate P4
                                        TP4 = 0
                                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                                        if (list[0] == list[2] or list[0] == list[
                                            3] or list[0] == list[4]):
                                            TP4 = TP4 + 1
                                            f4.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[
                                            4]):
                                            TP4 = TP4 + 1
                                            f4.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f4.append(list[1])
                                        if TP4 > 1:
                                            f4 = np.sort(f4[::-1]).tolist()
                                            a4.append(f4[0])
                                            a4.append(f4[1])
                                            Fin = Fin + 1
                                        # Evaluate P5
                                        TP5 = 0
                                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                                        if (list[0] == list[2] or list[0] ==
                                            list[3] or list[0] == list[4]):
                                            TP5 = TP5 + 1
                                            f5.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] ==
                                            list[4]):
                                            TP5 = TP5 + 1
                                            f5.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f5.append(list[1])
                                        if TP5 > 1:
                                            f5 = np.sort(f5[::-1]).tolist()
                                            a5.append(f5[0])
                                            a5.append(f5[1])
                                            Fin = Fin + 1
                                        #Check for two pair
                                        if Fin > 0:
                                            print "Two pair"
                                            b = max(max(a1),max(a2),max(a3),max(a4),max(a5))
                                            if max(a1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        #Check for one pair
                                        elif TP1+TP2+TP3+TP4+TP5 > 0:
                                            print "One pair"
                                            b = max(max(f1),max(f2),max(f3),max(f4),max(f5))
                                            if max(f1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        else:
                                            #Find the high card
                                            print "High Card"
                                            winner = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                         df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                         df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                                         df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                                         df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3], )
                                            if df1.iloc[i * 4 + k - 1, 1] == winner or df1.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if df2.iloc[i * 4 + k - 1, 1] == winner or df2.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if df3.iloc[i * 4 + k - 1, 1] == winner or df3.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if df4.iloc[i * 4 + k - 1, 1] == winner or df4.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if df5.iloc[i * 4 + k - 1, 1] == winner or df5.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df5.iloc[i * 4 + k - 1, 14] = 1

            # Create Turn Round
            if k == 3:
                df1.loc[i * 4 + k - 1] = df1.loc[i * 4 + k - 2]
                df2.loc[i * 4 + k - 1] = df2.loc[i * 4 + k - 2]
                df3.loc[i * 4 + k - 1] = df3.loc[i * 4 + k - 2]
                df4.loc[i * 4 + k - 1] = df4.loc[i * 4 + k - 2]
                df5.loc[i * 4 + k - 1] = df5.loc[i * 4 + k - 2]
                while x == 0:
                    print "Step 13"
                    #Generate 4th community card or the turn
                    df1.iloc[i * 4 + k - 1][10] = random.randrange(1, 5)
                    df1.iloc[i * 4 + k - 1][11] = random.randrange(2, 15)
                    df2.iloc[i * 4 + k - 1][10] = df1.iloc[i * 4 + k - 1][10]
                    df2.iloc[i * 4 + k - 1][11] = df1.iloc[i * 4 + k - 1][11]
                    df3.iloc[i * 4 + k - 1][10] = df1.iloc[i * 4 + k - 1][10]
                    df3.iloc[i * 4 + k - 1][11] = df1.iloc[i * 4 + k - 1][11]
                    df4.iloc[i * 4 + k - 1][10] = df1.iloc[i * 4 + k - 1][10]
                    df4.iloc[i * 4 + k - 1][11] = df1.iloc[i * 4 + k - 1][11]
                    df5.iloc[i * 4 + k - 1][10] = df1.iloc[i * 4 + k - 1][10]
                    df5.iloc[i * 4 + k - 1][11] = df1.iloc[i * 4 + k - 1][11]
                    # Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k - 1, 10] == df1.iloc[i * 4 + k - 1, 8] and df1.iloc[i * 4 + k - 1, 11] ==
                        df1.iloc[i * 4 + k - 1, 9]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df1.iloc[i * 4 + k - 1, 6] and df1.iloc[
                                            i * 4 + k - 1, 11] == df1.iloc[i * 4 + k - 1, 7]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df1.iloc[i * 4 + k - 1, 4] and df1.iloc[
                                            i * 4 + k - 1, 11] == df1.iloc[i * 4 + k - 1, 5]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df1.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 11] == df1.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df1.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 11] == df1.iloc[i * 4 + k - 1, 1])\
                            or (df1.iloc[i * 4 + k - 1, 10] == df2.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 11] == df2.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 10] == df3.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 11] == df3.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 10] == df4.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 11] == df4.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 10] == df5.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 11] == df5.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df2.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 11] == df2.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df3.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 11] == df3.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df4.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 11] == df4.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 10] == df5.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 11] == df5.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1

                #Evaluate turn round
                list = [[-1,-1],
                        [-1, -1],
                        [-1, -1],
                        [-1,-1],
                        [-1, -1],
                        [-1, -1]]

                df1.iloc[i * 4 + k - 1, 14] = 0
                df2.iloc[i * 4 + k - 1, 14] = 0
                df3.iloc[i * 4 + k - 1, 14] = 0
                df4.iloc[i * 4 + k - 1, 14] = 0
                df5.iloc[i * 4 + k - 1, 14] = 0
                # Straight Flush Evaluation
                SF = 0
                a1 = 0
                a2 = 0
                a3 = 0
                a4 = 0
                a5 = 0
                # P1 Evaluation
                #With Ace Low
                list[0] = [df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 0]]
                list[1] = [df1.iloc[i * 4 + k - 1, 3], df1.iloc[i * 4 + k - 1, 2]]
                list[2] = [df1.iloc[i * 4 + k - 1, 5], df1.iloc[i * 4 + k - 1, 4]]
                list[3] = [df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 6]]
                list[4] = [df1.iloc[i * 4 + k - 1, 9], df1.iloc[i * 4 + k - 1, 8]]
                list[5] = [df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 10]]
                for m in range(0, 6):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a1 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a1 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 0]]
                list[1] = [df1.iloc[i * 4 + k - 1, 3], df1.iloc[i * 4 + k - 1, 2]]
                list[2] = [df1.iloc[i * 4 + k - 1, 5], df1.iloc[i * 4 + k - 1, 4]]
                list[3] = [df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 6]]
                list[4] = [df1.iloc[i * 4 + k - 1, 9], df1.iloc[i * 4 + k - 1, 8]]
                list[5] = [df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 10]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a1 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a1 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P2 Evaluation
                #With Ace Low
                list[0] = [df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 0]]
                list[1] = [df2.iloc[i * 4 + k - 1, 3], df2.iloc[i * 4 + k - 1, 2]]
                list[2] = [df2.iloc[i * 4 + k - 1, 5], df2.iloc[i * 4 + k - 1, 4]]
                list[3] = [df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 6]]
                list[4] = [df2.iloc[i * 4 + k - 1, 9], df2.iloc[i * 4 + k - 1, 8]]
                list[5] = [df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 10]]
                for m in range(0, 6):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a2 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a2 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 0]]
                list[1] = [df2.iloc[i * 4 + k - 1, 3], df2.iloc[i * 4 + k - 1, 2]]
                list[2] = [df2.iloc[i * 4 + k - 1, 5], df2.iloc[i * 4 + k - 1, 4]]
                list[3] = [df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 6]]
                list[4] = [df2.iloc[i * 4 + k - 1, 9], df2.iloc[i * 4 + k - 1, 8]]
                list[5] = [df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 10]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a2 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a2 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P3 Evaluation
                #With Ace Low
                list[0] = [df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 0]]
                list[1] = [df3.iloc[i * 4 + k - 1, 3], df3.iloc[i * 4 + k - 1, 2]]
                list[2] = [df3.iloc[i * 4 + k - 1, 5], df3.iloc[i * 4 + k - 1, 4]]
                list[3] = [df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 6]]
                list[4] = [df3.iloc[i * 4 + k - 1, 9], df3.iloc[i * 4 + k - 1, 8]]
                list[5] = [df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 10]]
                for m in range(0, 6):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a3 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a3 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 0]]
                list[1] = [df3.iloc[i * 4 + k - 1, 3], df3.iloc[i * 4 + k - 1, 2]]
                list[2] = [df3.iloc[i * 4 + k - 1, 5], df3.iloc[i * 4 + k - 1, 4]]
                list[3] = [df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 6]]
                list[4] = [df3.iloc[i * 4 + k - 1, 9], df3.iloc[i * 4 + k - 1, 8]]
                list[5] = [df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 10]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a3 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a3 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P4 Evaluation
                #With Ace Low
                list[0] = [df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 0]]
                list[1] = [df4.iloc[i * 4 + k - 1, 3], df4.iloc[i * 4 + k - 1, 2]]
                list[2] = [df4.iloc[i * 4 + k - 1, 5], df4.iloc[i * 4 + k - 1, 4]]
                list[3] = [df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 6]]
                list[4] = [df4.iloc[i * 4 + k - 1, 9], df4.iloc[i * 4 + k - 1, 8]]
                list[5] = [df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 10]]
                for m in range(0, 6):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a4 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a4 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 0]]
                list[1] = [df4.iloc[i * 4 + k - 1, 3], df4.iloc[i * 4 + k - 1, 2]]
                list[2] = [df4.iloc[i * 4 + k - 1, 5], df4.iloc[i * 4 + k - 1, 4]]
                list[3] = [df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 6]]
                list[4] = [df4.iloc[i * 4 + k - 1, 9], df4.iloc[i * 4 + k - 1, 8]]
                list[5] = [df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 10]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a4 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a4 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P5 Evaluation
                #With Ace Low
                list[0] = [df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 0]]
                list[1] = [df5.iloc[i * 4 + k - 1, 3], df5.iloc[i * 4 + k - 1, 2]]
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                for m in range(0, 6):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a5 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a5 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 0]]
                list[1] = [df5.iloc[i * 4 + k - 1, 3], df5.iloc[i * 4 + k - 1, 2]]
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a5 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a5 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # Check for Straight flush
                if (SF > 0):
                    print "Straight Flush"
                    b = max(a1, a2, a3, a4, a5)
                    if a1 == b:
                        df1.iloc[i * 4 + k - 1, 14] = 1
                    if a2 == b:
                        df2.iloc[i * 4 + k - 1, 14] = 1
                    if a3 == b:
                        df3.iloc[i * 4 + k - 1, 14] = 1
                    if a4 == b:
                        df4.iloc[i * 4 + k - 1, 14] = 1
                    if a5 == b:
                        df5.iloc[i * 4 + k - 1, 14] = 1
                else:
                    # Check for four of a kind
                    FK = 0
                    a1 = 0
                    a2 = 0
                    a3 = 0
                    a4 = 0
                    a5 = 0
                    # Evaluate for P1
                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                    list[5] = df1.iloc[i * 4 + k - 1, 11]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a1 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P2
                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                    list[5] = df2.iloc[i * 4 + k - 1, 11]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a2 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P3
                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                    list[5] = df3.iloc[i * 4 + k - 1, 11]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a3 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P4
                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                    list[5] = df4.iloc[i * 4 + k - 1, 11]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a4 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P5
                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                    list[5] = df5.iloc[i * 4 + k - 1, 11]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a5 = m
                                break
                        if count == 4:
                            break
                    # Checking for Four of a kind
                    if (FK > 0):
                        print "Four of a kind"
                        b = max(a1, a2, a3, a4, a5)
                        if a1 == b:
                            df1.iloc[i * 4 + k - 1, 14] = 1
                        if a2 == b:
                            df2.iloc[i * 4 + k - 1, 14] = 1
                        if a3 == b:
                            df3.iloc[i * 4 + k - 1, 14] = 1
                        if a4 == b:
                            df4.iloc[i * 4 + k - 1, 14] = 1
                        if a5 == b:
                            df5.iloc[i * 4 + k - 1, 14] = 1
                    else:
                        # Check for full house
                        FH = 0
                        a1i = 0
                        a1ii = 0
                        a2i = 0
                        a2ii = 0
                        a3i = 0
                        a3ii = 0
                        a4i = 0
                        a4ii = 0
                        a5i = 0
                        a5ii = 0
                        # Evaluate for P1
                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                        list[5] = df1.iloc[i * 4 + k - 1, 11]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a1i = m
                                                a1ii = n
                                                break
                            if count == 2:
                                break
                        # Evaluate for P2
                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                        list[5] = df2.iloc[i * 4 + k - 1, 11]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a2i = m
                                                a2ii = n
                                                break
                        # Evaluate for P3
                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                        list[5] = df3.iloc[i * 4 + k - 1, 11]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a3i = m
                                                a3ii = n
                                                break
                        # Evaluate for P4
                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                        list[5] = df4.iloc[i * 4 + k - 1, 11]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a4i = m
                                                a4ii = n
                                                break
                        # Evaluate for P5
                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                        list[5] = df5.iloc[i * 4 + k - 1, 11]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a5i = m
                                                a5ii = n
                                                break
                        # Evaluating for Full House
                        if (FH > 1):
                            print "Full House"
                            b = max(a1i, a2i, a3i, a4i, a5i)
                            c = 0
                            if a1i == b:
                                c = c + 1
                            if a2i == b:
                                c = c + 1
                            if a3i == b:
                                c = c + 1
                            if a4i == b:
                                c = c + 1
                            if a5i == b:
                                c = c + 1
                            if c > 1:
                                b = max(a1ii, a2ii, a3ii, a4ii, a5ii)
                                if a1ii == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                if a2ii == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                if a3ii == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                if a4ii == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                if a5ii == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                b = max(a1i, a2i, a3i, a4i, a5i)
                                if a1i == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                elif a2i == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                elif a3i == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                elif a4i == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                elif a5i == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                        elif (FH == 1):
                            print "Full House"
                            b = max(a1i, a2i, a3i, a4i, a5i)
                            if a1i == b:
                                df1.iloc[i * 4 + k - 1, 14] = 1
                            elif a2i == b:
                                df2.iloc[i * 4 + k - 1, 14] = 1
                            elif a3i == b:
                                df3.iloc[i * 4 + k - 1, 14] = 1
                            elif a4i == b:
                                df4.iloc[i * 4 + k - 1, 14] = 1
                            elif a5i == b:
                                df5.iloc[i * 4 + k - 1, 14] = 1
                        else:
                            # Evaluate for Flush
                            F = 0
                            a1 = 0
                            a2 = 0
                            a3 = 0
                            a4 = 0
                            a5 = 0
                            # Evaluate P1
                            list[0] = df1.iloc[i * 4 + k - 1, 0]
                            list[1] = df1.iloc[i * 4 + k - 1, 2]
                            list[2] = df1.iloc[i * 4 + k - 1, 4]
                            list[3] = df1.iloc[i * 4 + k - 1, 6]
                            list[4] = df1.iloc[i * 4 + k - 1, 8]
                            list[5] = df1.iloc[i * 4 + k - 1, 10]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                         df1.iloc[i * 4 + k - 1, 5],
                                         df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 9])
                            elif list[5] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 3],
                                         df1.iloc[i * 4 + k - 1, 5],
                                         df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[5] and list[5] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 11],
                                         df1.iloc[i * 4 + k - 1, 5],
                                         df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[5] and list[5] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                         df1.iloc[i * 4 + k - 1, 11],
                                         df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[5] and list[5] == list[4]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                         df1.iloc[i * 4 + k - 1, 5],
                                         df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[5]:
                                F = F + 1
                                a1 = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                         df1.iloc[i * 4 + k - 1, 5],
                                         df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 11])
                            # Evaluate P2
                            list[0] = df2.iloc[i * 4 + k - 1, 0]
                            list[1] = df2.iloc[i * 4 + k - 1, 2]
                            list[2] = df2.iloc[i * 4 + k - 1, 4]
                            list[3] = df2.iloc[i * 4 + k - 1, 6]
                            list[4] = df2.iloc[i * 4 + k - 1, 8]
                            list[5] = df2.iloc[i * 4 + k - 1, 10]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                         df2.iloc[i * 4 + k - 1, 5],
                                         df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 9])
                            elif list[5] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 3],
                                         df2.iloc[i * 4 + k - 1, 5],
                                         df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[5] and list[5] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 11],
                                         df2.iloc[i * 4 + k - 1, 5],
                                         df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[5] and list[5] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                         df2.iloc[i * 4 + k - 1, 11],
                                         df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[5] and list[5] == list[
                                4]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                         df2.iloc[i * 4 + k - 1, 5],
                                         df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                5]:
                                F = F + 1
                                a2 = max(df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                         df2.iloc[i * 4 + k - 1, 5],
                                         df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 11])
                            # Evaluate P3
                            list[0] = df3.iloc[i * 4 + k - 1, 0]
                            list[1] = df3.iloc[i * 4 + k - 1, 2]
                            list[2] = df3.iloc[i * 4 + k - 1, 4]
                            list[3] = df3.iloc[i * 4 + k - 1, 6]
                            list[4] = df3.iloc[i * 4 + k - 1, 8]
                            list[5] = df3.iloc[i * 4 + k - 1, 10]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                         df3.iloc[i * 4 + k - 1, 5],
                                         df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 9])
                            elif list[5] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 3],
                                         df3.iloc[i * 4 + k - 1, 5],
                                         df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[5] and list[5] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 11],
                                         df3.iloc[i * 4 + k - 1, 5],
                                         df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[5] and list[5] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                         df3.iloc[i * 4 + k - 1, 11],
                                         df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[5] and list[5] == list[
                                4]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                         df3.iloc[i * 4 + k - 1, 5],
                                         df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                5]:
                                F = F + 1
                                a3 = max(df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                         df3.iloc[i * 4 + k - 1, 5],
                                         df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 11])
                            # Evaluate P4
                            list[0] = df4.iloc[i * 4 + k - 1, 0]
                            list[1] = df4.iloc[i * 4 + k - 1, 2]
                            list[2] = df4.iloc[i * 4 + k - 1, 4]
                            list[3] = df4.iloc[i * 4 + k - 1, 6]
                            list[4] = df4.iloc[i * 4 + k - 1, 8]
                            list[5] = df4.iloc[i * 4 + k - 1, 10]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                         df4.iloc[i * 4 + k - 1, 5],
                                         df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 9])
                            elif list[5] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 3],
                                         df4.iloc[i * 4 + k - 1, 5],
                                         df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[5] and list[5] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 11],
                                         df4.iloc[i * 4 + k - 1, 5],
                                         df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[5] and list[5] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                         df4.iloc[i * 4 + k - 1, 11],
                                         df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[5] and list[5] == list[
                                4]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                         df4.iloc[i * 4 + k - 1, 5],
                                         df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                5]:
                                F = F + 1
                                a4 = max(df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                         df4.iloc[i * 4 + k - 1, 5],
                                         df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 11])
                            # Evaluate P5
                            list[0] = df5.iloc[i * 4 + k - 1, 0]
                            list[1] = df5.iloc[i * 4 + k - 1, 2]
                            list[2] = df5.iloc[i * 4 + k - 1, 4]
                            list[3] = df5.iloc[i * 4 + k - 1, 6]
                            list[4] = df5.iloc[i * 4 + k - 1, 8]
                            list[5] = df5.iloc[i * 4 + k - 1, 10]
                            if list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],
                                         df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 9])
                            elif list[5] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 3],
                                         df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[5] and list[5] == list[2] and list[2] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 11],
                                         df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[5] and list[5] == list[3] and list[3] == list[
                                4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],
                                         df5.iloc[i * 4 + k - 1, 11],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[5] and list[5] == list[
                                4]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],
                                         df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 9])
                            elif list[0] == list[1] and list[1] == list[2] and list[2] == list[3] and list[3] == list[
                                5]:
                                F = F + 1
                                a5 = max(df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3],
                                         df5.iloc[i * 4 + k - 1, 5],
                                         df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 11])
                            if F > 0:
                                print "Flush"
                                b = max(a1, a2, a3, a4, a5)
                                if a1 == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                elif a2 == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                elif a3 == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                elif a4 == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                elif a5 == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                # Check for Straight
                                SF = 0
                                a1 = 0
                                a2 = 0
                                a3 = 0
                                a4 = 0
                                a5 = 0
                                # P1 Evaluation
                                # With Ace Low
                                list[0] = df1.iloc[i * 4 + k - 1, 1]
                                list[1] = df1.iloc[i * 4 + k - 1, 3]
                                list[2] = df1.iloc[i * 4 + k - 1, 5]
                                list[3] = df1.iloc[i * 4 + k - 1, 7]
                                list[4] = df1.iloc[i * 4 + k - 1, 9]
                                list[5] = df1.iloc[i * 4 + k - 1, 11]
                                for m in range(0, 6):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == list[5]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df1.iloc[i * 4 + k - 1, 1]
                                list[1] = df1.iloc[i * 4 + k - 1, 3]
                                list[2] = df1.iloc[i * 4 + k - 1, 5]
                                list[3] = df1.iloc[i * 4 + k - 1, 7]
                                list[4] = df1.iloc[i * 4 + k - 1, 9]
                                list[5] = df1.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == list[
                                            5]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P2 Evaluation
                                # With Ace Low
                                list[0] = df2.iloc[i * 4 + k - 1, 1]
                                list[1] = df2.iloc[i * 4 + k - 1, 3]
                                list[2] = df2.iloc[i * 4 + k - 1, 5]
                                list[3] = df2.iloc[i * 4 + k - 1, 7]
                                list[4] = df2.iloc[i * 4 + k - 1, 9]
                                list[5] = df2.iloc[i * 4 + k - 1, 11]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df2.iloc[i * 4 + k - 1, 1]
                                list[1] = df2.iloc[i * 4 + k - 1, 3]
                                list[2] = df2.iloc[i * 4 + k - 1, 5]
                                list[3] = df2.iloc[i * 4 + k - 1, 7]
                                list[4] = df2.iloc[i * 4 + k - 1, 9]
                                list[5] = df2.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1

                                # P3 Evaluation
                                # With Ace Low
                                list[0] = df3.iloc[i * 4 + k - 1, 1]
                                list[1] = df3.iloc[i * 4 + k - 1, 3]
                                list[2] = df3.iloc[i * 4 + k - 1, 5]
                                list[3] = df3.iloc[i * 4 + k - 1, 7]
                                list[4] = df3.iloc[i * 4 + k - 1, 9]
                                list[5] = df3.iloc[i * 4 + k - 1, 11]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[
                                                    4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df3.iloc[i * 4 + k - 1, 1]
                                list[1] = df3.iloc[i * 4 + k - 1, 3]
                                list[2] = df3.iloc[i * 4 + k - 1, 5]
                                list[3] = df3.iloc[i * 4 + k - 1, 7]
                                list[4] = df3.iloc[i * 4 + k - 1, 9]
                                list[5] = df3.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P4 Evaluation
                                # With Ace Low
                                list[0] = df4.iloc[i * 4 + k - 1, 1]
                                list[1] = df4.iloc[i * 4 + k - 1, 3]
                                list[2] = df4.iloc[i * 4 + k - 1, 5]
                                list[3] = df4.iloc[i * 4 + k - 1, 7]
                                list[4] = df4.iloc[i * 4 + k - 1, 9]
                                list[5] = df4.iloc[i * 4 + k - 1, 11]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df4.iloc[i * 4 + k - 1, 1]
                                list[1] = df4.iloc[i * 4 + k - 1, 3]
                                list[2] = df4.iloc[i * 4 + k - 1, 5]
                                list[3] = df4.iloc[i * 4 + k - 1, 7]
                                list[4] = df4.iloc[i * 4 + k - 1, 9]
                                list[5] = df4.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P5 Evaluation
                                # With Ace Low
                                list[0] = df5.iloc[i * 4 + k - 1, 1]
                                list[1] = df5.iloc[i * 4 + k - 1, 3]
                                list[2] = df5.iloc[i * 4 + k - 1, 5]
                                list[3] = df5.iloc[i * 4 + k - 1, 7]
                                list[4] = df5.iloc[i * 4 + k - 1, 9]
                                list[5] = df5.iloc[i * 4 + k - 1, 11]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df5.iloc[i * 4 + k - 1, 1]
                                list[1] = df5.iloc[i * 4 + k - 1, 3]
                                list[2] = df5.iloc[i * 4 + k - 1, 5]
                                list[3] = df5.iloc[i * 4 + k - 1, 7]
                                list[4] = df5.iloc[i * 4 + k - 1, 9]
                                list[5] = df5.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # Check for Straight
                                if (SF > 0):
                                    print "Straight"
                                    b = max(a1, a2, a3, a4, a5)
                                    if a1 == b:
                                        df1.iloc[i * 4 + k - 1, 14] = 1
                                    if a2 == b:
                                        df2.iloc[i * 4 + k - 1, 14] = 1
                                    if a3 == b:
                                        df3.iloc[i * 4 + k - 1, 14] = 1
                                    if a4 == b:
                                        df4.iloc[i * 4 + k - 1, 14] = 1
                                    if a5 == b:
                                        df5.iloc[i * 4 + k - 1, 14] = 1
                                else:
                                    # Check for 3 of a kind
                                    FH = 0
                                    a1i = 0
                                    a2i = 0
                                    a3i = 0
                                    a4i = 0
                                    a5i = 0
                                    # Evaluate for P1
                                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                                    list[5] = df1.iloc[i * 4 + k - 1, 11]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a1i = m
                                            break
                                    # Evaluate for P2
                                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                                    list[5] = df2.iloc[i * 4 + k - 1, 11]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a2i = m
                                            break
                                    # Evaluate for P3
                                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                                    list[5] = df3.iloc[i * 4 + k - 1, 11]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a3i = m
                                            break
                                    # Evaluate for P4
                                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                                    list[5] = df4.iloc[i * 4 + k - 1, 11]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a4i = m
                                            break
                                    # Evaluate for P5
                                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                                    list[5] = df5.iloc[i * 4 + k - 1, 11]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a5i = m
                                            break
                                    # Evaluating for 3 of a kind
                                    if (FH > 0):
                                        print "3 of a kind"
                                        b = max(a1i, a2i, a3i, a4i, a5i)
                                        if a1i == b:
                                            df1.iloc[i * 4 + k - 1, 14] = 1
                                        elif a2i == b:
                                            df2.iloc[i * 4 + k - 1, 14] = 1
                                        elif a3i == b:
                                            df3.iloc[i * 4 + k - 1, 14] = 1
                                        elif a4i == b:
                                            df4.iloc[i * 4 + k - 1, 14] = 1
                                        elif a5i == b:
                                            df5.iloc[i * 4 + k - 1, 14] = 1
                                    else:
                                        # Evaluate for two pair and one pair
                                        f1 = [0]
                                        f2 = [0]
                                        f3 = [0]
                                        f4 = [0]
                                        f5 = [0]
                                        a1 = [0]
                                        a2 = [0]
                                        a3 = [0]
                                        a4 = [0]
                                        a5 = [0]
                                        Fin = 0
                                        # Evaluate P1
                                        TP1 = 0
                                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                                        list[5] = df1.iloc[i * 4 + k - 1, 11]
                                        if (list[0] == list[2] or list[0] == list[3] or list[
                                            0] == list[4] or list[0] == list[5]):
                                            TP1 = TP1 + 1
                                            f1.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if TP1 > 1:
                                            f1 = np.sort(f1[::-1]).tolist()
                                            a1.append(f1[0])
                                            a1.append(f1[1])
                                            Fin = Fin + 1
                                        # Evaluate P2
                                        TP2 = 0
                                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                                        list[5] = df2.iloc[i * 4 + k - 1, 11]
                                        if (list[0] == list[2] or list[0] == list[3] or
                                                    list[0] == list[4] or list[0] == list[5]):
                                            TP2 = TP2 + 1
                                            f2.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5]):
                                            TP2 = TP2 + 1
                                            f2.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f2.append(list[1])
                                        if TP2 > 1:
                                            f2 = np.sort(f2[::-1]).tolist()
                                            a2.append(f2[0])
                                            a2.append(f2[1])
                                            Fin = Fin + 1
                                        # Evaluate P3
                                        TP3 = 0
                                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                                        list[5] = df3.iloc[i * 4 + k - 1, 11]
                                        if (list[0] == list[2] or list[0] == list[
                                            3] or list[0] == list[4] or list[0] == list[5]):
                                            TP3 = TP3 + 1
                                            f3.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5]):
                                            TP3 = TP3 + 1
                                            f3.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f3.append(list[1])
                                        if TP3 > 1:
                                            f3 = np.sort(f3[::-1]).tolist()
                                            a3.append(f3[0])
                                            a3.append(f3[1])
                                            Fin = Fin + 1
                                        # Evaluate P4
                                        TP4 = 0
                                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                                        list[5] = df4.iloc[i * 4 + k - 1, 11]
                                        if (list[0] == list[2] or list[0] == list[
                                            3] or list[0] == list[4] or list[0] == list[5]):
                                            TP4 = TP4 + 1
                                            f4.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[
                                            4] or list[1] == list[5]):
                                            TP4 = TP4 + 1
                                            f4.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f4.append(list[1])
                                        if TP4 > 1:
                                            f4 = np.sort(f4[::-1]).tolist()
                                            a4.append(f4[0])
                                            a4.append(f4[1])
                                            Fin = Fin + 1
                                        # Evaluate P5
                                        TP5 = 0
                                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                                        list[5] = df5.iloc[i * 4 + k - 1, 11]
                                        if (list[0] == list[2] or list[0] ==
                                            list[3] or list[0] == list[4] or list[0] == list[5]):
                                            TP5 = TP5 + 1
                                            f5.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] ==
                                            list[4] or list[1] == list[5]):
                                            TP5 = TP5 + 1
                                            f5.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f5.append(list[1])
                                        if TP5 > 1:
                                            f5 = np.sort(f5[::-1]).tolist()
                                            a5.append(f5[0])
                                            a5.append(f5[1])
                                            Fin = Fin + 1
                                        #Check for two pair
                                        if Fin > 0:
                                            print "Two pair"
                                            b = max(max(a1),max(a2),max(a3),max(a4),max(a5))
                                            if max(a1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        #Check for one pair
                                        elif TP1+TP2+TP3+TP4+TP5 > 0:
                                            print "One pair"
                                            b = max(max(f1),max(f2),max(f3),max(f4),max(f5))
                                            if max(f1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        else:
                                            # Find the high card
                                            print "High Card"
                                            winner = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                         df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                         df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                                         df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                                         df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3] )
                                            if df1.iloc[i * 4 + k - 1, 1] == winner or df1.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if df2.iloc[i * 4 + k - 1, 1] == winner or df2.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if df3.iloc[i * 4 + k - 1, 1] == winner or df3.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if df4.iloc[i * 4 + k - 1, 1] == winner or df4.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if df5.iloc[i * 4 + k - 1, 1] == winner or df5.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
            if k == 4:
                #Create the River
                df1.loc[i * 4 + k-1] = df1.loc[i * 4 + k - 2]
                df2.loc[i * 4 + k - 1] = df2.loc[i * 4 + k - 2]
                df3.loc[i * 4 + k - 1] = df3.loc[i * 4 + k - 2]
                df4.loc[i * 4 + k - 1] = df4.loc[i * 4 + k - 2]
                df5.loc[i * 4 + k - 1] = df5.loc[i * 4 + k - 2]
                while x == 0:
                    print "Step 14"
                    # Generate 5th community card or the river
                    df1.iloc[i * 4 + k-1][12] = random.randrange(1, 5)
                    df1.iloc[i * 4 + k-1][13] = random.randrange(2, 15)
                    df2.iloc[i * 4 + k - 1][12] = df1.iloc[i * 4 + k - 1][12]
                    df2.iloc[i * 4 + k - 1][13] = df1.iloc[i * 4 + k - 1][13]
                    df3.iloc[i * 4 + k - 1][12] = df1.iloc[i * 4 + k - 1][12]
                    df3.iloc[i * 4 + k - 1][13] = df1.iloc[i * 4 + k - 1][13]
                    df4.iloc[i * 4 + k - 1][12] = df1.iloc[i * 4 + k - 1][12]
                    df4.iloc[i * 4 + k - 1][13] = df1.iloc[i * 4 + k - 1][13]
                    df5.iloc[i * 4 + k - 1][12] = df1.iloc[i * 4 + k - 1][12]
                    df5.iloc[i * 4 + k - 1][13] = df1.iloc[i * 4 + k - 1][13]
                    # Check if this card is already generated in this game, then re-generate
                    if (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 10] and df1.iloc[i * 4 + k - 1, 13] ==
                        df1.iloc[i * 4 + k - 1, 11]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 8] and df1.iloc[
                                            i * 4 + k - 1, 13] == df1.iloc[i * 4 + k - 1, 9]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 6] and df1.iloc[
                                            i * 4 + k - 1, 13] == df1.iloc[i * 4 + k - 1, 7]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 4] and df1.iloc[
                                            i * 4 + k - 1, 13] == df1.iloc[i * 4 + k - 1, 5]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 13] == df1.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df1.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 13] == df1.iloc[i * 4 + k - 1, 1])\
                            or (df1.iloc[i * 4 + k - 1, 12] == df2.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 13] == df2.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 12] == df3.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 13] == df3.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 12] == df4.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 13] == df4.iloc[i * 4 + k - 1, 3])\
                            or (df1.iloc[i * 4 + k - 1, 12] == df5.iloc[i * 4 + k - 1, 2] and df1.iloc[
                                            i * 4 + k - 1, 13] == df5.iloc[i * 4 + k - 1, 3]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df2.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 13] == df2.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df3.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 13] == df3.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df4.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 13] == df4.iloc[i * 4 + k - 1, 1]) \
                            or (df1.iloc[i * 4 + k - 1, 12] == df5.iloc[i * 4 + k - 1, 0] and df1.iloc[
                                            i * 4 + k - 1, 13] == df5.iloc[i * 4 + k - 1, 1]):
                        continue
                    else:
                        x = 1
                #Evaluate river round
                list = [[-1, -1],
                        [-1, -1],
                        [-1, -1],
                        [-1, -1],
                        [-1, -1],
                        [-1, -1],
                        [-1, -1]]
                df1.iloc[i * 4 + k - 1, 14] = 0
                df2.iloc[i * 4 + k - 1, 14] = 0
                df3.iloc[i * 4 + k - 1, 14] = 0
                df4.iloc[i * 4 + k - 1, 14] = 0
                df5.iloc[i * 4 + k - 1, 14] = 0
                # Straight Flush Evaluation
                SF = 0
                a1 = 0
                a2 = 0
                a3 = 0
                a4 = 0
                a5 = 0
                # P1 Evaluation
                #With Ace Low
                list[0] = [df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 0]]
                list[1] = [df1.iloc[i * 4 + k - 1, 3], df1.iloc[i * 4 + k - 1, 2]]
                list[2] = [df1.iloc[i * 4 + k - 1, 5], df1.iloc[i * 4 + k - 1, 4]]
                list[3] = [df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 6]]
                list[4] = [df1.iloc[i * 4 + k - 1, 9], df1.iloc[i * 4 + k - 1, 8]]
                list[5] = [df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 10]]
                list[6] = [df1.iloc[i * 4 + k - 1, 13], df1.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a1 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a1 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][0] and list[5][0]+1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and list[5][1] == list[6][1]:
                    a1 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 0]]
                list[1] = [df1.iloc[i * 4 + k - 1, 3], df1.iloc[i * 4 + k - 1, 2]]
                list[2] = [df1.iloc[i * 4 + k - 1, 5], df1.iloc[i * 4 + k - 1, 4]]
                list[3] = [df1.iloc[i * 4 + k - 1, 7], df1.iloc[i * 4 + k - 1, 6]]
                list[4] = [df1.iloc[i * 4 + k - 1, 9], df1.iloc[i * 4 + k - 1, 8]]
                list[5] = [df1.iloc[i * 4 + k - 1, 11], df1.iloc[i * 4 + k - 1, 10]]
                list[6] = [df1.iloc[i * 4 + k - 1, 13], df1.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a1 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1]:
                    a1 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][0] and list[5][0]+1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and list[5][1] == list[6][1]:
                    a1 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P2 Evaluation
                # With Ace Low
                list[0] = [df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 0]]
                list[1] = [df2.iloc[i * 4 + k - 1, 3], df2.iloc[i * 4 + k - 1, 2]]
                list[2] = [df2.iloc[i * 4 + k - 1, 5], df2.iloc[i * 4 + k - 1, 4]]
                list[3] = [df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 6]]
                list[4] = [df2.iloc[i * 4 + k - 1, 9], df2.iloc[i * 4 + k - 1, 8]]
                list[5] = [df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 10]]
                list[6] = [df2.iloc[i * 4 + k - 1, 13], df2.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1]:
                    a2 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a2 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a2 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 0]]
                list[1] = [df2.iloc[i * 4 + k - 1, 3], df2.iloc[i * 4 + k - 1, 2]]
                list[2] = [df2.iloc[i * 4 + k - 1, 5], df2.iloc[i * 4 + k - 1, 4]]
                list[3] = [df2.iloc[i * 4 + k - 1, 7], df2.iloc[i * 4 + k - 1, 6]]
                list[4] = [df2.iloc[i * 4 + k - 1, 9], df2.iloc[i * 4 + k - 1, 8]]
                list[5] = [df2.iloc[i * 4 + k - 1, 11], df2.iloc[i * 4 + k - 1, 10]]
                list[6] = [df2.iloc[i * 4 + k - 1, 13], df2.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a2 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a2 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a2 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P3 Evaluation
                # With Ace Low
                list[0] = [df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 0]]
                list[1] = [df3.iloc[i * 4 + k - 1, 3], df3.iloc[i * 4 + k - 1, 2]]
                list[2] = [df3.iloc[i * 4 + k - 1, 5], df3.iloc[i * 4 + k - 1, 4]]
                list[3] = [df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 6]]
                list[4] = [df3.iloc[i * 4 + k - 1, 9], df3.iloc[i * 4 + k - 1, 8]]
                list[5] = [df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 10]]
                list[6] = [df3.iloc[i * 4 + k - 1, 13], df3.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a3 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a3 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a3 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 0]]
                list[1] = [df3.iloc[i * 4 + k - 1, 3], df3.iloc[i * 4 + k - 1, 2]]
                list[2] = [df3.iloc[i * 4 + k - 1, 5], df3.iloc[i * 4 + k - 1, 4]]
                list[3] = [df3.iloc[i * 4 + k - 1, 7], df3.iloc[i * 4 + k - 1, 6]]
                list[4] = [df3.iloc[i * 4 + k - 1, 9], df3.iloc[i * 4 + k - 1, 8]]
                list[5] = [df3.iloc[i * 4 + k - 1, 11], df3.iloc[i * 4 + k - 1, 10]]
                list[6] = [df3.iloc[i * 4 + k - 1, 13], df3.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a3 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a3 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a3 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P4 Evaluation
                # With Ace Low
                list[0] = [df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 0]]
                list[1] = [df4.iloc[i * 4 + k - 1, 3], df4.iloc[i * 4 + k - 1, 2]]
                list[2] = [df4.iloc[i * 4 + k - 1, 5], df4.iloc[i * 4 + k - 1, 4]]
                list[3] = [df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 6]]
                list[4] = [df4.iloc[i * 4 + k - 1, 9], df4.iloc[i * 4 + k - 1, 8]]
                list[5] = [df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 10]]
                list[6] = [df4.iloc[i * 4 + k - 1, 13], df4.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a4 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a4 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a4 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 0]]
                list[1] = [df4.iloc[i * 4 + k - 1, 3], df4.iloc[i * 4 + k - 1, 2]]
                list[2] = [df4.iloc[i * 4 + k - 1, 5], df4.iloc[i * 4 + k - 1, 4]]
                list[3] = [df4.iloc[i * 4 + k - 1, 7], df4.iloc[i * 4 + k - 1, 6]]
                list[4] = [df4.iloc[i * 4 + k - 1, 9], df4.iloc[i * 4 + k - 1, 8]]
                list[5] = [df4.iloc[i * 4 + k - 1, 11], df4.iloc[i * 4 + k - 1, 10]]
                list[6] = [df4.iloc[i * 4 + k - 1, 13], df4.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a4 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a4 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a4 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # P5 Evaluation
                # With Ace Low
                list[0] = [df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 0]]
                list[1] = [df5.iloc[i * 4 + k - 1, 3], df5.iloc[i * 4 + k - 1, 2]]
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                list[6] = [df5.iloc[i * 4 + k - 1, 13], df5.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a5 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a5 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a5 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # With Ace High
                list[0] = [df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 0]]
                list[1] = [df5.iloc[i * 4 + k - 1, 3], df5.iloc[i * 4 + k - 1, 2]]
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                list[6] = [df5.iloc[i * 4 + k - 1, 13], df5.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[0][0] + 1 == list[1][0] and list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][
                    0] and list[3][0] + 1 == list[
                    4][0] and list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and \
                                    list[3][1] == list[4][1]:
                    a5 = max(list[0][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[1][0] + 1 == list[2][0] and list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][
                    0] and list[4][0] + 1 == list[
                    5][0] and list[1][1] == list[2][1] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and \
                                    list[4][1] == list[5][1]:
                    a5 = max(list[5][0], list[1][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    a5 = max(list[5][0], list[6][0], list[2][0], list[3][0], list[4][0])
                    SF = SF + 1
                # Straight Flush Evaluation in community cards
                master = 0
                # With Ace Low
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                list[6] = [df5.iloc[i * 4 + k - 1, 13], df5.iloc[i * 4 + k - 1, 12]]
                for m in range(0, 7):
                    if list[m][0] == 14:
                        list[m][0] = 1
                list = sorted(list, key=lambda x: x[0])
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[
                    6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    master = 1
                # With Ace High
                list[2] = [df5.iloc[i * 4 + k - 1, 5], df5.iloc[i * 4 + k - 1, 4]]
                list[3] = [df5.iloc[i * 4 + k - 1, 7], df5.iloc[i * 4 + k - 1, 6]]
                list[4] = [df5.iloc[i * 4 + k - 1, 9], df5.iloc[i * 4 + k - 1, 8]]
                list[5] = [df5.iloc[i * 4 + k - 1, 11], df5.iloc[i * 4 + k - 1, 10]]
                list[6] = [df5.iloc[i * 4 + k - 1, 13], df5.iloc[i * 4 + k - 1, 12]]
                list = sorted(list, key=lambda x: x[0])
                if list[2][0] + 1 == list[3][0] and list[3][0] + 1 == list[4][0] and list[4][0] + 1 == list[5][
                    0] and list[5][0] + 1 == list[6][0] and list[2][1] == list[3][1] and list[3][1] == list[4][1] and list[4][1] == list[5][1] and \
                                    list[5][1] == list[6][1]:
                    master = 1
                # Check for Straight flush
                if master == 1:
                    print "Royal Flush in community cards"
                elif (SF > 0):
                    print "Straight Flush"
                    b = max(a1, a2, a3, a4, a5)
                    if a1 == b:
                        df1.iloc[i * 4 + k - 1, 14] = 1
                    if a2 == b:
                        df2.iloc[i * 4 + k - 1, 14] = 1
                    if a3 == b:
                        df3.iloc[i * 4 + k - 1, 14] = 1
                    if a4 == b:
                        df4.iloc[i * 4 + k - 1, 14] = 1
                    if a5 == b:
                        df5.iloc[i * 4 + k - 1, 14] = 1
                else:
                    # Check for four of a kind
                    FK = 0
                    a1 = 0
                    a2 = 0
                    a3 = 0
                    a4 = 0
                    a5 = 0
                    # Evaluate for P1
                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                    list[5] = df1.iloc[i * 4 + k - 1, 11]
                    list[6] = df1.iloc[i * 4 + k - 1, 13]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a1 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P2
                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                    list[5] = df2.iloc[i * 4 + k - 1, 11]
                    list[6] = df2.iloc[i * 4 + k - 1, 13]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a2 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P3
                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                    list[5] = df3.iloc[i * 4 + k - 1, 11]
                    list[6] = df3.iloc[i * 4 + k - 1, 13]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a3 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P4
                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                    list[5] = df4.iloc[i * 4 + k - 1, 11]
                    list[6] = df4.iloc[i * 4 + k - 1, 13]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a4 = m
                                break
                        if count == 4:
                            break
                    # Evaluate for P5
                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                    list[5] = df5.iloc[i * 4 + k - 1, 11]
                    list[6] = df5.iloc[i * 4 + k - 1, 13]
                    for m in (list[0], list[1]):
                        count = 0
                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                            if m == n:
                                count = count + 1
                            if count == 4:
                                FK = FK + 1
                                a5 = m
                                break
                        if count == 4:
                            break
                    # Checking for Four of a kind
                    if (FK > 0):
                        print "Four of a kind"
                        b = max(a1, a2, a3, a4, a5)
                        if a1 == b:
                            df1.iloc[i * 4 + k - 1, 14] = 1
                        if a2 == b:
                            df2.iloc[i * 4 + k - 1, 14] = 1
                        if a3 == b:
                            df3.iloc[i * 4 + k - 1, 14] = 1
                        if a4 == b:
                            df4.iloc[i * 4 + k - 1, 14] = 1
                        if a5 == b:
                            df5.iloc[i * 4 + k - 1, 14] = 1
                    else:
                        # Check for full house
                        FH = 0
                        a1i = 0
                        a1ii = 0
                        a2i = 0
                        a2ii = 0
                        a3i = 0
                        a3ii = 0
                        a4i = 0
                        a4ii = 0
                        a5i = 0
                        a5ii = 0
                        next = 0
                        # Evaluate for P1
                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                        list[5] = df1.iloc[i * 4 + k - 1, 11]
                        list[6] = df1.iloc[i * 4 + k - 1, 13]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a1i = m
                                                a1ii = n
                                                break
                            if count == 2:
                                break
                        # Evaluate for P2
                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                        list[5] = df2.iloc[i * 4 + k - 1, 11]
                        list[6] = df2.iloc[i * 4 + k - 1, 13]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a2i = m
                                                a2ii = n
                                                break
                        # Evaluate for P3
                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                        list[5] = df3.iloc[i * 4 + k - 1, 11]
                        list[6] = df3.iloc[i * 4 + k - 1, 13]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if n == o:
                                                count = count + 1
                                        if count == 2:
                                            FH = FH + 1
                                            a3i = m
                                            a3ii = n
                                            break
                        # Evaluate for P4
                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                        list[5] = df4.iloc[i * 4 + k - 1, 11]
                        list[6] = df4.iloc[i * 4 + k - 1, 13]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a4i = m
                                                a4ii = n
                                                break
                        # Evaluate for P5
                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                        list[5] = df5.iloc[i * 4 + k - 1, 11]
                        list[6] = df4.iloc[i * 4 + k - 1, 13]
                        for m in (list[0], list[1]):
                            count = 0
                            for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                if m == n:
                                    count = count + 1
                            if count == 3:
                                for n in (list[0], list[1]):
                                    count = 0
                                    if m == n:
                                        continue
                                    else:
                                        for o in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if n == o:
                                                count = count + 1
                                            if count == 2:
                                                FH = FH + 1
                                                a5i = m
                                                a5ii = n
                                                break
                        # Evaluating for Full House
                        if (FH > 1):
                            print "Full House"
                            b = max(a1i, a2i, a3i, a4i, a5i)
                            c = 0
                            if a1i == b:
                                c = c + 1
                            elif a2i == b:
                                c = c + 1
                            elif a3i == b:
                                c = c + 1
                            elif a4i == b:
                                c = c + 1
                            elif a5i == b:
                                c = c + 1
                            if c > 1:
                                b = max(a1ii, a2ii, a3ii, a4ii, a5ii)
                                if a1ii == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                if a2ii == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                if a3ii == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                if a4ii == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                if a5ii == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                b = max(a1i, a2i, a3i, a4i, a5i)
                                if a1i == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                elif a2i == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                elif a3i == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                elif a4i == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                elif a5i == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                        elif (FH == 1):
                            print "Full House"
                            b = max(a1i, a2i, a3i, a4i, a5i)
                            if a1i == b:
                                df1.iloc[i * 4 + k - 1, 14] = 1
                            elif a2i == b:
                                df2.iloc[i * 4 + k - 1, 14] = 1
                            elif a3i == b:
                                df3.iloc[i * 4 + k - 1, 14] = 1
                            elif a4i == b:
                                df4.iloc[i * 4 + k - 1, 14] = 1
                            elif a5i == b:
                                df5.iloc[i * 4 + k - 1, 14] = 1
                        else:
                            # Evaluate for Flush
                            F = 0
                            a1 = 0
                            a2 = 0
                            a3 = 0
                            a4 = 0
                            a5 = 0
                            # Evaluate P1
                            list[0] = df1.iloc[i * 4 + k - 1, 0]
                            list[1] = df1.iloc[i * 4 + k - 1, 2]
                            list[2] = df1.iloc[i * 4 + k - 1, 4]
                            list[3] = df1.iloc[i * 4 + k - 1, 6]
                            list[4] = df1.iloc[i * 4 + k - 1, 8]
                            list[5] = df1.iloc[i * 4 + k - 1, 10]
                            list[6] = df1.iloc[i * 4 + k - 1, 13]
                            for m in (list[0], list[1]):
                                count = 0
                                for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                    if m == n:
                                        count = count + 1
                                if count == 5:
                                    F = F + 1
                                    a1 = m
                                    break
                            # Evaluate P2
                            list[0] = df2.iloc[i * 4 + k - 1, 0]
                            list[1] = df2.iloc[i * 4 + k - 1, 2]
                            list[2] = df2.iloc[i * 4 + k - 1, 4]
                            list[3] = df2.iloc[i * 4 + k - 1, 6]
                            list[4] = df2.iloc[i * 4 + k - 1, 8]
                            list[5] = df2.iloc[i * 4 + k - 1, 10]
                            list[6] = df2.iloc[i * 4 + k - 1, 13]
                            for m in (list[0], list[1]):
                                count = 0
                                for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                    if m == n:
                                        count = count + 1
                                if count == 5:
                                    F = F + 1
                                    a2 = m
                                    break
                            # Evaluate P3
                            list[0] = df3.iloc[i * 4 + k - 1, 0]
                            list[1] = df3.iloc[i * 4 + k - 1, 2]
                            list[2] = df3.iloc[i * 4 + k - 1, 4]
                            list[3] = df3.iloc[i * 4 + k - 1, 6]
                            list[4] = df3.iloc[i * 4 + k - 1, 8]
                            list[5] = df3.iloc[i * 4 + k - 1, 10]
                            list[6] = df3.iloc[i * 4 + k - 1, 13]
                            for m in (list[0], list[1]):
                                count = 0
                                for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                    if m == n:
                                        count = count + 1
                                if count == 5:
                                    F = F + 1
                                    a3 = m
                                    break
                            # Evaluate P4
                            list[0] = df4.iloc[i * 4 + k - 1, 0]
                            list[1] = df4.iloc[i * 4 + k - 1, 2]
                            list[2] = df4.iloc[i * 4 + k - 1, 4]
                            list[3] = df4.iloc[i * 4 + k - 1, 6]
                            list[4] = df4.iloc[i * 4 + k - 1, 8]
                            list[5] = df4.iloc[i * 4 + k - 1, 10]
                            list[6] = df4.iloc[i * 4 + k - 1, 13]
                            for m in (list[0], list[1]):
                                count = 0
                                for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                    if m == n:
                                        count = count + 1
                                if count == 5:
                                    F = F + 1
                                    a4 = m
                                    break
                            # Evaluate P5
                            list[0] = df5.iloc[i * 4 + k - 1, 0]
                            list[1] = df5.iloc[i * 4 + k - 1, 2]
                            list[2] = df5.iloc[i * 4 + k - 1, 4]
                            list[3] = df5.iloc[i * 4 + k - 1, 6]
                            list[4] = df5.iloc[i * 4 + k - 1, 8]
                            list[5] = df5.iloc[i * 4 + k - 1, 10]
                            list[6] = df5.iloc[i * 4 + k - 1, 13]
                            for m in (list[0], list[1]):
                                count = 0
                                for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                    if m == n:
                                        count = count + 1
                                if count == 5:
                                    F = F + 1
                                    a5 = m
                                    break
                            if F > 0:
                                print "Flush"
                                b = max(a1, a2, a3, a4, a5)
                                if a1 == b:
                                    df1.iloc[i * 4 + k - 1, 14] = 1
                                elif a2 == b:
                                    df2.iloc[i * 4 + k - 1, 14] = 1
                                elif a3 == b:
                                    df3.iloc[i * 4 + k - 1, 14] = 1
                                elif a4 == b:
                                    df4.iloc[i * 4 + k - 1, 14] = 1
                                elif a5 == b:
                                    df5.iloc[i * 4 + k - 1, 14] = 1
                            else:
                                # Check for Straight
                                SF = 0
                                a1 = 0
                                a2 = 0
                                a3 = 0
                                a4 = 0
                                a5 = 0
                                # P1 Evaluation
                                # With Ace Low
                                list[0] = df1.iloc[i * 4 + k - 1, 1]
                                list[1] = df1.iloc[i * 4 + k - 1, 3]
                                list[2] = df1.iloc[i * 4 + k - 1, 5]
                                list[3] = df1.iloc[i * 4 + k - 1, 7]
                                list[4] = df1.iloc[i * 4 + k - 1, 9]
                                list[5] = df1.iloc[i * 4 + k - 1, 11]
                                list[6] = df1.iloc[i * 4 + k - 1, 13]
                                for m in range(0, 7):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == list[5]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == list[6]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df1.iloc[i * 4 + k - 1, 1]
                                list[1] = df1.iloc[i * 4 + k - 1, 3]
                                list[2] = df1.iloc[i * 4 + k - 1, 5]
                                list[3] = df1.iloc[i * 4 + k - 1, 7]
                                list[4] = df1.iloc[i * 4 + k - 1, 9]
                                list[5] = df1.iloc[i * 4 + k - 1, 11]
                                list[6] = df1.iloc[i * 4 + k - 1, 13]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a1 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == list[
                                            5]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a1 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P2 Evaluation
                                # With Ace Low
                                list[0] = df2.iloc[i * 4 + k - 1, 1]
                                list[1] = df2.iloc[i * 4 + k - 1, 3]
                                list[2] = df2.iloc[i * 4 + k - 1, 5]
                                list[3] = df2.iloc[i * 4 + k - 1, 7]
                                list[4] = df2.iloc[i * 4 + k - 1, 9]
                                list[5] = df2.iloc[i * 4 + k - 1, 11]
                                list[6] = df2.iloc[i * 4 + k - 1, 13]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df2.iloc[i * 4 + k - 1, 1]
                                list[1] = df2.iloc[i * 4 + k - 1, 3]
                                list[2] = df2.iloc[i * 4 + k - 1, 5]
                                list[3] = df2.iloc[i * 4 + k - 1, 7]
                                list[4] = df2.iloc[i * 4 + k - 1, 9]
                                list[5] = df2.iloc[i * 4 + k - 1, 11]
                                list[6] = df2.iloc[i * 4 + k - 1, 11]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a2 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a2 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P3 Evaluation
                                # With Ace Low
                                list[0] = df3.iloc[i * 4 + k - 1, 1]
                                list[1] = df3.iloc[i * 4 + k - 1, 3]
                                list[2] = df3.iloc[i * 4 + k - 1, 5]
                                list[3] = df3.iloc[i * 4 + k - 1, 7]
                                list[4] = df3.iloc[i * 4 + k - 1, 9]
                                list[5] = df3.iloc[i * 4 + k - 1, 11]
                                list[6] = df3.iloc[i * 4 + k - 1, 13]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[
                                                    4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df3.iloc[i * 4 + k - 1, 1]
                                list[1] = df3.iloc[i * 4 + k - 1, 3]
                                list[2] = df3.iloc[i * 4 + k - 1, 5]
                                list[3] = df3.iloc[i * 4 + k - 1, 7]
                                list[4] = df3.iloc[i * 4 + k - 1, 9]
                                list[5] = df3.iloc[i * 4 + k - 1, 11]
                                list[6] = df3.iloc[i * 4 + k - 1, 13]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a3 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a3 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P4 Evaluation
                                # With Ace Low
                                list[0] = df4.iloc[i * 4 + k - 1, 1]
                                list[1] = df4.iloc[i * 4 + k - 1, 3]
                                list[2] = df4.iloc[i * 4 + k - 1, 5]
                                list[3] = df4.iloc[i * 4 + k - 1, 7]
                                list[4] = df4.iloc[i * 4 + k - 1, 9]
                                list[5] = df4.iloc[i * 4 + k - 1, 11]
                                list[6] = df4.iloc[i * 4 + k - 1, 13]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df4.iloc[i * 4 + k - 1, 1]
                                list[1] = df4.iloc[i * 4 + k - 1, 3]
                                list[2] = df4.iloc[i * 4 + k - 1, 5]
                                list[3] = df4.iloc[i * 4 + k - 1, 7]
                                list[4] = df4.iloc[i * 4 + k - 1, 9]
                                list[5] = df4.iloc[i * 4 + k - 1, 11]
                                list[6] = df4.iloc[i * 4 + k - 1, 13]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a4 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a4 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # P5 Evaluation
                                # With Ace Low
                                list[0] = df5.iloc[i * 4 + k - 1, 1]
                                list[1] = df5.iloc[i * 4 + k - 1, 3]
                                list[2] = df5.iloc[i * 4 + k - 1, 5]
                                list[3] = df5.iloc[i * 4 + k - 1, 7]
                                list[4] = df5.iloc[i * 4 + k - 1, 9]
                                list[5] = df5.iloc[i * 4 + k - 1, 11]
                                list[6] = df5.iloc[i * 4 + k - 1, 13]
                                for m in range(0, 5):
                                    if list[m] == 14:
                                        list[m] = 1
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == \
                                                list[4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # With Ace High
                                list[0] = df5.iloc[i * 4 + k - 1, 1]
                                list[1] = df5.iloc[i * 4 + k - 1, 3]
                                list[2] = df5.iloc[i * 4 + k - 1, 5]
                                list[3] = df5.iloc[i * 4 + k - 1, 7]
                                list[4] = df5.iloc[i * 4 + k - 1, 9]
                                list[5] = df5.iloc[i * 4 + k - 1, 11]
                                list[6] = df5.iloc[i * 4 + k - 1, 13]
                                list = np.sort(list).tolist()
                                if list[0] + 1 == list[1] and list[1] + 1 == list[2] and list[2] + 1 == list[3] and \
                                                        list[3] + 1 == list[
                                            4]:
                                    a5 = max(list[0], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[1] + 1 == list[2] and list[2] + 1 == list[3] and list[3] + 1 == list[4] and \
                                                        list[4] + 1 == \
                                                list[
                                                    5]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                if list[2] + 1 == list[3] and list[3] + 1 == list[4] and list[4] + 1 == list[5] and \
                                                        list[5] + 1 == \
                                                list[6]:
                                    a5 = max(list[5], list[1], list[2], list[3], list[4])
                                    SF = SF + 1
                                # Check for Straight
                                if (SF > 0):
                                    print "Straight"
                                    b = max(a1, a2, a3, a4, a5)
                                    if a1 == b:
                                        df1.iloc[i * 4 + k - 1, 14] = 1
                                    if a2 == b:
                                        df2.iloc[i * 4 + k - 1, 14] = 1
                                    if a3 == b:
                                        df3.iloc[i * 4 + k - 1, 14] = 1
                                    if a4 == b:
                                        df4.iloc[i * 4 + k - 1, 14] = 1
                                    if a5 == b:
                                        df5.iloc[i * 4 + k - 1, 14] = 1
                                else:
                                    # Check for 3 of a kind
                                    FH = 0
                                    a1i = 0
                                    a2i = 0
                                    a3i = 0
                                    a4i = 0
                                    a5i = 0
                                    # Evaluate for P1
                                    list[0] = df1.iloc[i * 4 + k - 1, 1]
                                    list[1] = df1.iloc[i * 4 + k - 1, 3]
                                    list[2] = df1.iloc[i * 4 + k - 1, 5]
                                    list[3] = df1.iloc[i * 4 + k - 1, 7]
                                    list[4] = df1.iloc[i * 4 + k - 1, 9]
                                    list[5] = df1.iloc[i * 4 + k - 1, 11]
                                    list[6] = df1.iloc[i * 4 + k - 1, 13]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a1i = m
                                            break
                                    # Evaluate for P2
                                    list[0] = df2.iloc[i * 4 + k - 1, 1]
                                    list[1] = df2.iloc[i * 4 + k - 1, 3]
                                    list[2] = df2.iloc[i * 4 + k - 1, 5]
                                    list[3] = df2.iloc[i * 4 + k - 1, 7]
                                    list[4] = df2.iloc[i * 4 + k - 1, 9]
                                    list[5] = df2.iloc[i * 4 + k - 1, 11]
                                    list[6] = df2.iloc[i * 4 + k - 1, 13]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a2i = m
                                            break
                                    # Evaluate for P3
                                    list[0] = df3.iloc[i * 4 + k - 1, 1]
                                    list[1] = df3.iloc[i * 4 + k - 1, 3]
                                    list[2] = df3.iloc[i * 4 + k - 1, 5]
                                    list[3] = df3.iloc[i * 4 + k - 1, 7]
                                    list[4] = df3.iloc[i * 4 + k - 1, 9]
                                    list[5] = df3.iloc[i * 4 + k - 1, 11]
                                    list[6] = df3.iloc[i * 4 + k - 1, 13]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a3i = m
                                            break
                                    # Evaluate for P4
                                    list[0] = df4.iloc[i * 4 + k - 1, 1]
                                    list[1] = df4.iloc[i * 4 + k - 1, 3]
                                    list[2] = df4.iloc[i * 4 + k - 1, 5]
                                    list[3] = df4.iloc[i * 4 + k - 1, 7]
                                    list[4] = df4.iloc[i * 4 + k - 1, 9]
                                    list[5] = df4.iloc[i * 4 + k - 1, 11]
                                    list[6] = df4.iloc[i * 4 + k - 1, 13]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a4i = m
                                            break
                                    # Evaluate for P5
                                    list[0] = df5.iloc[i * 4 + k - 1, 1]
                                    list[1] = df5.iloc[i * 4 + k - 1, 3]
                                    list[2] = df5.iloc[i * 4 + k - 1, 5]
                                    list[3] = df5.iloc[i * 4 + k - 1, 7]
                                    list[4] = df5.iloc[i * 4 + k - 1, 9]
                                    list[5] = df5.iloc[i * 4 + k - 1, 11]
                                    list[6] = df5.iloc[i * 4 + k - 1, 13]
                                    for m in (list[0], list[1]):
                                        count = 0
                                        for n in (list[0], list[1], list[2], list[3], list[4], list[5], list[6]):
                                            if m == n:
                                                count = count + 1
                                        if count == 3:
                                            FH = FH + 1
                                            a5i = m
                                            break
                                    # Evaluating for 3 of a kind
                                    if (FH > 0):
                                        print "3 of a kind"
                                        b = max(a1i, a2i, a3i, a4i, a5i)
                                        if a1i == b:
                                            df1.iloc[i * 4 + k - 1, 14] = 1
                                        elif a2i == b:
                                            df2.iloc[i * 4 + k - 1, 14] = 1
                                        elif a3i == b:
                                            df3.iloc[i * 4 + k - 1, 14] = 1
                                        elif a4i == b:
                                            df4.iloc[i * 4 + k - 1, 14] = 1
                                        elif a5i == b:
                                            df5.iloc[i * 4 + k - 1, 14] = 1
                                    else:
                                        # Evaluate for two pair and one pair
                                        f1 = [0]
                                        f2 = [0]
                                        f3 = [0]
                                        f4 = [0]
                                        f5 = [0]
                                        a1 = [0]
                                        a2 = [0]
                                        a3 = [0]
                                        a4 = [0]
                                        a5 = [0]
                                        Fin = 0
                                        # Evaluate P1
                                        TP1 = 0
                                        list[0] = df1.iloc[i * 4 + k - 1, 1]
                                        list[1] = df1.iloc[i * 4 + k - 1, 3]
                                        list[2] = df1.iloc[i * 4 + k - 1, 5]
                                        list[3] = df1.iloc[i * 4 + k - 1, 7]
                                        list[4] = df1.iloc[i * 4 + k - 1, 9]
                                        list[5] = df1.iloc[i * 4 + k - 1, 11]
                                        list[6] = df1.iloc[i * 4 + k - 1, 13]
                                        if (list[0] == list[2] or list[0] == list[3] or list[
                                            0] == list[4] or list[0] == list[5] or list[0] == list[6]):
                                            TP1 = TP1 + 1
                                            f1.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5] or list[1] == list[6]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f1.append(list[1])
                                        if TP1 > 1:
                                            f1 = np.sort(f1[::-1]).tolist()
                                            a1.append(f1[0])
                                            a1.append(f1[1])
                                            Fin = Fin + 1
                                        # Evaluate P2
                                        TP2 = 0
                                        list[0] = df2.iloc[i * 4 + k - 1, 1]
                                        list[1] = df2.iloc[i * 4 + k - 1, 3]
                                        list[2] = df2.iloc[i * 4 + k - 1, 5]
                                        list[3] = df2.iloc[i * 4 + k - 1, 7]
                                        list[4] = df2.iloc[i * 4 + k - 1, 9]
                                        list[5] = df2.iloc[i * 4 + k - 1, 11]
                                        list[6] = df2.iloc[i * 4 + k - 1, 13]
                                        if (list[0] == list[2] or list[0] == list[3] or
                                                    list[0] == list[4] or list[0] == list[5] or list[0] == list[6]):
                                            TP2 = TP2 + 1
                                            f2.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5] or list[1] == list[6]):
                                            TP2 = TP2 + 1
                                            f2.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f2.append(list[1])
                                        if TP2 > 1:
                                            f2 = np.sort(f2[::-1]).tolist()
                                            a2.append(f2[0])
                                            a2.append(f2[1])
                                            Fin = Fin + 1
                                        # Evaluate P3
                                        TP3 = 0
                                        list[0] = df3.iloc[i * 4 + k - 1, 1]
                                        list[1] = df3.iloc[i * 4 + k - 1, 3]
                                        list[2] = df3.iloc[i * 4 + k - 1, 5]
                                        list[3] = df3.iloc[i * 4 + k - 1, 7]
                                        list[4] = df3.iloc[i * 4 + k - 1, 9]
                                        list[5] = df3.iloc[i * 4 + k - 1, 11]
                                        list[6] = df3.iloc[i * 4 + k - 1, 13]
                                        if (list[0] == list[2] or list[0] == list[
                                            3] or list[0] == list[4] or list[0] == list[5] or list[0] == list[6]):
                                            TP3 = TP3 + 1
                                            f3.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[4] or list[1] == list[5] or list[1] == list[6]):
                                            TP3 = TP3 + 1
                                            f3.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f3.append(list[1])
                                        if TP3 > 1:
                                            f3 = np.sort(f3[::-1]).tolist()
                                            a3.append(f3[0])
                                            a3.append(f3[1])
                                            Fin = Fin + 1
                                        # Evaluate P4
                                        TP4 = 0
                                        list[0] = df4.iloc[i * 4 + k - 1, 1]
                                        list[1] = df4.iloc[i * 4 + k - 1, 3]
                                        list[2] = df4.iloc[i * 4 + k - 1, 5]
                                        list[3] = df4.iloc[i * 4 + k - 1, 7]
                                        list[4] = df4.iloc[i * 4 + k - 1, 9]
                                        list[5] = df4.iloc[i * 4 + k - 1, 11]
                                        list[6] = df4.iloc[i * 4 + k - 1, 13]
                                        if (list[0] == list[2] or list[0] == list[3] or list[0] == list[4] or list[0] == list[5] or list[0] == list[6]):
                                            TP4 = TP4 + 1
                                            f4.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] == list[
                                            4] or list[1] == list[5] or list[1] == list[6]):
                                            TP4 = TP4 + 1
                                            f4.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f4.append(list[1])
                                        if TP4 > 1:
                                            f4 = np.sort(f4[::-1]).tolist()
                                            a4.append(f4[0])
                                            a4.append(f4[1])
                                            Fin = Fin + 1
                                        # Evaluate P5
                                        TP5 = 0
                                        list[0] = df5.iloc[i * 4 + k - 1, 1]
                                        list[1] = df5.iloc[i * 4 + k - 1, 3]
                                        list[2] = df5.iloc[i * 4 + k - 1, 5]
                                        list[3] = df5.iloc[i * 4 + k - 1, 7]
                                        list[4] = df5.iloc[i * 4 + k - 1, 9]
                                        list[5] = df5.iloc[i * 4 + k - 1, 11]
                                        list[6] = df5.iloc[i * 4 + k - 1, 13]
                                        if (list[0] == list[2] or list[0] ==
                                            list[3] or list[0] == list[4] or list[0] == list[5] or list[0] == list[6]):
                                            TP5 = TP5 + 1
                                            f5.append(list[0])
                                        if (list[1] == list[2] or list[1] == list[3] or list[1] ==
                                            list[4] or list[1] == list[5] or list[1] == list[6]):
                                            TP5 = TP5 + 1
                                            f5.append(list[1])
                                        if (list[0] == list[1]):
                                            TP1 = TP1 + 1
                                            f5.append(list[1])
                                        if TP5 > 1:
                                            f5 = np.sort(f5[::-1]).tolist()
                                            a5.append(f5[0])
                                            a5.append(f5[1])
                                            Fin = Fin + 1
                                        #Check for two pair
                                        if Fin > 0:
                                            print "Two pair"
                                            b = max(max(a1),max(a2),max(a3),max(a4),max(a5))
                                            if max(a1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            elif max(a5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        #Check for one pair
                                        elif TP1+TP2+TP3+TP4+TP5 > 0:
                                            print "One pair"
                                            b = max(max(f1),max(f2),max(f3),max(f4),max(f5))
                                            if max(f1) == b:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f2) == b:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f3) == b:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f4) == b:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if max(f5) == b:
                                                df5.iloc[i * 4 + k - 1, 14] = 1
                                        else:
                                            # Find the high card
                                            print "High Card"
                                            winner = max(df1.iloc[i * 4 + k - 1, 1], df1.iloc[i * 4 + k - 1, 3],
                                                         df2.iloc[i * 4 + k - 1, 1], df2.iloc[i * 4 + k - 1, 3],
                                                         df3.iloc[i * 4 + k - 1, 1], df3.iloc[i * 4 + k - 1, 3],
                                                         df4.iloc[i * 4 + k - 1, 1], df4.iloc[i * 4 + k - 1, 3],
                                                         df5.iloc[i * 4 + k - 1, 1], df5.iloc[i * 4 + k - 1, 3])
                                            if df1.iloc[i * 4 + k - 1, 1] == winner or df1.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df1.iloc[i * 4 + k - 1, 14] = 1
                                            if df2.iloc[i * 4 + k - 1, 1] == winner or df2.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df2.iloc[i * 4 + k - 1, 14] = 1
                                            if df3.iloc[i * 4 + k - 1, 1] == winner or df3.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df3.iloc[i * 4 + k - 1, 14] = 1
                                            if df4.iloc[i * 4 + k - 1, 1] == winner or df4.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df4.iloc[i * 4 + k - 1, 14] = 1
                                            if df5.iloc[i * 4 + k - 1, 1] == winner or df5.iloc[
                                                                        i * 4 + k - 1, 3] == winner:
                                                df5.iloc[i * 4 + k - 1, 14] = 1


df1.to_csv('P1.csv', index= False)
df2.to_csv('P2.csv', index= False)
df3.to_csv('P3.csv', index= False)
df4.to_csv('P4.csv', index= False)
df5.to_csv('P5.csv', index= False)
