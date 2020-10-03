from random import seed, shuffle

FACES = 'B123456789TJCQK'
UNICODE_FACES = '0123456789ABCDE'
SUITS = 'SHDC'
UNICODE_SUITS = 'ABCD'
COLORS = ['\x1b[%dm' % c for c in (30, 31, 34, 32, 39)]


def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    if card[:1].upper() == 'B':
        face, suit = 'BS'
    else:
        face, suit = card.upper()
    c = chr(int('0001f0%s%s' % (
        UNICODE_SUITS[SUITS.index(suit)],
        UNICODE_FACES[FACES.index(face)]
    ), base=16))
    if color:
        c = COLORS[SUITS.index(suit)] + c + COLORS[-1]
    return c


def generate_dial_and_centre(for_seed):
    colours = 'CDHS'  # Clubs, Diamonds, Hearts, Spades
    #                                            jacks, queens, kings
    ranks = list(str(x) for x in range(1, 11)) + list('jqk')
    seed(for_seed)
    cards = [colour + rank for colour in colours for rank in ranks]
    shuffle(cards)
    dial = dict.fromkeys(range(1, 13))
    for i in range(12):
        dial[i + 1] = [cards[i + 13 * j] for j in range(4)]
    return dial, [cards[12 + 13 * j] for j in range(4)]


def initial_hour(hour, dial):
    for i in dial[hour]:
        a = unicard(i[1:] + i[0])
        if i == dial[hour][-1]:
            print('hidden' + a, end='')
        else:
            print('hidden' + a, end='  ')
    print()


# REPLACE PASS ABOVE WITH YOUR CODE


def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,
                                                  centre
                                                  ):
    all_list = []
    card_list = []
    for j in range(1, 13):
        for n in dial[j]:
            card_list.append(n)
        all_list.append(card_list)
        card_list = []
    all_list.append(centre)
    p = all_list[-1][-1][1:]
    q = all_list[-1][-1]
    s = 12
    if p == 'j':
        p = 11
    if p == 'q':
        p = 12
    if p == 'k':
        p = 13
    all_list[p - 1].insert(0, unicard(q[1:] + q[0]))
    del all_list[12][-1]
    for i in range(nb_of_steps - 1):
        q = all_list[int(p) - 1][-1]
        p = all_list[int(p) - 1][-1][1:]
        if p == 'j':
            p = 11
        if p == 'q':
            p = 12
        if p == 'k':
            p = 13
        del all_list[s - 1][-1]
        if p == '':
            if nb_of_steps < 53:
                return print('Could not play that far...')
            else:
                for i in all_list[hour - 1]:
                    if i == all_list[hour - 1][-1]:
                        print(i, end='')
                    else:
                        print(i, end='  ')
                return print()
        s = int(p)
        all_list[int(p) - 1].insert(0, unicard(q[1:] + q[0]))
    for m in range(len(all_list[hour - 1])):
        cards = all_list[hour - 1][m]
        if len(cards) != 1:
            all_list[hour - 1][m] = 'hidden' + unicard(cards[1:] + cards[0])
    for i in all_list[hour - 1]:
        if i == all_list[hour - 1][-1]:
            print(i, end='')
        else:
            print(i, end='  ')
    print()
    # REPLACE PRINT() ABOVE WITH YOUR CODE


def kings_at_end_of_game(dial, centre):
    all_list = []
    card_list = []
    for j in range(1, 13):
        for n in dial[j]:
            card_list.append(n)
        all_list.append(card_list)
        card_list = []
    all_list.append(centre)
    p = all_list[-1][-1][1:]
    q = all_list[-1][-1]
    s = 12
    if p == 'j':
        p = 11
    if p == 'q':
        p = 12
    if p == 'k':
        p = 13
    all_list[int(p) - 1].insert(0, unicard(q[1:] + q[0]))
    del all_list[12][-1]
    for i in range(100):
        q = all_list[int(p) - 1][-1]
        p = all_list[int(p) - 1][-1][1:]
        if p == 'j':
            p = 11
        if p == 'q':
            p = 12
        if p == 'k':
            p = 13
        if i != 51:
            del all_list[s - 1][-1]
        if p == '':
            if i < 51:
                return print('No success...')
            else:
                for i in all_list[12]:
                    if i == all_list[12][-1]:
                        print(i, end='')
                    else:
                        print(i, end='  ')
                return print()
        s = int(p)
        all_list[int(p) - 1].insert(0, unicard(q[1:] + q[0]))

# REPLACE PRINT() ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS
