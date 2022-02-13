
## result will be numernical, setWinner is str val of team
def score_logger(setWinner, result):
    current_best_team = ''
    scores = {current_best_team: 0}
    print(setWinner, result)




def whosWinner():
    HOME_WIN = 1
    competitions = [
        ['HTML', 'C#'],
        ['C#', 'Python'],
        ['Python', 'HTML']
    ]
    ''' 
        * Enumerate through input list and map competitions
        * Then update scores array as loops pass 
    '''
    results = [0, 0, 1]

    for index, teamSet in enumerate(competitions):
        result = results[index]
       # print(result)
        home, away = teamSet  # splits array into two sepearte
       # print(home, away)

        if result == 0:
            setWinner = away
          #  print(type(setWinner))
           # print(setWinner)
            score_logger(setWinner, result)

        else:
            setWinner = home
          #  print(setWinner)
            score_logger(setWinner, result)

## function to log wins and scors

def main():
    whosWinner()


main()
