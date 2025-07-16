from task_00_intro import generate_invitations

# Création du template dans un fichier
template_text = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""

with open("template.txt", "w") as f:
    f.write(template_text)

# Lecture du template
with open("template.txt", "r") as f:
    template_content = f.read()

# Liste d'invités pour le test
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Appel de la fonction
generate_invitations(template_content, attendees)