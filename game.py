from main import Wordle
from rich.table import Table
from rich.live import Live
from rich.prompt import Prompt
from leaderboard import lb
from rich import box
from alphabet import alphabet

table = Table("Guesses", box=box.ASCII, caption_justify="middle")

diff = Prompt.ask("Choose a game mode(4 for 4-lettered, 5 for 5-lettered, 6 for 6-lettered), or type 1 for leaderboard")
while diff not in ["4","5","6","1"]:
    print("Type a valid input!")
    diff = Prompt.ask("Choose a game mode(4 for 4-lettered, 5 for 5-lettered, 6 for 6-lettered), or type 1 for leaderboard")
if diff == "1":
    lb(1,0,0,0,0)
    diff = Prompt.ask("Type 0 to clear leaderboard or choose a game mode(4 for 4-lettered, 5 for 5-lettered, 6 for 6-lettered)")
    if diff == "0":
        lb(2,0,0,0,0)
        diff = Prompt.ask("You have to choose a game mode(4 for 4-lettered, 5 for 5-lettered, 6 for 6-lettered)")
mode = Prompt.ask("Type 1 for normal mode, type 2 for 120 seconds mode")

if diff == "6" and mode == "1":
    choices = 7
if diff == "4" and mode == "1":
    choices = 5
if mode == "1" and diff == "5":
    choices = 6
if mode == "2":
    choices = 4
game = (Wordle(mode))


while choices > -1:
    if choices == 0:
        game.game_over()
    game.out_of_time()
    a = game.user_guess(choices,diff)
    lst = game.color(a)
    print(alphabet(a))
    with Live(table, auto_refresh=False) as live:
        b = " ".join(lst)
        table.add_row(b)
        live.refresh()
    choices -= 1



