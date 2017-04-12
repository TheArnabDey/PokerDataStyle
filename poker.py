import random
import pandas as pd
df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('train.csv')
df3 = pd.read_csv('train.csv')
df4 = pd.read_csv('train.csv')
df5 = pd.read_csv('train.csv')
for i in range(0,1):
        for k in range (1,5):
            x = 0
            if k == 1:
                #Create Pre-Flop round
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
            if k == 2:
                #Create Flop Round
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
            #Flop hand evaluation
            x = 0
            list = []
            df1.iloc[i * 4 + k - 1, 14] = 0
            df2.iloc[i * 4 + k - 1, 14] = 0
            df3.iloc[i * 4 + k - 1, 14] = 0
            df4.iloc[i * 4 + k - 1, 14] = 0
            df5.iloc[i * 4 + k - 1, 14] = 0
            #Straight Flush Evaluation
            #if df1.iloc[i * 4 + k - 1, 8]:





            if k == 3:
                #Create Turn Round
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

df1.to_csv('P1.csv', index= False)
df2.to_csv('P2.csv', index= False)
df3.to_csv('P3.csv', index= False)
df4.to_csv('P4.csv', index= False)
df5.to_csv('P5.csv', index= False)
