from tkinter import*
from PIL import ImageTk, Image
import random
from random import randint
from tkinter import messagebox

def new_game():

    root.destroy()
    start()
    
def start():

    global chosen_word
    global length
    global root
    global text_word
    global n
    global word_label
    global hangman_image_label
    global image_list

    root = Tk()

    root.title("Hangman")

    img_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\1.png"))
    img_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\2.png"))
    img_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\3.png"))
    img_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\4.png"))
    img_5 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\5.png"))
    img_6 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\6.png"))
    img_7 = ImageTk.PhotoImage(Image.open(r"C:\Users\Tirth\Pictures\Hangman\7.png"))

    image_list = [img_1, img_2, img_3, img_4, img_5, img_6, img_7]

    n = 0

    words = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']


    k = random.randint(0, len(words)-1)

    chosen_word = words[k]

    length = len(chosen_word)

    text_word = []

    for m in range(0, length):

        text_word.append('_ ')

    text1 = '_ ' * length

    hangman_image_label = Label(root, image = image_list[n])

    title_label = Label(root, text = 'HANGMAN', font = '-family {Segoe UI} -size 20 -weight bold')

    info_label = Label(root, text = 'Guess the word letter by letter before the Man is Hanged. Guess wrong 7 times and you are OUT', font = '-family {Segoe UI} -size 12')

    word_label = Label(root, text = text1, font = '-family {Segoe UI} -size 20 -weight bold')

    guess_entry = Entry(root, width = 40)

    guess_button = Button(root, text = 'Guess', font = '-family {Segoe UI} -size 13', command = lambda:guess(guess_entry.get()))

    title_label.grid(row = 0, column = 0)
    info_label.grid(row = 1, column = 0)
    hangman_image_label.grid(row = 2, column = 0)
    word_label.grid(row = 3, column = 0)
    guess_entry.grid(row = 4, column = 0)
    guess_button.grid(row = 5, column = 0)
                      
def guess(letter):

    global chosen_word
    global length
    global root
    global text_word
    global n
    global word_label
    global hangman_image_label
    global image_list

    text1 = ''
    
    if letter in chosen_word:

        correct_pos = []

        for i in range(0, len(chosen_word)):
            
            if chosen_word[i] == letter:

                correct_pos.append(i)

            else:

                pass

        for j in range(0, len(chosen_word)):

            if j in correct_pos:

                text_word[j] = chosen_word[j]

            else:
                pass

        for b in range(0, len(text_word)):

            text1 += text_word[b]

        if text1 == chosen_word:

            messagebox.showinfo('Congratulations!', 'You guessed the word!')

            new = Button(root, text = 'New Game', font = '-family {Segoe UI} -size 13', command = new_game)

            new.grid(row = 6, column = 0)

        else:
            pass
                
        word_label.grid_forget()

        word_label = Label(root, text = text1, font = '-family {Segoe UI} -size 20 -weight bold')

        word_label.grid(row = 3, column = 0)
        
    else:

        messagebox.showinfo('Oh No!','Wrong Guess. %s tries left'%(6-n))

        if n == 6:

            messagebox.showinfo('Game Over!', 'You could not guess the word')

            new = Button(root, text = 'New Game', font = '-family {Segoe UI} -size 13', command = new_game)

            new.grid(row = 6, column = 0)


            text1 = chosen_word

            word_label.grid_forget()
            word_label = Label(root, text = text1, font = '-family {Segoe UI} -size 20 -weight bold')
            
            word_label.grid(row = 3, column = 0)
            
        elif n < 6:

            n += 1

            hangman_image_label.grid_forget()

            hangman_image_label = Label(root, image = image_list[n])

            hangman_image_label.grid(row = 2, column = 0)

start()
root.mainloop()
