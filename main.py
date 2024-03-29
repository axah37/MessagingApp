import hashlib
import uuid

from flask import Flask, render_template, request, make_response, redirect, url_for
from models import User, Message, db

app = Flask(__name__)
db.create_all()

# Route Handles the homepage
@app.route("/", methods=["GET"])
def index():
    # Get the session_token to check if user is signed im

    # If session_token, get the user and messages from the database

    # Else set user and messages to none

    # Return render_template for Index HTML and pass user and messages variables.

    # Remove pass once complete
    pass

# Route Handles a User wanting to sign up to your website
@app.route("/signup", methods=["POST"])
def signup():

    # GET all values from form including user-name, user-password and user-password-confirm

    # Hash the password

    # Check is the user already exists in the database

    # If a user is not found

        # If the password matches the confirmed-password

            # Create a new session_token

            # Create a new user object

            # Add and commit to database

            # Use make response to set a cookie containing the session_token

            # Return response

        # Else - the passwords do not match

            # Just return the the index page

    # Else - a user already exists

        # Just return the index page


    pass

# Handles a return user signing into their account
@app.route("/login", methods=["POST"])
def login():

    # Get all the values from the from including user-name, user-password

    # Hash the password

    # Get the user from the database

    # If no user is found

        # Just return the index page

    #Else - User is found

        # If the hashed password matches the database password

            # Create a new session_token

            # Update the user object with the new session token

            # Save changes to the database

            # Use make response to send the user back to the index page with a cookies containing the session_token

        # Else - The user enter the wrong password

            # Just return the index page
    pass


# The route handles users wanting to logout of the website
@app.route('/logout', methods=["GET"])
def logout():

    # Get the session_token

    # If session_token is found

        # Use make response to send the user to the index page and set empty cookie with expiry

    # Else - no session_token

        # Just send the user to the index page

    pass


# This route handles sending messages
@app.route('/send', methods=["GET", "POST"])
def send():

    # Get the session_token

    # If session_token found

        # Get the user from the database

        # If get request -- i.e we just show the user the messages page

            # Get all the users in the database

            # Send the user to the send html page, set user and users in return

        # ELIF - post request

            # GET the receiver and message_body from the form

            # Get the receiver from the database

            # If receiver is found

                # Create a message object and set the send, receiver and message

                # Save the message object to the database

                # Send the user back to the index page

            # Else - receiver was not found

                # Send the user to the index page

        # Else - not a get or post request

            # Send the user to the index page

    # Else - no session_token found

        # Send the user to the index page

    pass


# This route handles deleting messages
@app.route("/delete/<msg_id>", methods=["GET"])
def delete(msg_id):

    # Get session_token

    # Get the user from the database

    # Get the message using msg_id from database

    # If the user.id matchs the message.receiver

        # Delete the message from the database

        # Send the user to the index page

    # Else - the message does not belong to the user

        # Send the user to the index page

    pass


if __name__ == '__main__':
    app.run(debug=True)