""" Module providing functionality to check the type of space the player is
    on. """

import sys
import json
import backend.player
import backend.properties
import backend.miscellaneous
from backend.charge_rent import charge_rent
from backend.pay_tax import pay_tax


def check_position(source=sys.stdin):
    """Check the type of space the player is on.

    The two types of space this function recognises are properties and
    miscellaneous (chance, tax, etc.).

    """
    # Get the player id from the client
    details = json.load(source)
    player_id = details["player_id"]

    # Create a player instance based who has to pay tax
    player = backend.player.Player(player_id)
    player_position = player.board_position

    # Check if player on a property space
    if player_position in backend.properties.property_positions():
        # Check if property is owned
        if backend.properties.is_property_owned(player_position):
            # Call function to offer buying this property
            charge_rent(player_id)
        else:
            # Some code to allow purchasing of this property
            pass

    # Check if player on miscellaneous space
    elif player_position in backend.miscellaneous.get_misc_positions():
        # Get the details of the miscellaneous space the player is on
        misc_position = \
                    backend.miscellaneous.get_space_details(player_position)
        position_type = misc_position["type"]
        # Check the type of space the player is on, and act appropriately
        if position_type == "tax":
            pay_tax(player_id, misc_position["value"])
        elif position_type == "chance":
            pass
        elif position_type == "community_chest":
            pass
        elif position_type == "jail":
            pass
        elif position_type == "to_jail":
            pass
        elif position_type == "parking":
            pass
