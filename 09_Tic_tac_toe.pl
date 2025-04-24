% Tic-Tac-Toe Game in Prolog
% Representation:
% Board: A list of 9 elements representing the board.
% '-' for empty, 'x' for player X, 'o' for player O.
% Moves: Numbers 1-9 representing the positions on the board.
% Display the board
display_board(Board) :-
nth0(0, Board, A), nth0(1, Board, B), nth0(2, Board, C),
nth0(3, Board, D), nth0(4, Board, E), nth0(5, Board, F),
nth0(6, Board, G), nth0(7, Board, H), nth0(8, Board, I),
format('......................................~n'),
format('~w | ~w | ~w~n', [A, B, C]),
format('---------~n'),
format('~w | ~w | ~w~n', [D, E, F]),
format('---------~n'),
format('~w | ~w | ~w~n', [G, H, I]).
% Check if a player has won
win(Board, Player) :-
win_line(Board, Player).
win_line(Board, Player) :-
% Rows
(nth0(0, Board, Player), nth0(1, Board, Player), nth0(2, Board, Player));
(nth0(3, Board, Player), nth0(4, Board, Player), nth0(5, Board, Player));
(nth0(6, Board, Player), nth0(7, Board, Player), nth0(8, Board, Player));
% Columns
(nth0(0, Board, Player), nth0(3, Board, Player), nth0(6, Board, Player));
(nth0(1, Board, Player), nth0(4, Board, Player), nth0(7, Board, Player));
(nth0(2, Board, Player), nth0(5, Board, Player), nth0(8, Board, Player));
% Diagonals
(nth0(0, Board, Player), nth0(4, Board, Player), nth0(8, Board, Player));
(nth0(2, Board, Player), nth0(4, Board, Player), nth0(6, Board, Player)).
% Check if the board is full
full_board(Board) :-
\+ member('-', Board).


% Get available moves
available_moves(Board, Moves) :-
findall(Move, (nth0(Index, Board, '-'), Move is Index + 1), Moves).
% Make a move
make_move(Board, Move, Player, NewBoard) :-
Index is Move - 1,
replace(Board, Index, Player, NewBoard).
% Replace an element in a list
replace(List, Index, Element, NewList) :-
replace(List, Index, Element, 0, NewList).
replace([_|Rest], 0, Element, _, [Element|Rest]).
replace([H|Rest], Index, Element, Count, [H|NewRest]) :-
NextCount is Count + 1,
NextIndex is Index - 1,
replace(Rest, NextIndex, Element, NextCount, NewRest).
% AI's turn (simple strategy: win, block, or random)
ai_move(Board, Move, Player) :-
% Check if AI can win
available_moves(Board, Moves),
member(Move, Moves),
make_move(Board, Move, Player, TempBoard),
win(TempBoard, Player), !.
ai_move(Board, Move, Player) :-
% Check if AI can block
opponent(Player, Opponent),
available_moves(Board, Moves),
member(Move, Moves),
make_move(Board, Move, Opponent, TempBoard),
win(TempBoard, Opponent), !.
ai_move(Board, Move, _) :-
% Otherwise, choose a random available move
available_moves(Board, Moves),
random_member(Move, Moves).

opponent(x, o).
opponent(o, x).
% Game loop
play_game(Board, Player) :-
display_board(Board),
(win(Board, x) -> format('Player X wins!~n');
win(Board, o) -> format('Player O wins!~n');
full_board(Board) -> format('It\'s a draw!~n');
(Player = x -> player_move(Board, NewBoard), NextPlayer = o;
Player = o -> ai_move(Board, Move, o), make_move(Board, Move, o, NewBoard),
NextPlayer = x),
play_game(NewBoard, NextPlayer)).
% Player's move
player_move(Board, NewBoard) :-
repeat,
write('Enter your move (1-9): '),
read(Move),
(integer(Move), Move >= 1, Move =< 9 ->
available_moves(Board, Moves),
member(Move, Moves),
make_move(Board, Move, x, NewBoard), !;
write('Invalid move. Try again.~n'), fail).
% Start the game
start_game :-
play_game(['-', '-', '-', '-', '-', '-', '-', '-', '-'], x).
%random member
random_member(X, L) :-
length(L, Len),
random(0, Len, Index),
nth0(Index, L, X).



# #OUTPUT
# 1) Start the game by running:
#     ?- start_game.




