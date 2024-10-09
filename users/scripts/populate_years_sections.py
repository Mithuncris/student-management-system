from users.models import Year, Section

def create_years_and_sections():
    # Create years
    years = ['I Year', 'II Year', 'III Year', 'IV Year']
    sections_per_year = {
        'I Year': 4,
        'II Year': 3,
        'III Year': 2,
        'IV Year': 1
    }

    for year in years:
        # Create the year if it doesn't already exist
        year_obj, created = Year.objects.get_or_create(name=year)
        
        # Add sections for the year
        for section_num in range(1, sections_per_year[year] + 1):
            section_name = f'Section {section_num}'
            Section.objects.get_or_create(year=year_obj, name=section_name)

    print("Years and sections created successfully.")
