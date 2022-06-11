def lb(n,score, word, chance,mode):
    # writes the score into leaderboard.txt when it's called
    dct = {"1":"Normal", "2":"Hard"}
    if n == 0:
        f = open('Leaderboard.txt', 'rb')
        leng = len(f.readlines())
        f = open('Leaderboard.txt', 'a')
        f.write("{}: Rating was {:.2f} Word was {} amount of chances you've spent was {} the game mode was {}\n".format(leng+1,score,word,chance+1,dct[mode]))
    elif n == 1:
        # if user wants to read it, it sorts them according to their rating.
        f = open('Leaderboard.txt', 'r')
        file_content = ranking()
        file_content = f.read()
        print(file_content)
    elif n == 2:
        f = open("Leaderboard.txt", 'r+')
        f.truncate(0)
def ranking():
    # ranking among the scores in the leaderboard
    a_file = open("Leaderboard.txt", "r")
    list_of_lists = []
    for line in a_file:
        list_of_lists.append(line.split())
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists)):
            if (list_of_lists[i][3]) > (list_of_lists[j][3]):
                list_of_lists[i], list_of_lists[j] = list_of_lists[j], list_of_lists[i]
    prnt_lst = [" ".join(i) for i in list_of_lists]
    with open('Leaderboard.txt', "r+") as overwrite:
        for i in prnt_lst:
            overwrite.write("{}\n".format(i))
        return overwrite

