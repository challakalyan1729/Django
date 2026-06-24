from django.shortcuts import render
from django.http import HttpResponse
def fun(request):
    return HttpResponse("""<h1>Welcome to Vibekhel</h1>

<p>Play. Compete. Connect.</p>

<p>
Vibekhel is a platform where players can discover, create, and join local sports events.
</p>

<h2>Popular Sports</h2>

<ul>
    <li>Cricket</li>
    <li>Kabaddi</li>
    <li>Football</li>
    <li>Volleyball</li>
    <li>Chess</li>
</ul>

<h2>Features</h2>

<ul>
    <li>Find nearby matches</li>
    <li>Create your own events</li>
    <li>Join local tournaments</li>
    <li>Connect with players</li>
</ul>

<p>
<a href="/events/">View Events</a>
</p>

<p>
<a href="/create/">Create Event</a>
</p>

<hr>

<p>Vibekhel - Bringing local sports communities together.</p>""")
def create_event(request):
    return HttpResponse("""
    <h1>Create Sports Event</h1>

    <form>

        <label>Event Name:</label><br>
        <input type="text" placeholder="Enter event name"><br><br>

        <label>Sport Type:</label><br>
        <select>
            <option>Cricket</option>
            <option>Kabaddi</option>
            <option>Football</option>
            <option>Volleyball</option>
            <option>Chess</option>
        </select><br><br>

        <label>Date:</label><br>
        <input type="date"><br><br>

        <label>Time:</label><br>
        <input type="time"><br><br>

        <label>Location:</label><br>
        <input type="text" placeholder="Enter location"><br><br>

        <label>Maximum Players:</label><br>
        <input type="number"><br><br>

        <label>Description:</label><br>
        <textarea rows="5" cols="40"
        placeholder="Describe your event"></textarea><br><br>

        <input type="submit" value="Create Event">

    </form>

    <hr>

    <p><a href="/">Back to Home</a></p>
    """)
def events(request):
    return HttpResponse("""
    <h1>Upcoming Sports Events</h1>

    <hr>

    <h2>🏏 Cricket Tournament</h2>
    <p><strong>Date:</strong> 28 June 2026</p>
    <p><strong>Time:</strong> 7:00 AM</p>
    <p><strong>Location:</strong> Rajahmundry</p>
    <p><strong>Players Needed:</strong> 22</p>

    <hr>

    <h2>🤼 Kabaddi Championship</h2>
    <p><strong>Date:</strong> 30 June 2026</p>
    <p><strong>Time:</strong> 6:00 PM</p>
    <p><strong>Location:</strong> Kakinada</p>
    <p><strong>Players Needed:</strong> 14</p>

    <hr>

    <h2>⚽ Football Match</h2>
    <p><strong>Date:</strong> 2 July 2026</p>
    <p><strong>Time:</strong> 5:00 PM</p>
    <p><strong>Location:</strong> Hyderabad</p>
    <p><strong>Players Needed:</strong> 22</p>

    <hr>

    <h2>🏐 Volleyball Tournament</h2>
    <p><strong>Date:</strong> 5 July 2026</p>
    <p><strong>Time:</strong> 4:00 PM</p>
    <p><strong>Location:</strong> Vijayawada</p>
    <p><strong>Players Needed:</strong> 12</p>

    <hr>

    <p><a href="/">Home</a></p>
    <p><a href="/create/">Create Event</a></p>
    """)
