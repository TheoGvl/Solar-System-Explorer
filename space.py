import flet as ft

# --- Solar System Data ---
# All planet names, types, and descriptions have been translated to English.
PLANETS_DATA = {
    "Mercury": {"color": "grey500", "size": 80, "type": "Terrestrial Planet", "dist": "0.39 AU", "mass": "0.055 Earths", "grav": "3.7 m/s²", "desc": "The smallest and closest planet to the Sun. It has no atmosphere and is heavily cratered."},
    "Venus": {"color": "orange300", "size": 130, "type": "Terrestrial Planet", "dist": "0.72 AU", "mass": "0.815 Earths", "grav": "8.87 m/s²", "desc": "The hottest planet in the solar system, with an incredibly thick and toxic atmosphere of carbon dioxide."},
    "Earth": {"color": "blue400", "size": 140, "type": "Terrestrial Planet", "dist": "1.00 AU", "mass": "1.00 Earths", "grav": "9.8 m/s²", "desc": "Our home. The only known planet in the universe with liquid water on its surface and life."},
    "Mars": {"color": "red500", "size": 100, "type": "Terrestrial Planet", "dist": "1.52 AU", "mass": "0.107 Earths", "grav": "3.71 m/s²", "desc": "The Red Planet. Home to the tallest mountain in the solar system (Olympus Mons) and a primary target for future colonization."},
    "Jupiter": {"color": "brown400", "size": 280, "type": "Gas Giant", "dist": "5.20 AU", "mass": "317.8 Earths", "grav": "24.79 m/s²", "desc": "The absolute giant of the system. Known for the 'Great Red Spot', a massive storm raging for centuries."},
    "Saturn": {"color": "yellow200", "size": 250, "type": "Gas Giant", "dist": "9.58 AU", "mass": "95.1 Earths", "grav": "10.44 m/s²", "desc": "Perhaps the most visually stunning planet thanks to its massive and complex ring system made of ice and rock."},
    "Uranus": {"color": "cyan200", "size": 190, "type": "Ice Giant", "dist": "19.22 AU", "mass": "14.5 Earths", "grav": "8.69 m/s²", "desc": "Rotates 'on its side' (like a barrel). It has an extremely cold, blue-green atmosphere rich in methane."},
    "Neptune": {"color": "blue800", "size": 180, "type": "Ice Giant", "dist": "30.05 AU", "mass": "17.1 Earths", "grav": "11.15 m/s²", "desc": "The most distant planet. It is a dark, freezing world whipped by supersonic winds."}
}

def main(page: ft.Page):
    # --- Window Configuration ---
    page.title = "Solar System Explorer"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40
    page.window.width = 800
    page.window.height = 750
    page.bgcolor = "#0a0a1a" # Deep space background color

    # --- UI Elements ---
    
    # The visual representation of the planet
    planet_visual = ft.Container(
        width=140,
        height=140,
        bgcolor="blue400",
        shape=ft.BoxShape.CIRCLE,
        shadow=ft.BoxShadow(spread_radius=2, blur_radius=20, color="blue400"),
        animate=ft.Animation(600, ft.AnimationCurve.EASE_OUT), # Smooth 600ms morphing animation
    )

    # Dynamic text fields for planet information (initialized with Earth data)
    title_text = ft.Text("Earth", size=40, weight=ft.FontWeight.BOLD, color="white")
    type_text = ft.Text("Terrestrial Planet", size=18, color="grey400", italic=True)
    desc_text = ft.Text(PLANETS_DATA["Earth"]["desc"], size=16, text_align=ft.TextAlign.CENTER, width=600)

    # Dynamic text variables for the stat boxes
    dist_val = ft.Text(PLANETS_DATA["Earth"]["dist"], size=18, color="white", weight=ft.FontWeight.BOLD)
    mass_val = ft.Text(PLANETS_DATA["Earth"]["mass"], size=18, color="white", weight=ft.FontWeight.BOLD)
    grav_val = ft.Text(PLANETS_DATA["Earth"]["grav"], size=18, color="white", weight=ft.FontWeight.BOLD)

    # Helper function to generate standardized stat boxes
    def create_stat_box(label, text_control):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(label, size=14, color="grey400", weight=ft.FontWeight.BOLD),
                    text_control
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2
            ),
            bgcolor="#15152a",
            padding=15,
            border_radius=10,
            width=150,
            border=ft.Border.all(1, "#2a2a4a")
        )

    # Create the 3 individual stat boxes
    stat_dist = create_stat_box("Distance", dist_val)
    stat_mass = create_stat_box("Mass", mass_val)
    stat_grav = create_stat_box("Gravity", grav_val)

    # --- Interaction Logic ---
    # Function triggered when a new planet is selected from the dropdown
    def planet_changed(e):
        selected = e.control.value
        data = PLANETS_DATA[selected]

        # Update text fields
        title_text.value = selected
        type_text.value = data["type"]
        desc_text.value = data["desc"]
        
        # Update stat variables directly
        dist_val.value = data["dist"]
        mass_val.value = data["mass"]
        grav_val.value = data["grav"]

        # Update visual representation 
        planet_visual.bgcolor = data["color"]
        planet_visual.width = data["size"]
        planet_visual.height = data["size"]
        planet_visual.shadow = ft.BoxShadow(spread_radius=2, blur_radius=20, color=data["color"])

        # Refresh the UI to show changes
        page.update()

    # The dropdown menu using English keys
    planet_dropdown = ft.Dropdown(
        label="Select a Planet",
        width=300,
        options=[ft.dropdown.Option(name) for name in PLANETS_DATA.keys()],
        value="Earth",
        on_select=planet_changed,
        border_color="blue400"
    )

    # --- Layout Structure ---
    # Add all components to the main window page
    page.add(
        ft.Text("Solar System", size=24, weight=ft.FontWeight.BOLD, color="white"),
        ft.Divider(height=10, color="transparent"),
        
        planet_dropdown,
        
        ft.Divider(height=30, color="transparent"),
        
        # Wrapper container for the planet visual to prevent layout shifting during animation
        ft.Container(
            content=planet_visual,
            height=300,
            alignment=ft.Alignment(0, 0)
        ),
        
        title_text,
        type_text,
        
        ft.Divider(height=10, color="transparent"),
        
        desc_text,
        
        ft.Divider(height=20, color="transparent"),
        
        # Horizontal row containing the 3 stat boxes
        ft.Row(
            [stat_dist, stat_mass, stat_grav],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main) # type: ignore