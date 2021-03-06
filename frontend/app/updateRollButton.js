// Import sendJSON functionality
import * as sendJSON from './sendJSON';
// Import getCookie functionality
import * as getCookie from './checkUserIDCookie';

/**
 * Callback for when player's roll dice values successfully received.
 *
 * @param {XMLHttpRequest} req Contains the response with the roll dice values.
 */
export function checkRollValuesEqual(req) {
    // Enables the roll button for the player if the previous
    // roll values are equal
    const response = JSON.parse(req.responseText);
    const roll = response.your_rolls;
    const rollDie = document.querySelector('#roll-dice');
    if (roll[0] === roll[1]) {
        rollDie.disabled = false;
    } else {
        rollDie.disabled = true;
    }
}

/**
 * Make a request for roll dice.
 *
 * @param {Function} JSONSend The function to make the request to the server.
 */
export function requestCompareRolls(JSONSend = sendJSON.sendJSON) {
    // Adds 'event listener' to the roll button for the player to
    // enable/disable the button
    const details = getCookie.checkUserDetails();
    const id = details.user_id;
    JSONSend({
        serverAddress: 'cgi-bin/roll_dice.py',
        jsonObject: {user_id: id},
        checkRollValuesEqual,
    });
}
