def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated. ")
        return

    for index, person in enumerate(attendees, start=1):
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        cleaned_data = {
            "name": name,
            "event_title": event_title,
            "event_date": event_date,
            "event_location": event_location
        }

        template_copy = template
    
        for key, value in cleaned_data.items():
            template_copy = template_copy.replace(f"{{{key}}}", value)

        with open(f"output_{index}.txt", "w") as fichier:
            fichier.write(template_copy)

        
        

