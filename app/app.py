from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_user_by_username, create_user, save_prediction
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "fraudshield-secret-key"
