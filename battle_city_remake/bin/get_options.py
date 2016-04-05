#!/usr/bin/env python2
# This script needs to be run to play the game
# It sets the color and starting position of player 1 and player2
# Run this script with the options --player 1 [color]  [starting_position] --player2 [color] [starting_position]
# Possible color options = green, grey, purple, yellow
# Possible starting positions = up or down


def cl_handler():
    """
    Handles the command line input. This script can be run without
    """
    
    parser = argparse.ArgumentParser(description="find strings inside files")
    parser.add_argument("strings", nargs = "*", help="The files will be searched according to this words")
    parser.add_argument("-o", action="store_true", help="This option resets the string1 AND string2 and string3 logic to a string1 OR string2 OR string3 search logic")
    args = parser.parse_args()
    return args.strings, args.o
